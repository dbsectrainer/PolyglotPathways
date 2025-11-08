import 'package:flutter/material.dart';

enum AchievementType {
  firstLesson,
  firstWeek,
  firstMonth,
  streak7,
  streak14,
  streak30,
  streak100,
  complete10Lessons,
  complete25Lessons,
  complete50Lessons,
  multilingualBronze, // 2 languages
  multilingualSilver, // 3 languages
  multilingualGold, // 5 languages
  earlyBird, // Complete lesson before 9 AM
  nightOwl, // Complete lesson after 9 PM
  speedLearner, // Complete 3 lessons in one day
  perfectWeek, // 7 day streak
}

class Achievement {
  final AchievementType type;
  final String title;
  final String description;
  final IconData icon;
  final Color color;
  final int requiredValue;
  final bool isUnlocked;
  final DateTime? unlockedAt;

  Achievement({
    required this.type,
    required this.title,
    required this.description,
    required this.icon,
    required this.color,
    required this.requiredValue,
    this.isUnlocked = false,
    this.unlockedAt,
  });

  Achievement copyWith({
    AchievementType? type,
    String? title,
    String? description,
    IconData? icon,
    Color? color,
    int? requiredValue,
    bool? isUnlocked,
    DateTime? unlockedAt,
  }) {
    return Achievement(
      type: type ?? this.type,
      title: title ?? this.title,
      description: description ?? this.description,
      icon: icon ?? this.icon,
      color: color ?? this.color,
      requiredValue: requiredValue ?? this.requiredValue,
      isUnlocked: isUnlocked ?? this.isUnlocked,
      unlockedAt: unlockedAt ?? this.unlockedAt,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'type': type.toString(),
      'isUnlocked': isUnlocked,
      'unlockedAt': unlockedAt?.toIso8601String(),
    };
  }

  factory Achievement.fromJson(Map<String, dynamic> json, Achievement template) {
    return template.copyWith(
      isUnlocked: json['isUnlocked'] as bool? ?? false,
      unlockedAt: json['unlockedAt'] != null
          ? DateTime.parse(json['unlockedAt'] as String)
          : null,
    );
  }

  static List<Achievement> getAllAchievements() {
    return [
      Achievement(
        type: AchievementType.firstLesson,
        title: 'First Steps',
        description: 'Complete your first lesson',
        icon: Icons.rocket_launch,
        color: const Color(0xFF4A90E2),
        requiredValue: 1,
      ),
      Achievement(
        type: AchievementType.firstWeek,
        title: 'Week Warrior',
        description: 'Complete 7 lessons',
        icon: Icons.calendar_view_week,
        color: const Color(0xFF50C878),
        requiredValue: 7,
      ),
      Achievement(
        type: AchievementType.firstMonth,
        title: 'Monthly Master',
        description: 'Complete 30 lessons',
        icon: Icons.calendar_month,
        color: const Color(0xFF9B59B6),
        requiredValue: 30,
      ),
      Achievement(
        type: AchievementType.streak7,
        title: '7 Day Streak',
        description: 'Learn for 7 days in a row',
        icon: Icons.local_fire_department,
        color: const Color(0xFFFF6B6B),
        requiredValue: 7,
      ),
      Achievement(
        type: AchievementType.streak14,
        title: '14 Day Streak',
        description: 'Learn for 14 days in a row',
        icon: Icons.whatshot,
        color: const Color(0xFFFF4757),
        requiredValue: 14,
      ),
      Achievement(
        type: AchievementType.streak30,
        title: '30 Day Streak',
        description: 'Learn for 30 days in a row',
        icon: Icons.fireplace,
        color: const Color(0xFFE74C3C),
        requiredValue: 30,
      ),
      Achievement(
        type: AchievementType.streak100,
        title: 'Century Streak',
        description: 'Learn for 100 days in a row',
        icon: Icons.military_tech,
        color: const Color(0xFFFFD700),
        requiredValue: 100,
      ),
      Achievement(
        type: AchievementType.complete10Lessons,
        title: 'Getting Started',
        description: 'Complete 10 lessons',
        icon: Icons.looks_one,
        color: const Color(0xFF3498DB),
        requiredValue: 10,
      ),
      Achievement(
        type: AchievementType.complete25Lessons,
        title: 'Quarter Century',
        description: 'Complete 25 lessons',
        icon: Icons.looks_two,
        color: const Color(0xFF2ECC71),
        requiredValue: 25,
      ),
      Achievement(
        type: AchievementType.complete50Lessons,
        title: 'Half Century',
        description: 'Complete 50 lessons - Full course!',
        icon: Icons.emoji_events,
        color: const Color(0xFFFFD700),
        requiredValue: 50,
      ),
      Achievement(
        type: AchievementType.multilingualBronze,
        title: 'Bilingual Bronze',
        description: 'Start learning 2 languages',
        icon: Icons.translate,
        color: const Color(0xFFCD7F32),
        requiredValue: 2,
      ),
      Achievement(
        type: AchievementType.multilingualSilver,
        title: 'Trilingual Silver',
        description: 'Start learning 3 languages',
        icon: Icons.language,
        color: const Color(0xFFC0C0C0),
        requiredValue: 3,
      ),
      Achievement(
        type: AchievementType.multilingualGold,
        title: 'Polyglot Gold',
        description: 'Start learning all 5 languages',
        icon: Icons.public,
        color: const Color(0xFFFFD700),
        requiredValue: 5,
      ),
      Achievement(
        type: AchievementType.earlyBird,
        title: 'Early Bird',
        description: 'Complete a lesson before 9 AM',
        icon: Icons.wb_sunny,
        color: const Color(0xFFFFA500),
        requiredValue: 1,
      ),
      Achievement(
        type: AchievementType.nightOwl,
        title: 'Night Owl',
        description: 'Complete a lesson after 9 PM',
        icon: Icons.nightlight_round,
        color: const Color(0xFF9B59B6),
        requiredValue: 1,
      ),
      Achievement(
        type: AchievementType.speedLearner,
        title: 'Speed Learner',
        description: 'Complete 3 lessons in one day',
        icon: Icons.speed,
        color: const Color(0xFFE74C3C),
        requiredValue: 3,
      ),
      Achievement(
        type: AchievementType.perfectWeek,
        title: 'Perfect Week',
        description: 'Maintain a 7 day learning streak',
        icon: Icons.star,
        color: const Color(0xFFFFD700),
        requiredValue: 7,
      ),
    ];
  }
}
