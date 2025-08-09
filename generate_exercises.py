#!/usr/bin/env python3
"""
Exercise Generator for Polyglot Pathways

This script generates interactive exercise files for all 50 days in all 5 languages.
It creates JSON files following the day1 model with drag-drop, fill-blank, and matching exercises.
"""

import json
import random
import os
import re
from typing import Dict, List, Any

# Language codes
LANGUAGES = ['en', 'es', 'pt', 'fr', 'de']

# Language names for titles
LANGUAGE_NAMES = {
    'en': 'English',
    'es': 'Spanish', 
    'pt': 'Portuguese',
    'fr': 'French',
    'de': 'German'
}

# Sample data for testing - we'll expand this
SAMPLE_PHRASES = {
    1: {
        "Basic Greetings & Common Phrases": [
            {"en": "Hello", "es": "Hola", "pt": "Olá", "fr": "Bonjour", "de": "Hallo"},
            {"en": "Good morning", "es": "Buenos días", "pt": "Bom dia", "fr": "Bonjour", "de": "Guten Morgen"},
            {"en": "How are you?", "es": "¿Cómo estás?", "pt": "Como você está?", "fr": "Comment ça va ?", "de": "Wie geht es dir?"},
            {"en": "Thank you", "es": "Gracias", "pt": "Obrigado", "fr": "Merci", "de": "Danke"},
            {"en": "Please", "es": "Por favor", "pt": "Por favor", "fr": "S'il vous plaît", "de": "Bitte"},
            {"en": "Excuse me", "es": "Disculpe", "pt": "Com licença", "fr": "Excusez-moi", "de": "Entschuldigung"}
        ],
        "Travel Phrases": [
            {"en": "Where is the bathroom?", "es": "¿Dónde está el baño?", "pt": "Onde fica o banheiro?", "fr": "Où sont les toilettes ?", "de": "Wo ist die Toilette?"},
            {"en": "How much does it cost?", "es": "¿Cuánto cuesta?", "pt": "Quanto custa?", "fr": "Combien ça coûte ?", "de": "Wie viel kostet das?"},
            {"en": "I need help", "es": "Necesito ayuda", "pt": "Preciso de ajuda", "fr": "J'ai besoin d'aide", "de": "Ich brauche Hilfe"},
            {"en": "Where is...?", "es": "¿Dónde está...?", "pt": "Onde fica...?", "fr": "Où est... ?", "de": "Wo ist...?"}
        ],
        "Numbers": [
            {"en": "One", "es": "Uno", "pt": "Um", "fr": "Un", "de": "Eins"},
            {"en": "Two", "es": "Dos", "pt": "Dois", "fr": "Deux", "de": "Zwei"},
            {"en": "Three", "es": "Tres", "pt": "Três", "fr": "Trois", "de": "Drei"},
            {"en": "Four", "es": "Cuatro", "pt": "Quatro", "fr": "Quatre", "de": "Vier"},
            {"en": "Five", "es": "Cinco", "pt": "Cinco", "fr": "Cinq", "de": "Fünf"}
        ]
    }
}

