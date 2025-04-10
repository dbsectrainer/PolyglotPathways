# Polyglot Pathways

## Overview
A comprehensive multilingual learning platform that helps users master English, Spanish, Portuguese, French, and German through a structured 50-day program. The project combines interactive web interfaces with rich audio-visual content, focusing on global professional and cultural integration.

## Project Structure
- **website/**: Web interface for interactive learning
  - `index.html`: Main dashboard with language progress tracking
  - `day.html`: Daily lesson interface with audio and text content
  - `css/`: Stylesheets for the web interface
  - `js/`: JavaScript functionality
- **audio_files/**: MP3 audio files for each day and language
- **text_files/**: Text transcripts of all phrases
- **language_phrases_days_*.py**: Python scripts for content generation

## Course Structure

### Basic Vocabulary & Essential Phrases (Days 1-7)
- Fundamental vocabulary and essential phrases for beginners
- Core communication building blocks
- Basic grammar structures

### Advanced Phrases (Days 8-15)
- Complex conversations and intermediate vocabulary
- Professional communication
- Cultural expressions and idioms

### International Living & Working (Days 16-26)
- Global professional environments
- Cross-cultural communication
- Business and workplace vocabulary
- Housing and daily life across cultures

### Tech Professional Content (Days 27-31)
- Software engineering terminology
- Technical vocabulary
- Digital communication
- Industry-specific phrases

### Advanced Academic & Professional (Days 32-50)
- Advanced language skills for global contexts
- Academic writing and presentations
- Professional negotiations
- Complex business communication

## Features

### Interactive Web Interface
- Progress tracking for each language
- Audio playback with text transcripts
- Copy-to-clipboard functionality
- Mobile-responsive design
- Session persistence

### Language Support
All content is available in five languages:
- 🇬🇧 English (en)
- 🇪🇸 Spanish (es)
- 🇧🇷 Portuguese (pt)
- 🇫🇷 French (fr)
- 🇩🇪 German (de)

### Key Benefits
1. **Global Reach & Communication**
   - English: Global lingua franca for business, science, and tech
   - Spanish: 2nd most spoken native language worldwide
   - Portuguese: Key for Brazil's huge market and African nations
   - French: Official in 29 countries across multiple continents
   - German: Most spoken native language in Europe

2. **Career & Business Opportunities**
   - Access to global job markets
   - International freelancing opportunities
   - Positions in international organizations
   - Enhanced remote work capabilities

3. **Strategic Language Combinations**
   - Spanish + Portuguese: Covers almost all of Latin America
   - French + English: Dominates diplomacy & Africa
   - German + English: Opens EU corporate doors
   - All 5 Languages: Communicate with ~2 billion people

## Development

### Requirements
- Python 3.12+
- gTTS (Google Text-to-Speech) library
```bash
pip install gtts
```

### Content Generation
```bash
# Generate content for specific days
python language_phrases_days_01_07.py
python language_phrases_days_08_15.py
python language_phrases_days_16_26.py
python language_phrases_days_27_31.py
python language_phrases_days_32_44.py
python language_phrases_days_45_50.py
```

### Running the Website
The website can be accessed directly by opening `website/index.html` in a web browser. No server setup is required as it uses client-side JavaScript for all functionality.

## Usage
1. Open `website/index.html` in a web browser
2. Select your target language
3. Progress through daily lessons sequentially
4. Use the audio player and text content for comprehensive learning
5. Mark lessons as complete to track your progress
6. Switch between languages to practice multiple languages simultaneously

## Storage
The application uses localStorage to maintain:
- Progress tracking for each language
- Completed lessons
- Current language selection
