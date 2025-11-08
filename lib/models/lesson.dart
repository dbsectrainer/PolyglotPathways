import 'package:flutter/services.dart';
import 'language.dart';

class Lesson {
  final int day;
  final Language language;
  final String title;
  final String description;
  final String audioPath;
  final String? textContent;

  Lesson({
    required this.day,
    required this.language,
    required this.title,
    required this.description,
    required this.audioPath,
    this.textContent,
  });

  String get phase {
    if (day >= 1 && day <= 7) {
      return 'Basic Vocabulary & Essential Phrases';
    } else if (day >= 8 && day <= 15) {
      return 'Advanced Communication for Intermediate Learners';
    } else if (day >= 16 && day <= 26) {
      return 'Global Living & Professional Skills';
    } else if (day >= 27 && day <= 31) {
      return 'Tech Professional Content';
    } else {
      return 'Advanced Academic & Professional Communication';
    }
  }

  static Lesson create(int day, Language language) {
    return Lesson(
      day: day,
      language: language,
      title: 'Day $day',
      description: _getDescription(day),
      audioPath: language.getAudioFileName(day),
    );
  }

  String getTextFilePath() {
    return 'assets/lessons/day${day}_${language.code}.txt';
  }

  Future<String> loadTextContent() async {
    try {
      return await rootBundle.loadString(getTextFilePath());
    } catch (e) {
      return 'Text content not available for this lesson.';
    }
  }

  static String _getDescription(int day) {
    final descriptions = {
      1: 'Greetings and Basic Introductions',
      2: 'Numbers and Counting',
      3: 'Days of the Week and Months',
      4: 'Basic Questions and Responses',
      5: 'Common Verbs and Actions',
      6: 'Food and Dining Vocabulary',
      7: 'Shopping and Transactions',
      8: 'Directions and Navigation',
      9: 'Travel and Transportation',
      10: 'Weather and Climate',
      11: 'Health and Medical Terms',
      12: 'Family and Relationships',
      13: 'Hobbies and Interests',
      14: 'Technology and Digital Life',
      15: 'Education and Learning',
      16: 'Work and Career',
      17: 'Housing and Accommodation',
      18: 'Clothing and Fashion',
      19: 'Sports and Fitness',
      20: 'Entertainment and Media',
      21: 'Environment and Nature',
      22: 'Culture and Traditions',
      23: 'Government and Politics',
      24: 'Law and Justice',
      25: 'Economy and Finance',
      26: 'Business Meetings and Presentations',
      27: 'Software Development',
      28: 'Data Science and Analytics',
      29: 'Cybersecurity',
      30: 'Cloud Computing',
      31: 'AI and Machine Learning',
      32: 'Academic Writing',
      33: 'Research Methods',
      34: 'Critical Thinking',
      35: 'Public Speaking',
      36: 'Negotiation Skills',
      37: 'Leadership and Management',
      38: 'Project Management',
      39: 'Marketing and Branding',
      40: 'Sales and Customer Relations',
      41: 'International Relations',
      42: 'Philosophy and Ethics',
      43: 'Psychology and Behavior',
      44: 'Sociology and Society',
      45: 'History and Heritage',
      46: 'Art and Aesthetics',
      47: 'Literature and Writing',
      48: 'Music and Performance',
      49: 'Science and Innovation',
      50: 'Future Trends and Technology',
    };
    return descriptions[day] ?? 'Lesson $day';
  }
}
