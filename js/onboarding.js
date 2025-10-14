/**
 * Progressive Disclosure Onboarding System
 * Handles the 3-step guided journey for new users
 */

// Language data with recommendations and details
const languageData = {
  en: {
    name: 'English',
    flag: '🇬🇧',
    difficulty: 3,
    speakers: '1.5B speakers worldwide',
    benefits: [
      'Global business language',
      'Tech industry standard',
      '1.5B speakers worldwide',
      'International communication'
    ],
    gradient: 'linear-gradient(135deg, #3498db, #2980b9)'
  },
  es: {
    name: 'Spanish',
    flag: '🇪🇸',
    difficulty: 2,
    speakers: '500M speakers globally',
    benefits: [
      '500M speakers globally',
      'Growing US market',
      'Latin America business',
      'Second most spoken language'
    ],
    gradient: 'linear-gradient(135deg, #e74c3c, #c0392b)'
  },
  pt: {
    name: 'Portuguese',
    flag: '🇧🇷',
    difficulty: 2,
    speakers: '260M speakers',
    benefits: [
      'Brazil market access',
      '260M speakers',
      'Emerging economy',
      'Growing global influence'
    ],
    gradient: 'linear-gradient(135deg, #2ecc71, #27ae60)'
  },
  fr: {
    name: 'French',
    flag: '🇫🇷',
    difficulty: 3,
    speakers: '280M speakers',
    benefits: [
      'International diplomacy',
      'African markets',
      'Luxury industry',
      '280M speakers'
    ],
    gradient: 'linear-gradient(135deg, #9b59b6, #8e44ad)'
  },
  de: {
    name: 'German',
    flag: '🇩🇪',
    difficulty: 4,
    speakers: '130M speakers',
    benefits: [
      'Engineering hub',
      'EU economic leader',
      'Industry 4.0',
      'Strong economy'
    ],
    gradient: 'linear-gradient(135deg, #f1c40f, #f39c12)'
  }
};

// Language recommendations based on user goals
const goalRecommendations = {
  career: ['en', 'de', 'fr'],
  travel: ['es', 'pt', 'fr'],
  business: ['en', 'de', 'es'],
  personal: ['fr', 'pt', 'de']
};

const PROGRAM_TOTAL_DAYS = 50;

// Onboarding state
let onboardingState = {
  currentStep: 1,
  selectedGoal: null,
  selectedLanguage: null,
  hasCompletedOnboarding: false
};

// Initialize onboarding system
document.addEventListener('DOMContentLoaded', function() {
  initializeOnboarding();
});

function initializeOnboarding() {
  // Check if user has completed onboarding before
  checkReturningUser();

  // Set up event listeners
  setupAssessmentListeners();
  setupNavigationListeners();
  setupHeroListeners();

  // Initialize step display
  updateStepDisplay();
}

/**
 * Check if user is returning and has completed onboarding
 */
function checkReturningUser() {
  const userProgress = localStorage.getItem('userProgress');
  const onboardingComplete = localStorage.getItem('onboardingComplete');

  if (userProgress || onboardingComplete) {
    onboardingState.hasCompletedOnboarding = true;

    // Show returning user badge
    const userStatusBadge = document.getElementById('userStatus');
    if (userStatusBadge) {
      userStatusBadge.style.display = 'block';
    }

    configureResumeJourneyCTA();

    // Skip onboarding, show main content
    if (onboardingComplete) {
      skipToMainContent();
    }
  } else {
    // Ensure resume CTA stays hidden for brand-new users
    const resumeButton = document.getElementById('resumeJourney');
    if (resumeButton) {
      resumeButton.style.display = 'none';
    }
  }
}

/**
 * Skip onboarding and show main content
 */
function skipToMainContent() {
  onboardingState.hasCompletedOnboarding = true;

  // Hide onboarding sections
  document.querySelectorAll('.onboarding-section').forEach(section => {
    section.classList.add('section-hidden');
    section.classList.remove('section-visible');
  });

  // Hide step indicator and navigation
  const stepIndicator = document.getElementById('stepIndicator');
  const navigationControls = document.getElementById('navigationControls');
  if (stepIndicator) stepIndicator.style.display = 'none';
  if (navigationControls) navigationControls.style.display = 'none';

  // Show main content
  document.getElementById('language-cards').classList.remove('section-hidden');
  document.getElementById('userDashboard').classList.remove('section-hidden');
  document.querySelector('.course-overview').classList.remove('section-hidden');
  document.getElementById('day-selection').classList.remove('section-hidden');
  document.querySelector('.benefits-section').classList.remove('section-hidden');
  document.querySelectorAll('.section-divider').forEach(div => div.classList.remove('section-hidden'));
}

