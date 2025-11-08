import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/language.dart';
import '../services/language_service.dart';
import '../services/progress_service.dart';
import '../utils/app_localizations.dart';
import '../widgets/language_card.dart';
import '../widgets/course_structure.dart';
import '../widgets/day_grid.dart';
import 'lesson_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Language? _selectedLanguage;

  @override
  Widget build(BuildContext context) {
    final languageService = Provider.of<LanguageService>(context);
    final progressService = Provider.of<ProgressService>(context);
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
            // Hero Section
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
                  Text(
                    loc.heroTitle,
                    style: const TextStyle(
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 12),
                  Text(
                    loc.heroSubtitle,
                    style: const TextStyle(
                      fontSize: 16,
                      color: Colors.white,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),

            // Language Selection
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Select Learning Language',
                    style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                  const SizedBox(height: 16),
                  ...Language.values.map((language) {
                    final completedCount =
                        progressService.getCompletedCount(language);
                    final currentDay = progressService.getCurrentDay(language);
                    final progress = progressService.getProgress(language);

                    return LanguageCard(
                      language: language,
                      completedCount: completedCount,
                      currentDay: currentDay,
                      progress: progress,
                      isSelected: _selectedLanguage == language,
                      onTap: () {
                        setState(() {
                          _selectedLanguage = language;
                        });
                      },
                    );
                  }).toList(),
                ],
              ),
            ),

            // Course Structure
            if (_selectedLanguage == null)
              const Padding(
                padding: EdgeInsets.all(16),
                child: CourseStructure(),
              ),

            // Day Grid (shown when language is selected)
            if (_selectedLanguage != null)
              Padding(
                padding: const EdgeInsets.all(16),
                child: DayGrid(
                  language: _selectedLanguage!,
                  onDaySelected: (day) {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => LessonScreen(
                          language: _selectedLanguage!,
                          initialDay: day,
                        ),
                      ),
                    );
                  },
                ),
              ),
          ],
        ),
      ),
    );
  }
}
