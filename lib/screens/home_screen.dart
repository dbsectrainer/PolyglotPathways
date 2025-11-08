import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:fl_chart/fl_chart.dart';
import '../models/language.dart';
import '../services/language_service.dart';
import '../services/progress_service.dart';
import '../services/gamification_service.dart';
import '../services/settings_service.dart';
import '../utils/app_localizations.dart';
import '../widgets/language_card.dart';
import '../widgets/course_structure.dart';
import '../widgets/daily_lessons_sheet.dart';
import '../theme/app_theme.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    final languageService = Provider.of<LanguageService>(context);
    final progressService = Provider.of<ProgressService>(context);
    final gamificationService = Provider.of<GamificationService>(context);
    final settingsService = Provider.of<SettingsService>(context);
    final loc = AppLocalizations.of(context);

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              loc.appTitle,
              style: const TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
            Text(
              loc.appSubtitle,
              style: const TextStyle(
                fontSize: 12,
                fontWeight: FontWeight.w300,
              ),
            ),
          ],
        ),
        actions: [
          PopupMenuButton<Language>(
            icon: const Icon(Icons.language),
            tooltip: 'Change UI Language',
            onSelected: (Language language) {
              languageService.setLanguage(language);
            },
            itemBuilder: (BuildContext context) {
              return Language.values.map((Language language) {
                return PopupMenuItem<Language>(
                  value: language,
                  child: Row(
                    children: [
                      Text(
                        language.flag,
                        style: const TextStyle(fontSize: 20),
                      ),
                      const SizedBox(width: 8),
                      Text(language.name),
                    ],
                  ),
                );
              }).toList();
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Hero Section with Streak
            Container(
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [
                    Theme.of(context).colorScheme.primary,
                    Theme.of(context).colorScheme.secondary,
                  ],
                ),
              ),
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        Icons.local_fire_department,
                        color: gamificationService.streak.currentStreak > 0
                            ? Colors.orange
                            : Colors.white70,
                        size: 32,
                      ),
                      const SizedBox(width: 8),
                      Text(
                        '${gamificationService.streak.currentStreak} Day Streak',
                        style: const TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                    ],
                  ).animate().fadeIn().slideY(begin: -0.3, duration: 600.ms),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      _buildStatCard(
                        icon: Icons.emoji_events,
                        value: gamificationService.achievementCount.toString(),
                        label: 'Achievements',
                      ),
                      _buildStatCard(
                        icon: Icons.check_circle,
                        value: gamificationService.streak.totalLessonsCompleted
                            .toString(),
                        label: 'Lessons',
                      ),
                      _buildStatCard(
                        icon: Icons.military_tech,
                        value: gamificationService.streak.longestStreak
                            .toString(),
                        label: 'Best Streak',
                      ),
                    ],
                  ).animate().fadeIn(delay: 300.ms).slideY(begin: -0.2),
                ],
              ),
            ),

            // Daily Goal Progress
            if (settingsService.dailyGoal > 0)
              _buildDailyGoalCard(gamificationService, settingsService)
                  .animate()
                  .fadeIn(delay: 400.ms)
                  .slideY(begin: 0.1),

            // Language Selection
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Select Learning Language',
                    style:
                        Theme.of(context).textTheme.headlineSmall?.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                  ),
                  const SizedBox(height: 16),
                  ...Language.values.asMap().entries.map((entry) {
                    final index = entry.key;
                    final language = entry.value;
                    final completedCount =
                        progressService.getCompletedCount(language);
                    final currentDay = progressService.getCurrentDay(language);
                    final progress = progressService.getProgress(language);

                    return LanguageCard(
                      language: language,
                      completedCount: completedCount,
                      currentDay: currentDay,
                      progress: progress,
                      isSelected: false,
                      onTap: () {
                        DailyLessonsSheet.show(context, language);
                      },
                    )
                        .animate()
                        .fadeIn(delay: (500 + index * 100).ms)
                        .slideX(begin: -0.1);
                  }),
                ],
              ),
            ),

            // Course Structure
            const Padding(
              padding: EdgeInsets.all(16),
              child: CourseStructure(),
            ).animate().fadeIn(delay: 800.ms),
          ],
        ),
      ),
    );
  }

  Widget _buildStatCard({
    required IconData icon,
    required String value,
    required String label,
  }) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: Colors.white.withValues(alpha: 0.2),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        children: [
          Icon(icon, color: Colors.white, size: 24),
          const SizedBox(height: 4),
          Text(
            value,
            style: const TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          Text(
            label,
            style: const TextStyle(
              fontSize: 12,
              color: Colors.white70,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDailyGoalCard(
    GamificationService gamificationService,
    SettingsService settingsService,
  ) {
    final now = DateTime.now();
    final lessonsToday = gamificationService.streak.getLessonsCompletedOnDate(now);
    final dailyGoal = settingsService.dailyGoal;
    final progress = (lessonsToday / dailyGoal).clamp(0.0, 1.0);

    return Padding(
      padding: const EdgeInsets.all(16.0),
      child: Card(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    'Daily Goal',
                    style: Theme.of(context).textTheme.titleLarge?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 12,
                      vertical: 6,
                    ),
                    decoration: BoxDecoration(
                      color: progress >= 1.0
                          ? AppTheme.secondaryGreen
                          : AppTheme.primaryBlue,
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      '$lessonsToday / $dailyGoal',
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              ClipRRect(
                borderRadius: BorderRadius.circular(8),
                child: LinearProgressIndicator(
                  value: progress,
                  minHeight: 8,
                  backgroundColor: Colors.grey[300],
                  valueColor: AlwaysStoppedAnimation<Color>(
                    progress >= 1.0
                        ? AppTheme.secondaryGreen
                        : AppTheme.primaryBlue,
                  ),
                ),
              ),
              if (progress >= 1.0)
                Padding(
                  padding: const EdgeInsets.only(top: 12.0),
                  child: Row(
                    children: [
                      Icon(
                        Icons.celebration,
                        color: AppTheme.secondaryGreen,
                        size: 20,
                      ),
                      const SizedBox(width: 8),
                      Text(
                        'Daily goal completed! Great job!',
                        style: TextStyle(
                          color: AppTheme.secondaryGreen,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ],
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
