import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:polyglot_pathways/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  // Get language from environment variable or default to 'en'
  const String languageCode = String.fromEnvironment(
    'SCREENSHOT_LANGUAGE',
    defaultValue: 'en',
  );

  group('Screenshot Tests', () {
    testWidgets('Generate screenshots for $languageCode', (WidgetTester tester) async {
      // Clear SharedPreferences to start fresh
      final prefs = await SharedPreferences.getInstance();
      await prefs.clear();

      // Set the language
      await prefs.setString('selectedLanguage', languageCode);
      
      // Set onboarding as completed so we can navigate to main screens
      await prefs.setBool('has_completed_onboarding', true);

      // Build the app
      await tester.pumpWidget(app.MyApp(prefs: prefs));
      await tester.pumpAndSettle(const Duration(seconds: 2));

      // Wait for any animations
      await Future.delayed(const Duration(milliseconds: 500));

      // Screenshot: Home Screen
      await takeScreenshot(tester, '01_home');

      // Navigate to Achievements tab
      await tester.tap(find.text('Achievements').last);
      await tester.pumpAndSettle(const Duration(seconds: 2));
      await Future.delayed(const Duration(milliseconds: 500));
      await takeScreenshot(tester, '02_achievements');

      // Navigate to Profile tab
      await tester.tap(find.text('Profile').last);
      await tester.pumpAndSettle(const Duration(seconds: 2));
      await Future.delayed(const Duration(milliseconds: 500));
      await takeScreenshot(tester, '03_profile');

      // Navigate to Settings tab
      await tester.tap(find.text('Settings').last);
      await tester.pumpAndSettle(const Duration(seconds: 2));
      await Future.delayed(const Duration(milliseconds: 500));
      await takeScreenshot(tester, '04_settings');

      // Go back to Home tab
      await tester.tap(find.text('Home').last);
      await tester.pumpAndSettle(const Duration(seconds: 2));
      await Future.delayed(const Duration(milliseconds: 500));

      // Try to open language selection - look for language cards more carefully
      // First, scroll if needed to see language cards
      try {
        final scrollable = find.byType(Scrollable);
        if (scrollable.evaluate().isNotEmpty) {
          await tester.drag(scrollable.first, const Offset(0, -200));
          await tester.pumpAndSettle(const Duration(seconds: 1));
        }
      } catch (e) {
        // Ignore if scroll fails
      }
      
      // Try to find and tap a language card by looking for InkWell widgets
      // that are likely language cards (they're tappable)
      try {
        final inkWells = find.byType(InkWell);
        if (inkWells.evaluate().length > 2) {
          // Skip the first few (might be navigation), tap a language card
          await tester.tap(inkWells.at(2));
          await tester.pumpAndSettle(const Duration(seconds: 2));
          await Future.delayed(const Duration(milliseconds: 500));
          await takeScreenshot(tester, '05_language_selection');
          
          // Try to close the sheet and go back
          final closeButton = find.byIcon(Icons.close);
          if (closeButton.evaluate().isNotEmpty) {
            await tester.tap(closeButton.first);
            await tester.pumpAndSettle(const Duration(seconds: 1));
          }
        }
      } catch (e) {
        // If language selection fails, continue with onboarding screens
        print('Could not capture language selection: $e');
      }

      // For onboarding screens, we need to restart the app
      // This is complex in integration tests, so we'll skip for now
      // and focus on the main app screens which are more important
    });
  });
}

Future<void> takeScreenshot(WidgetTester tester, String name) async {
  await tester.binding.defaultBinaryMessenger.handlePlatformMessage(
    'flutter/screenshot',
    null,
    (ByteData? data) {},
  );
  
  await IntegrationTestWidgetsFlutterBinding.instance.takeScreenshot(name);
}

