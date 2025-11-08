import 'language.dart';

class Progress {
  final Map<Language, Set<int>> completedLessons;
  final Map<Language, int> currentDay;
  // Map of language -> day -> set of completed exercise IDs
  final Map<Language, Map<int, Set<String>>> completedExercises;

  Progress({
    Map<Language, Set<int>>? completedLessons,
    Map<Language, int>? currentDay,
    Map<Language, Map<int, Set<String>>>? completedExercises,
  })  : completedLessons = completedLessons ?? {},
        currentDay = currentDay ?? {},
        completedExercises = completedExercises ?? {};

  bool isLessonCompleted(Language language, int day) {
    return completedLessons[language]?.contains(day) ?? false;
  }

  int getCompletedCount(Language language) {
    return completedLessons[language]?.length ?? 0;
  }

  int getCurrentDay(Language language) {
    return currentDay[language] ?? 1;
  }

  double getProgress(Language language) {
    final completed = getCompletedCount(language);
    return completed / 50.0;
  }

  bool isExerciseCompleted(Language language, int day, String exerciseId) {
    return completedExercises[language]?[day]?.contains(exerciseId) ?? false;
  }

  int getCompletedExercisesCount(Language language, int day) {
    return completedExercises[language]?[day]?.length ?? 0;
  }

  Set<String> getCompletedExerciseIds(Language language, int day) {
    return completedExercises[language]?[day] ?? {};
  }

  Progress copyWith({
    Map<Language, Set<int>>? completedLessons,
    Map<Language, int>? currentDay,
    Map<Language, Map<int, Set<String>>>? completedExercises,
  }) {
    return Progress(
      completedLessons: completedLessons ?? this.completedLessons,
      currentDay: currentDay ?? this.currentDay,
      completedExercises: completedExercises ?? this.completedExercises,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'completedLessons': completedLessons.map(
        (key, value) => MapEntry(key.code, value.toList()),
      ),
      'currentDay': currentDay.map(
        (key, value) => MapEntry(key.code, value),
      ),
      'completedExercises': completedExercises.map(
        (lang, dayMap) => MapEntry(
          lang.code,
          dayMap.map(
            (day, exerciseIds) => MapEntry(day.toString(), exerciseIds.toList()),
          ),
        ),
      ),
    };
  }

  factory Progress.fromJson(Map<String, dynamic> json) {
    final completedLessonsMap = <Language, Set<int>>{};
    final currentDayMap = <Language, int>{};
    final completedExercisesMap = <Language, Map<int, Set<String>>>{};

    if (json['completedLessons'] != null) {
      (json['completedLessons'] as Map<String, dynamic>).forEach((key, value) {
        final language = Language.fromCode(key);
        completedLessonsMap[language] = (value as List).cast<int>().toSet();
      });
    }

    if (json['currentDay'] != null) {
      (json['currentDay'] as Map<String, dynamic>).forEach((key, value) {
        final language = Language.fromCode(key);
        currentDayMap[language] = value as int;
      });
    }

    if (json['completedExercises'] != null) {
      (json['completedExercises'] as Map<String, dynamic>).forEach((langCode, dayMap) {
        final language = Language.fromCode(langCode);
        final exercisesByDay = <int, Set<String>>{};

        (dayMap as Map<String, dynamic>).forEach((dayStr, exerciseIds) {
          final day = int.parse(dayStr);
          exercisesByDay[day] = (exerciseIds as List).cast<String>().toSet();
        });

        completedExercisesMap[language] = exercisesByDay;
      });
    }

    return Progress(
      completedLessons: completedLessonsMap,
      currentDay: currentDayMap,
      completedExercises: completedExercisesMap,
    );
  }
}
