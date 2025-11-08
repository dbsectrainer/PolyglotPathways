import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'screens/onboarding_screen.dart';
import 'screens/main_navigation_screen.dart';
import 'services/language_service.dart';
import 'services/progress_service.dart';
import 'services/settings_service.dart';
import 'services/gamification_service.dart';
import 'utils/app_localizations.dart';
import 'theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final prefs = await SharedPreferences.getInstance();
  runApp(MyApp(prefs: prefs));
}

class MyApp extends StatelessWidget {
  final SharedPreferences prefs;

  const MyApp({super.key, required this.prefs});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (_) => SettingsService(),
        ),
        ChangeNotifierProvider(
          create: (_) => LanguageService(prefs),
        ),
        ChangeNotifierProvider(
          create: (_) => ProgressService(prefs),
        ),
        ChangeNotifierProvider(
          create: (_) => GamificationService(),
        ),
      ],
      child: Consumer2<LanguageService, SettingsService>(
        builder: (context, languageService, settingsService, _) {
          return MaterialApp(
            title: 'Polyglot Pathways',
            debugShowCheckedModeBanner: false,

            // Theme configuration with dark mode support
            theme: AppTheme.lightTheme,
            darkTheme: AppTheme.darkTheme,
            themeMode: settingsService.themeMode,

            // Text scaling for accessibility
            builder: (context, child) {
              return MediaQuery(
                data: MediaQuery.of(context).copyWith(
                  textScaler: TextScaler.linear(settingsService.textScale),
                ),
                child: child!,
              );
            },

            locale: languageService.currentLocale,
            supportedLocales: const [
              Locale('en'),
              Locale('es'),
              Locale('pt'),
              Locale('fr'),
              Locale('de'),
            ],
            localizationsDelegates: const [
              AppLocalizations.delegate,
              GlobalMaterialLocalizations.delegate,
              GlobalWidgetsLocalizations.delegate,
              GlobalCupertinoLocalizations.delegate,
            ],

            // Show onboarding on first launch, otherwise show main navigation
            home: settingsService.hasCompletedOnboarding
                ? const MainNavigationScreen()
                : const OnboardingScreen(),
          );
        },
      ),
    );
  }
}
