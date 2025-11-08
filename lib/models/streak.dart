class Streak {
  final int currentStreak;
  final int longestStreak;
  final DateTime? lastCompletionDate;
  final int totalLessonsCompleted;
  final Map<String, int> lessonsPerDay; // date -> count

  Streak({
    this.currentStreak = 0,
    this.longestStreak = 0,
    this.lastCompletionDate,
    this.totalLessonsCompleted = 0,
    this.lessonsPerDay = const {},
  });

  bool get isActiveToday {
    if (lastCompletionDate == null) return false;
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final lastDate = DateTime(
      lastCompletionDate!.year,
      lastCompletionDate!.month,
      lastCompletionDate!.day,
    );
    return today == lastDate;
  }

  bool get isStreakBroken {
    if (lastCompletionDate == null) return false;
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    final lastDate = DateTime(
      lastCompletionDate!.year,
      lastCompletionDate!.month,
      lastCompletionDate!.day,
    );
    final difference = today.difference(lastDate).inDays;
    return difference > 1;
  }

  Streak copyWith({
    int? currentStreak,
    int? longestStreak,
    DateTime? lastCompletionDate,
    int? totalLessonsCompleted,
    Map<String, int>? lessonsPerDay,
  }) {
    return Streak(
      currentStreak: currentStreak ?? this.currentStreak,
      longestStreak: longestStreak ?? this.longestStreak,
      lastCompletionDate: lastCompletionDate ?? this.lastCompletionDate,
      totalLessonsCompleted: totalLessonsCompleted ?? this.totalLessonsCompleted,
      lessonsPerDay: lessonsPerDay ?? this.lessonsPerDay,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'currentStreak': currentStreak,
      'longestStreak': longestStreak,
      'lastCompletionDate': lastCompletionDate?.toIso8601String(),
      'totalLessonsCompleted': totalLessonsCompleted,
      'lessonsPerDay': lessonsPerDay,
    };
  }

  factory Streak.fromJson(Map<String, dynamic> json) {
    return Streak(
      currentStreak: json['currentStreak'] as int? ?? 0,
      longestStreak: json['longestStreak'] as int? ?? 0,
      lastCompletionDate: json['lastCompletionDate'] != null
          ? DateTime.parse(json['lastCompletionDate'] as String)
          : null,
      totalLessonsCompleted: json['totalLessonsCompleted'] as int? ?? 0,
      lessonsPerDay: Map<String, int>.from(json['lessonsPerDay'] as Map? ?? {}),
    );
  }

  int getLessonsCompletedOnDate(DateTime date) {
    final dateKey = _formatDate(date);
    return lessonsPerDay[dateKey] ?? 0;
  }

  static String _formatDate(DateTime date) {
    return '${date.year}-${date.month.toString().padLeft(2, '0')}-${date.day.toString().padLeft(2, '0')}';
  }
}
