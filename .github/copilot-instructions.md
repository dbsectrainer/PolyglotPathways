# Copilot Instructions for Polyglot Pathways

## Project Overview
Polyglot Pathways is a multilingual language learning platform that provides a structured 50-day curriculum across 5 languages (English, Spanish, Portuguese, French, German). The platform emphasizes vanilla JavaScript, accessibility, and offline-first architecture.

## Architecture & Technology Stack

### Core Technologies
- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3
- **No frameworks**: Prefer vanilla JavaScript over frameworks like React, Vue, or Angular
- **State Management**: localStorage for persistence
- **Audio**: Native Web Audio API and HTML5 audio elements
- **Internationalization**: Custom i18n implementation in `js/i18n.js`
- **Content Generation**: Python scripts for automated content creation

### Key Principles
1. **Vanilla JavaScript First**: Avoid adding dependencies unless absolutely necessary
2. **Accessibility**: Full keyboard navigation, screen reader support, ARIA labels
3. **Multilingual Support**: All UI elements must support i18n
4. **Offline-First**: Application should work without internet connectivity
5. **Progressive Enhancement**: Graceful degradation when features aren't available
6. **Mobile-Responsive**: Touch-friendly interfaces for all screen sizes

## File Structure & Naming Conventions

### JavaScript Modules (`js/`)
- `script.js` - Main application logic and initialization
- `i18n.js` - Core internationalization engine
- `day-i18n.js` - Day-specific i18n configurations
- `language-selector.js` - Dynamic language switching
- `exercises.js` - Interactive exercise controller
- `drag-drop.js` - Drag-and-drop exercise component
- `fill-blank.js` - Fill-in-the-blank exercise component
- `matching.js` - Matching game component

### Content Files
- `translations/*.json` - Language resource files
- `exercises/day{N}_{lang}.json` - Exercise data (e.g., `day1_en.json`, `day1_es.json`)
- `audio_files/day{N}_{lang}.mp3` - Audio content
- `text_files/` - Text transcripts

### Content Generation Scripts
- `language_phrases_days_*.py` - Python scripts for generating course content
- Follow existing patterns when adding new content generation

## Coding Standards

### JavaScript
- Use ES6+ features (arrow functions, const/let, destructuring, modules)
- Prefer functional programming patterns when appropriate
- Use meaningful variable names (e.g., `currentLanguage`, `exerciseProgress`)
- Add error handling for all async operations
- Include accessibility features in all interactive components

```javascript
// Good: Comprehensive error handling and accessibility
async function loadExerciseData(day, language) {
    try {
        const response = await fetch(`exercises/day${day}_${language}.json`);
        if (!response.ok) {
            throw new Error(`Failed to load exercise: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.warn(`Exercise data not available: ${error.message}`);
        return null; // Graceful degradation
    }
}

// Good: Accessibility-aware component
function createInteractiveButton(text, onClick) {
    const button = document.createElement('button');
    button.textContent = text;
    button.setAttribute('aria-label', text);
    button.addEventListener('click', onClick);
    button.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            onClick(e);
        }
    });
    return button;
}
```

### CSS
- Use BEM methodology for class naming
- Include focus states for all interactive elements
- Ensure sufficient color contrast (WCAG AA compliance)
- Use relative units (rem, em) for scalability
- Include print stylesheets where appropriate

### HTML
- Use semantic HTML5 elements
- Include proper ARIA labels and roles
- Ensure logical tab order
- Add lang attributes for multilingual content

## Internationalization (i18n) Guidelines

### Adding New UI Text
1. Never hardcode text strings in JavaScript or HTML
2. Add all text to appropriate translation files in `translations/`
3. Use the i18n system: `i18n.translate('key.path')`
4. Support all 5 languages: `en`, `es`, `pt`, `fr`, `de`

```javascript
// Bad
document.querySelector('.error').textContent = 'Error loading content';

