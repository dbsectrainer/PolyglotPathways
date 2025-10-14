#!/usr/bin/env python3
"""
Exercise Generator for Polyglot Pathways
Generates comprehensive interactive exercises for all 50 days across 5 languages
Based on existing text file content from text_files/ directory
"""

import os
import re
import json
import random

# Language configuration
LANGUAGES = ['es', 'pt', 'fr', 'de', 'en']
LANGUAGE_NAMES = {
    'es': 'español',
    'pt': 'português', 
    'fr': 'français',
    'de': 'Deutsch',
    'en': 'English'
}

# Phonetic patterns for common words (simplified)
PHONETICS = {
    'es': {
        'hola': '[ˈo.la]',
        'buenos': '[ˈbwe.nos]',
        'días': '[ˈdi.as]',
        'gracias': '[ˈɡɾa.sjas]',
        'por favor': '[poɾ fa.ˈβoɾ]',
    },
    'pt': {
        'olá': '[oˈla]',
        'bom': '[bõ]',
        'dia': '[ˈdiɐ]',
        'obrigado': '[obɾiˈɡadu]',
        'por favor': '[puɾ fɐˈvoɾ]',
    },
    'fr': {
        'bonjour': '[bɔ̃.ʒuʁ]',
        'merci': '[mɛʁ.si]',
        's\'il vous plaît': '[sil vu plɛ]',
    },
    'de': {
        'hallo': '[ˈha.loː]',
        'guten': '[ˈɡuːtn̩]',
        'morgen': '[ˈmɔʁɡn̩]',
        'danke': '[ˈdaŋ.kə]',
        'bitte': '[ˈbɪ.tə]',
    }
}

def parse_text_file(filepath):
    """Parse a text file and extract phrases by category"""
    phrases = {}
    current_category = None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        
        if not line:
            continue
        
        # Skip lines that are just dashes (category underlines)
        if set(line.replace(' ', '')) == {'-'}:
            continue
        
        # Check if next line is dashes - if so, current line is definitely a category header
        is_category = False
        if i < len(lines):
            next_line = lines[i].strip()
            if next_line and set(next_line.replace(' ', '')) == {'-'}:
                is_category = True
                i += 1  # Skip the dash line
        
        if is_category:
            current_category = line
            if current_category not in phrases:
                phrases[current_category] = []
        elif current_category and line:
            # This is content under a category
            phrases[current_category].append(line)
        elif not current_category:
            # No category yet, create a default one
            if 'General Phrases' not in phrases:
                phrases['General Phrases'] = []
            phrases['General Phrases'].append(line)
    
    return phrases

def get_translation_pair(phrase, lang_code):
    """Try to find English translation for a phrase"""
    # For English files, phrases are already in English
    if lang_code == 'en':
        return phrase, phrase
    
    # Try to load corresponding English file
    en_file = f"text_files/day{os.path.basename(phrase).split('_')[0].replace('day', '')}_en.txt"
    return phrase, "Translation"

def create_listening_exercise(day, lang, phrase, translation, audio_path, idx):
    """Create a listening comprehension exercise"""
    # Create distractor options
    options = [phrase]
    
    # Add some random distractors (simplified)
    distractors = [
        "Option A", "Option B", "Option C"
    ]
    options.extend(distractors[:3])
    random.shuffle(options)
    correct_idx = options.index(phrase)
    
    question_templates = {
        'es': '¿Qué frase escuchaste?',
        'pt': 'Que frase você ouviu?',
        'fr': 'Quelle phrase avez-vous entendue?',
        'de': 'Welchen Satz hast du gehört?',
        'en': 'What phrase did you hear?'
    }
    
    return {
        'id': f'day{day}_{lang}_listening_{idx}',
        'type': 'listening',
        'language': lang,
        'audio': audio_path,
        'text': phrase,
        'translation': translation,
        'question': question_templates.get(lang, 'What did you hear?'),
        'options': options,
        'correct': correct_idx
    }

def create_pronunciation_exercise(day, lang, phrase, idx):
    """Create a pronunciation practice exercise"""
    # Generate a simple phonetic representation
    phonetic = f'[{phrase.lower()}]'
    
    return {
        'id': f'day{day}_{lang}_pronunciation_{idx}',
        'type': 'pronunciation',
        'language': lang,
        'text': phrase,
        'phonetic': phonetic,
        'targetAccuracy': 85
    }

