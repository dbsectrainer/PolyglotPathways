/**
 * UI Utilities Module
 * Handles notifications, animations, and UI helpers
 */

// Notification system
window.showNotification = function(message, type = 'info') {
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;

  let icon = '';
  switch (type) {
    case 'success':
      icon = '<i class="fas fa-check-circle"></i>';
      break;
    case 'error':
      icon = '<i class="fas fa-times-circle"></i>';
      break;
    case 'xp':
      icon = '<i class="fas fa-star"></i>';
      break;
    case 'badge':
      icon = '<i class="fas fa-trophy"></i>';
      break;
    default:
      icon = '<i class="fas fa-info-circle"></i>';
  }

  notification.innerHTML = `${icon} <span>${message}</span>`;

  document.body.appendChild(notification);

  // Trigger animation
  setTimeout(() => {
    notification.classList.add('show');
  }, 10);

  // Remove after 3 seconds
  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => {
      document.body.removeChild(notification);
    }, 300);
  }, 3000);
};

// Progress bar animation
window.animateProgressBar = function(element, targetPercentage) {
  let currentPercentage = 0;
  const duration = 1000; // 1 second
  const startTime = performance.now();

  const animate = (currentTime) => {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    currentPercentage = targetPercentage * progress;
    element.style.width = `${currentPercentage}%`;

    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  };

  requestAnimationFrame(animate);
};

// Level up animation
window.showLevelUpAnimation = function(level) {
  const overlay = document.createElement('div');
  overlay.className = 'level-up-overlay';
  overlay.innerHTML = `
    <div class="level-up-content">
      <div class="level-up-icon">
        <i class="fas fa-trophy"></i>
      </div>
      <h2 class="level-up-title">Level Up!</h2>
      <p class="level-up-level">Level ${level}</p>
      <p class="level-up-message">You're making great progress!</p>
    </div>
  `;

  document.body.appendChild(overlay);

  setTimeout(() => {
    overlay.classList.add('show');
  }, 10);

  setTimeout(() => {
    overlay.classList.remove('show');
    setTimeout(() => {
      document.body.removeChild(overlay);
    }, 500);
  }, 3000);
};

// Badge notification
window.showBadgeNotification = function(badge) {
  const badgeInfo = window.BADGE_DEFINITIONS[badge.id];
  if (!badgeInfo) return;

  const notification = document.createElement('div');
  notification.className = 'badge-notification';
  notification.innerHTML = `
    <div class="badge-notification-content">
      <div class="badge-icon">${badgeInfo.icon}</div>
      <div class="badge-info">
        <h3>New Badge!</h3>
        <p class="badge-name">${badgeInfo.name}</p>
        <p class="badge-description">${badgeInfo.description}</p>
      </div>
    </div>
  `;

  document.body.appendChild(notification);

  setTimeout(() => {
    notification.classList.add('show');
  }, 10);

  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => {
      document.body.removeChild(notification);
    }, 500);
  }, 4000);
};

// Confetti animation for achievements
window.showConfetti = function() {
  const confettiCount = 50;
  const colors = ['#3498db', '#2ecc71', '#f1c40f', '#e74c3c', '#9b59b6'];

  for (let i = 0; i < confettiCount; i++) {
    const confetti = document.createElement('div');
    confetti.className = 'confetti';
    confetti.style.left = `${Math.random() * 100}%`;
    confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    confetti.style.animationDelay = `${Math.random() * 0.5}s`;
    confetti.style.animationDuration = `${2 + Math.random() * 2}s`;

    document.body.appendChild(confetti);

    setTimeout(() => {
      document.body.removeChild(confetti);
    }, 4000);
  }
};

