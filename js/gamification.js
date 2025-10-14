/**
 * Gamification Module
 * Handles user progress tracking, XP, streaks, badges, and levels
 */

class ProgressTracker {
  constructor() {
    this.loadProgress();
  }

  loadProgress() {
    const savedProgress = localStorage.getItem('userProgress');
    if (savedProgress) {
      const progress = JSON.parse(savedProgress);
      this.streakCount = progress.streakCount || 0;
      this.totalXP = progress.totalXP || 0;
      this.badges = progress.badges || [];
      this.level = progress.level || 1;
      this.lastStudyDate = progress.lastStudyDate || null;
      this.completedExercises = progress.completedExercises || {};
    } else {
      this.streakCount = 0;
      this.totalXP = 0;
      this.badges = [];
      this.level = 1;
      this.lastStudyDate = null;
      this.completedExercises = {};
    }
  }

  saveProgress() {
    const progress = {
      streakCount: this.streakCount,
      totalXP: this.totalXP,
      badges: this.badges,
      level: this.level,
      lastStudyDate: this.lastStudyDate,
      completedExercises: this.completedExercises
    };
    localStorage.setItem('userProgress', JSON.stringify(progress));
  }

  updateStreak() {
    const today = new Date().toDateString();
    const lastStudy = this.lastStudyDate ? new Date(this.lastStudyDate).toDateString() : null;

    if (lastStudy === today) {
      // Already studied today
      return this.streakCount;
    }

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toDateString();

    if (lastStudy === yesterdayStr) {
      // Continuing streak
      this.streakCount++;
      this.checkStreakBadges();
    } else if (!lastStudy) {
      // First day
      this.streakCount = 1;
    } else {
      // Streak broken
      this.streakCount = 1;
    }

    this.lastStudyDate = today;
    this.saveProgress();
    return this.streakCount;
  }

  addXP(amount) {
    this.totalXP += amount;
    const newLevel = Math.floor(this.totalXP / 250) + 1;

    if (newLevel > this.level) {
      this.level = newLevel;
      this.onLevelUp(newLevel);
    }

    this.saveProgress();
    return this.totalXP;
  }

  onLevelUp(newLevel) {
    // Show level up notification
    if (typeof window !== 'undefined' && window.showNotification) {
      window.showNotification(`Level Up! You're now level ${newLevel}!`, 'success');
    }

    // Award level badge
    if (newLevel === 5) {
      this.awardBadge('level-5', 'Reached Level 5');
    } else if (newLevel === 10) {
      this.awardBadge('level-10', 'Reached Level 10');
    } else if (newLevel === 20) {
      this.awardBadge('level-20', 'Master Learner');
    }
  }

  awardBadge(badgeId, badgeName) {
    if (!this.badges.find(b => b.id === badgeId)) {
      this.badges.push({ id: badgeId, name: badgeName, earnedDate: new Date().toISOString() });
      this.saveProgress();

      if (typeof window !== 'undefined' && window.showNotification) {
        window.showNotification(`New Badge: ${badgeName}!`, 'badge');
      }
    }
  }

  checkStreakBadges() {
    if (this.streakCount === 3) {
      this.awardBadge('streak-3', '3 Day Streak');
    } else if (this.streakCount === 7) {
      this.awardBadge('streak-7', 'Week Warrior');
    } else if (this.streakCount === 30) {
      this.awardBadge('streak-30', 'Month Master');
    } else if (this.streakCount === 100) {
      this.awardBadge('streak-100', 'Century Achiever');
    }
  }

  checkPronunciationBadges(score) {
    if (score >= 95) {
      this.awardBadge('pronunciation-master', 'Pronunciation Master');
    } else if (score >= 90) {
      this.awardBadge('pronunciation-expert', 'Pronunciation Expert');
    }
  }

  completeExercise(exerciseId, accuracy) {
    this.completedExercises[exerciseId] = {
      completedDate: new Date().toISOString(),
      accuracy: accuracy
    };

    // Award XP based on accuracy
    let xpAmount = 10;
    if (accuracy >= 90) {
      xpAmount = 20;
    } else if (accuracy >= 70) {
      xpAmount = 15;
    }

    this.addXP(xpAmount);
    this.updateStreak();
    this.saveProgress();

    // Check for perfect completion badge
    const totalExercises = Object.keys(this.completedExercises).length;
    if (totalExercises === 50) {
      this.awardBadge('complete-50', 'Completed 50 Exercises');
    } else if (totalExercises === 100) {
      this.awardBadge('complete-100', 'Completed 100 Exercises');
    } else if (totalExercises === 250) {
      this.awardBadge('complete-250', 'Exercise Master');
    }
  }

  getProgress() {
    return {
      streakCount: this.streakCount,
      totalXP: this.totalXP,
      badges: this.badges,
      level: this.level,
      xpToNextLevel: 250 - (this.totalXP % 250),
      percentToNextLevel: ((this.totalXP % 250) / 250) * 100
    };
  }

  getStats() {
    const totalCompleted = Object.keys(this.completedExercises).length;
    const avgAccuracy = totalCompleted > 0
      ? Object.values(this.completedExercises).reduce((sum, ex) => sum + ex.accuracy, 0) / totalCompleted
      : 0;

    return {
      totalCompleted,
      avgAccuracy: Math.round(avgAccuracy),
      totalXP: this.totalXP,
      level: this.level,
      streakCount: this.streakCount,
      badgeCount: this.badges.length
    };
  }
}

// Badge definitions with icons and descriptions
const BADGE_DEFINITIONS = {
  'first-lesson': { name: 'First Steps', icon: '🎯', description: 'Complete your first lesson' },
  'streak-3': { name: '3 Day Streak', icon: '🔥', description: 'Study for 3 consecutive days' },
  'streak-7': { name: 'Week Warrior', icon: '⚡', description: 'Study for 7 consecutive days' },
  'streak-30': { name: 'Month Master', icon: '💪', description: 'Study for 30 consecutive days' },
  'streak-100': { name: 'Century Achiever', icon: '🏆', description: 'Study for 100 consecutive days' },
  'pronunciation-expert': { name: 'Pronunciation Expert', icon: '🎤', description: 'Score 90%+ on pronunciation' },
  'pronunciation-master': { name: 'Pronunciation Master', icon: '🎙️', description: 'Score 95%+ on pronunciation' },
  'level-5': { name: 'Level 5', icon: '⭐', description: 'Reach Level 5' },
  'level-10': { name: 'Level 10', icon: '🌟', description: 'Reach Level 10' },
  'level-20': { name: 'Master Learner', icon: '💎', description: 'Reach Level 20' },
  'complete-50': { name: '50 Exercises', icon: '🎓', description: 'Complete 50 exercises' },
  'complete-100': { name: '100 Exercises', icon: '📚', description: 'Complete 100 exercises' },
  'complete-250': { name: 'Exercise Master', icon: '🏅', description: 'Complete 250 exercises' },
  'perfect-score': { name: 'Perfect Score', icon: '💯', description: 'Score 100% on any exercise' }
};

// Export for use in other modules
if (typeof window !== 'undefined') {
  window.ProgressTracker = ProgressTracker;
  window.BADGE_DEFINITIONS = BADGE_DEFINITIONS;
}