/**
 * Set up assessment option listeners
 */
function setupAssessmentListeners() {
  const assessmentOptions = document.querySelectorAll('.assessment-option');

  assessmentOptions.forEach(option => {
    option.addEventListener('click', function() {
      // Remove selected class from all options
      assessmentOptions.forEach(opt => opt.classList.remove('selected'));

      // Add selected class to clicked option
      this.classList.add('selected');

      // Store selected goal
      onboardingState.selectedGoal = this.dataset.goal;

      // Enable next button
      updateNavigationButtons();
    });
  });
}

/**
 * Set up navigation button listeners
 */
function setupNavigationListeners() {
  const nextButton = document.getElementById('nextButton');
  const prevButton = document.getElementById('prevButton');

  if (nextButton) {
    nextButton.addEventListener('click', nextStep);
  }

  if (prevButton) {
    prevButton.addEventListener('click', prevStep);
  }
}

/**
 * Set up hero section listeners
 */
function setupHeroListeners() {
  const startJourneyBtn = document.getElementById('startJourney');
  const learnMoreBtn = document.getElementById('learnMore');
  const startLearningBtn = document.getElementById('startLearningBtn');
  const resumeJourneyBtn = document.getElementById('resumeJourney');

  if (startJourneyBtn) {
    startJourneyBtn.addEventListener('click', function(e) {
      e.preventDefault();
      if (onboardingState.hasCompletedOnboarding) {
        skipToMainContent();
        scrollToSection('language-cards');
      } else {
        scrollToSection('assessment-section');
      }
    });
  }

  if (learnMoreBtn) {
    learnMoreBtn.addEventListener('click', function(e) {
      e.preventDefault();
      showProductTour();
    });
  }

  if (startLearningBtn) {
    startLearningBtn.addEventListener('click', function(e) {
      e.preventDefault();
      completeOnboarding();
    });
  }

  if (resumeJourneyBtn) {
    resumeJourneyBtn.addEventListener('click', function() {
      localStorage.setItem('onboardingComplete', 'true');
    });
  }
}

/**
 * Move to next step
 */
function nextStep() {
  if (onboardingState.currentStep < 3) {
    onboardingState.currentStep++;
    updateStepDisplay();

    if (onboardingState.currentStep === 2) {
      populateLanguageRecommendations();
    } else if (onboardingState.currentStep === 3) {
      setupLearningPath();
    }

    // Scroll to the new section
    scrollToCurrentStep();
  }
}

/**
 * Move to previous step
 */
function prevStep() {
  if (onboardingState.currentStep > 1) {
    onboardingState.currentStep--;
    updateStepDisplay();
    scrollToCurrentStep();
  }
}

/**
 * Update step indicator and section visibility
 */
function updateStepDisplay() {
  // Update step indicator
  const steps = document.querySelectorAll('.step');
  steps.forEach((step, index) => {
    step.classList.remove('active', 'completed');

    if (index + 1 < onboardingState.currentStep) {
      step.classList.add('completed');
    } else if (index + 1 === onboardingState.currentStep) {
      step.classList.add('active');
    }
  });

  // Update section visibility
  const sections = ['assessment-section', 'language-section', 'path-section'];
  sections.forEach((sectionId, index) => {
    const section = document.getElementById(sectionId);
    if (section) {
      if (index + 1 === onboardingState.currentStep) {
        section.classList.remove('section-hidden');
        section.classList.add('section-visible');
      } else {
        section.classList.remove('section-visible');
        section.classList.add('section-hidden');
      }
    }
  });

  // Update navigation buttons
  updateNavigationButtons();

  // Update current step text
  const currentStepText = document.getElementById('currentStep');
  if (currentStepText) {
    currentStepText.textContent = onboardingState.currentStep;
  }
}

