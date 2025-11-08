import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class AppLocalizations {
  final Locale locale;
  late Map<String, dynamic> _localizedStrings;
  late Map<String, dynamic> _dayLocalizedStrings;

  AppLocalizations(this.locale);

  static AppLocalizations of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations)!;
  }

  static const LocalizationsDelegate<AppLocalizations> delegate =
      _AppLocalizationsDelegate();

  Future<bool> load() async {
    try {
      // Load main translations
      String jsonString =
          await rootBundle.loadString('assets/translations/${locale.languageCode}.json');
      _localizedStrings = json.decode(jsonString);

      // Load day/lesson translations
      String dayJsonString =
          await rootBundle.loadString('assets/translations/day.${locale.languageCode}.json');
      _dayLocalizedStrings = json.decode(dayJsonString);

      return true;
    } catch (e) {
      debugPrint('Error loading translations: $e');
      return false;
    }
  }

  String translate(String key, {Map<String, String>? params}) {
    String? value = _getNestedValue(_localizedStrings, key) ??
        _getNestedValue(_dayLocalizedStrings, key);

    if (value == null) {
      return key;
    }

    if (params != null) {
      params.forEach((paramKey, paramValue) {
        value = value!.replaceAll('{$paramKey}', paramValue);
      });
    }

    return value!;
  }

  String? _getNestedValue(Map<String, dynamic> map, String key) {
    final keys = key.split('.');
    dynamic value = map;

    for (final k in keys) {
      if (value is Map<String, dynamic> && value.containsKey(k)) {
        value = value[k];
      } else {
        return null;
      }
    }

    return value?.toString();
  }

  // Convenience getters for common translations
  String get appTitle => translate('header.title');
  String get appSubtitle => translate('header.subtitle');
  String get heroTitle => translate('hero.title');
  String get heroSubtitle => translate('hero.subtitle');

  // Day/Lesson specific
  String get previousDay => translate('navigation.previousDay');
  String get nextDay => translate('navigation.nextDay');
  String get backToHome => translate('navigation.backToHome');
  String get markComplete => translate('lesson.markComplete');
  String get completed => translate('lesson.completed');
  String get dayMarkedComplete => translate('lesson.dayMarkedComplete');

  // Languages
  String languageName(String code) {
    return translate('languages.$code');
  }
}

class _AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizations> {
  const _AppLocalizationsDelegate();

  @override
  bool isSupported(Locale locale) {
    return ['en', 'es', 'pt', 'fr', 'de'].contains(locale.languageCode);
  }

  @override
  Future<AppLocalizations> load(Locale locale) async {
    AppLocalizations localizations = AppLocalizations(locale);
    await localizations.load();
    return localizations;
  }

  @override
  bool shouldReload(_AppLocalizationsDelegate old) => false;
}
