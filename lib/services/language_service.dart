import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/language.dart';

class LanguageService extends ChangeNotifier {
  final SharedPreferences _prefs;
  Language _currentLanguage = Language.english;

  LanguageService(this._prefs) {
    _loadLanguage();
  }

  Language get currentLanguage => _currentLanguage;

  Locale get currentLocale => Locale(_currentLanguage.code);

  void _loadLanguage() {
    final languageCode = _prefs.getString('selectedLanguage') ?? 'en';
    _currentLanguage = Language.fromCode(languageCode);
    notifyListeners();
  }

  Future<void> setLanguage(Language language) async {
    _currentLanguage = language;
    await _prefs.setString('selectedLanguage', language.code);
    notifyListeners();
  }

  Future<void> setLanguageByCode(String code) async {
    final language = Language.fromCode(code);
    await setLanguage(language);
  }
}