def extract_key_word(phrase: str) -> str:
    """Extract a key word from a phrase that could be used as a blank."""
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', phrase.lower())
    # Filter out very short words and common words
    common_words = {'i', 'a', 'an', 'the', 'is', 'am', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'to', 'of', 'in', 'on', 'at', 'by', 'for', 'with', 'from', 'as', 'and', 'or', 'but', 'so', 'if', 'that', 'this', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'el', 'la', 'los', 'las', 'un', 'una', 'de', 'en', 'que', 'es', 'se', 'no', 'te', 'lo', 'le', 'da', 'su', 'por', 'son', 'con', 'para', 'al', 'del', 'me', 'ya', 'si', 'cuando', 'él', 'muy', 'sin', 'sobre', 'hace', 'o', 'donde', 'eu', 'que', 'não', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'ohne', 'bei', 'sie', 'von', 'sie', 'ein', 'auf', 'eine', 'als', 'an', 'nach', 'wie', 'im', 'für', 'man', 'aber', 'aus', 'durch', 'wenn', 'nur', 'war', 'noch', 'werden', 'bei', 'hat', 'wir', 'was', 'ihr', 'ihre', 'dem', 'den', 'des', 'der', 'die', 'das', 'du', 'er', 'es', 'je', 'tu', 'il', 'de', 'et', 'à', 'un', 'le', 'être', 'avoir', 'ne', 'ce', 'son', 'que', 'se', 'qui', 'dans', 'en', 'sur', 'avec', 'ne', 'se', 'pas', 'tout', 'plus', 'par', 'grand', 'le', 'de', 'un', 'à', 'être', 'et', 'en', 'avoir', 'que', 'pour'}
    
    meaningful_words = [w for w in words if len(w) > 2 and w not in common_words]
    
    if meaningful_words:
        # Prefer words from the middle or end of the phrase
        if len(meaningful_words) > 1:
            return meaningful_words[len(meaningful_words) // 2]
        return meaningful_words[0]
    elif words:
        # Fallback to any word if no meaningful words found
        return words[-1]
    return "word"

def create_drag_drop_exercise(phrases: List[Dict[str, str]], lang: str, category: str) -> Dict[str, Any]:
    """Create a drag-and-drop exercise from phrase data."""
    # Select 3-4 phrases for the exercise
    selected_phrases = random.sample(phrases, min(4, len(phrases)))
    
    sentences = []
    word_bank = []
    extra_words = []
    
    for phrase_dict in selected_phrases:
        phrase = phrase_dict[lang]
        key_word = extract_key_word(phrase)
        
        # Create sentence with blank
        sentence_with_blank = phrase.replace(key_word, f"[{key_word}]", 1)
        
        sentences.append({
            "text": sentence_with_blank,
            "blanks": [{
                "placeholder": key_word,
                "correct": key_word
            }]
        })
        
        word_bank.append(key_word)
    
    # Add some distractor words from other phrases in the same category
    other_phrases = [p for p in phrases if p not in selected_phrases]
    if other_phrases:
        for phrase_dict in random.sample(other_phrases, min(3, len(other_phrases))):
            distractor = extract_key_word(phrase_dict[lang])
            if distractor not in word_bank:
                extra_words.append(distractor)
    
    # Language-specific titles and instructions
    titles = {
        'en': f"Complete the {category} Phrases",
        'es': f"Completa las Frases de {category}",
        'pt': f"Complete as Frases de {category}",
        'fr': f"Complétez les Phrases de {category}",
        'de': f"Vervollständigen Sie die {category}-Phrasen"
    }
    
    instructions = {
        'en': "Drag the correct words to complete each phrase.",
        'es': "Arrastra las palabras correctas para completar cada frase.",
        'pt': "Arraste as palavras corretas para completar cada frase.",
        'fr': "Faites glisser les mots corrects pour compléter chaque phrase.",
        'de': "Ziehen Sie die richtigen Wörter, um jede Phrase zu vervollständigen."
    }
    
    return {
        "type": "drag-drop",
        "title": titles.get(lang, titles['en']),
        "instructions": instructions.get(lang, instructions['en']),
        "sentences": sentences,
        "extraWords": extra_words[:3]  # Limit to 3 extra words
    }

def create_fill_blank_exercise(phrases: List[Dict[str, str]], lang: str, category: str) -> Dict[str, Any]:
    """Create a fill-in-the-blank exercise from phrase data."""
    # Select 3-4 phrases for the exercise
    selected_phrases = random.sample(phrases, min(4, len(phrases)))
    
    sentences = []
    word_bank = []
    
    for phrase_dict in selected_phrases:
        phrase = phrase_dict[lang]
        key_word = extract_key_word(phrase)
        
        # Create sentence with blank
        sentence_with_blank = phrase.replace(key_word, f"[{key_word}]", 1)
        
        # Create some alternative correct answers if possible
        correct_answers = [key_word]
        
        sentences.append({
            "text": sentence_with_blank,
            "blanks": [{
                "placeholder": key_word,
                "correct": correct_answers,
                "hint": f"Key word from this phrase"
            }]
        })
        
        word_bank.append(key_word)
    
    # Add a couple more words to the word bank
    other_phrases = [p for p in phrases if p not in selected_phrases]
    for phrase_dict in random.sample(other_phrases, min(2, len(other_phrases))):
        extra_word = extract_key_word(phrase_dict[lang])
        if extra_word not in word_bank:
            word_bank.append(extra_word)
    
    # Language-specific titles and instructions
    titles = {
        'en': f"Fill in {category} Phrases",
        'es': f"Completa las Frases de {category}",
        'pt': f"Preencha as Frases de {category}",
        'fr': f"Remplissez les Phrases de {category}",
        'de': f"Füllen Sie die {category}-Phrasen aus"
    }
    
    instructions = {
        'en': "Complete these phrases by filling in the missing words.",
        'es': "Completa estas frases llenando las palabras que faltan.",
        'pt': "Complete essas frases preenchendo as palavras em falta.",
        'fr': "Complétez ces phrases en remplissant les mots manquants.",
        'de': "Vervollständigen Sie diese Phrasen, indem Sie die fehlenden Wörter einfügen."
    }
    
    return {
        "type": "fill-blank",
        "title": titles.get(lang, titles['en']),
        "instructions": instructions.get(lang, instructions['en']),
        "sentences": sentences,
        "wordBank": word_bank
    }

def create_matching_exercise(phrases: List[Dict[str, str]], lang: str, category: str) -> Dict[str, Any]:
    """Create a matching exercise from phrase data."""
    # For matching, we'll create pairs from the phrases
    # We can match questions with answers, or create related pairs
    
    # Select 4 phrases and create pairs
    selected_phrases = random.sample(phrases, min(4, len(phrases)))
    
    left_items = []
    right_items = []
    correct_pairs = []
    
    # Create pairs from the phrases - split each phrase to create question/answer style
    for i, phrase_dict in enumerate(selected_phrases):
        phrase = phrase_dict[lang]
        
        # Try to create meaningful pairs by splitting phrases
        if '?' in phrase:
            # For questions, use the question as left, create a response as right
            left_text = phrase
            # Create a simple response
            responses = {
                'en': ["Yes", "No", "I don't know", "Maybe"],
                'es': ["Sí", "No", "No sé", "Tal vez"],
                'pt': ["Sim", "Não", "Não sei", "Talvez"],
                'fr': ["Oui", "Non", "Je ne sais pas", "Peut-être"],
                'de': ["Ja", "Nein", "Ich weiß nicht", "Vielleicht"]
            }
            right_text = responses.get(lang, responses['en'])[i % 4]
        else:
            # For statements, create a related phrase or translation concept
            left_text = phrase
            # Use part of the phrase or a related concept
            words = phrase.split()
            if len(words) > 2:
                right_text = ' '.join(words[-2:])  # Last two words
            else:
                right_text = words[-1] if words else phrase
        
        left_id = f"item{i+1}"
        right_id = f"response{i+1}"
        
        left_items.append({
            "id": left_id,
            "text": left_text,
            "type": "text"
        })
        
        right_items.append({
            "id": right_id,
            "text": right_text,
            "type": "text"
        })
        
        correct_pairs.append({
            "leftId": left_id,
            "rightId": right_id
        })
    
    # Language-specific titles and instructions
    titles = {
        'en': f"Match {category} Items",
        'es': f"Relaciona Elementos de {category}",
        'pt': f"Combine Itens de {category}",
        'fr': f"Associez les Éléments de {category}",
        'de': f"Ordnen Sie {category}-Elemente zu"
    }
    
    instructions = {
        'en': "Match each item with its appropriate pair.",
        'es': "Relaciona cada elemento con su pareja apropiada.",
        'pt': "Combine cada item com seu par apropriado.",
        'fr': "Associez chaque élément à sa paire appropriée.",
        'de': "Ordnen Sie jeden Gegenstand seinem entsprechenden Paar zu."
    }
    
    left_titles = {
        'en': "Phrases",
        'es': "Frases",
        'pt': "Frases", 
        'fr': "Phrases",
        'de': "Phrasen"
    }
    
    right_titles = {
        'en': "Responses",
        'es': "Respuestas",
        'pt': "Respostas",
        'fr': "Réponses", 
        'de': "Antworten"
    }
    
    return {
        "type": "matching",
        "title": titles.get(lang, titles['en']),
        "instructions": instructions.get(lang, instructions['en']),
        "leftTitle": left_titles.get(lang, left_titles['en']),
        "rightTitle": right_titles.get(lang, right_titles['en']),
        "leftItems": left_items,
        "rightItems": right_items,
        "correctPairs": correct_pairs
    }

def generate_exercises_for_day(day: int, lang: str) -> Dict[str, Any]:
    """Generate all exercises for a specific day and language."""
    if day not in SAMPLE_PHRASES:
        print(f"Warning: No data found for day {day}")
        return {"exercises": []}
    
    day_phrases = SAMPLE_PHRASES[day]
    exercises = []
    
    # Get the categories and phrases for this day
    categories = list(day_phrases.keys())
    
    # Try to create 3 exercises using different categories
    if len(categories) >= 3:
        # Use 3 different categories for variety
        selected_categories = random.sample(categories, 3)
        exercise_types = ['drag-drop', 'fill-blank', 'matching']
        
        for i, (category, ex_type) in enumerate(zip(selected_categories, exercise_types)):
            phrases = day_phrases[category]
            if len(phrases) >= 3:  # Need at least 3 phrases for a good exercise
                if ex_type == 'drag-drop':
                    exercise = create_drag_drop_exercise(phrases, lang, category)
                elif ex_type == 'fill-blank':
                    exercise = create_fill_blank_exercise(phrases, lang, category)
                else:  # matching
                    exercise = create_matching_exercise(phrases, lang, category)
                
                exercises.append(exercise)
    else:
        # Use available categories, repeat if necessary
        available_categories = [(cat, day_phrases[cat]) for cat in categories if len(day_phrases[cat]) >= 3]
        
        if available_categories:
            # Create at least one exercise from the first available category
            category, phrases = available_categories[0]
            exercises.append(create_drag_drop_exercise(phrases, lang, category))
            
            # Add more exercises if possible
            if len(available_categories) >= 2:
                category, phrases = available_categories[1]
                exercises.append(create_fill_blank_exercise(phrases, lang, category))
            
            if len(available_categories) >= 3:
                category, phrases = available_categories[2]
                exercises.append(create_matching_exercise(phrases, lang, category))
    
    return {"exercises": exercises}

def extend_sample_data_for_days():
    """Extend SAMPLE_PHRASES to cover more days with variations."""
    # For now, create exercises for days 2-50 by creating variations of day 1 data
    for day in range(2, 51):
        # Create themed variations for each day
        SAMPLE_PHRASES[day] = {}
        
        # Day 2-10: Basic conversational themes
        if day <= 10:
            SAMPLE_PHRASES[day]["Daily Conversations"] = [
                {"en": f"Good day {day}!", "es": f"¡Buen día {day}!", "pt": f"Bom dia {day}!", "fr": f"Bonne journée {day}!", "de": f"Guten Tag {day}!"},
                {"en": "How is everything?", "es": "¿Cómo está todo?", "pt": "Como está tudo?", "fr": "Comment va tout ?", "de": "Wie läuft alles?"},
                {"en": "Very well", "es": "Muy bien", "pt": "Muito bem", "fr": "Très bien", "de": "Sehr gut"},
                {"en": "See you later", "es": "Hasta luego", "pt": "Até mais", "fr": "À plus tard", "de": "Bis später"},
                {"en": "Have a nice day", "es": "Que tengas un buen día", "pt": "Tenha um bom dia", "fr": "Bonne journée", "de": "Einen schönen Tag noch"}
            ]
            
            SAMPLE_PHRASES[day]["Learning Progress"] = [
                {"en": f"This is lesson {day}", "es": f"Esta es la lección {day}", "pt": f"Esta é a lição {day}", "fr": f"C'est la leçon {day}", "de": f"Das ist Lektion {day}"},
                {"en": "I am learning", "es": "Estoy aprendiendo", "pt": "Estou aprendendo", "fr": "J'apprends", "de": "Ich lerne"},
                {"en": "This is useful", "es": "Esto es útil", "pt": "Isso é útil", "fr": "C'est utile", "de": "Das ist nützlich"},
                {"en": "I understand", "es": "Entiendo", "pt": "Eu entendo", "fr": "Je comprends", "de": "Ich verstehe"}
            ]
        
        # Day 11-20: Travel and directions
        elif day <= 20:
            SAMPLE_PHRASES[day]["Travel & Directions"] = [
                {"en": "Turn left", "es": "Gira a la izquierda", "pt": "Vire à esquerda", "fr": "Tournez à gauche", "de": "Links abbiegen"},
                {"en": "Turn right", "es": "Gira a la derecha", "pt": "Vire à direita", "fr": "Tournez à droite", "de": "Rechts abbiegen"},
                {"en": "Go straight", "es": "Ve derecho", "pt": "Vá em frente", "fr": "Allez tout droit", "de": "Geradeaus gehen"},
                {"en": "It's near", "es": "Está cerca", "pt": "Está perto", "fr": "C'est près", "de": "Es ist nah"},
                {"en": "It's far", "es": "Está lejos", "pt": "Está longe", "fr": "C'est loin", "de": "Es ist weit"}
            ]
            
            SAMPLE_PHRASES[day]["Transportation"] = [
                {"en": "Bus", "es": "Autobús", "pt": "Ônibus", "fr": "Bus", "de": "Bus"},
                {"en": "Train", "es": "Tren", "pt": "Trem", "fr": "Train", "de": "Zug"},
                {"en": "Taxi", "es": "Taxi", "pt": "Táxi", "fr": "Taxi", "de": "Taxi"},
                {"en": "Airport", "es": "Aeropuerto", "pt": "Aeroporto", "fr": "Aéroport", "de": "Flughafen"}
            ]
        
        # Day 21-30: Food and dining
        elif day <= 30:
            SAMPLE_PHRASES[day]["Food & Dining"] = [
                {"en": "I am hungry", "es": "Tengo hambre", "pt": "Estou com fome", "fr": "J'ai faim", "de": "Ich habe Hunger"},
                {"en": "I am thirsty", "es": "Tengo sed", "pt": "Estou com sede", "fr": "J'ai soif", "de": "Ich habe Durst"},
                {"en": "The menu, please", "es": "El menú, por favor", "pt": "O cardápio, por favor", "fr": "Le menu, s'il vous plaît", "de": "Die Speisekarte, bitte"},
                {"en": "This is delicious", "es": "Esto está delicioso", "pt": "Isso está delicioso", "fr": "C'est délicieux", "de": "Das ist köstlich"},
                {"en": "The check, please", "es": "La cuenta, por favor", "pt": "A conta, por favor", "fr": "L'addition, s'il vous plaît", "de": "Die Rechnung, bitte"}
            ]
            
            SAMPLE_PHRASES[day]["Restaurants"] = [
                {"en": "Table for two", "es": "Mesa para dos", "pt": "Mesa para dois", "fr": "Table pour deux", "de": "Tisch für zwei"},
                {"en": "I would like", "es": "Me gustaría", "pt": "Eu gostaria", "fr": "Je voudrais", "de": "Ich hätte gerne"},
                {"en": "Water", "es": "Agua", "pt": "Água", "fr": "Eau", "de": "Wasser"},
                {"en": "Coffee", "es": "Café", "pt": "Café", "fr": "Café", "de": "Kaffee"}
            ]
        
        # Day 31-40: Shopping and money
        elif day <= 40:
            SAMPLE_PHRASES[day]["Shopping"] = [
                {"en": "How much is this?", "es": "¿Cuánto cuesta esto?", "pt": "Quanto custa isso?", "fr": "Combien ça coûte ?", "de": "Wie viel kostet das?"},
                {"en": "It's expensive", "es": "Es caro", "pt": "É caro", "fr": "C'est cher", "de": "Es ist teuer"},
                {"en": "It's cheap", "es": "Es barato", "pt": "É barato", "fr": "C'est bon marché", "de": "Es ist billig"},
                {"en": "I'll take it", "es": "Me lo llevo", "pt": "Eu vou levar", "fr": "Je le prends", "de": "Ich nehme es"},
                {"en": "Can I pay with card?", "es": "¿Puedo pagar con tarjeta?", "pt": "Posso pagar com cartão?", "fr": "Puis-je payer par carte ?", "de": "Kann ich mit Karte zahlen?"}
            ]
            
            SAMPLE_PHRASES[day]["Money"] = [
                {"en": "Cash", "es": "Efectivo", "pt": "Dinheiro", "fr": "Espèces", "de": "Bargeld"},
                {"en": "Credit card", "es": "Tarjeta de crédito", "pt": "Cartão de crédito", "fr": "Carte de crédit", "de": "Kreditkarte"},
                {"en": "Receipt", "es": "Recibo", "pt": "Recibo", "fr": "Reçu", "de": "Quittung"},
                {"en": "Change", "es": "Cambio", "pt": "Troco", "fr": "Monnaie", "de": "Wechselgeld"}
            ]
        
        # Day 41-50: Advanced topics
        else:
            SAMPLE_PHRASES[day]["Weather & Time"] = [
                {"en": "What time is it?", "es": "¿Qué hora es?", "pt": "Que horas são?", "fr": "Quelle heure est-il ?", "de": "Wie spät ist es?"},
                {"en": "It's sunny", "es": "Está soleado", "pt": "Está ensolarado", "fr": "Il fait beau", "de": "Es ist sonnig"},
                {"en": "It's raining", "es": "Está lloviendo", "pt": "Está chovendo", "fr": "Il pleut", "de": "Es regnet"},
                {"en": "Yesterday", "es": "Ayer", "pt": "Ontem", "fr": "Hier", "de": "Gestern"},
                {"en": "Tomorrow", "es": "Mañana", "pt": "Amanhã", "fr": "Demain", "de": "Morgen"}
            ]
            
            SAMPLE_PHRASES[day]["Feelings & Opinions"] = [
                {"en": "I like it", "es": "Me gusta", "pt": "Eu gosto", "fr": "J'aime ça", "de": "Das gefällt mir"},
                {"en": "I don't like it", "es": "No me gusta", "pt": "Eu não gosto", "fr": "Je n'aime pas ça", "de": "Das gefällt mir nicht"},
                {"en": "I'm happy", "es": "Estoy feliz", "pt": "Estou feliz", "fr": "Je suis heureux", "de": "Ich bin glücklich"},
                {"en": "I'm tired", "es": "Estoy cansado", "pt": "Estou cansado", "fr": "Je suis fatigué", "de": "Ich bin müde"}
            ]

def main():
    """Generate exercise files for all days and languages."""
    # Create exercises directory if it doesn't exist
    exercises_dir = "exercises"
    os.makedirs(exercises_dir, exist_ok=True)
    
    # Extend our sample data to cover all 50 days
    extend_sample_data_for_days()
    
    print("Generating exercise files for all 50 days in 5 languages...")
    
    total_files = 0
    for day in range(1, 51):
        for lang in LANGUAGES:
            try:
                exercise_data = generate_exercises_for_day(day, lang)
                
                if exercise_data["exercises"]:  # Only create file if exercises exist
                    filename = f"day{day}_{lang}.json"
                    filepath = os.path.join(exercises_dir, filename)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(exercise_data, f, indent=2, ensure_ascii=False)
                    
                    total_files += 1
                    print(f"✓ Created {filename} with {len(exercise_data['exercises'])} exercises")
                else:
                    print(f"⚠ Skipped day{day}_{lang}.json - no suitable phrase data")
                    
            except Exception as e:
                print(f"✗ Error creating day{day}_{lang}.json: {e}")
    
    print(f"\nCompleted! Generated {total_files} exercise files.")
    print(f"Files are located in the '{exercises_dir}/' directory.")

if __name__ == "__main__":
    main()