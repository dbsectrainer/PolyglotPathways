import 'package:flutter/material.dart';
import 'package:badges/badges.dart' as badges;
import 'package:provider/provider.dart';
import '../services/gamification_service.dart';
import 'home_screen.dart';
import 'profile_screen.dart';
import 'achievements_screen.dart';
import 'settings_screen.dart';

class MainNavigationScreen extends StatefulWidget {
  const MainNavigationScreen({super.key});

  @override
  State<MainNavigationScreen> createState() => _MainNavigationScreenState();
}

class _MainNavigationScreenState extends State<MainNavigationScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = [
    const HomeScreen(),
    const AchievementsScreen(),
    const ProfileScreen(),
    const SettingsScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    final gamificationService = Provider.of<GamificationService>(context);
    final hasNewAchievements = gamificationService.recentlyUnlocked.isNotEmpty;

    return Scaffold(
      body: IndexedStack(
        index: _currentIndex,
        children: _screens,
      ),
      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.1),
              blurRadius: 8,
              offset: const Offset(0, -2),
            ),
          ],
        ),
        child: BottomNavigationBar(
          currentIndex: _currentIndex,
          onTap: (index) {
            setState(() {
              _currentIndex = index;
            });

            // Clear new achievements notification when viewing achievements screen
            if (index == 1 && hasNewAchievements) {
              Future.delayed(const Duration(seconds: 1), () {
                gamificationService.clearRecentlyUnlocked();
              });
            }
          },
          type: BottomNavigationBarType.fixed,
          selectedItemColor: Theme.of(context).colorScheme.primary,
          unselectedItemColor: Colors.grey,
          selectedFontSize: 12,
          unselectedFontSize: 12,
          items: [
            const BottomNavigationBarItem(
              icon: Icon(Icons.home_outlined),
              activeIcon: Icon(Icons.home),
              label: 'Home',
            ),
            BottomNavigationBarItem(
              icon: hasNewAchievements
                  ? badges.Badge(
                      badgeContent: Text(
                        gamificationService.recentlyUnlocked.length.toString(),
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 10,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      badgeStyle: badges.BadgeStyle(
                        badgeColor: Colors.red,
                        padding: const EdgeInsets.all(4),
                      ),
                      child: const Icon(Icons.emoji_events_outlined),
                    )
                  : const Icon(Icons.emoji_events_outlined),
              activeIcon: hasNewAchievements
                  ? badges.Badge(
                      badgeContent: Text(
                        gamificationService.recentlyUnlocked.length.toString(),
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 10,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      badgeStyle: badges.BadgeStyle(
                        badgeColor: Colors.red,
                        padding: const EdgeInsets.all(4),
                      ),
                      child: const Icon(Icons.emoji_events),
                    )
                  : const Icon(Icons.emoji_events),
              label: 'Achievements',
            ),
            const BottomNavigationBarItem(
              icon: Icon(Icons.person_outline),
              activeIcon: Icon(Icons.person),
              label: 'Profile',
            ),
            const BottomNavigationBarItem(
              icon: Icon(Icons.settings_outlined),
              activeIcon: Icon(Icons.settings),
              label: 'Settings',
            ),
          ],
        ),
      ),
    );
  }
}
