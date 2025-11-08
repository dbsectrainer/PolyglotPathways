enum ExerciseType {
  multipleChoice,
  fillInBlank,
  matching,
  translation,
  listening,
}

abstract class Exercise {
  final String id;
  final ExerciseType type;
  final String question;
  final String? audioHint;

  Exercise({
    required this.id,
    required this.type,
    required this.question,
    this.audioHint,
  });

  bool checkAnswer(dynamic answer);
  dynamic getCorrectAnswer();
  Map<String, dynamic> toJson();
}

class MultipleChoiceExercise extends Exercise {
  final List<String> options;
  final int correctOptionIndex;

  MultipleChoiceExercise({
    required String id,
    required String question,
    required this.options,
    required this.correctOptionIndex,
    String? audioHint,
  }) : super(
          id: id,
          type: ExerciseType.multipleChoice,
          question: question,
          audioHint: audioHint,
        );

  @override
  bool checkAnswer(dynamic answer) {
    if (answer is! int) return false;
    return answer == correctOptionIndex;
  }

  @override
  dynamic getCorrectAnswer() => correctOptionIndex;

  @override
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'type': 'multipleChoice',
      'question': question,
      'options': options,
      'correctOptionIndex': correctOptionIndex,
      'audioHint': audioHint,
    };
  }

  factory MultipleChoiceExercise.fromJson(Map<String, dynamic> json) {
    return MultipleChoiceExercise(
      id: json['id'],
      question: json['question'],
      options: List<String>.from(json['options']),
      correctOptionIndex: json['correctOptionIndex'],
      audioHint: json['audioHint'],
    );
  }
}

class FillInBlankExercise extends Exercise {
  final String correctAnswer;
  final List<String>? acceptableAlternatives;
  final bool caseSensitive;

  FillInBlankExercise({
    required String id,
    required String question,
    required this.correctAnswer,
    this.acceptableAlternatives,
    this.caseSensitive = false,
    String? audioHint,
  }) : super(
          id: id,
          type: ExerciseType.fillInBlank,
          question: question,
          audioHint: audioHint,
        );

  @override
  bool checkAnswer(dynamic answer) {
    if (answer is! String) return false;

    final userAnswer = caseSensitive ? answer : answer.toLowerCase();
    final correct = caseSensitive ? correctAnswer : correctAnswer.toLowerCase();

    if (userAnswer == correct) return true;

    if (acceptableAlternatives != null) {
      for (final alternative in acceptableAlternatives!) {
        final alt = caseSensitive ? alternative : alternative.toLowerCase();
        if (userAnswer == alt) return true;
      }
    }

    return false;
  }

  @override
  dynamic getCorrectAnswer() => correctAnswer;

  @override
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'type': 'fillInBlank',
      'question': question,
      'correctAnswer': correctAnswer,
      'acceptableAlternatives': acceptableAlternatives,
      'caseSensitive': caseSensitive,
      'audioHint': audioHint,
    };
  }

  factory FillInBlankExercise.fromJson(Map<String, dynamic> json) {
    return FillInBlankExercise(
      id: json['id'],
      question: json['question'],
      correctAnswer: json['correctAnswer'],
      acceptableAlternatives: json['acceptableAlternatives'] != null
          ? List<String>.from(json['acceptableAlternatives'])
          : null,
      caseSensitive: json['caseSensitive'] ?? false,
      audioHint: json['audioHint'],
    );
  }
}

class MatchingPair {
  final String left;
  final String right;

  MatchingPair({
    required this.left,
    required this.right,
  });

  Map<String, dynamic> toJson() {
    return {
      'left': left,
      'right': right,
    };
  }

  factory MatchingPair.fromJson(Map<String, dynamic> json) {
    return MatchingPair(
      left: json['left'],
      right: json['right'],
    );
  }
}

class MatchingExercise extends Exercise {
  final List<MatchingPair> pairs;

  MatchingExercise({
    required String id,
    required String question,
    required this.pairs,
    String? audioHint,
  }) : super(
          id: id,
          type: ExerciseType.matching,
          question: question,
          audioHint: audioHint,
        );

  @override
  bool checkAnswer(dynamic answer) {
    if (answer is! Map<String, String>) return false;

    for (final pair in pairs) {
      if (answer[pair.left] != pair.right) {
        return false;
      }
    }

    return answer.length == pairs.length;
  }

  @override
  dynamic getCorrectAnswer() {
    return Map.fromEntries(
      pairs.map((pair) => MapEntry(pair.left, pair.right)),
    );
  }

  @override
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'type': 'matching',
      'question': question,
      'pairs': pairs.map((p) => p.toJson()).toList(),
      'audioHint': audioHint,
    };
  }

  factory MatchingExercise.fromJson(Map<String, dynamic> json) {
    return MatchingExercise(
      id: json['id'],
      question: json['question'],
      pairs: (json['pairs'] as List)
          .map((p) => MatchingPair.fromJson(p))
          .toList(),
      audioHint: json['audioHint'],
    );
  }
}

class TranslationExercise extends Exercise {
  final String targetText;
  final String correctTranslation;
  final List<String>? acceptableAlternatives;

  TranslationExercise({
    required String id,
    required String question,
    required this.targetText,
    required this.correctTranslation,
    this.acceptableAlternatives,
    String? audioHint,
  }) : super(
          id: id,
          type: ExerciseType.translation,
          question: question,
          audioHint: audioHint,
        );

  @override
  bool checkAnswer(dynamic answer) {
    if (answer is! String) return false;

    final userAnswer = answer.trim().toLowerCase();
    final correct = correctTranslation.trim().toLowerCase();

    if (userAnswer == correct) return true;

    if (acceptableAlternatives != null) {
      for (final alternative in acceptableAlternatives!) {
        if (userAnswer == alternative.trim().toLowerCase()) {
          return true;
        }
      }
    }

    return false;
  }

  @override
  dynamic getCorrectAnswer() => correctTranslation;

  @override
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'type': 'translation',
      'question': question,
      'targetText': targetText,
      'correctTranslation': correctTranslation,
      'acceptableAlternatives': acceptableAlternatives,
      'audioHint': audioHint,
    };
  }

  factory TranslationExercise.fromJson(Map<String, dynamic> json) {
    return TranslationExercise(
      id: json['id'],
      question: json['question'],
      targetText: json['targetText'],
      correctTranslation: json['correctTranslation'],
      acceptableAlternatives: json['acceptableAlternatives'] != null
          ? List<String>.from(json['acceptableAlternatives'])
          : null,
      audioHint: json['audioHint'],
    );
  }
}

// Factory method to create exercises from JSON
Exercise exerciseFromJson(Map<String, dynamic> json) {
  switch (json['type']) {
    case 'multipleChoice':
      return MultipleChoiceExercise.fromJson(json);
    case 'fillInBlank':
      return FillInBlankExercise.fromJson(json);
    case 'matching':
      return MatchingExercise.fromJson(json);
    case 'translation':
      return TranslationExercise.fromJson(json);
    default:
      throw Exception('Unknown exercise type: ${json['type']}');
  }
}
