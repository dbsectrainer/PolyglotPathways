document.addEventListener('DOMContentLoaded', function() {
    // Generate day grid
    generateDayGrid();

    // Initialize language cards
    initializeLanguageCards();

    // Apply stored or default language selection without scrolling
    setActiveLanguageCard(selectedLanguage, { scrollToDaySelection: false });

    // Add scroll animations
    initializeScrollAnimations();

    // Initialize day grid pagination
    initializeDayPagination();

    // Add micro-interactions
    initializeMicroInteractions();
});

// Language metadata for display logic
const languageDisplayNames = {
    en: 'English',
    es: 'Spanish',
    pt: 'Portuguese',
    fr: 'French',
    de: 'German'
};
const supportedLessonLanguages = Object.keys(languageDisplayNames);
const urlParams = new URLSearchParams(window.location.search);
const langFromUrl = urlParams.get('lang');
const storedLanguagePreference = localStorage.getItem('preferredLanguage') || localStorage.getItem('lastSelectedLanguage');

// Global variables for pagination
let currentDayPage = 1;
const daysPerPage = 10;
const totalDays = 50;
let selectedLanguage = 'en';

if (langFromUrl && supportedLessonLanguages.includes(langFromUrl)) {
    selectedLanguage = langFromUrl;
} else if (storedLanguagePreference && supportedLessonLanguages.includes(storedLanguagePreference)) {
    selectedLanguage = storedLanguagePreference;
} else if (window.i18n && supportedLessonLanguages.includes(window.i18n.currentLang)) {
    selectedLanguage = window.i18n.currentLang;
}

function generateDayGrid() {
    const dayGrid = document.querySelector('.day-grid');
    
    // Clear existing days
    dayGrid.innerHTML = '';
    
    // Calculate start and end days for current page
    const startDay = (currentDayPage - 1) * daysPerPage + 1;
    const endDay = Math.min(startDay + daysPerPage - 1, totalDays);
    
    // Update day range display
    if (document.getElementById('dayRangeStart')) {
        document.getElementById('dayRangeStart').textContent = startDay;
        document.getElementById('dayRangeEnd').textContent = endDay;
    }
    
    for (let i = startDay; i <= endDay; i++) {
        const dayLink = document.createElement('a');
        // Use the currently selected learning language for links
        const currentLang = supportedLessonLanguages.includes(selectedLanguage) ? selectedLanguage : 'en';
        dayLink.href = `day.html?day=${i}&lang=${currentLang}`;
        dayLink.className = 'animate-fade-in hover-scale';
        dayLink.style.animationDelay = `${(i - startDay) * 0.05}s`;
        
        const dayNumber = document.createElement('div');
        dayNumber.className = 'day-number';
        dayNumber.textContent = i;
        
        const dayStatus = document.createElement('div');
        dayStatus.className = 'day-status';
        
        // Add status icon and tooltip based on day ranges
        dayStatus.innerHTML = '<i class="fas fa-circle" style="color: var(--warning-color);"></i>';
        
        if (i <= 7) {
            addDayTooltip(dayLink, 'Basic vocabulary and essential phrases');
        } else if (i <= 15) {
            addDayTooltip(dayLink, 'Advanced phrases for intermediate learners');
        } else if (i <= 26) {
            addDayTooltip(dayLink, 'Living & Working in South America');
        } else if (i <= 31) {
            addDayTooltip(dayLink, 'Tech Professional Content');
        } else {
            addDayTooltip(dayLink, 'Advanced Academic & Professional Communication');
        }
        
        dayLink.appendChild(dayNumber);
        dayLink.appendChild(dayStatus);
        dayGrid.appendChild(dayLink);
    }
    
    // Update progress based on available lessons
    updateProgress(0); // Reset progress to 0
}

// Initialize day grid pagination
function initializeDayPagination() {
    const prevButton = document.getElementById('prevDays');
    const nextButton = document.getElementById('nextDays');
    
    if (prevButton && nextButton) {
        prevButton.addEventListener('click', function() {
            if (currentDayPage > 1) {
                currentDayPage--;
                generateDayGrid();
                
                // Scroll animation
                document.querySelector('.day-grid').classList.add('animate-fade-in');
                setTimeout(() => {
                    document.querySelector('.day-grid').classList.remove('animate-fade-in');
                }, 800);
            }
        });
        
        nextButton.addEventListener('click', function() {
            if (currentDayPage < Math.ceil(totalDays / daysPerPage)) {
                currentDayPage++;
                generateDayGrid();
                
                // Scroll animation
                document.querySelector('.day-grid').classList.add('animate-fade-in');
                setTimeout(() => {
                    document.querySelector('.day-grid').classList.remove('animate-fade-in');
                }, 800);
            }
        });
    }
}

function addDayTooltip(element, text) {
    element.setAttribute('title', text);
}

