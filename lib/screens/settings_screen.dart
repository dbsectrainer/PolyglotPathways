import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_animate/flutter_animate.dart';
import '../models/language.dart';
import '../services/language_service.dart';
import '../services/settings_service.dart';
import '../services/progress_service.dart';
import '../services/gamification_service.dart';
import '../theme/app_theme.dart';
import 'onboarding_screen.dart';

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final settingsService = Provider.of<SettingsService>(context);
    final languageService = Provider.of<LanguageService>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Appearance Section
            _buildSection(
              context,
              title: 'Appearance',
              icon: Icons.palette,
              children: [
                _buildSwitchTile(
                  context,
                  title: 'Dark Mode',
                  subtitle: 'Use dark theme',
                  icon: Icons.dark_mode,
                  value: settingsService.isDarkMode,
                  onChanged: (value) => settingsService.toggleDarkMode(),
                ),
                _buildSliderTile(
                  context,
                  title: 'Text Size',
                  subtitle: settingsService.getTextScaleLabel(),
                  icon: Icons.format_size,
                  value: settingsService.textScale,
                  min: 0.85,
                  max: 1.3,
                  divisions: 9,
                  onChanged: (value) => settingsService.setTextScale(value),
                ),
              ],
            ).animate().fadeIn(delay: 100.ms).slideX(begin: -0.1),

            // Learning Section
            _buildSection(
              context,
              title: 'Learning',
              icon: Icons.school,
              children: [
                _buildSliderTile(
                  context,
                  title: 'Daily Goal',
                  subtitle: '${settingsService.dailyGoal} ${settingsService.dailyGoal == 1 ? "lesson" : "lessons"} per day',
                  icon: Icons.track_changes,
                  value: settingsService.dailyGoal.toDouble(),
                  min: 1,
                  max: 10,
                  divisions: 9,
                  onChanged: (value) =>
                      settingsService.setDailyGoal(value.toInt()),
                ),
                _buildSwitchTile(
                  context,
                  title: 'Show Hints',
                  subtitle: 'Display helpful tips and hints',
                  icon: Icons.lightbulb_outline,
                  value: settingsService.showHints,
                  onChanged: (value) => settingsService.toggleHints(),
                ),
              ],
            ).animate().fadeIn(delay: 200.ms).slideX(begin: -0.1),

            // Audio & Sound Section
            _buildSection(
              context,
              title: 'Audio & Sound',
              icon: Icons.volume_up,
              children: [
                _buildSwitchTile(
                  context,
                  title: 'Sound Effects',
                  subtitle: 'Play sounds for actions',
                  icon: Icons.music_note,
                  value: settingsService.soundEnabled,
                  onChanged: (value) => settingsService.toggleSound(),
                ),
              ],
            ).animate().fadeIn(delay: 300.ms).slideX(begin: -0.1),

            // Notifications Section
            _buildSection(
              context,
              title: 'Notifications',
              icon: Icons.notifications,
              children: [
                _buildSwitchTile(
                  context,
                  title: 'Daily Reminders',
                  subtitle: 'Get reminded to practice',
                  icon: Icons.alarm,
                  value: settingsService.notificationsEnabled,
                  onChanged: (value) => settingsService.toggleNotifications(),
                ),
              ],
            ).animate().fadeIn(delay: 400.ms).slideX(begin: -0.1),

            // Language Section
            _buildSection(
              context,
              title: 'Interface Language',
              icon: Icons.language,
              children: [
                _buildLanguageSelector(context, languageService),
              ],
            ).animate().fadeIn(delay: 500.ms).slideX(begin: -0.1),

            // About Section
            _buildSection(
              context,
              title: 'About',
              icon: Icons.info,
              children: [
                _buildActionTile(
                  context,
                  title: 'Tutorial',
                  subtitle: 'View onboarding again',
                  icon: Icons.help_outline,
                  onTap: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (context) => const OnboardingScreen(),
                      ),
                    );
                  },
                ),
                _buildActionTile(
                  context,
                  title: 'App Version',
                  subtitle: '1.0.0',
                  icon: Icons.info_outline,
                  onTap: null,
                ),
              ],
            ).animate().fadeIn(delay: 600.ms).slideX(begin: -0.1),

            // Danger Zone
            _buildSection(
              context,
              title: 'Data Management',
              icon: Icons.warning,
              children: [
                _buildActionTile(
                  context,
                  title: 'Reset Settings',
                  subtitle: 'Restore default settings',
                  icon: Icons.restart_alt,
                  onTap: () => _showResetSettingsDialog(context),
                ),
                _buildActionTile(
                  context,
                  title: 'Reset Progress',
                  subtitle: 'Clear all learning progress',
                  icon: Icons.delete_forever,
                  onTap: () => _showResetProgressDialog(context),
                  textColor: Colors.red,
                ),
              ],
            ).animate().fadeIn(delay: 700.ms).slideX(begin: -0.1),

            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }

  Widget _buildSection(
    BuildContext context, {
    required String title,
    required IconData icon,
    required List<Widget> children,
  }) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: Card(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: const EdgeInsets.all(16),
              child: Row(
                children: [
                  Icon(icon, color: AppTheme.primaryBlue, size: 24),
                  const SizedBox(width: 12),
                  Text(
                    title,
                    style: const TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ],
              ),
            ),
            const Divider(height: 1),
            ...children,
          ],
        ),
      ),
    );
  }

  Widget _buildSwitchTile(
    BuildContext context, {
    required String title,
    required String subtitle,
    required IconData icon,
    required bool value,
    required Function(bool) onChanged,
  }) {
    return ListTile(
      leading: Icon(icon, color: AppTheme.primaryBlue),
      title: Text(title, style: const TextStyle(fontWeight: FontWeight.w500)),
      subtitle: Text(subtitle),
      trailing: Switch(
        value: value,
        onChanged: onChanged,
        activeColor: AppTheme.primaryBlue,
      ),
    );
  }

  Widget _buildSliderTile(
    BuildContext context, {
    required String title,
    required String subtitle,
    required IconData icon,
    required double value,
    required double min,
    required double max,
    required int divisions,
    required Function(double) onChanged,
  }) {
    return ListTile(
      leading: Icon(icon, color: AppTheme.primaryBlue),
      title: Text(title, style: const TextStyle(fontWeight: FontWeight.w500)),
      subtitle: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(subtitle),
          Slider(
            value: value,
            min: min,
            max: max,
            divisions: divisions,
            onChanged: onChanged,
            activeColor: AppTheme.primaryBlue,
          ),
        ],
      ),
    );
  }

  Widget _buildActionTile(
    BuildContext context, {
    required String title,
    required String subtitle,
    required IconData icon,
    required VoidCallback? onTap,
    Color? textColor,
  }) {
    return ListTile(
      leading: Icon(icon, color: textColor ?? AppTheme.primaryBlue),
      title: Text(
        title,
        style: TextStyle(
          fontWeight: FontWeight.w500,
          color: textColor,
        ),
      ),
      subtitle: Text(subtitle),
      onTap: onTap,
      trailing: onTap != null
          ? Icon(Icons.chevron_right, color: Colors.grey[400])
          : null,
    );
  }

  Widget _buildLanguageSelector(
    BuildContext context,
    LanguageService languageService,
  ) {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Wrap(
        spacing: 8,
        runSpacing: 8,
        children: Language.values.map((language) {
          final isSelected =
              languageService.currentLanguage.code == language.code;
          return ChoiceChip(
            label: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(language.flag, style: const TextStyle(fontSize: 20)),
                const SizedBox(width: 8),
                Text(language.name),
              ],
            ),
            selected: isSelected,
            onSelected: (selected) {
              if (selected) {
                languageService.setLanguage(language);
              }
            },
            selectedColor: AppTheme.primaryBlue.withOpacity(0.2),
            backgroundColor: Colors.grey[200],
          );
        }).toList(),
      ),
    );
  }

  void _showResetSettingsDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Reset Settings'),
          content: const Text(
            'Are you sure you want to reset all settings to default values? This cannot be undone.',
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancel'),
            ),
            ElevatedButton(
              onPressed: () {
                Provider.of<SettingsService>(context, listen: false)
                    .resetAllSettings();
                Navigator.of(context).pop();
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Settings reset successfully')),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: AppTheme.primaryBlue,
              ),
              child: const Text('Reset'),
            ),
          ],
        );
      },
    );
  }

  void _showResetProgressDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Reset Progress'),
          content: const Text(
            'Are you sure you want to delete all your learning progress, streaks, and achievements? This action cannot be undone!',
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancel'),
            ),
            ElevatedButton(
              onPressed: () {
                Provider.of<ProgressService>(context, listen: false).resetAll();
                Provider.of<GamificationService>(context, listen: false)
                    .resetAll();
                Navigator.of(context).pop();
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('All progress has been reset'),
                    backgroundColor: Colors.red,
                  ),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.red,
              ),
              child: const Text('Delete All'),
            ),
          ],
        );
      },
    );
  }
}
