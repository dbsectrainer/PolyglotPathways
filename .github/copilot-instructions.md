# Copilot Instructions for Polyglot Pathways

## Project Overview
Polyglot Pathways is a static, client-side web application for multilingual language learning. It supports English, Spanish, Portuguese, French, and German, offering a 50-day structured curriculum with text and audio content. No server or build step is required—open `index.html` in a browser to run.

## Key Components & Data Flow
- **index.html**: Main dashboard, tracks user progress.
- **day.html**: Daily lesson interface, loads content dynamically.
- **js/**: Contains all core logic:
  - `i18n.js`: Internationalization engine, loads translations.
  - `day-i18n.js`: Handles day-specific language content.
  - `language-selector.js`: Manages language switching UI.
  - `script.js`: Main app logic, state management, audio playback.
- **audio_files/**: MP3s for each day/language, named `day{N}_{lang}.mp3`.
- **translations/**: Language resource files for UI and lessons.
- **language_phrases_days_*.py**: Python scripts for generating lesson content.

## Developer Workflows
- **No build or install step**: Just edit files and refresh the browser.
- **Content updates**: Use the Python scripts to generate or update lesson text/audio. Place new files in `audio_files/` and `translations/`.
- **Testing**: Manual—open in browser, switch languages, play audio, check localStorage persistence.
- **Debugging**: Use browser dev tools. All logic is client-side JS.

## Project-Specific Patterns
- **File naming**: Audio files strictly follow `day{N}_{lang}.mp3` (e.g., `day10_fr.mp3`).
- **State**: User progress and preferences are stored in `localStorage`.
- **Offline support**: App is designed to work offline after initial load; resources are cached by the browser.
- **Fallbacks**: If translation or audio fails to load, default to English or text-only mode.
- **No external dependencies**: All JS/CSS is local; no npm, no frameworks.

## Integration Points
- **Content generation**: Python scripts output lesson data; update both text and audio assets together for consistency.
- **CI**: GitHub Actions workflow exists for basic checks, but no automated deployment/build.

## Examples
- To add a new language, update all translation files, generate new audio, and extend JS logic if needed.
- To add a new lesson day, update Python scripts, generate new audio/text, and add files to the appropriate folders.

## References
- See `README.md` for architecture diagrams and curriculum breakdown.
- See `CONTRIBUTING.md` for contribution process and code of conduct.

---
For any ambiguity or missing conventions, prefer the patterns in `js/`, `audio_files/`, and `translations/` as canonical. When in doubt, check the `README.md` for the latest project structure and workflow.