function initializeLanguageCards() {
    const cards = document.querySelectorAll('.language-card');

    cards.forEach(card => {
        const language = card.getAttribute('data-language');
        if (!language) {
            return;
        }

        card.dataset.selected = 'false';

        card.addEventListener('click', function() {
            setActiveLanguageCard(language);
        });

        // Add hover effects that respect selection state
        card.addEventListener('mouseenter', function() {
            if (this.dataset.selected === 'true') {
                return;
            }
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 15px 30px rgba(0,0,0,0.15)';
        });

        card.addEventListener('mouseleave', function() {
            if (this.dataset.selected === 'true') {
                return;
            }
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });
}

function updateDayGridLanguage(language) {
    // Update selected language
    selectedLanguage = language;
    // Update localStorage
    localStorage.setItem('preferredLanguage', language);
    updateDaySelectionHeading(language);
    // Update day links
    const dayLinks = document.querySelectorAll('.day-grid a');
    dayLinks.forEach(link => {
        const day = link.querySelector('.day-number').textContent;
        link.href = `day.html?day=${day}&lang=${language}`;
    });
}

function updateDaySelectionHeading(language) {
    const heading = document.querySelector('#day-selection h2');
    if (!heading) return;
    const displayName = languageDisplayNames[language] || languageDisplayNames.en;
    heading.textContent = `${displayName} Lessons`;
}

function setActiveLanguageCard(language, options = {}) {
    const { scrollToDaySelection = true } = options;
    const cards = document.querySelectorAll('.language-card');
    let matchedCard = null;

    cards.forEach(card => {
        if (card.getAttribute('data-language') === language) {
            matchedCard = card;
        }
    });

    if (matchedCard) {
        cards.forEach(card => {
            if (card === matchedCard) {
                card.dataset.selected = 'true';
                card.style.opacity = '1';
                card.style.transform = 'translateY(-10px)';
                card.style.boxShadow = '0 15px 30px rgba(0,0,0,0.15)';
            } else {
                card.dataset.selected = 'false';
                card.style.opacity = '0.7';
                card.style.transform = 'none';
                card.style.boxShadow = '';
            }
        });
    } else {
        cards.forEach(card => {
            card.dataset.selected = 'false';
            card.style.opacity = '';
            card.style.transform = '';
            card.style.boxShadow = '';
        });
    }

    updateDayGridLanguage(language);

    if (matchedCard && scrollToDaySelection) {
        const daySection = document.querySelector('#day-selection');
        daySection && daySection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}
function initializeScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Apply different animations based on element type
                if (entry.target.classList.contains('section-card')) {
                    entry.target.classList.add('animate-slide-right');
                } else if (entry.target.classList.contains('benefit-card')) {
                    entry.target.classList.add('animate-slide-left');
                } else {
                    entry.target.classList.add('animate-fade-in');
                }
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    // Observe all sections, cards, and course sections
    document.querySelectorAll('section, .language-card, .section-card, .benefit-card, .section-divider').forEach(el => {
        if (!el.classList.contains('animate-fade-in') &&
            !el.classList.contains('animate-slide-right') &&
            !el.classList.contains('animate-slide-left')) {
            observer.observe(el);
        }
    });
    
    // Add floating animation to visual anchors
    document.querySelectorAll('.visual-anchor').forEach(anchor => {
        anchor.classList.add('animate-float');
    });
}

// Initialize micro-interactions
function initializeMicroInteractions() {
    // Add pulse animation to section dividers
    document.querySelectorAll('.section-divider').forEach(divider => {
        divider.classList.add('animate-pulse');
    });
    
    // Add hover effects to benefit cards
    document.querySelectorAll('.benefit-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.background = 'linear-gradient(135deg, white, #f8f9fa)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.background = 'white';
        });
    });
    
    // Add hover effects to course section cards
    document.querySelectorAll('.section-card').forEach((card, index) => {
        card.addEventListener('mouseenter', function() {
            this.style.borderLeftWidth = '8px';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.borderLeftWidth = '4px';
        });
    });
}

// Progress tracking
function updateProgress(day) {
    const progressFills = document.querySelectorAll('.progress-fill');
    const progress = (day / 50) * 100;
    
    progressFills.forEach(fill => {
        fill.style.width = `${progress}%`;
    });
    
    // Update all progress texts
    document.querySelectorAll('.progress-container p span').forEach(text => {
        text.setAttribute('data-i18n', 'progress.status');
        text.setAttribute('data-i18n-params', JSON.stringify({ completed: day }));
        if (window.i18n) {
            window.i18n.updateLanguage(window.i18n.currentLang);
        }
    });
}

// Helper function to format dates
function formatDate(date) {
    return new Intl.DateTimeFormat('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
}

// Error handling
function handleError(error) {
    console.error('An error occurred:', error);
    const main = document.querySelector('main');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error animate-fade-in';
    errorDiv.textContent = 'An error occurred. Please try again later.';
    main.prepend(errorDiv);
}
