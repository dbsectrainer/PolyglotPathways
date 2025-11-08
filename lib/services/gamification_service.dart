import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/achievement.dart';
import '../models/streak.dart';
import '../models/language.dart';

class GamificationService extends ChangeNotifier {
  static const String _streakKey = 'streak_data';
  static const String _achievementsKey = 'achievements_data';
  static const String _languagesStartedKey = 'languages_started';

  Streak _streak = Streak();
  List<Achievement> _achievements = Achievement.getAllAchievements();
  Set<String> _languagesStarted = {};
  List<Achievement> _recentlyUnlocked = [];

  Streak get streak => _streak;
  List<Achievement> get achievements => _achievements;
  List<Achievement> get unlockedAchievements =>
      _achievements.where((a) => a.isUnlocked).toList();
  List<Achievement> get lockedAchievements =>
      _achievements.where((a) => !a.isUnlocked).toList();
  int get achievementCount => unlockedAchievements.length;
  int get totalAchievements => _achievements.length;
  List<Achievement> get recentlyUnlocked => _recentlyUnlocked;

  GamificationService() {
    _loadData();
  }

  Future<void> _loadData() async {
    final prefs = await SharedPreferences.getInstance();

    // Load streak
    final streakJson = prefs.getString(_streakKey);
    if (streakJson != null) {
      _streak = Streak.fromJson(json.decode(streakJson));
    }

    // Load achievements
    final achievementsJson = prefs.getString(_achievementsKey);
    if (achievementsJson != null) {
      final List<dynamic> savedAchievements = json.decode(achievementsJson);
      final allAchievements = Achievement.getAllAchievements();

      _achievements = allAchievements.map((template) {
        final saved = savedAchievements.firstWhere(
          (a) => a['type'] == template.type.toString(),
          orElse: () => null,
        );
        if (saved != null) {
          return Achievement.fromJson(saved, template);
        }
        return template;
      }).toList();
    }

    // Load languages started
    final languagesJson = prefs.getStringList(_languagesStartedKey);
    if (languagesJson != null) {
      _languagesStarted = Set<String>.from(languagesJson);
    }

    notifyListeners();
  }

  Future<void> _saveData() async {
    final prefs = await SharedPreferences.getInstance();

    // Save streak
    await prefs.setString(_streakKey, json.encode(_streak.toJson()));

    // Save achievements
    final achievementsJson = _achievements.map((a) => a.toJson()).toList();
    await prefs.setString(_achievementsKey, json.encode(achievementsJson));

    // Save languages started
    await prefs.setStringList(_languagesStartedKey, _languagesStarted.toList());
  }

  Future<void> recordLessonCompletion(Language language) async {
    _recentlyUnlocked.clear();

    // Track language started
    _languagesStarted.add(language.code);

    // Update streak
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final dateKey = _formatDate(today);

    Map<String, int> updatedLessonsPerDay = Map.from(_streak.lessonsPerDay);
    updatedLessonsPerDay[dateKey] = (updatedLessonsPerDay[dateKey] ?? 0) + 1;

    int newCurrentStreak = _streak.currentStreak;
    if (_streak.lastCompletionDate == null) {
      newCurrentStreak = 1;
    } else {
      final lastDate = DateTime(
        _streak.lastCompletionDate!.year,
        _streak.lastCompletionDate!.month,
        _streak.lastCompletionDate!.day,
      );
      final daysDifference = today.difference(lastDate).inDays;

      if (daysDifference == 0) {
        // Same day, keep current streak
      } else if (daysDifference == 1) {
        // Consecutive day
        newCurrentStreak = _streak.currentStreak + 1;
      } else {
        // Streak broken
        newCurrentStreak = 1;
      }
    }

    final newLongestStreak = newCurrentStreak > _streak.longestStreak
        ? newCurrentStreak
        : _streak.longestStreak;

    _streak = _streak.copyWith(
      currentStreak: newCurrentStreak,
      longestStreak: newLongestStreak,
      lastCompletionDate: now,
      totalLessonsCompleted: _streak.totalLessonsCompleted + 1,
      lessonsPerDay: updatedLessonsPerDay,
    );

    // Check for achievements
    await _checkAchievements(updatedLessonsPerDay[dateKey] ?? 1);

    await _saveData();
    notifyListeners();
  }

