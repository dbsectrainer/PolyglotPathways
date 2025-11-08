import 'language.dart';

class Progress {
  final Map<Language, Set<int>> completedLessons;
  final Map<Language, int> currentDay;

  Progress({
    Map<Language, Set<int>>? completedLessons,
    Map<Language, int>? currentDay,
  })  : completedLessons = completedLessons ?? {},
        currentDay = currentDay ?? {};

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

  Progress copyWith({
    Map<Language, Set<int>>? completedLessons,
    Map<Language, int>? currentDay,
  }) {
    return Progress(
      completedLessons: completedLessons ?? this.completedLessons,
      currentDay: currentDay ?? this.currentDay,
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
    };
  }

  factory Progress.fromJson(Map<String, dynamic> json) {
    final completedLessonsMap = <Language, Set<int>>{};
    final currentDayMap = <Language, int>{};

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

    return Progress(
      completedLessons: completedLessonsMap,
      currentDay: currentDayMap,
    );
  }
}
