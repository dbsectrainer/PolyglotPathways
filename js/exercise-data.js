/**
 * Exercise Data
 * Sample exercise data for different days and languages
 */

const EXERCISE_DATA = {
  // Day 1 - Spanish
  'day1_es': [
    {
      id: 'day1_es_listening',
      type: 'listening',
      language: 'es',
      audio: 'audio_files/day1_es.mp3',
      text: 'Buenos días',
      translation: 'Good morning',
      question: '¿Cómo se dice "Good morning" en español?',
      options: ['Buenas noches', 'Buenos días', 'Buenas tardes', 'Hola'],
      correct: 1
    },
    {
      id: 'day1_es_pronunciation',
      type: 'pronunciation',
      language: 'es',
      text: 'Buenos días',
      phonetic: '[ˈbwe.nos ˈdi.as]',
      targetAccuracy: 85
    },
    {
      id: 'day1_es_fillblank',
      type: 'fill-blank',
      language: 'es',
      sentence: '__ días',
      options: ['Buenos', 'Malos', 'Grandes', 'Pequeños'],
      correct: 'Buenos'
    },
    {
      id: 'day1_es_matching',
      type: 'matching',
      language: 'es',
      pairs: [
        { source: 'Buenos días', target: 'Good morning' },
        { source: 'Buenas tardes', target: 'Good afternoon' },
        { source: 'Buenas noches', target: 'Good evening' },
        { source: 'Hola', target: 'Hello' }
      ]
    }
  ],

  // Day 1 - Portuguese
  'day1_pt': [
    {
      id: 'day1_pt_listening',
      type: 'listening',
      language: 'pt',
      audio: 'audio_files/day1_pt.mp3',
      text: 'Bom dia',
      translation: 'Good morning',
      question: 'Como se diz "Good morning" em português?',
      options: ['Boa noite', 'Bom dia', 'Boa tarde', 'Olá'],
      correct: 1
    },
    {
      id: 'day1_pt_pronunciation',
      type: 'pronunciation',
      language: 'pt',
      text: 'Bom dia',
      phonetic: '[bõ ˈdiɐ]',
      targetAccuracy: 85
    },
    {
      id: 'day1_pt_fillblank',
      type: 'fill-blank',
      language: 'pt',
      sentence: '__ dia',
      options: ['Bom', 'Mau', 'Grande', 'Pequeno'],
      correct: 'Bom'
    }
  ],

  // Day 1 - French
  'day1_fr': [
    {
      id: 'day1_fr_listening',
      type: 'listening',
      language: 'fr',
      audio: 'audio_files/day1_fr.mp3',
      text: 'Bonjour',
      translation: 'Good morning',
      question: 'Comment dit-on "Good morning" en français?',
      options: ['Bonsoir', 'Bonjour', 'Bonne nuit', 'Salut'],
      correct: 1
    },
    {
      id: 'day1_fr_pronunciation',
      type: 'pronunciation',
      language: 'fr',
      text: 'Bonjour',
      phonetic: '[bɔ̃.ʒuʁ]',
      targetAccuracy: 85
    },
    {
      id: 'day1_fr_sentence',
      type: 'sentence-reconstruction',
      language: 'fr',
      words: ['Bonjour', 'comment', 'allez-vous'],
      translation: 'Hello, how are you?',
      correctSentence: 'Bonjour comment allez-vous'
    }
  ],

  // Day 1 - German
  'day1_de': [
    {
      id: 'day1_de_listening',
      type: 'listening',
      language: 'de',
      audio: 'audio_files/day1_de.mp3',
      text: 'Guten Morgen',
      translation: 'Good morning',
      question: 'Wie sagt man "Good morning" auf Deutsch?',
      options: ['Gute Nacht', 'Guten Morgen', 'Guten Tag', 'Hallo'],
      correct: 1
    },
    {
      id: 'day1_de_pronunciation',
      type: 'pronunciation',
      language: 'de',
      text: 'Guten Morgen',
      phonetic: '[ˈɡuːtn̩ ˈmɔʁɡn̩]',
      targetAccuracy: 85
    }
  ],

  // ========== DAY 2 - INTRODUCTIONS ==========

  'day2_es': [
    {
      id: 'day2_es_listening',
      type: 'listening',
      language: 'es',
      audio: 'audio_files/day2_es.mp3',
      text: 'Me llamo María',
      translation: 'My name is María',
      question: '¿Cómo se presenta María?',
      options: ['Soy María', 'Me llamo María', 'Eres María', 'Te llamas María'],
      correct: 1
    },
    {
      id: 'day2_es_pronunciation',
      type: 'pronunciation',
      language: 'es',
      text: '¿Cómo te llamas?',
      phonetic: '[ˈko.mo te ˈʎa.mas]',
      targetAccuracy: 85
    },
    {
      id: 'day2_es_fillblank',
      type: 'fill-blank',
      language: 'es',
      sentence: 'Me __ Carlos',
      options: ['llamo', 'llamas', 'llama', 'llamamos'],
      correct: 'llamo'
    },
    {
      id: 'day2_es_matching',
      type: 'matching',
      language: 'es',
      pairs: [
        { source: '¿Cómo te llamas?', target: 'What is your name?' },
        { source: 'Me llamo...', target: 'My name is...' },
        { source: 'Mucho gusto', target: 'Nice to meet you' },
        { source: '¿Y tú?', target: 'And you?' }
      ]
    }
  ],

  'day2_pt': [
    {
      id: 'day2_pt_listening',
      type: 'listening',
      language: 'pt',
      audio: 'audio_files/day2_pt.mp3',
      text: 'Meu nome é João',
      translation: 'My name is João',
      question: 'Como João se apresenta?',
      options: ['Eu sou João', 'Meu nome é João', 'Você é João', 'Seu nome é João'],
      correct: 1
    },
    {
      id: 'day2_pt_pronunciation',
      type: 'pronunciation',
      language: 'pt',
      text: 'Como você se chama?',
      phonetic: '[ˈko.mu voˈse si ˈʃɐ.mɐ]',
      targetAccuracy: 85
    },
    {
      id: 'day2_pt_fillblank',
      type: 'fill-blank',
      language: 'pt',
      sentence: 'Meu __ é Ana',
      options: ['nome', 'casa', 'amigo', 'dia'],
      correct: 'nome'
    },
    {
      id: 'day2_pt_sentence',
      type: 'sentence-reconstruction',
      language: 'pt',
      words: ['Prazer', 'em', 'conhecê-lo'],
      translation: 'Nice to meet you',
      correctSentence: 'Prazer em conhecê-lo'
    }
  ],

  'day2_fr': [
    {
      id: 'day2_fr_listening',
      type: 'listening',
      language: 'fr',
      audio: 'audio_files/day2_fr.mp3',
      text: 'Je m\'appelle Sophie',
      translation: 'My name is Sophie',
      question: 'Comment Sophie se présente?',
      options: ['Tu t\'appelles Sophie', 'Je m\'appelle Sophie', 'Il s\'appelle Sophie', 'Nous nous appelons Sophie'],
      correct: 1
    },
    {
      id: 'day2_fr_pronunciation',
      type: 'pronunciation',
      language: 'fr',
      text: 'Enchanté',
      phonetic: '[ɑ̃.ʃɑ̃.te]',
      targetAccuracy: 85
    },
    {
      id: 'day2_fr_fillblank',
      type: 'fill-blank',
      language: 'fr',
      sentence: 'Je __ Pierre',
      options: ['m\'appelle', 't\'appelles', 's\'appelle', 'nous appelons'],
      correct: 'm\'appelle'
    },
    {
      id: 'day2_fr_matching',
      type: 'matching',
      language: 'fr',
      pairs: [
        { source: 'Comment tu t\'appelles?', target: 'What\'s your name?' },
        { source: 'Je m\'appelle...', target: 'My name is...' },
        { source: 'Enchanté', target: 'Nice to meet you' },
        { source: 'Et toi?', target: 'And you?' }
      ]
    }
  ],

  'day2_de': [
    {
      id: 'day2_de_listening',
      type: 'listening',
      language: 'de',
      audio: 'audio_files/day2_de.mp3',
      text: 'Ich heiße Hans',
      translation: 'My name is Hans',
      question: 'Wie stellt Hans sich vor?',
      options: ['Du heißt Hans', 'Ich heiße Hans', 'Er heißt Hans', 'Sie heißen Hans'],
      correct: 1
    },
    {
      id: 'day2_de_pronunciation',
      type: 'pronunciation',
      language: 'de',
      text: 'Wie heißen Sie?',
      phonetic: '[viː ˈhaɪsn̩ ziː]',
      targetAccuracy: 85
    },
    {
      id: 'day2_de_fillblank',
      type: 'fill-blank',
      language: 'de',
      sentence: 'Ich __ Anna',
      options: ['heiße', 'heißt', 'heißen', 'bin'],
      correct: 'heiße'
    },
    {
      id: 'day2_de_sentence',
      type: 'sentence-reconstruction',
      language: 'de',
      words: ['Freut', 'mich'],
      translation: 'Nice to meet you',
      correctSentence: 'Freut mich'
    }
  ],

  'day2_en': [
    {
      id: 'day2_en_listening',
      type: 'listening',
      language: 'en',
      audio: 'audio_files/day2_en.mp3',
      text: 'My name is Michael',
      translation: 'Me llamo Michael',
      question: 'How does Michael introduce himself?',
      options: ['Your name is Michael', 'My name is Michael', 'His name is Michael', 'Their name is Michael'],
      correct: 1
    },
    {
      id: 'day2_en_fillblank',
      type: 'fill-blank',
      language: 'en',
      sentence: 'Nice to __ you',
      options: ['meet', 'meat', 'met', 'meeting'],
      correct: 'meet'
    },
    {
      id: 'day2_en_matching',
      type: 'matching',
      language: 'en',
      pairs: [
        { source: 'What\'s your name?', target: 'Question about name' },
        { source: 'My name is...', target: 'Stating your name' },
        { source: 'Nice to meet you', target: 'Polite greeting' },
        { source: 'How are you?', target: 'Question about wellbeing' }
      ]
    }
  ],

  // ========== DAY 3 - NUMBERS 1-10 ==========

  'day3_es': [
    {
      id: 'day3_es_listening',
      type: 'listening',
      language: 'es',
      audio: 'audio_files/day3_es.mp3',
      text: 'uno, dos, tres',
      translation: 'one, two, three',
      question: '¿Qué número viene después de dos?',
      options: ['uno', 'tres', 'cuatro', 'cinco'],
      correct: 1
    },
    {
      id: 'day3_es_pronunciation',
      type: 'pronunciation',
      language: 'es',
      text: 'cinco',
      phonetic: '[ˈsiŋ.ko]',
      targetAccuracy: 85
    },
    {
      id: 'day3_es_fillblank',
      type: 'fill-blank',
      language: 'es',
      sentence: 'uno, dos, __, cuatro',
      options: ['tres', 'cinco', 'seis', 'siete'],
      correct: 'tres'
    },
    {
      id: 'day3_es_matching',
      type: 'matching',
      language: 'es',
      pairs: [
        { source: 'uno', target: 'one' },
        { source: 'cinco', target: 'five' },
        { source: 'siete', target: 'seven' },
        { source: 'diez', target: 'ten' }
      ]
    }
  ],

  'day3_pt': [
    {
      id: 'day3_pt_listening',
      type: 'listening',
      language: 'pt',
      audio: 'audio_files/day3_pt.mp3',
      text: 'um, dois, três',
      translation: 'one, two, three',
      question: 'Qual número vem depois de dois?',
      options: ['um', 'três', 'quatro', 'cinco'],
      correct: 1
    },
    {
      id: 'day3_pt_pronunciation',
      type: 'pronunciation',
      language: 'pt',
      text: 'sete',
      phonetic: '[ˈsɛ.tʃi]',
      targetAccuracy: 85
    },
    {
      id: 'day3_pt_fillblank',
      type: 'fill-blank',
      language: 'pt',
      sentence: 'um, dois, __, quatro',
      options: ['três', 'cinco', 'seis', 'sete'],
      correct: 'três'
    },
    {
      id: 'day3_pt_matching',
      type: 'matching',
      language: 'pt',
      pairs: [
        { source: 'um', target: 'one' },
        { source: 'quatro', target: 'four' },
        { source: 'oito', target: 'eight' },
        { source: 'dez', target: 'ten' }
      ]
    }
  ],

  'day3_fr': [
    {
      id: 'day3_fr_listening',
      type: 'listening',
      language: 'fr',
      audio: 'audio_files/day3_fr.mp3',
      text: 'un, deux, trois',
      translation: 'one, two, three',
      question: 'Quel nombre vient après deux?',
      options: ['un', 'trois', 'quatre', 'cinq'],
      correct: 1
    },
    {
      id: 'day3_fr_pronunciation',
      type: 'pronunciation',
      language: 'fr',
      text: 'six',
      phonetic: '[sis]',
      targetAccuracy: 85
    },
    {
      id: 'day3_fr_fillblank',
      type: 'fill-blank',
      language: 'fr',
      sentence: 'un, deux, __, quatre',
      options: ['trois', 'cinq', 'six', 'sept'],
      correct: 'trois'
    },
    {
      id: 'day3_fr_sentence',
      type: 'sentence-reconstruction',
      language: 'fr',
      words: ['J\'ai', 'cinq', 'pommes'],
      translation: 'I have five apples',
      correctSentence: 'J\'ai cinq pommes'
    }
  ],

  'day3_de': [
    {
      id: 'day3_de_listening',
      type: 'listening',
      language: 'de',
      audio: 'audio_files/day3_de.mp3',
      text: 'eins, zwei, drei',
      translation: 'one, two, three',
      question: 'Welche Zahl kommt nach zwei?',
      options: ['eins', 'drei', 'vier', 'fünf'],
      correct: 1
    },
    {
      id: 'day3_de_pronunciation',
      type: 'pronunciation',
      language: 'de',
      text: 'neun',
      phonetic: '[nɔʏn]',
      targetAccuracy: 85
    },
    {
      id: 'day3_de_fillblank',
      type: 'fill-blank',
      language: 'de',
      sentence: 'eins, zwei, __, vier',
      options: ['drei', 'fünf', 'sechs', 'sieben'],
      correct: 'drei'
    },
    {
      id: 'day3_de_matching',
      type: 'matching',
      language: 'de',
      pairs: [
        { source: 'zwei', target: 'two' },
        { source: 'fünf', target: 'five' },
        { source: 'acht', target: 'eight' },
        { source: 'zehn', target: 'ten' }
      ]
    }
  ],

  'day3_en': [
    {
      id: 'day3_en_listening',
      type: 'listening',
      language: 'en',
      audio: 'audio_files/day3_en.mp3',
      text: 'one, two, three',
      translation: 'uno, dos, tres',
      question: 'What number comes after nine?',
      options: ['eight', 'nine', 'ten', 'eleven'],
      correct: 2
    },
    {
      id: 'day3_en_fillblank',
      type: 'fill-blank',
      language: 'en',
      sentence: 'one, two, __, four',
      options: ['three', 'five', 'six', 'seven'],
      correct: 'three'
    },
    {
      id: 'day3_en_matching',
      type: 'matching',
      language: 'en',
      pairs: [
        { source: 'six', target: '6' },
        { source: 'seven', target: '7' },
        { source: 'eight', target: '8' },
        { source: 'nine', target: '9' }
      ]
    }
  ],

  // Day 15 - Spanish (Business meeting example from roadmap)
  'day15_es': [
    {
      id: 'day15_es_listening',
      type: 'listening',
      language: 'es',
      audio: 'audio_files/day15_es.mp3',
      text: 'La reunión comenzará a las nueve en punto',
      translation: 'The meeting will start at nine o\'clock sharp',
      question: '¿A qué hora comenzará la reunión?',
      options: ['A las ocho', 'A las nueve', 'A las diez', 'A las once'],
      correct: 1
    },
    {
      id: 'day15_es_pronunciation',
      type: 'pronunciation',
      language: 'es',
      text: 'La reunión comenzará a las nueve en punto',
      phonetic: '[la re.uˈnjon ko.men.saˈɾa a las ˈnwe.βe en ˈpun.to]',
      targetAccuracy: 85
    },
    {
      id: 'day15_es_fillblank',
      type: 'fill-blank',
      language: 'es',
      sentence: 'La __ comenzará a las nueve en punto',
      options: ['reunión', 'comida', 'fiesta', 'clase'],
      correct: 'reunión'
    },
    {
      id: 'day15_es_translation',
      type: 'translation',
      language: 'es',
      text: 'The meeting will start at nine o\'clock sharp',
      correctAnswer: 'La reunión comenzará a las nueve en punto'
    }
  ]
};

// Function to get exercises for a specific day and language
window.getExercisesForDay = function(day, language) {
  const key = `day${day}_${language}`;
  return EXERCISE_DATA[key] || EXERCISE_DATA['day1_es']; // Fallback to day 1 Spanish
};

// Function to check if exercises exist for a day
window.hasExercises = function(day, language) {
  const key = `day${day}_${language}`;
  return key in EXERCISE_DATA;
};

// Export data
if (typeof window !== 'undefined') {
  window.EXERCISE_DATA = EXERCISE_DATA;
}