// Good
document.querySelector('.error').textContent = i18n.translate('errors.loading_content');
```

### Translation File Structure
```json
{
  "navigation": {
    "home": "Home",
    "lessons": "Lessons"
  },
  "exercises": {
    "drag_drop": {
      "instructions": "Drag the words to complete the sentence",
      "word_bank": "Word Bank"
    }
  }
}
```

## Interactive Exercises

### Exercise Types
1. **Drag-and-Drop**: Word placement with visual feedback
2. **Fill-in-the-Blank**: Text input with real-time validation
3. **Matching Games**: Two-column item association

### Exercise Implementation Requirements
- Full keyboard navigation support
- Touch-friendly mobile interactions
- Screen reader announcements for all state changes
- Visual feedback for hover, focus, and active states
- Graceful handling when exercise data is unavailable
- Progress tracking integration with localStorage

### Exercise Data Format
```json
{
  "type": "drag-drop",
  "title": "Complete the Greetings",
  "instructions": "Drag words from the bank to complete each sentence",
  "sentences": [
    {
      "text": "Good [morning] everyone!",
      "blanks": [
        {
          "placeholder": "morning",
          "correct": ["morning", "afternoon", "evening"],
          "position": 5
        }
      ]
    }
  ],
  "wordBank": ["morning", "afternoon", "evening", "night"],
  "distractors": ["apple", "car"]
}
```

## Accessibility Requirements

### Keyboard Navigation
- All interactive elements must be keyboard accessible
- Logical tab order throughout the application
- Clear focus indicators with sufficient contrast
- Support for standard keyboard shortcuts (Arrow keys, Enter, Space, Escape)

### Screen Reader Support
- ARIA labels for all interactive elements
- Live regions for dynamic content updates
- Proper heading hierarchy (h1, h2, h3...)
- Alt text for images and meaningful icons

### Visual Design
- Minimum contrast ratio of 4.5:1 for normal text
- Minimum contrast ratio of 3:1 for large text
- Focus indicators must be clearly visible
- Support for reduced motion preferences

## Performance Considerations

### Loading Strategies
- Lazy load audio files and large resources
- Cache translation files in localStorage
- Preload critical resources for next lesson
- Compress images and audio files appropriately

### Memory Management
- Clean up event listeners when components are destroyed
- Avoid memory leaks in long-running sessions
- Use WeakMap/WeakSet for temporary references

## Testing Guidelines

### Manual Testing Checklist
- [ ] Test with keyboard-only navigation
- [ ] Verify screen reader announcements
- [ ] Test on mobile devices with touch interactions
- [ ] Verify offline functionality
- [ ] Check all 5 language translations
- [ ] Test with slow network connections

### Browser Support
- Modern browsers with ES6+ support
- iOS Safari 12+
- Android Chrome 70+
- Desktop Chrome, Firefox, Safari, Edge (latest versions)

## Common Patterns

### Module Structure
```javascript
// exercises.js - Main controller pattern
(function() {
    'use strict';
    
    class ExerciseController {
        constructor() {
            this.currentExercise = null;
            this.progress = this.loadProgress();
        }
        
        async init(day, language) {
            // Implementation
        }
        
        loadProgress() {
            // localStorage integration
        }
        
        saveProgress() {
            // localStorage integration
        }
    }
    
    window.ExerciseController = ExerciseController;
})();
```

### Error Handling Pattern
```javascript
function withErrorHandling(fn, fallback = null) {
    return async (...args) => {
        try {
            return await fn(...args);
        } catch (error) {
            console.warn(`Operation failed: ${error.message}`);
            return fallback;
        }
    };
}
```

## Content Guidelines

### Language Learning Content
- Use authentic, practical phrases and vocabulary
- Include cultural context where appropriate
- Provide audio pronunciation for all content
- Ensure translations are culturally appropriate, not literal
- Include progressive difficulty across the 50-day curriculum

### Exercise Design
- Start with simple concepts and build complexity
- Include multiple learning modalities (visual, auditory, kinesthetic)
- Provide immediate feedback on user interactions
- Allow multiple attempts with encouraging messaging
- Track progress without creating anxiety

## Maintenance Notes

### When Adding New Features
1. Consider impact on all 5 languages
2. Ensure accessibility compliance
3. Test offline functionality
4. Update relevant documentation
5. Follow existing file naming conventions
6. Add appropriate error handling

### Content Updates
- Use Python scripts for bulk content generation
- Maintain consistency across all language versions
- Validate audio file availability
- Check translation accuracy with native speakers when possible

This repository prioritizes accessibility, multilingual support, and vanilla JavaScript simplicity. When in doubt, favor solutions that enhance these core principles.