// Update progress display
window.updateProgressDisplay = function(progressData) {
  // Update XP
  const xpElement = document.getElementById('user-xp');
  if (xpElement) {
    xpElement.textContent = `${progressData.totalXP} XP`;
  }

  // Update Level
  const levelElement = document.getElementById('user-level');
  if (levelElement) {
    levelElement.textContent = `Level ${progressData.level}`;
  }

  // Update Streak
  const streakElement = document.getElementById('user-streak');
  if (streakElement) {
    streakElement.innerHTML = `<i class="fas fa-fire"></i> ${progressData.streakCount} day streak`;
  }

  // Update level progress bar
  const levelProgressBar = document.getElementById('level-progress-bar');
  if (levelProgressBar) {
    window.animateProgressBar(levelProgressBar, progressData.percentToNextLevel);
  }

  // Update XP to next level text
  const xpToNextElement = document.getElementById('xp-to-next');
  if (xpToNextElement) {
    xpToNextElement.textContent = `${progressData.xpToNextLevel} XP to Level ${progressData.level + 1}`;
  }
};

// Render badges
window.renderBadges = function(badges) {
  const badgesContainer = document.getElementById('badges-container');
  if (!badgesContainer) return;

  badgesContainer.innerHTML = '';

  if (badges.length === 0) {
    badgesContainer.innerHTML = '<p class="no-badges">Complete lessons to earn badges!</p>';
    return;
  }

  badges.forEach(badge => {
    const badgeInfo = window.BADGE_DEFINITIONS[badge.id];
    if (!badgeInfo) return;

    const badgeElement = document.createElement('div');
    badgeElement.className = 'badge-item';
    badgeElement.title = badgeInfo.description;
    badgeElement.innerHTML = `
      <div class="badge-icon-display">${badgeInfo.icon}</div>
      <p class="badge-name-display">${badgeInfo.name}</p>
    `;

    badgesContainer.appendChild(badgeElement);
  });
};

// Smooth scroll to element
window.smoothScrollTo = function(element) {
  element.scrollIntoView({
    behavior: 'smooth',
    block: 'start'
  });
};

// Format date
window.formatDate = function(dateString) {
  const date = new Date(dateString);
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return date.toLocaleDateString('en-US', options);
};

// Calculate completion percentage
window.calculateCompletionPercentage = function(completed, total) {
  return Math.round((completed / total) * 100);
};

// Debounce function for input handlers
window.debounce = function(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};

// Local storage helpers
window.storage = {
  set: function(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (error) {
      console.error('Error saving to localStorage:', error);
      return false;
    }
  },

  get: function(key, defaultValue = null) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : defaultValue;
    } catch (error) {
      console.error('Error reading from localStorage:', error);
      return defaultValue;
    }
  },

  remove: function(key) {
    try {
      localStorage.removeItem(key);
      return true;
    } catch (error) {
      console.error('Error removing from localStorage:', error);
      return false;
    }
  },

  clear: function() {
    try {
      localStorage.clear();
      return true;
    } catch (error) {
      console.error('Error clearing localStorage:', error);
      return false;
    }
  }
};

// Initialize tooltips
window.initializeTooltips = function() {
  const tooltipElements = document.querySelectorAll('[data-tooltip]');

  tooltipElements.forEach(element => {
    element.addEventListener('mouseenter', function() {
      const tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = this.dataset.tooltip;

      document.body.appendChild(tooltip);

      const rect = this.getBoundingClientRect();
      tooltip.style.left = `${rect.left + rect.width / 2}px`;
      tooltip.style.top = `${rect.top - tooltip.offsetHeight - 10}px`;

      setTimeout(() => {
        tooltip.classList.add('show');
      }, 10);

      this.addEventListener('mouseleave', function() {
        tooltip.classList.remove('show');
        setTimeout(() => {
          document.body.removeChild(tooltip);
        }, 200);
      }, { once: true });
    });
  });
};

// Loading spinner
window.showLoadingSpinner = function(container) {
  const spinner = document.createElement('div');
  spinner.className = 'loading-spinner';
  spinner.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
  container.appendChild(spinner);
  return spinner;
};

window.hideLoadingSpinner = function(spinner) {
  if (spinner && spinner.parentNode) {
    spinner.parentNode.removeChild(spinner);
  }
};
