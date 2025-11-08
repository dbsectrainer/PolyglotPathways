import 'package:flutter/material.dart';

class AppTheme {
  // Primary colors
  static const Color primaryBlue = Color(0xFF4A90E2);
  static const Color secondaryGreen = Color(0xFF50C878);
  static const Color accentOrange = Color(0xFFFF9500);
  static const Color accentPurple = Color(0xFF9B59B6);

  // Light theme colors
  static const Color lightBackground = Color(0xFFF8F9FA);
  static const Color lightSurface = Colors.white;
  static const Color lightOnSurface = Color(0xFF2C3E50);
  static const Color lightCardBackground = Colors.white;

  // Dark theme colors
  static const Color darkBackground = Color(0xFF121212);
  static const Color darkSurface = Color(0xFF1E1E1E);
  static const Color darkOnSurface = Color(0xFFE0E0E0);
  static const Color darkCardBackground = Color(0xFF2C2C2C);

  // Gradient colors
  static const List<Color> primaryGradient = [primaryBlue, secondaryGreen];
  static const List<Color> accentGradient = [accentOrange, accentPurple];

  // Achievement badge colors
  static const Color bronzeBadge = Color(0xFFCD7F32);
  static const Color silverBadge = Color(0xFFC0C0C0);
  static const Color goldBadge = Color(0xFFFFD700);

  // Light Theme
  static ThemeData lightTheme = ThemeData(
    useMaterial3: true,
    brightness: Brightness.light,
    colorScheme: ColorScheme.fromSeed(
      seedColor: primaryBlue,
      brightness: Brightness.light,
      primary: primaryBlue,
      secondary: secondaryGreen,
      tertiary: accentOrange,
      surface: lightSurface,
      background: lightBackground,
      onSurface: lightOnSurface,
    ),
    scaffoldBackgroundColor: lightBackground,
    appBarTheme: const AppBarTheme(
      backgroundColor: primaryBlue,
      foregroundColor: Colors.white,
      elevation: 0,
      centerTitle: true,
      iconTheme: IconThemeData(color: Colors.white),
    ),
    cardTheme: CardTheme(
      color: lightCardBackground,
      elevation: 2,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: primaryBlue,
        foregroundColor: Colors.white,
        elevation: 2,
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    ),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        foregroundColor: primaryBlue,
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      ),
    ),
    bottomNavigationBarTheme: const BottomNavigationBarThemeData(
      backgroundColor: Colors.white,
      selectedItemColor: primaryBlue,
      unselectedItemColor: Colors.grey,
      type: BottomNavigationBarType.fixed,
      elevation: 8,
    ),
    progressIndicatorTheme: const ProgressIndicatorThemeData(
      color: primaryBlue,
      linearTrackColor: Color(0xFFE0E0E0),
    ),
    sliderTheme: SliderThemeData(
      activeTrackColor: primaryBlue,
      inactiveTrackColor: primaryBlue.withOpacity(0.3),
      thumbColor: primaryBlue,
      overlayColor: primaryBlue.withOpacity(0.2),
    ),
    chipTheme: ChipThemeData(
      backgroundColor: primaryBlue.withOpacity(0.1),
      labelStyle: const TextStyle(color: primaryBlue),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(20),
      ),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: Colors.grey[100],
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(color: primaryBlue, width: 2),
      ),
    ),
  );

  // Dark Theme
  static ThemeData darkTheme = ThemeData(
    useMaterial3: true,
    brightness: Brightness.dark,
    colorScheme: ColorScheme.fromSeed(
      seedColor: primaryBlue,
      brightness: Brightness.dark,
      primary: primaryBlue,
      secondary: secondaryGreen,
      tertiary: accentOrange,
      surface: darkSurface,
      background: darkBackground,
      onSurface: darkOnSurface,
    ),
    scaffoldBackgroundColor: darkBackground,
    appBarTheme: const AppBarTheme(
      backgroundColor: darkSurface,
      foregroundColor: Colors.white,
      elevation: 0,
      centerTitle: true,
      iconTheme: IconThemeData(color: Colors.white),
    ),
    cardTheme: CardTheme(
      color: darkCardBackground,
      elevation: 4,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: primaryBlue,
        foregroundColor: Colors.white,
        elevation: 2,
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
    ),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        foregroundColor: primaryBlue,
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      ),
    ),
    bottomNavigationBarTheme: const BottomNavigationBarThemeData(
      backgroundColor: darkSurface,
      selectedItemColor: primaryBlue,
      unselectedItemColor: Colors.grey,
      type: BottomNavigationBarType.fixed,
      elevation: 8,
    ),
    progressIndicatorTheme: const ProgressIndicatorThemeData(
      color: primaryBlue,
      linearTrackColor: Color(0xFF424242),
    ),
    sliderTheme: SliderThemeData(
      activeTrackColor: primaryBlue,
      inactiveTrackColor: primaryBlue.withOpacity(0.3),
      thumbColor: primaryBlue,
      overlayColor: primaryBlue.withOpacity(0.2),
    ),
    chipTheme: ChipThemeData(
      backgroundColor: primaryBlue.withOpacity(0.2),
      labelStyle: const TextStyle(color: Colors.white),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(20),
      ),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: darkSurface,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: BorderSide.none,
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(12),
        borderSide: const BorderSide(color: primaryBlue, width: 2),
      ),
    ),
  );

  // Text Styles
  static TextStyle headlineLarge(BuildContext context) => Theme.of(context).textTheme.headlineLarge!.copyWith(
        fontWeight: FontWeight.bold,
        color: Theme.of(context).colorScheme.onSurface,
      );

  static TextStyle headlineMedium(BuildContext context) => Theme.of(context).textTheme.headlineMedium!.copyWith(
        fontWeight: FontWeight.w600,
        color: Theme.of(context).colorScheme.onSurface,
      );

  static TextStyle titleLarge(BuildContext context) => Theme.of(context).textTheme.titleLarge!.copyWith(
        fontWeight: FontWeight.w600,
        color: Theme.of(context).colorScheme.onSurface,
      );

  static TextStyle bodyLarge(BuildContext context) => Theme.of(context).textTheme.bodyLarge!.copyWith(
        color: Theme.of(context).colorScheme.onSurface,
      );

  static TextStyle bodyMedium(BuildContext context) => Theme.of(context).textTheme.bodyMedium!.copyWith(
        color: Theme.of(context).colorScheme.onSurface.withOpacity(0.8),
      );

  // Gradient decorations
  static BoxDecoration primaryGradientDecoration({double borderRadius = 0}) {
    return BoxDecoration(
      gradient: const LinearGradient(
        colors: primaryGradient,
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
      ),
      borderRadius: BorderRadius.circular(borderRadius),
    );
  }

  static BoxDecoration accentGradientDecoration({double borderRadius = 0}) {
    return BoxDecoration(
      gradient: const LinearGradient(
        colors: accentGradient,
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
      ),
      borderRadius: BorderRadius.circular(borderRadius),
    );
  }

  // Shadow styles
  static List<BoxShadow> cardShadow(BuildContext context) {
    return [
      BoxShadow(
        color: Theme.of(context).brightness == Brightness.light
            ? Colors.black.withOpacity(0.1)
            : Colors.black.withOpacity(0.3),
        blurRadius: 8,
        offset: const Offset(0, 2),
      ),
    ];
  }
}
