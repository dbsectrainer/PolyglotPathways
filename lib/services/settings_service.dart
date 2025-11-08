import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SettingsService extends ChangeNotifier {
  static const String _darkModeKey = 'dark_mode';
  static const String _textScaleKey = 'text_scale';
  static const String _showHintsKey = 'show_hints';
  static const String _dailyGoalKey = 'daily_goal';
  static const String _notificationsEnabledKey = 'notifications_enabled';
  static const String _soundEnabledKey = 'sound_enabled';
  static const String _hasCompletedOnboardingKey = 'has_completed_onboarding';

  bool _isDarkMode = false;
  double _textScale = 1.0;
  bool _showHints = true;
  int _dailyGoal = 1; // lessons per day
  bool _notificationsEnabled = true;
  bool _soundEnabled = true;
  bool _hasCompletedOnboarding = false;

  bool get isDarkMode => _isDarkMode;
  double get textScale => _textScale;
  bool get showHints => _showHints;
  int get dailyGoal => _dailyGoal;
  bool get notificationsEnabled => _notificationsEnabled;
  bool get soundEnabled => _soundEnabled;
  bool get hasCompletedOnboarding => _hasCompletedOnboarding;

  ThemeMode get themeMode => _isDarkMode ? ThemeMode.dark : ThemeMode.light;

  SettingsService() {
    _loadSettings();
  }

  Future<void> _loadSettings() async {
    final prefs = await SharedPreferences.getInstance();
    _isDarkMode = prefs.getBool(_darkModeKey) ?? false;
    _textScale = prefs.getDouble(_textScaleKey) ?? 1.0;
    _showHints = prefs.getBool(_showHintsKey) ?? true;
    _dailyGoal = prefs.getInt(_dailyGoalKey) ?? 1;
    _notificationsEnabled = prefs.getBool(_notificationsEnabledKey) ?? true;
    _soundEnabled = prefs.getBool(_soundEnabledKey) ?? true;
    _hasCompletedOnboarding = prefs.getBool(_hasCompletedOnboardingKey) ?? false;
    notifyListeners();
  }

  Future<void> toggleDarkMode() async {
    _isDarkMode = !_isDarkMode;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_darkModeKey, _isDarkMode);
    notifyListeners();
  }

  Future<void> setTextScale(double scale) async {
    if (scale >= 0.8 && scale <= 1.5) {
      _textScale = scale;
      final prefs = await SharedPreferences.getInstance();
      await prefs.setDouble(_textScaleKey, scale);
      notifyListeners();
    }
  }

  Future<void> toggleHints() async {
    _showHints = !_showHints;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_showHintsKey, _showHints);
    notifyListeners();
  }

  Future<void> setDailyGoal(int goal) async {
    if (goal >= 1 && goal <= 10) {
      _dailyGoal = goal;
      final prefs = await SharedPreferences.getInstance();
      await prefs.setInt(_dailyGoalKey, goal);
      notifyListeners();
    }
  }

  Future<void> toggleNotifications() async {
    _notificationsEnabled = !_notificationsEnabled;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_notificationsEnabledKey, _notificationsEnabled);
    notifyListeners();
  }

  Future<void> toggleSound() async {
    _soundEnabled = !_soundEnabled;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_soundEnabledKey, _soundEnabled);
    notifyListeners();
  }

  Future<void> completeOnboarding() async {
    _hasCompletedOnboarding = true;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_hasCompletedOnboardingKey, true);
    notifyListeners();
  }

  Future<void> resetOnboarding() async {
    _hasCompletedOnboarding = false;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_hasCompletedOnboardingKey, false);
    notifyListeners();
  }

  Future<void> resetAllSettings() async {
    _isDarkMode = false;
    _textScale = 1.0;
    _showHints = true;
    _dailyGoal = 1;
    _notificationsEnabled = true;
    _soundEnabled = true;
    // Don't reset onboarding

    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_darkModeKey, false);
    await prefs.setDouble(_textScaleKey, 1.0);
    await prefs.setBool(_showHintsKey, true);
    await prefs.setInt(_dailyGoalKey, 1);
    await prefs.setBool(_notificationsEnabledKey, true);
    await prefs.setBool(_soundEnabledKey, true);

    notifyListeners();
  }

  // Text scale presets
  static const double textScaleSmall = 0.85;
  static const double textScaleNormal = 1.0;
  static const double textScaleLarge = 1.15;
  static const double textScaleExtraLarge = 1.3;

  String getTextScaleLabel() {
    if (_textScale <= 0.9) return 'Small';
    if (_textScale <= 1.05) return 'Normal';
    if (_textScale <= 1.2) return 'Large';
    return 'Extra Large';
  }
}
