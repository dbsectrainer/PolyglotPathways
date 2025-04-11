document.addEventListener('DOMContentLoaded', function() {
    // Initialize language buttons
    const langButtons = document.querySelectorAll('.lang-btn');
    const progressCards = document.querySelectorAll('.progress-card');
    
    // Function to update active language
    function setActiveLanguage(lang) {
        // Update button states
        langButtons.forEach(btn => {
            btn.classList.remove('active');
            if (btn.getAttribute('data-lang') === lang) {
                btn.classList.add('active');
            }
        });

        // Update progress card visibility
        progressCards.forEach(card => {
            card.style.display = 'none';
            if (card.classList.contains(lang)) {
                card.style.display = 'block';
            }
        });

        // Store selected language
        localStorage.setItem('selectedLanguage', lang);
    }

    // Add click handlers to language buttons
    langButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const lang = this.getAttribute('data-lang');
            setActiveLanguage(lang);
        });
    });

    // Set initial active language
    const savedLang = localStorage.getItem('selectedLanguage') || 'english';
    setActiveLanguage(savedLang);

    // Update progress when localStorage changes
    window.addEventListener('storage', function(e) {
        if (e.key === 'completedDays') {
            const completedDays = JSON.parse(e.newValue || '{}');
            updateAllProgress(completedDays);
        }
    });

    // Function to update progress for all languages
    function updateAllProgress(completedDays) {
        const languages = ['english', 'spanish', 'portuguese', 'french', 'german'];
        const langCodes = { english: 'en', spanish: 'es', portuguese: 'pt', french: 'fr', german: 'de' };

        languages.forEach(lang => {
            const completed = Object.keys(completedDays).filter(key => 
                key.endsWith(`_${langCodes[lang]}`)).length;
            
            const card = document.querySelector(`.progress-card.${lang}`);
            if (card) {
                const progressText = card.querySelector('.completed');
                const progressBar = card.querySelector('.progress-fill');
                
                if (progressText) progressText.textContent = completed;
                if (progressBar) progressBar.style.width = `${(completed / 50) * 100}%`;
            }
        });
    }

    // Initialize progress on load
    const completedDays = JSON.parse(localStorage.getItem('completedDays') || '{}');
    updateAllProgress(completedDays);
});
