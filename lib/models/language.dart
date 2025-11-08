enum Language {
  english('en', 'English', '🇬🇧'),
  spanish('es', 'Español', '🇪🇸'),
  portuguese('pt', 'Português', '🇵🇹'),
  french('fr', 'Français', '🇫🇷'),
  german('de', 'Deutsch', '🇩🇪');

  final String code;
  final String name;
  final String flag;

  const Language(this.code, this.name, this.flag);

  static Language fromCode(String code) {
    return Language.values.firstWhere(
      (lang) => lang.code == code,
      orElse: () => Language.english,
    );
  }

  String getAudioFileName(int day) {
    return 'assets/audio/day${day}_$code.mp3';
  }

  String getTextFileName(int day) {
    return 'assets/text/day${day}_$code.txt';
  }
}
