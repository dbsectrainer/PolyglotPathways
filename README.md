# South American Language Learning Project

## Overview
This project provides comprehensive language learning resources for English speakers learning Spanish, Portuguese, French, and German, with a focus on living and working in South America. It includes audio files and text transcripts for 31 days of language learning content, covering basic to advanced topics.

## Project Structure
- **audio_files/**: Contains all MP3 audio files for each day and language
- **text_files/**: Contains text transcripts of all phrases
- **scripts/**: Contains Python scripts used to generate the audio and text files

## Content Overview

### Basic Phrases (Days 1–7)
Basic vocabulary and essential phrases for beginners.

### Advanced Phrases (Days 8–15)
More complex conversations and vocabulary for intermediate learners:
- Philosophical conversations
- Storytelling techniques
- Debating and persuasion
- Advanced humor and wit
- Professional vocabulary
- Cultural expressions

### Living & Working in South America (Days 16–26)
Practical phrases specifically for expatriates and travelers in South America:

#### Days 16–19: Essential Living Topics
- Finding housing and accommodation
- Job hunting in South America
- Banking and finance
- Healthcare systems

#### Days 20–22: Cultural Integration
- Regional cultural nuances
- Workplace language and etiquette
- Renting and housing vocabulary

#### Days 23–24: Practical Daily Life
- Banking and bureaucracy
- Transportation and logistics

#### Days 25–26: Social Integration
- Making local friends and building community
- Dating and relationships
- Safety and street smarts
- Religion, traditions, and holidays
- Country-specific slang (Argentina, Brazil, Colombia, Peru, Chile)

### Enhanced Content for Tech Professionals (Days 27–31)
Additional specialized content for software engineers and tech professionals working in South America:

#### Days 27–28: Tech & Software Engineering
- Software engineering workplace vocabulary
- Programming languages and concepts
- Development tools and methodologies
- Tech problem solving
- Digital life and tech vocabulary
- Digital security and privacy

#### Day 29: Environmental & Geographical Terms
- South American geography
- Climate and weather terminology
- Natural landscapes
- Sustainability and conservation
- Outdoor activities

#### Day 30: Indigenous Influence & Cultural Heritage
- Indigenous words in Spanish/Portuguese
- Indigenous cultural heritage
- Traditional knowledge and practices
- Cultural celebrations
- Indigenous communities today

#### Day 31: Contemporary Slang & Modern Communication
- Country-specific contemporary slang
- Modern workplace expressions
- Digital communication slang

## Languages
All content is available in five languages:
- English (en)
- Spanish (es)
- Portuguese (pt)
- French (fr)
- German (de)

## How to Use
The Python scripts can generate audio files and text transcripts for specific days and languages:

### Generate Audio and Text Files
```bash
# Generate all files for all days in all supported languages (default: Spanish and Portuguese)
python scripts/language_phrases.py                     # Days 1–7
python scripts/language_phrases_advanced.py            # Days 8–15
python scripts/language_phrases_advanced_extended.py   # Days 16–26
python scripts/language_phrases_advanced_enhanced.py   # Days 27–31 (Tech Professional content)

# Generate files for a specific day
python scripts/language_phrases_advanced_extended.py --day 20
python scripts/language_phrases_advanced_enhanced.py --day 27

# Generate files for a specific language
python scripts/language_phrases_advanced_extended.py --languages fr
python scripts/language_phrases_advanced_enhanced.py --languages de

# Generate text files only (no audio)
python scripts/language_phrases_advanced_extended.py --text-only
python scripts/language_phrases_advanced_enhanced.py --text-only
```

### Learning Approach
1. Listen to the audio files for your target language
2. Use the text files as reference for reading practice
3. Progress through the days sequentially, or focus on specific topics relevant to your needs

## Requirements
- Python 3.6+
- gTTS (Google Text-to-Speech) library
```bash
pip install gtts
