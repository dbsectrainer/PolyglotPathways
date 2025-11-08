class VocabularyItem {
  final String word;
  final String translation;
  final String? phonetic;
  final String? example;
  final String? exampleTranslation;
  final String? audioPath;
  final String? imageUrl;
  final List<String>? tags;

  VocabularyItem({
    required this.word,
    required this.translation,
    this.phonetic,
    this.example,
    this.exampleTranslation,
    this.audioPath,
    this.imageUrl,
    this.tags,
  });

  Map<String, dynamic> toJson() {
    return {
      'word': word,
      'translation': translation,
      'phonetic': phonetic,
      'example': example,
      'exampleTranslation': exampleTranslation,
      'audioPath': audioPath,
      'imageUrl': imageUrl,
      'tags': tags,
    };
  }

  factory VocabularyItem.fromJson(Map<String, dynamic> json) {
    return VocabularyItem(
      word: json['word'],
      translation: json['translation'],
      phonetic: json['phonetic'],
      example: json['example'],
      exampleTranslation: json['exampleTranslation'],
      audioPath: json['audioPath'],
      imageUrl: json['imageUrl'],
      tags: json['tags'] != null ? List<String>.from(json['tags']) : null,
    );
  }
}
