class DayI18n {
    constructor() {
        this.translations = {};
        this.currentLang = new URLSearchParams(window.location.search).get('lang') ||
                          localStorage.getItem('preferredLanguage') ||
                          navigator.language.split('-')[0] ||
                          'en';
        this.supportedLanguages = ['en', 'es', 'de', 'fr', 'pt'];
        
        // If language is not supported, default to English
        if (!this.supportedLanguages.includes(this.currentLang)) {
            this.currentLang = 'en';
        }
    }

    async init() {
        // Load translations for current language
        try {
            const response = await fetch(`translations/day.${this.currentLang}.json`);
            if (!response.ok) {
                throw new Error(`Failed to load translations for ${this.currentLang}`);
            }
            this.translations = await response.json();
            
            // Update all translations on the page
            this.updatePageTranslations();
            
            // Update section info
            const day = parseInt(new URLSearchParams(window.location.search).get('day')) || 1;
            const sectionInfo = this.getSectionInfo(day);
            const titleElement = document.getElementById('section-title');
            const descriptionElement = document.getElementById('section-description');
            
            if (titleElement && descriptionElement) {
                titleElement.textContent = sectionInfo.title;
                descriptionElement.textContent = sectionInfo.description;
            }

            // Update language buttons active state
            this.updateLanguageButtons();
        } catch (error) {
            console.error('Error loading translations:', error);
            // Fallback to English if translation fails
            if (this.currentLang !== 'en') {
                this.currentLang = 'en';
                await this.init();
            }
        }
    }

    updateLanguageButtons() {
        document.querySelectorAll('.language-btn').forEach(btn => {
            const isActive = btn.dataset.lang === this.currentLang;
            btn.classList.toggle('active', isActive);
            if (isActive) {
                btn.setAttribute('aria-current', 'true');
                // Update localStorage when language button is active
                localStorage.setItem('preferredLanguage', this.currentLang);
            } else {
                btn.removeAttribute('aria-current');
            }
        });
    }

    updatePageTranslations() {
        // Update all elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const keys = element.getAttribute('data-i18n').split('.');
            let value = this.translations;
            
            // Traverse the nested object
            for (const key of keys) {
                if (value && value[key]) {
                    value = value[key];
                } else {
                    console.warn(`Translation missing for key: ${keys.join('.')} in language: ${this.currentLang}`);
                    return;
                }
            }

            // Handle different element types
            if (element.tagName === 'INPUT' && element.type === 'placeholder') {
                element.placeholder = value;
            } else {
                element.innerHTML = value;
            }
        });

        // Update language buttons
        document.querySelectorAll('.language-btn').forEach(btn => {
            const lang = btn.dataset.lang;
            const langKey = {
                'en': 'english',
                'es': 'spanish',
                'pt': 'portuguese',
                'fr': 'french',
                'de': 'german'
            }[lang];
            
            if (this.translations.languages && this.translations.languages[langKey]) {
                const text = btn.querySelector('.language-text');
                if (text) {
                    text.textContent = this.translations.languages[langKey];
                }
            }
            
            // Set active state
            if (lang === this.currentLang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        // Update document language
        document.documentElement.lang = this.currentLang;
    }

    translate(key, params = null) {
        const keys = key.split('.');
        let value = this.translations;
        
        for (const k of keys) {
            if (value && value[k]) {
                value = value[k];
            } else {
                console.warn(`Translation missing for key: ${key} in language: ${this.currentLang}`);
                return key;
            }
        }

        if (params && typeof value === 'string') {
            Object.entries(params).forEach(([key, val]) => {
                value = value.replace(`{${key}}`, val);
            });
        }

        return value;
    }

    getSectionInfo(day) {
        let section;
        if (day <= 7) {
            section = 'basic';
        } else if (day <= 15) {
            section = 'advanced';
        } else if (day <= 26) {
            section = 'international';
        } else if (day <= 31) {
            section = 'tech';
        } else {
            section = 'academic';
        }

        // Default values in case translations fail
        const defaults = {
            basic: {
                title: 'Basic Vocabulary & Essential Phrases',
                description: 'Learn fundamental vocabulary and essential phrases for beginners.'
            },
            advanced: {
                title: 'Advanced Phrases',
                description: 'More complex conversations and vocabulary for intermediate learners.'
            },
            international: {
                title: 'International Living & Working',
                description: 'Practical phrases for global living and professional environments.'
            },
            tech: {
                title: 'Tech Professional Content',
                description: 'Specialized content for software engineers and tech professionals.'
            },
            academic: {
                title: 'Advanced Academic & Professional',
                description: 'Advanced language skills for academic and professional settings.'
            }
        };

        try {
            if (this.translations?.sections?.[section]?.title && this.translations?.sections?.[section]?.description) {
                return {
                    title: this.translations.sections[section].title,
                    description: this.translations.sections[section].description
                };
            }
            // If translation is missing, use default English values
            return defaults[section];
        } catch (error) {
            console.warn(`Using default values for section ${section}:`, error);
            return defaults[section];
        }
    }
}

// Initialize i18n when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.i18n = new DayI18n();
    window.i18n.init();
});