class I18n {
    constructor() {
        this.translations = {};
        const urlParams = new URLSearchParams(window.location.search);
        this.currentLang = urlParams.get('lang') || localStorage.getItem('preferredLanguage') || navigator.language.split('-')[0] || 'en';
        this.supportedLanguages = ['en', 'es', 'de', 'fr', 'pt'];
        
        // If saved language is not supported, default to English
        if (!this.supportedLanguages.includes(this.currentLang)) {
            this.currentLang = 'en';
        }
    }

    async init() {
        // Load all translations
        await Promise.all(this.supportedLanguages.map(lang => 
            fetch(`translations/${lang}.json`)
                .then(response => response.json())
                .then(data => {
                    this.translations[lang] = data;
                })
                .catch(error => console.error(`Error loading ${lang} translations:`, error))
        ));

        // Initial translation
        this.updateLanguage(this.currentLang);
        this.setupLanguageSelector();
    }

    setupLanguageSelector() {
        const selector = document.getElementById('languageSelector');
        if (!selector) return;

        // Clear existing options
        selector.innerHTML = '';

        // Add options for each supported language
        const languageNames = {
            en: 'English',
            es: 'Español',
            de: 'Deutsch',
            fr: 'Français',
            pt: 'Português'
        };

        this.supportedLanguages.forEach(lang => {
            const option = document.createElement('option');
            option.value = lang;
            option.textContent = languageNames[lang];
            option.selected = lang === this.currentLang;
            selector.appendChild(option);
        });

        // Listen for changes
        selector.addEventListener('change', (e) => {
            this.updateLanguage(e.target.value);
        });
    }

    updateLanguage(lang) {
        if (!this.translations[lang]) return;
        
        this.currentLang = lang;
        localStorage.setItem('preferredLanguage', lang);
        document.documentElement.lang = lang;

        // Update all elements with data-i18n attribute
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const keys = element.getAttribute('data-i18n').split('.');
            let value = this.translations[lang];
            
            // Traverse the nested object
            for (const key of keys) {
                if (value && value[key]) {
                    value = value[key];
                } else {
                    console.warn(`Translation missing for key: ${keys.join('.')} in language: ${lang}`);
                    return;
                }
            }

            // Handle different element types
            if (element.tagName === 'INPUT' && element.type === 'placeholder') {
                element.placeholder = value;
            } else if (element.tagName === 'META' && element.name === 'description') {
                element.content = value;
            } else {
                // Replace any placeholders in the translation
                if (typeof value === 'string' && element.hasAttribute('data-i18n-params')) {
                    const params = JSON.parse(element.getAttribute('data-i18n-params'));
                    value = this.replacePlaceholders(value, params);
                }
                element.innerHTML = value;
            }
        });

        // Update lists that use data-i18n-list
        document.querySelectorAll('[data-i18n-list]').forEach(element => {
            const keys = element.getAttribute('data-i18n-list').split('.');
            let items = this.translations[lang];
            
            // Traverse the nested object to get the array
            for (const key of keys) {
                if (items && items[key]) {
                    items = items[key];
                } else {
                    console.warn(`Translation missing for list: ${keys.join('.')} in language: ${lang}`);
                    return;
                }
            }

            if (Array.isArray(items)) {
                element.innerHTML = items.map(item => `<li>${item}</li>`).join('');
            }
        });

        // Dispatch event for other components that might need to know about language changes
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
    }

    replacePlaceholders(text, params) {
        return text.replace(/\{(\w+)\}/g, (match, key) => {
            return params[key] !== undefined ? params[key] : match;
        });
    }

    // Helper method to get a translation by key
    translate(key, params = null) {
        const keys = key.split('.');
        let value = this.translations[this.currentLang];
        
        for (const k of keys) {
            if (value && value[k]) {
                value = value[k];
            } else {
                console.warn(`Translation missing for key: ${key} in language: ${this.currentLang}`);
                return key;
            }
        }

        if (params && typeof value === 'string') {
            value = this.replacePlaceholders(value, params);
        }

        return value;
    }
}

// Initialize i18n when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.i18n = new I18n();
    window.i18n.init();
});