def create_fillblank_exercise(day, lang, phrase, idx):
    """Create a fill-in-the-blank exercise"""
    words = phrase.split()
    if len(words) < 2:
        return None
    
    # Pick a meaningful word to blank out (prefer longer words)
    word_to_blank = max(words, key=len) if len(words) > 1 else words[0]
    blank_position = phrase.find(word_to_blank)
    
    sentence = phrase[:blank_position] + '__' + phrase[blank_position + len(word_to_blank):]
    
    # Generate options (correct + distractors)
    options = [word_to_blank, 'OptionA', 'OptionB', 'OptionC']
    random.shuffle(options)
    
    return {
        'id': f'day{day}_{lang}_fillblank_{idx}',
        'type': 'fill-blank',
        'language': lang,
        'sentence': sentence,
        'options': options,
        'correct': word_to_blank
    }

def create_translation_exercise(day, lang, english_text, target_text, idx):
    """Create a translation exercise"""
    return {
        'id': f'day{day}_{lang}_translation_{idx}',
        'type': 'translation',
        'language': lang,
        'text': english_text,
        'correctAnswer': target_text
    }

def create_matching_exercise(day, lang, pairs, idx):
    """Create a matching exercise"""
    if len(pairs) < 4:
        return None
    
    return {
        'id': f'day{day}_{lang}_matching_{idx}',
        'type': 'matching',
        'language': lang,
        'pairs': pairs[:4]  # Limit to 4 pairs
    }

def create_sentence_reconstruction_exercise(day, lang, phrase, translation, idx):
    """Create a sentence reconstruction exercise"""
    words = phrase.split()
    if len(words) < 2:
        return None
    
    return {
        'id': f'day{day}_{lang}_sentence_{idx}',
        'type': 'sentence-reconstruction',
        'language': lang,
        'words': words,
        'translation': translation,
        'correctSentence': phrase
    }

def generate_exercises_for_day(day, lang):
    """Generate a varied set of exercises for a specific day and language"""
    text_file = f'text_files/day{day}_{lang}.txt'
    en_text_file = f'text_files/day{day}_en.txt'
    
    if not os.path.exists(text_file):
        print(f"Warning: {text_file} not found")
        return []
    
    # Parse the text files
    phrases = parse_text_file(text_file)
    en_phrases = parse_text_file(en_text_file) if os.path.exists(en_text_file) else {}
    
    # Flatten phrases from all categories
    all_phrases = []
    all_en_phrases = []
    
    for category, phrase_list in phrases.items():
        all_phrases.extend(phrase_list)
    
    for category, phrase_list in en_phrases.items():
        all_en_phrases.extend(phrase_list)
    
    if not all_phrases:
        print(f"Warning: No phrases found in {text_file}")
        return []
    
    # Ensure we have parallel English translations
    if len(all_en_phrases) < len(all_phrases):
        all_en_phrases = all_phrases  # Fallback
    
    exercises = []
    audio_path = f'audio_files/day{day}_{lang}.mp3'
    
    # Select phrases for different exercise types
    # Aim for 4-6 exercises per day
    selected_indices = random.sample(range(min(10, len(all_phrases))), min(6, len(all_phrases)))
    
    exercise_count = 0
    
    # 1. Listening comprehension (1-2 exercises)
    for i in range(min(2, len(selected_indices))):
        idx = selected_indices[i]
        if idx < len(all_phrases):
            phrase = all_phrases[idx]
            translation = all_en_phrases[idx] if idx < len(all_en_phrases) else phrase
            ex = create_listening_exercise(day, lang, phrase, translation, audio_path, exercise_count)
            exercises.append(ex)
            exercise_count += 1
    
    # 2. Pronunciation practice (1 exercise)
    if len(selected_indices) > 2:
        idx = selected_indices[2]
        if idx < len(all_phrases):
            phrase = all_phrases[idx]
            ex = create_pronunciation_exercise(day, lang, phrase, exercise_count)
            exercises.append(ex)
            exercise_count += 1
    
    # 3. Fill-in-the-blank (1 exercise)
    if len(selected_indices) > 3:
        idx = selected_indices[3]
        if idx < len(all_phrases):
            phrase = all_phrases[idx]
            ex = create_fillblank_exercise(day, lang, phrase, exercise_count)
            if ex:
                exercises.append(ex)
                exercise_count += 1
    
    # 4. Translation (1 exercise)
    if len(selected_indices) > 4:
        idx = selected_indices[4]
        if idx < len(all_phrases) and idx < len(all_en_phrases):
            en_text = all_en_phrases[idx]
            target_text = all_phrases[idx]
            ex = create_translation_exercise(day, lang, en_text, target_text, exercise_count)
            exercises.append(ex)
            exercise_count += 1
    
    # 5. Matching exercise (if we have enough phrases)
    if len(all_phrases) >= 4 and len(all_en_phrases) >= 4:
        pairs = []
        for i in range(min(4, len(all_phrases))):
            if i < len(all_en_phrases):
                pairs.append({
                    'source': all_phrases[i],
                    'target': all_en_phrases[i]
                })
        if len(pairs) >= 4:
            ex = create_matching_exercise(day, lang, pairs, exercise_count)
            if ex:
                exercises.append(ex)
                exercise_count += 1
    
    # 6. Sentence reconstruction (1 exercise)
    if len(selected_indices) > 5:
        idx = selected_indices[5]
        if idx < len(all_phrases) and idx < len(all_en_phrases):
            phrase = all_phrases[idx]
            translation = all_en_phrases[idx]
            ex = create_sentence_reconstruction_exercise(day, lang, phrase, translation, exercise_count)
            if ex:
                exercises.append(ex)
                exercise_count += 1
    
    return exercises