  Future<void> _checkAchievements(int lessonsToday) async {
    final now = DateTime.now();
    final hour = now.hour;

    // First lesson
    _unlockAchievement(
      AchievementType.firstLesson,
      _streak.totalLessonsCompleted >= 1,
    );

    // Lesson milestones
    _unlockAchievement(
      AchievementType.firstWeek,
      _streak.totalLessonsCompleted >= 7,
    );
    _unlockAchievement(
      AchievementType.firstMonth,
      _streak.totalLessonsCompleted >= 30,
    );
    _unlockAchievement(
      AchievementType.complete10Lessons,
      _streak.totalLessonsCompleted >= 10,
    );
    _unlockAchievement(
      AchievementType.complete25Lessons,
      _streak.totalLessonsCompleted >= 25,
    );
    _unlockAchievement(
      AchievementType.complete50Lessons,
      _streak.totalLessonsCompleted >= 50,
    );

    // Streak achievements
    _unlockAchievement(
      AchievementType.streak7,
      _streak.currentStreak >= 7,
    );
    _unlockAchievement(
      AchievementType.streak14,
      _streak.currentStreak >= 14,
    );
    _unlockAchievement(
      AchievementType.streak30,
      _streak.currentStreak >= 30,
    );
    _unlockAchievement(
      AchievementType.streak100,
      _streak.currentStreak >= 100,
    );
    _unlockAchievement(
      AchievementType.perfectWeek,
      _streak.currentStreak >= 7,
    );

    // Multilingual achievements
    _unlockAchievement(
      AchievementType.multilingualBronze,
      _languagesStarted.length >= 2,
    );
    _unlockAchievement(
      AchievementType.multilingualSilver,
      _languagesStarted.length >= 3,
    );
    _unlockAchievement(
      AchievementType.multilingualGold,
      _languagesStarted.length >= 5,
    );

    // Time-based achievements
    _unlockAchievement(
      AchievementType.earlyBird,
      hour < 9,
    );
    _unlockAchievement(
      AchievementType.nightOwl,
      hour >= 21,
    );

    // Speed learner
    _unlockAchievement(
      AchievementType.speedLearner,
      lessonsToday >= 3,
    );
  }

  void _unlockAchievement(AchievementType type, bool condition) {
    if (!condition) return;

    final index = _achievements.indexWhere((a) => a.type == type);
    if (index != -1 && !_achievements[index].isUnlocked) {
      _achievements[index] = _achievements[index].copyWith(
        isUnlocked: true,
        unlockedAt: DateTime.now(),
      );
      _recentlyUnlocked.add(_achievements[index]);
    }
  }

  Future<void> resetStreak() async {
    _streak = Streak();
    await _saveData();
    notifyListeners();
  }

  Future<void> resetAchievements() async {
    _achievements = Achievement.getAllAchievements();
    _recentlyUnlocked.clear();
    await _saveData();
    notifyListeners();
  }

  Future<void> resetAll() async {
    _streak = Streak();
    _achievements = Achievement.getAllAchievements();
    _languagesStarted = {};
    _recentlyUnlocked.clear();
    await _saveData();
    notifyListeners();
  }

  void clearRecentlyUnlocked() {
    _recentlyUnlocked.clear();
    notifyListeners();
  }

  static String _formatDate(DateTime date) {
    return '${date.year}-${date.month.toString().padLeft(2, '0')}-${date.day.toString().padLeft(2, '0')}';
  }

  // Get achievements by category
  List<Achievement> getStreakAchievements() {
    return _achievements
        .where((a) =>
            a.type == AchievementType.streak7 ||
            a.type == AchievementType.streak14 ||
            a.type == AchievementType.streak30 ||
            a.type == AchievementType.streak100 ||
            a.type == AchievementType.perfectWeek)
        .toList();
  }

  List<Achievement> getLessonAchievements() {
    return _achievements
        .where((a) =>
            a.type == AchievementType.firstLesson ||
            a.type == AchievementType.firstWeek ||
            a.type == AchievementType.firstMonth ||
            a.type == AchievementType.complete10Lessons ||
            a.type == AchievementType.complete25Lessons ||
            a.type == AchievementType.complete50Lessons)
        .toList();
  }

  List<Achievement> getMultilingualAchievements() {
    return _achievements
        .where((a) =>
            a.type == AchievementType.multilingualBronze ||
            a.type == AchievementType.multilingualSilver ||
            a.type == AchievementType.multilingualGold)
        .toList();
  }

  List<Achievement> getSpecialAchievements() {
    return _achievements
        .where((a) =>
            a.type == AchievementType.earlyBird ||
            a.type == AchievementType.nightOwl ||
            a.type == AchievementType.speedLearner)
        .toList();
  }
}