/**
 * Update navigation button states
 */
function updateNavigationButtons() {
  const nextButton = document.getElementById('nextButton');
  const prevButton = document.getElementById('prevButton');

  // Previous button
  if (prevButton) {
    prevButton.disabled = onboardingState.currentStep === 1;
  }

  // Next button
  if (nextButton) {
    switch (onboardingState.currentStep) {
      case 1:
        nextButton.disabled = !onboardingState.selectedGoal;
        break;
      case 2:
        nextButton.disabled = !onboardingState.selectedLanguage;
        break;
      case 3:
        nextButton.style.display = 'none';
        break;
      default:
        nextButton.disabled = true;
    }
  }
}

/**
 * Populate language recommendations based on selected goal
 */
function populateLanguageRecommendations() {
  const container = document.getElementById('languageCardsEnhanced');
  if (!container) return;

  container.innerHTML = '';

  const recommended = goalRecommendations[onboardingState.selectedGoal] || ['en', 'es', 'fr'];

  // Add recommended languages first
  recommended.forEach(langCode => {
    const card = createLanguageCard(langCode, true);
    container.appendChild(card);
  });

  // Add other languages
  Object.keys(languageData).forEach(langCode => {
    if (!recommended.includes(langCode)) {
      const card = createLanguageCard(langCode, false);
      container.appendChild(card);
    }
  });
}

/**
 * Create a language card element
 */
function createLanguageCard(langCode, isRecommended) {
  const lang = languageData[langCode];
  const card = document.createElement('div');
  card.className = `language-card-enhanced ${isRecommended ? 'recommended' : ''}`;
  card.dataset.language = langCode;

  // Create difficulty dots
  const difficultyDots = Array.from({ length: 5 }, (_, i) =>
    `<div class="difficulty-dot ${i < lang.difficulty ? 'filled' : ''}"></div>`
  ).join('');

  // Create benefits list
  const benefitsList = lang.benefits.map(benefit =>
    `<li>${benefit}</li>`
  ).join('');

  card.innerHTML = `
    <div class="card-header-enhanced" style="background: ${lang.gradient};">
      <h3>
        <span class="flag">${lang.flag}</span>
        ${lang.name}
      </h3>
    </div>
    <div class="card-content-enhanced">
      <div class="speakers-count">
        <i class="fas fa-users"></i> ${lang.speakers}
      </div>
      <div class="difficulty-indicator">
        <span class="difficulty-label">Difficulty:</span>
        <div class="difficulty-dots">${difficultyDots}</div>
      </div>
      <ul class="language-benefits">
        ${benefitsList}
      </ul>
    </div>
  `;

  // Add click listener
  card.addEventListener('click', function() {
    // Remove selected class from all cards
    document.querySelectorAll('.language-card-enhanced').forEach(c =>
      c.classList.remove('selected')
    );

    // Add selected class to this card
    this.classList.add('selected');

    // Store selected language
    onboardingState.selectedLanguage = langCode;

    // Enable next button
    updateNavigationButtons();
  });

  return card;
}

/**
 * Set up the learning path section
 */
function setupLearningPath() {
  const lang = languageData[onboardingState.selectedLanguage];
  if (!lang) return;

  // Update the path section title
  const pathLanguageName = document.getElementById('pathLanguageName');
  if (pathLanguageName) {
    pathLanguageName.textContent = `Your ${lang.name} Learning Path - Here's what your 50-day journey will look like:`;
  }

  // Store onboarding selections in localStorage
  localStorage.setItem('onboardingData', JSON.stringify({
    goal: onboardingState.selectedGoal,
    language: onboardingState.selectedLanguage,
    timestamp: new Date().toISOString()
  }));
}

/**
 * Complete onboarding and transition to main app
 */