def format_exercise_as_js(exercise):
    """Format an exercise dictionary as JavaScript object literal"""
    lines = ['    {']
    
    def escape_js_string(s):
        """Escape a string for JavaScript"""
        return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
    
    for key, value in exercise.items():
        if isinstance(value, str):
            value_escaped = escape_js_string(value)
            lines.append(f"      {key}: '{value_escaped}',")
        elif isinstance(value, int):
            lines.append(f"      {key}: {value},")
        elif isinstance(value, list):
            if key == 'pairs':
                lines.append(f"      {key}: [")
                for pair in value:
                    source = escape_js_string(pair['source'])
                    target = escape_js_string(pair['target'])
                    lines.append(f"        {{ source: '{source}', target: '{target}' }},")
                lines.append("      ],")
            elif key == 'words':
                words_str = ', '.join([f"'{escape_js_string(w)}'" for w in value])
                lines.append(f"      {key}: [{words_str}],")
            else:
                items_str = ', '.join([f"'{escape_js_string(item)}'" for item in value])
                lines.append(f"      {key}: [{items_str}],")
    
    lines.append('    }')
    return '\n'.join(lines)

def generate_all_exercises():
    """Generate exercises for all 50 days and 5 languages"""
    output = []
    output.append("/**")
    output.append(" * Exercise Data")
    output.append(" * Generated exercise data for all 50 days and 5 languages")
    output.append(" * Generated by generate_exercises.py")
    output.append(" */")
    output.append("")
    output.append("const EXERCISE_DATA = {")
    
    total_count = 0
    
    for day in range(1, 51):
        for lang in LANGUAGES:
            print(f"Generating exercises for Day {day} - {LANGUAGE_NAMES[lang]}...")
            exercises = generate_exercises_for_day(day, lang)
            
            if exercises:
                output.append(f"  // Day {day} - {LANGUAGE_NAMES[lang]}")
                output.append(f"  'day{day}_{lang}': [")
                
                for i, exercise in enumerate(exercises):
                    ex_js = format_exercise_as_js(exercise)
                    if i < len(exercises) - 1:
                        output.append(ex_js + ',')
                    else:
                        output.append(ex_js)
                
                output.append("  ],")
                output.append("")
                total_count += len(exercises)
    
    output.append("};")
    output.append("")
    output.append("// Function to get exercises for a specific day and language")
    output.append("window.getExercisesForDay = function(day, language) {")
    output.append("  const key = `day${day}_${language}`;")
    output.append("  return EXERCISE_DATA[key] || EXERCISE_DATA['day1_es']; // Fallback to day 1 Spanish")
    output.append("};")
    output.append("")
    output.append("// Function to check if exercises exist for a day")
    output.append("window.hasExercises = function(day, language) {")
    output.append("  const key = `day${day}_${language}`;")
    output.append("  return key in EXERCISE_DATA;")
    output.append("};")
    output.append("")
    output.append("// Export data")
    output.append("if (typeof window !== 'undefined') {")
    output.append("  window.EXERCISE_DATA = EXERCISE_DATA;")
    output.append("}")
    
    print(f"\nTotal exercises generated: {total_count}")
    print(f"Expected: {50 * 5} exercise sets (250)")
    
    return '\n'.join(output)

if __name__ == '__main__':
    print("Generating exercises for all 50 days across 5 languages...")
    print("=" * 60)
    
    js_content = generate_all_exercises()
    
    # Write to exercise-data.js
    output_file = 'js/exercise-data.js'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"\n✓ Exercises written to {output_file}")
    print("Done!")
