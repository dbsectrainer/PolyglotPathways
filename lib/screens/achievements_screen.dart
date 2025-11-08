import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:confetti/confetti.dart';
import '../services/gamification_service.dart';
import '../theme/app_theme.dart';

class AchievementsScreen extends StatefulWidget {
  const AchievementsScreen({super.key});

  @override
  State<AchievementsScreen> createState() => _AchievementsScreenState();
}

class _AchievementsScreenState extends State<AchievementsScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  late ConfettiController _confettiController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 5, vsync: this);
    _confettiController = ConfettiController(duration: const Duration(seconds: 3));

    // Show confetti if there are newly unlocked achievements
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final gamificationService =
          Provider.of<GamificationService>(context, listen: false);
      if (gamificationService.recentlyUnlocked.isNotEmpty) {
        _confettiController.play();
      }
    });
  }

  @override
  void dispose() {
    _tabController.dispose();
    _confettiController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final gamificationService = Provider.of<GamificationService>(context);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Achievements'),
        centerTitle: true,
        bottom: TabBar(
          controller: _tabController,
          isScrollable: true,
          indicatorColor: Colors.white,
          labelColor: Colors.white,
          unselectedLabelColor: Colors.white70,
          tabs: const [
            Tab(text: 'All'),
            Tab(text: 'Lessons'),
            Tab(text: 'Streaks'),
            Tab(text: 'Languages'),
            Tab(text: 'Special'),
          ],
        ),
      ),
      body: Stack(
        children: [
          Column(
            children: [
              // Progress Header
              _buildProgressHeader(gamificationService)
                  .animate()
                  .fadeIn()
                  .slideY(begin: -0.2, duration: 500.ms),

              // Tabs Content
              Expanded(
                child: TabBarView(
                  controller: _tabController,
                  children: [
                    _buildAchievementsList(gamificationService.achievements),
                    _buildAchievementsList(
                        gamificationService.getLessonAchievements()),
                    _buildAchievementsList(
                        gamificationService.getStreakAchievements()),
                    _buildAchievementsList(
                        gamificationService.getMultilingualAchievements()),
                    _buildAchievementsList(
                        gamificationService.getSpecialAchievements()),
                  ],
                ),
              ),
            ],
          ),

          // Confetti overlay
          Align(
            alignment: Alignment.topCenter,
            child: ConfettiWidget(
              confettiController: _confettiController,
              blastDirectionality: BlastDirectionality.explosive,
              shouldLoop: false,
              colors: const [
                AppTheme.primaryBlue,
                AppTheme.secondaryGreen,
                AppTheme.accentOrange,
                AppTheme.accentPurple,
                AppTheme.goldBadge,
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildProgressHeader(GamificationService gamificationService) {
    final unlocked = gamificationService.achievementCount;
    final total = gamificationService.totalAchievements;
    final progress = unlocked / total;

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: AppTheme.primaryGradient,
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(
                Icons.emoji_events,
                color: AppTheme.goldBadge,
                size: 32,
              ),
              const SizedBox(width: 12),
              Text(
                '$unlocked / $total',
                style: const TextStyle(
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          const Text(
            'Achievements Unlocked',
            style: TextStyle(
              fontSize: 16,
              color: Colors.white70,
            ),
          ),
          const SizedBox(height: 16),
          ClipRRect(
            borderRadius: BorderRadius.circular(10),
            child: LinearProgressIndicator(
              value: progress,
              minHeight: 10,
              backgroundColor: Colors.white.withOpacity(0.3),
              valueColor: const AlwaysStoppedAnimation<Color>(Colors.white),
            ),
          ),
          const SizedBox(height: 8),
          Text(
            '${(progress * 100).toStringAsFixed(0)}% Complete',
            style: const TextStyle(
              fontSize: 14,
              color: Colors.white,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildAchievementsList(List achievements) {
    if (achievements.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.emoji_events_outlined,
              size: 64,
              color: Colors.grey[400],
            ),
            const SizedBox(height: 16),
            Text(
              'No achievements in this category',
              style: TextStyle(
                fontSize: 16,
                color: Colors.grey[600],
              ),
            ),
          ],
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: achievements.length,
      itemBuilder: (context, index) {
        final achievement = achievements[index];
        return _buildAchievementCard(achievement, index)
            .animate()
            .fadeIn(delay: (index * 50).ms)
            .slideX(begin: -0.1);
      },
    );
  }

  Widget _buildAchievementCard(achievement, int index) {
    final isUnlocked = achievement.isUnlocked;

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      elevation: isUnlocked ? 4 : 1,
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(12),
          gradient: isUnlocked
              ? LinearGradient(
                  colors: [
                    achievement.color.withOpacity(0.1),
                    achievement.color.withOpacity(0.05),
                  ],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                )
              : null,
        ),
        child: ListTile(
          contentPadding: const EdgeInsets.all(16),
          leading: Container(
            width: 56,
            height: 56,
            decoration: BoxDecoration(
              color: isUnlocked
                  ? achievement.color.withOpacity(0.2)
                  : Colors.grey[300],
              shape: BoxShape.circle,
              boxShadow: isUnlocked
                  ? [
                      BoxShadow(
                        color: achievement.color.withOpacity(0.3),
                        blurRadius: 8,
                        offset: const Offset(0, 2),
                      ),
                    ]
                  : null,
            ),
            child: Icon(
              achievement.icon,
              color: isUnlocked ? achievement.color : Colors.grey[500],
              size: 32,
            ),
          ),
          title: Text(
            achievement.title,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 16,
              color: isUnlocked ? null : Colors.grey[600],
            ),
          ),
          subtitle: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 4),
              Text(
                achievement.description,
                style: TextStyle(
                  fontSize: 14,
                  color: isUnlocked ? Colors.grey[700] : Colors.grey[500],
                ),
              ),
              if (isUnlocked && achievement.unlockedAt != null) ...[
                const SizedBox(height: 8),
                Row(
                  children: [
                    Icon(
                      Icons.check_circle,
                      size: 14,
                      color: achievement.color,
                    ),
                    const SizedBox(width: 4),
                    Text(
                      'Unlocked ${_formatDate(achievement.unlockedAt!)}',
                      style: TextStyle(
                        fontSize: 12,
                        color: achievement.color,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              ],
            ],
          ),
          trailing: isUnlocked
              ? Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: achievement.color,
                    shape: BoxShape.circle,
                  ),
                  child: const Icon(
                    Icons.check,
                    color: Colors.white,
                    size: 20,
                  ),
                )
              : Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.grey[300],
                    shape: BoxShape.circle,
                  ),
                  child: Icon(
                    Icons.lock,
                    color: Colors.grey[500],
                    size: 20,
                  ),
                ),
        ),
      ),
    );
  }

  String _formatDate(DateTime date) {
    final now = DateTime.now();
    final difference = now.difference(date);

    if (difference.inDays == 0) {
      return 'today';
    } else if (difference.inDays == 1) {
      return 'yesterday';
    } else if (difference.inDays < 7) {
      return '${difference.inDays} days ago';
    } else {
      return 'on ${date.month}/${date.day}/${date.year}';
    }
  }
}