function completeOnboarding() {
  // Mark onboarding as complete
  localStorage.setItem('onboardingComplete', 'true');

  // If user selected a language during onboarding, take them directly to Day 1
  if (onboardingState.selectedLanguage) {
    // Store the selected language for future reference
    localStorage.setItem('lastSelectedLanguage', onboardingState.selectedLanguage);

    // Redirect directly to Day 1 with the selected language
    window.location.href = `day.html?day=1&lang=${onboardingState.selectedLanguage}`;
    return; // Stop execution - redirect will handle the rest
  }

  // Fallback: If no language was selected (shouldn't happen in normal flow)
  // Show main content and let user choose from language cards

  // Hide onboarding sections
  document.querySelectorAll('.onboarding-section').forEach(section => {
    section.classList.add('section-hidden');
    section.classList.remove('section-visible');
  });

  // Hide step indicator and navigation
  const stepIndicator = document.getElementById('stepIndicator');
  const navigationControls = document.getElementById('navigationControls');
  if (stepIndicator) stepIndicator.style.display = 'none';
  if (navigationControls) navigationControls.style.display = 'none';

  // Show main content with animation
  setTimeout(() => {
    document.getElementById('language-cards').classList.remove('section-hidden');
    document.getElementById('userDashboard').classList.remove('section-hidden');
    document.querySelector('.course-overview').classList.remove('section-hidden');
    document.getElementById('day-selection').classList.remove('section-hidden');
    document.querySelector('.benefits-section').classList.remove('section-hidden');
    document.querySelectorAll('.section-divider').forEach(div => div.classList.remove('section-hidden'));

    // Scroll to language cards
    scrollToSection('language-cards');

    // Show welcome notification
    if (window.showNotification) {
      window.showNotification('Welcome to Polyglot Pathways! Start your language learning journey today.', 'success');
    }
  }, 300);
}

/**
 * Scroll to a specific section
 */
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    setTimeout(() => {
      section.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }, 100);
  }
}

/**
 * Scroll to the current step section
 */
function scrollToCurrentStep() {
  const sections = ['assessment-section', 'language-section', 'path-section'];
  const currentSectionId = sections[onboardingState.currentStep - 1];
  scrollToSection(currentSectionId);
}

/**
 * Show product tour (placeholder)
 */
function showProductTour() {
  // This could be enhanced with a modal or video
  if (window.showNotification) {
    window.showNotification('Product tour coming soon! For now, scroll down to see how it works.', 'info');
  } else {
    alert('Product tour: Polyglot Pathways offers a 50-day structured learning program for 5 strategic languages. Complete daily lessons, earn XP and badges, and track your progress!');
  }

  // Scroll to assessment section
  scrollToSection('assessment-section');
}

/**
 * Reset onboarding (for testing)
 */
function resetOnboarding() {
  localStorage.removeItem('onboardingComplete');
  localStorage.removeItem('onboardingData');
  location.reload();
}

// Export for debugging
if (typeof window !== 'undefined') {
  window.onboardingState = onboardingState;
  window.resetOnboarding = resetOnboarding;
}

/**
 * Configure the hero CTA for returning users
 */
function configureResumeJourneyCTA() {
  const resumeBtn = document.getElementById('resumeJourney');
  if (!resumeBtn) return;

  const storedProgress = JSON.parse(localStorage.getItem('currentProgress') || 'null');
  const storedLanguage =
    (storedProgress && storedProgress.lang) ||
    localStorage.getItem('lastSelectedLanguage') ||
    localStorage.getItem('preferredLanguage');

  if (!storedLanguage) {
    resumeBtn.style.display = 'none';
    return;
  }

  const completedDays = storedProgress && typeof storedProgress.completed === 'number'
    ? storedProgress.completed
    : 0;
  const nextDay = Math.min(completedDays + 1, PROGRAM_TOTAL_DAYS);
  const languageName = languageData[storedLanguage]?.name || storedLanguage.toUpperCase();

  let buttonLabel;
  if (completedDays >= PROGRAM_TOTAL_DAYS) {
    buttonLabel = `Review ${languageName} - Day ${PROGRAM_TOTAL_DAYS}`;
  } else if (completedDays > 0) {
    buttonLabel = `Continue ${languageName} - Day ${nextDay}`;
  } else {
    buttonLabel = `Start ${languageName} - Day ${nextDay}`;
  }

  resumeBtn.href = `day.html?day=${nextDay}&lang=${storedLanguage}`;
  resumeBtn.innerHTML = `<i class="fas fa-undo"></i> ${buttonLabel}`;
  resumeBtn.style.display = 'inline-flex';
}
