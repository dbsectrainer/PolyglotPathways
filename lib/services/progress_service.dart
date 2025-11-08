import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/language.dart';
import '../models/progress.dart';

class ProgressService extends ChangeNotifier {
  final SharedPreferences _prefs;
  Progress _progress = Progress();

  ProgressService(this._prefs) {
    _loadProgress();
  }

  Progress get progress => _progress;

  void _loadProgress() {
    final progressJson = _prefs.getString('progress');
    if (progressJson != null) {
      try {
        final decoded = json.decode(progressJson);
        _progress = Progress.fromJson(decoded);
      } catch (e) {
        debugPrint('Error loading progress: $e');
        _progress = Progress();
      }
    }
    notifyListeners();
  }

  Future<void> _saveProgress() async {
    final progressJson = json.encode(_progress.toJson());
    await _prefs.setString('progress', progressJson);
  }

  Future<void> markLessonComplete(Language language, int day) async {
    final completed = Set<int>.from(_progress.completedLessons[language] ?? {});
    completed.add(day);

    final newCompletedLessons = Map<Language, Set<int>>.from(_progress.completedLessons);
    newCompletedLessons[language] = completed;

    final newCurrentDay = Map<Language, int>.from(_progress.currentDay);
    if (day >= (newCurrentDay[language] ?? 1)) {
      newCurrentDay[language] = day < 50 ? day + 1 : 50;
    }

    _progress = Progress(
      completedLessons: newCompletedLessons,
      currentDay: newCurrentDay,
      completedExercises: _progress.completedExercises,
    );

    await _saveProgress();
    notifyListeners();
  }

  Future<void> unmarkLessonComplete(Language language, int day) async {
    final completed = Set<int>.from(_progress.completedLessons[language] ?? {});
    completed.remove(day);

    final newCompletedLessons = Map<Language, Set<int>>.from(_progress.completedLessons);
    newCompletedLessons[language] = completed;

    _progress = Progress(
      completedLessons: newCompletedLessons,
      currentDay: _progress.currentDay,
      completedExercises: _progress.completedExercises,
    );

    await _saveProgress();
    notifyListeners();
  }

  bool isLessonCompleted(Language language, int day) {
    return _progress.isLessonCompleted(language, day);
  }

  int getCompletedCount(Language language) {
    return _progress.getCompletedCount(language);
  }

  int getCurrentDay(Language language) {
    return _progress.getCurrentDay(language);
  }

  double getProgress(Language language) {
    return _progress.getProgress(language);
  }

  Future<void> markExerciseComplete(Language language, int day, String exerciseId) async {
    final newCompletedExercises = Map<Language, Map<int, Set<String>>>.from(_progress.completedExercises);

    if (!newCompletedExercises.containsKey(language)) {
      newCompletedExercises[language] = {};
    }

    if (!newCompletedExercises[language]!.containsKey(day)) {
      newCompletedExercises[language]![day] = {};
    }

    final dayExercises = Set<String>.from(newCompletedExercises[language]![day]!);
    dayExercises.add(exerciseId);
    newCompletedExercises[language]![day] = dayExercises;

    _progress = Progress(
      completedLessons: _progress.completedLessons,
      currentDay: _progress.currentDay,
      completedExercises: newCompletedExercises,
    );

    await _saveProgress();
    notifyListeners();
  }

  bool isExerciseCompleted(Language language, int day, String exerciseId) {
    return _progress.isExerciseCompleted(language, day, exerciseId);
  }

  int getCompletedExercisesCount(Language language, int day) {
    return _progress.getCompletedExercisesCount(language, day);
  }

  Set<String> getCompletedExerciseIds(Language language, int day) {
    return _progress.getCompletedExerciseIds(language, day);
  }

  Future<void> resetAll() async {
    _progress = Progress();
    await _saveProgress();
    notifyListeners();
  }
}
