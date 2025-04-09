import argparse
import os
import time
from gtts import gTTS

# This file contains days 45-50 of advanced language phrases
# Following the same structure as previous files but with enhanced content
# focusing on Regional Variations & Dialects and Abstract & Philosophical Discourse

# Day 45: Regional Variations & Dialects - Country-Specific Expressions
day45_phrases = {
    "Spanish Regional Variations": [
        {"en": "Cool/Awesome (Spain)", "es": "Guay/Mola", "pt": "Legal/Fixe", 
         "fr": "Cool/Super", "de": "Cool/Toll"},
        {"en": "Cool/Awesome (Argentina)", "es": "Copado/Bárbaro", "pt": "Legal/Bacana",
         "fr": "Cool/Génial", "de": "Cool/Klasse"},
        {"en": "Cool/Awesome (Mexico)", "es": "Padre/Chido", "pt": "Legal/Massa",
         "fr": "Cool/Chouette", "de": "Cool/Spitze"},
        {"en": "Money (Spain)", "es": "Pasta/Pelas", "pt": "Dinheiro/Guita",
         "fr": "Argent/Fric", "de": "Geld/Kohle"},
        {"en": "Money (Argentina)", "es": "Guita/Plata", "pt": "Dinheiro/Grana",
         "fr": "Argent/Pognon", "de": "Geld/Knete"},
        {"en": "Money (Mexico)", "es": "Lana/Varo", "pt": "Dinheiro/Bufunfa",
         "fr": "Argent/Thune", "de": "Geld/Mäuse"},
        {"en": "Friend (Spain)", "es": "Tío/Colega", "pt": "Amigo/Mano",
         "fr": "Ami/Pote", "de": "Freund/Kumpel"},
        {"en": "Friend (Argentina)", "es": "Pibe/Chabón", "pt": "Amigo/Parceiro",
         "fr": "Ami/Copain", "de": "Freund/Alter"},
        {"en": "Friend (Mexico)", "es": "Cuate/Compa", "pt": "Amigo/Brother",
         "fr": "Ami/Mec", "de": "Freund/Digger"},
        {"en": "Work (Regional)", "es": "Curro/Laburo/Chamba", "pt": "Trampo/Serviço",
         "fr": "Boulot/Taf", "de": "Arbeit/Job"}
    ],
    "Portuguese Regional Variations": [
        {"en": "Cool/Awesome (Brazil)", "es": "Genial/Increíble", "pt": "Legal/Massa",
         "fr": "Cool/Super", "de": "Cool/Toll"},
        {"en": "Cool/Awesome (Portugal)", "es": "Guay/Estupendo", "pt": "Fixe/Porreiro",
         "fr": "Cool/Génial", "de": "Cool/Klasse"},
        {"en": "Money (Brazil)", "es": "Dinero/Plata", "pt": "Grana/Bufunfa",
         "fr": "Argent/Fric", "de": "Geld/Kohle"},
        {"en": "Money (Portugal)", "es": "Dinero/Pasta", "pt": "Guito/Massa",
         "fr": "Argent/Pognon", "de": "Geld/Knete"},
        {"en": "Friend (Brazil)", "es": "Amigo/Compañero", "pt": "Mano/Parceiro",
         "fr": "Ami/Pote", "de": "Freund/Kumpel"},
        {"en": "Friend (Portugal)", "es": "Amigo/Colega", "pt": "Meu/Puto",
         "fr": "Ami/Copain", "de": "Freund/Alter"},
        {"en": "Work (Brazil)", "es": "Trabajo/Laburo", "pt": "Trampo/Serviço",
         "fr": "Boulot/Taf", "de": "Arbeit/Job"},
        {"en": "Work (Portugal)", "es": "Trabajo/Curro", "pt": "Trabalho/Biscate",
         "fr": "Travail/Boulot", "de": "Arbeit/Maloche"},
        {"en": "House (Regional)", "es": "Casa/Hogar", "pt": "Casa/Barraco/Moradia",
         "fr": "Maison/Baraque", "de": "Haus/Bude"},
        {"en": "Food (Regional)", "es": "Comida/Alimento", "pt": "Rango/Bóia/Paparoca",
         "fr": "Bouffe/Graille", "de": "Essen/Futter"}
    ],
    "Regional Greetings": [
        {"en": "Hi/Hello (Spain)", "es": "Hola/¿Qué tal?", "pt": "Olá/Oi",
         "fr": "Salut/Bonjour", "de": "Hallo/Servus"},
        {"en": "Hi/Hello (Argentina)", "es": "Che/¿Qué hacés?", "pt": "Oi/E aí",
         "fr": "Salut/Coucou", "de": "Hi/Moin"},
        {"en": "Hi/Hello (Mexico)", "es": "¿Qué onda?/¿Qué pedo?", "pt": "Oi/Beleza",
         "fr": "Salut/Hey", "de": "Hallo/Na"},
        {"en": "Goodbye (Spain)", "es": "Adiós/Hasta luego", "pt": "Tchau/Até logo",
         "fr": "Au revoir/À plus", "de": "Tschüss/Servus"},
        {"en": "Goodbye (Argentina)", "es": "Chau/Nos vemos", "pt": "Tchau/Falou",
         "fr": "Salut/À plus", "de": "Tschüss/Mach's gut"},
        {"en": "Goodbye (Mexico)", "es": "Adiós/Nos vemos", "pt": "Tchau/Valeu",
         "fr": "Ciao/À plus", "de": "Tschüss/Bis dann"},
        {"en": "Good morning (Regional)", "es": "Buenos días/Buen día", "pt": "Bom dia/Dia",
         "fr": "Bonjour/Salut", "de": "Guten Morgen/Moin"},
        {"en": "Good night (Regional)", "es": "Buenas noches/Que descanses", "pt": "Boa noite/Noite",
         "fr": "Bonne nuit/Bonsoir", "de": "Gute Nacht/Nacht"},
        {"en": "See you later (Regional)", "es": "Hasta luego/Nos vemos", "pt": "Até logo/Falou",
         "fr": "À plus tard/À tout", "de": "Bis später/Bis dann"},
        {"en": "Take care (Regional)", "es": "Cuídate/Que estés bien", "pt": "Se cuida/Fica bem",
         "fr": "Prends soin de toi/Fais gaffe", "de": "Pass auf dich auf/Mach's gut"}
    ]
}

# Day 46: Regional Accents and Pronunciation Differences
day46_phrases = {
    "Regional Pronunciation Patterns": [
        {"en": "Seseo vs Ceceo (Spain)", "es": "Zapato/Sapato", "pt": "Sapato",
         "fr": "Chaussure", "de": "Schuh"},
        {"en": "Yeísmo (Argentina)", "es": "Yo/Lluvia", "pt": "Eu/Chuva",
         "fr": "Je/Pluie", "de": "Ich/Regen"},
        {"en": "S-aspiration (Caribbean)", "es": "Está/E'tá", "pt": "Está",
         "fr": "Est", "de": "Ist"},
        {"en": "Brazilian vs European Portuguese", "es": "Diferencias de acento", "pt": "Diferenças de sotaque",
         "fr": "Différences d'accent", "de": "Akzentunterschiede"},
        {"en": "Rioplatense accent", "es": "Acento rioplatense", "pt": "Sotaque do Rio da Prata",
         "fr": "Accent rioplatense", "de": "Rioplatense-Akzent"},
        {"en": "Mexican accent", "es": "Acento mexicano", "pt": "Sotaque mexicano",
         "fr": "Accent mexicain", "de": "Mexikanischer Akzent"},
        {"en": "Andean accent", "es": "Acento andino", "pt": "Sotaque andino",
         "fr": "Accent andin", "de": "Anden-Akzent"},
        {"en": "Caribbean accent", "es": "Acento caribeño", "pt": "Sotaque caribenho",
         "fr": "Accent caribéen", "de": "Karibischer Akzent"},
        {"en": "Carioca accent", "es": "Acento carioca", "pt": "Sotaque carioca",
         "fr": "Accent carioca", "de": "Carioca-Akzent"},
        {"en": "Paulista accent", "es": "Acento paulista", "pt": "Sotaque paulista",
         "fr": "Accent paulista", "de": "Paulista-Akzent"}
    ],
    "Regional Sound Changes": [
        {"en": "S-dropping (Caribbean)", "es": "Escuela/E'cuela", "pt": "Escola",
         "fr": "École", "de": "Schule"},
        {"en": "R-variations (Brazil)", "es": "Variaciones de R", "pt": "Variações do R",
         "fr": "Variations du R", "de": "R-Variationen"},
        {"en": "T/D palatalization (Brazil)", "es": "Palatización de T/D", "pt": "Palatalização de T/D",
         "fr": "Palatalisation de T/D", "de": "T/D-Palatalisierung"},
        {"en": "Ch/Ll distinction (Spain)", "es": "Distinción ch/ll", "pt": "Distinção ch/lh",
         "fr": "Distinction ch/ll", "de": "Ch/Ll-Unterscheidung"},
        {"en": "Voseo pronunciation", "es": "Pronunciación del voseo", "pt": "Pronúncia do voseo",
         "fr": "Prononciation du voseo", "de": "Voseo-Aussprache"},
        {"en": "Open vs closed vowels", "es": "Vocales abiertas vs cerradas", "pt": "Vogais abertas vs fechadas",
         "fr": "Voyelles ouvertes vs fermées", "de": "Offene vs geschlossene Vokale"},
        {"en": "Nasal sounds", "es": "Sonidos nasales", "pt": "Sons nasais",
         "fr": "Sons nasaux", "de": "Nasallaute"},
        {"en": "Stress patterns", "es": "Patrones de acentuación", "pt": "Padrões de acentuação",
         "fr": "Schémas d'accentuation", "de": "Betonungsmuster"},
        {"en": "Intonation patterns", "es": "Patrones de entonación", "pt": "Padrões de entonação",
         "fr": "Schémas d'intonation", "de": "Intonationsmuster"},
        {"en": "Regional rhythm", "es": "Ritmo regional", "pt": "Ritmo regional",
         "fr": "Rythme régional", "de": "Regionaler Rhythmus"}
    ],
    "Pronunciation Exercises": [
        {"en": "Minimal pairs practice", "es": "Práctica de pares mínimos", "pt": "Prática de pares mínimos",
         "fr": "Pratique des paires minimales", "de": "Minimalpaar-Übungen"},
        {"en": "Stress pattern drills", "es": "Ejercicios de acentuación", "pt": "Exercícios de acentuação",
         "fr": "Exercices d'accentuation", "de": "Betonungsübungen"},
        {"en": "Intonation exercises", "es": "Ejercicios de entonación", "pt": "Exercícios de entonação",
         "fr": "Exercices d'intonation", "de": "Intonationsübungen"},
        {"en": "Tongue twisters", "es": "Trabalenguas", "pt": "Trava-línguas",
         "fr": "Virelangues", "de": "Zungenbrecher"},
        {"en": "Rhythm practice", "es": "Práctica de ritmo", "pt": "Prática de ritmo",
         "fr": "Pratique du rythme", "de": "Rhythmusübungen"},
        {"en": "Sound discrimination", "es": "Discriminación de sonidos", "pt": "Discriminação de sons",
         "fr": "Discrimination des sons", "de": "Lautunterscheidung"},
        {"en": "Connected speech", "es": "Habla conectada", "pt": "Fala conectada",
         "fr": "Parole connectée", "de": "Verbundene Sprache"},
        {"en": "Accent reduction", "es": "Reducción de acento", "pt": "Redução de sotaque",
         "fr": "Réduction d'accent", "de": "Akzentreduzierung"},
        {"en": "Pronunciation feedback", "es": "Retroalimentación de pronunciación", "pt": "Feedback de pronúncia",
         "fr": "Retour sur la prononciation", "de": "Aussprache-Feedback"},
        {"en": "Self-recording exercises", "es": "Ejercicios de autograbación", "pt": "Exercícios de autogravação",
         "fr": "Exercices d'auto-enregistrement", "de": "Selbstaufnahme-Übungen"}
    ]
}

# Day 47: Historical Evolution of Language in Different Regions
day47_phrases = {
    "Historical Language Changes": [
        {"en": "Latin influence", "es": "Influencia del latín", "pt": "Influência do latim",
         "fr": "Influence du latin", "de": "Lateinischer Einfluss"},
        {"en": "Arabic influence", "es": "Influencia árabe", "pt": "Influência árabe",
         "fr": "Influence arabe", "de": "Arabischer Einfluss"},
        {"en": "Indigenous influences", "es": "Influencias indígenas", "pt": "Influências indígenas",
         "fr": "Influences indigènes", "de": "Indigene Einflüsse"},
        {"en": "African influences", "es": "Influencias africanas", "pt": "Influências africanas",
         "fr": "Influences africaines", "de": "Afrikanische Einflüsse"},
        {"en": "Colonial period changes", "es": "Cambios del período colonial", "pt": "Mudanças do período colonial",
         "fr": "Changements de la période coloniale", "de": "Kolonialzeitliche Veränderungen"},
        {"en": "Modern adaptations", "es": "Adaptaciones modernas", "pt": "Adaptações modernas",
         "fr": "Adaptations modernes", "de": "Moderne Anpassungen"},
        {"en": "Vocabulary evolution", "es": "Evolución del vocabulario", "pt": "Evolução do vocabulário",
         "fr": "Évolution du vocabulaire", "de": "Wortschatzentwicklung"},
        {"en": "Grammar changes", "es": "Cambios gramaticales", "pt": "Mudanças gramaticais",
         "fr": "Changements grammaticaux", "de": "Grammatikalische Veränderungen"},
        {"en": "Pronunciation shifts", "es": "Cambios de pronunciación", "pt": "Mudanças de pronúncia",
         "fr": "Changements de prononciation", "de": "Ausspracheverschiebungen"},
        {"en": "Writing system evolution", "es": "Evolución del sistema de escritura", "pt": "Evolução do sistema de escrita",
         "fr": "Évolution du système d'écriture", "de": "Entwicklung des Schriftsystems"}
    ],
    "Cultural Language Evolution": [
        {"en": "Traditional expressions", "es": "Expresiones tradicionales", "pt": "Expressões tradicionais",
         "fr": "Expressions traditionnelles", "de": "Traditionelle Ausdrücke"},
        {"en": "Modern slang", "es": "Jerga moderna", "pt": "Gíria moderna",
         "fr": "Argot moderne", "de": "Moderner Slang"},
        {"en": "Social media influence", "es": "Influencia de las redes sociales", "pt": "Influência das redes sociais",
         "fr": "Influence des réseaux sociaux", "de": "Einfluss sozialer Medien"},
        {"en": "Generational differences", "es": "Diferencias generacionales", "pt": "Diferenças geracionais",
         "fr": "Différences générationnelles", "de": "Generationsunterschiede"},
        {"en": "Urban vs rural speech", "es": "Habla urbana vs rural", "pt": "Fala urbana vs rural",
         "fr": "Parler urbain vs rural", "de": "Städtische vs ländliche Sprache"},
        {"en": "Professional jargon", "es": "Jerga profesional", "pt": "Jargão profissional",
         "fr": "Jargon professionnel", "de": "Fachsprache"},
        {"en": "Youth language", "es": "Lenguaje juvenil", "pt": "Linguagem juvenil",
         "fr": "Langage des jeunes", "de": "Jugendsprache"},
        {"en": "Academic language", "es": "Lenguaje académico", "pt": "Linguagem acadêmica",
         "fr": "Langage académique", "de": "Akademische Sprache"},
        {"en": "Media influence", "es": "Influencia de los medios", "pt": "Influência da mídia",
         "fr": "Influence des médias", "de": "Medieneinfluss"},
        {"en": "Technology impact", "es": "Impacto de la tecnología", "pt": "Impacto da tecnologia",
         "fr": "Impact de la technologie", "de": "Technologieeinfluss"}
    ],
    "Language Preservation": [
        {"en": "Traditional dialects", "es": "Dialectos tradicionales", "pt": "Dialetos tradicionais",
         "fr": "Dialectes traditionnels", "de": "Traditionelle Dialekte"},
        {"en": "Endangered varieties", "es": "Variedades en peligro", "pt": "Variedades em perigo",
         "fr": "Variétés en danger", "de": "Gefährdete Varietäten"},
        {"en": "Language documentation", "es": "Documentación lingüística", "pt": "Documentação linguística",
         "fr": "Documentation linguistique", "de": "Sprachdokumentation"},
        {"en": "Cultural heritage", "es": "Patrimonio cultural", "pt": "Património cultural",
         "fr": "Patrimoine culturel", "de": "Kulturerbe"},
        {"en": "Language revival", "es": "Revitalización lingüística", "pt": "Revitalização linguística",
         "fr": "Revitalisation linguistique", "de": "Sprachrevitalisierung"},
        {"en": "Community efforts", "es": "Esfuerzos comunitarios", "pt": "Esforços comunitários",
         "fr": "Efforts communautaires", "de": "Gemeinschaftliche Bemühungen"},
        {"en": "Educational programs", "es": "Programas educativos", "pt": "Programas educacionais",
         "fr": "Programmes éducatifs", "de": "Bildungsprogramme"},
        {"en": "Language policies", "es": "Políticas lingüísticas", "pt": "Políticas linguísticas",
         "fr": "Politiques linguistiques", "de": "Sprachpolitik"},
        {"en": "Cultural transmission", "es": "Transmisión cultural", "pt": "Transmissão cultural",
         "fr": "Transmission culturelle", "de": "Kulturelle Übermittlung"},
        {"en": "Intergenerational learning", "es": "Aprendizaje intergeneracional", "pt": "Aprendizagem intergeracional",
         "fr": "Apprentissage intergénérationnel", "de": "Generationsübergreifendes Lernen"}
    ]
}

# Day 48: Philosophical Concepts and Terminology
day48_phrases = {
    "Philosophical Concepts": [
        {"en": "Existentialism", "es": "Existencialismo", "pt": "Existencialismo",
         "fr": "Existentialisme", "de": "Existenzialismus"},
        {"en": "Free will", "es": "Libre albedrío", "pt": "Livre arbítrio",
         "fr": "Libre arbitre", "de": "Freier Wille"},
        {"en": "Consciousness", "es": "Consciencia", "pt": "Consciência",
         "fr": "Conscience", "de": "Bewusstsein"},
        {"en": "Reality perception", "es": "Percepción de la realidad", "pt": "Percepção da realidade",
         "fr": "Perception de la réalité", "de": "Realitätswahrnehmung"},
        {"en": "Truth and knowledge", "es": "Verdad y conocimiento", "pt": "Verdade e conhecimento",
         "fr": "Vérité et connaissance", "de": "Wahrheit und Wissen"},
        {"en": "Moral relativism", "es": "Relativismo moral", "pt": "Relativismo moral",
         "fr": "Relativisme moral", "de": "Moralischer Relativismus"},
        {"en": "Determinism", "es": "Determinismo", "pt": "Determinismo",
         "fr": "Déterminisme", "de": "Determinismus"},
        {"en": "Metaphysics", "es": "Metafísica", "pt": "Metafísica",
         "fr": "Métaphysique", "de": "Metaphysik"},
        {"en": "Epistemology", "es": "Epistemología", "pt": "Epistemologia",
         "fr": "Épistémologie", "de": "Erkenntnistheorie"},
        {"en": "Ethics", "es": "Ética", "pt": "Ética",
         "fr": "Éthique", "de": "Ethik"}
    ],
    "Abstract Reasoning": [
        {"en": "Logical deduction", "es": "Deducción lógica", "pt": "Dedução lógica",
         "fr": "Déduction logique", "de": "Logische Deduktion"},
        {"en": "Critical thinking", "es": "Pensamiento crítico", "pt": "Pensamento crítico",
         "fr": "Pensée critique", "de": "Kritisches Denken"},
        {"en": "Conceptual analysis", "es": "Análisis conceptual", "pt": "Análise conceitual",
         "fr": "Analyse conceptuelle", "de": "Konzeptuelle Analyse"},
        {"en": "Abstract thought", "es": "Pensamiento abstracto", "pt": "Pensamento abstrato",
         "fr": "Pensée abstraite", "de": "Abstraktes Denken"},
        {"en": "Theoretical framework", "es": "Marco teórico", "pt": "Marco teórico",
         "fr": "Cadre théorique", "de": "Theoretischer Rahmen"},
        {"en": "Cognitive processes", "es": "Procesos cognitivos", "pt": "Processos cognitivos",
         "fr": "Processus cognitifs", "de": "Kognitive Prozesse"},
        {"en": "Mental models", "es": "Modelos mentales", "pt": "Modelos mentais",
         "fr": "Modèles mentaux", "de": "Mentale Modelle"},
        {"en": "Paradigm shift", "es": "Cambio de paradigma", "pt": "Mudança de paradigma",
         "fr": "Changement de paradigme", "de": "Paradigmenwechsel"},
        {"en": "Systematic thinking", "es": "Pensamiento sistemático", "pt": "Pensamento sistemático",
         "fr": "Pensée systématique", "de": "Systematisches Denken"},
        {"en": "Analytical reasoning", "es": "Razonamiento analítico", "pt": "Raciocínio analítico",
         "fr": "Raisonnement analytique", "de": "Analytisches Denken"}
    ],
    "Philosophical Discourse": [
        {"en": "Let's examine the premise", "es": "Examinemos la premisa", "pt": "Vamos examinar a premissa",
         "fr": "Examinons la prémisse", "de": "Lassen Sie uns die Prämisse untersuchen"},
        {"en": "This raises the question", "es": "Esto plantea la pregunta", "pt": "Isso levanta a questão",
         "fr": "Cela soulève la question", "de": "Dies wirft die Frage auf"},
        {"en": "Consider the implications", "es": "Consideremos las implicaciones", "pt": "Considere as implicações",
         "fr": "Considérons les implications", "de": "Betrachten wir die Implikationen"},
        {"en": "From a theoretical perspective", "es": "Desde una perspectiva teórica", "pt": "De uma perspectiva teórica",
         "fr": "D'un point de vue théorique", "de": "Aus theoretischer Sicht"},
        {"en": "The fundamental question is", "es": "La pregunta fundamental es", "pt": "A questão fundamental é",
         "fr": "La question fondamentale est", "de": "Die grundlegende Frage ist"},
        {"en": "This leads us to conclude", "es": "Esto nos lleva a concluir", "pt": "Isso nos leva a concluir",
         "fr": "Cela nous amène à conclure", "de": "Dies führt uns zu dem Schluss"},
        {"en": "Let's analyze this further", "es": "Analicemos esto más a fondo", "pt": "Vamos analisar isso mais a fundo",
         "fr": "Analysons cela plus en détail", "de": "Lassen Sie uns das näher analysieren"},
        {"en": "The logical conclusion is", "es": "La conclusión lógica es", "pt": "A conclusão lógica é",
         "fr": "La conclusion logique est", "de": "Die logische Schlussfolgerung ist"},
        {"en": "This concept suggests that", "es": "Este concepto sugiere que", "pt": "Este conceito sugere que",
         "fr": "Ce concept suggère que", "de": "Dieses Konzept deutet darauf hin, dass"},
        {"en": "Let's challenge this assumption", "es": "Cuestionemos esta suposición", "pt": "Vamos questionar essa suposição",
         "fr": "Remettons en question cette hypothèse", "de": "Lassen Sie uns diese Annahme hinterfragen"}
    ]
}

# Day 49: Ethical Debates and Moral Reasoning
day49_phrases = {
    "Ethical Principles": [
        {"en": "Moral values", "es": "Valores morales", "pt": "Valores morais",
         "fr": "Valeurs morales", "de": "Moralische Werte"},
        {"en": "Ethical dilemma", "es": "Dilema ético", "pt": "Dilema ético",
         "fr": "Dilemme éthique", "de": "Ethisches Dilemma"},
        {"en": "Social responsibility", "es": "Responsabilidad social", "pt": "Responsabilidade social",
         "fr": "Responsabilité sociale", "de": "Soziale Verantwortung"},
        {"en": "Human rights", "es": "Derechos humanos", "pt": "Direitos humanos",
         "fr": "Droits de l'homme", "de": "Menschenrechte"},
        {"en": "Justice and fairness", "es": "Justicia y equidad", "pt": "Justiça e equidade",
         "fr": "Justice et équité", "de": "Gerechtigkeit und Fairness"},
        {"en": "Moral obligation", "es": "Obligación moral", "pt": "Obrigação moral",
         "fr": "Obligation morale", "de": "Moralische Verpflichtung"},
        {"en": "Ethical conduct", "es": "Conducta ética", "pt": "Conduta ética",
         "fr": "Conduite éthique", "de": "Ethisches Verhalten"},
        {"en": "Personal integrity", "es": "Integridad personal", "pt": "Integridade pessoal",
         "fr": "Intégrité personnelle", "de": "Persönliche Integrität"},
        {"en": "Moral compass", "es": "Brújula moral", "pt": "Bússola moral",
         "fr": "Boussole morale", "de": "Moralischer Kompass"},
        {"en": "Ethical framework", "es": "Marco ético", "pt": "Marco ético",
         "fr": "Cadre éthique", "de": "Ethischer Rahmen"}
    ],
    "Moral Reasoning": [
        {"en": "Consider the consequences", "es": "Considerar las consecuencias", "pt": "Considerar as consequências",
         "fr": "Considérer les conséquences", "de": "Die Konsequenzen bedenken"},
        {"en": "Weigh the options", "es": "Sopesar las opciones", "pt": "Pesar as opções",
         "fr": "Peser les options", "de": "Die Optionen abwägen"},
        {"en": "Ethical implications", "es": "Implicaciones éticas", "pt": "Implicações éticas",
         "fr": "Implications éthiques", "de": "Ethische Implikationen"},
        {"en": "Moral judgment", "es": "Juicio moral", "pt": "Julgamento moral",
         "fr": "Jugement moral", "de": "Moralisches Urteil"},
        {"en": "Ethical decision-making", "es": "Toma de decisiones éticas", "pt": "Tomada de decisões éticas",
         "fr": "Prise de décision éthique", "de": "Ethische Entscheidungsfindung"},
        {"en": "Moral principles", "es": "Principios morales", "pt": "Princípios morais",
         "fr": "Principes moraux", "de": "Moralische Prinzipien"},
        {"en": "Value system", "es": "Sistema de valores", "pt": "Sistema de valores",
         "fr": "Système de valeurs", "de": "Wertesystem"},
        {"en": "Ethical standards", "es": "Estándares éticos", "pt": "Padrões éticos",
         "fr": "Normes éthiques", "de": "Ethische Standards"},
        {"en": "Moral responsibility", "es": "Responsabilidad moral", "pt": "Responsabilidade moral",
         "fr": "Responsabilité morale", "de": "Moralische Verantwortung"},
        {"en": "Ethical behavior", "es": "Comportamiento ético", "pt": "Comportamento ético",
         "fr": "Comportement éthique", "de": "Ethisches Verhalten"}
    ],
    "Ethical Debates": [
        {"en": "Let's discuss the ethical aspects", "es": "Discutamos los aspectos éticos", "pt": "Vamos discutir os aspectos éticos",
         "fr": "Discutons des aspects éthiques", "de": "Lassen Sie uns die ethischen Aspekte diskutieren"},
        {"en": "From a moral standpoint", "es": "Desde un punto de vista moral", "pt": "De um ponto de vista moral",
         "fr": "D'un point de vue moral", "de": "Aus moralischer Sicht"},
        {"en": "The ethical question is", "es": "La cuestión ética es", "pt": "A questão ética é",
         "fr": "La question éthique est", "de": "Die ethische Frage ist"},
        {"en": "Consider the moral implications", "es": "Considera las implicaciones morales", "pt": "Considere as implicações morais",
         "fr": "Considérez les implications morales", "de": "Bedenken Sie die moralischen Implikationen"},
        {"en": "What is the right thing to do?", "es": "¿Cuál es lo correcto?", "pt": "Qual é a coisa certa a fazer?",
         "fr": "Quelle est la bonne chose à faire ?", "de": "Was ist das Richtige zu tun?"},
        {"en": "Moral considerations", "es": "Consideraciones morales", "pt": "Considerações morais",
         "fr": "Considérations morales", "de": "Moralische Überlegungen"},
        {"en": "Ethical concerns", "es": "Preocupaciones éticas", "pt": "Preocupações éticas",
         "fr": "Préoccupations éthiques", "de": "Ethische Bedenken"},
        {"en": "Moral dilemma", "es": "Dilema moral", "pt": "Dilema moral",
         "fr": "Dilemme moral", "de": "Moralisches Dilemma"},
        {"en": "Ethical perspective", "es": "Perspectiva ética", "pt": "Perspectiva ética",
         "fr": "Perspective éthique", "de": "Ethische Perspektive"},
        {"en": "Moral reasoning", "es": "Razonamiento moral", "pt": "Raciocínio moral",
         "fr": "Raisonnement moral", "de": "Moralische Argumentation"}
    ]
}

# Day 50: Theoretical Frameworks and Abstract Thinking
day50_phrases = {
    "Theoretical Concepts": [
        {"en": "Conceptual framework", "es": "Marco conceptual", "pt": "Marco conceitual",
         "fr": "Cadre conceptuel", "de": "Konzeptioneller Rahmen"},
        {"en": "Theoretical model", "es": "Modelo teórico", "pt": "Modelo teórico",
         "fr": "Modèle théorique", "de": "Theoretisches Modell"},
        {"en": "Abstract thinking", "es": "Pensamiento abstracto", "pt": "Pensamento abstrato",
         "fr": "Pensée abstraite", "de": "Abstraktes Denken"},
        {"en": "Cognitive framework", "es": "Marco cognitivo", "pt": "Marco cognitivo",
         "fr": "Cadre cognitif", "de": "Kognitiver Rahmen"},
        {"en": "Theoretical basis", "es": "Base teórica", "pt": "Base teórica",
         "fr": "Base théorique", "de": "Theoretische Grundlage"},
        {"en": "Conceptual understanding", "es": "Comprensión conceptual", "pt": "Compreensão conceitual",
         "fr": "Compréhension conceptuelle", "de": "Konzeptuelles Verständnis"},
        {"en": "Theoretical perspective", "es": "Perspectiva teórica", "pt": "Perspectiva teórica",
         "fr": "Perspective théorique", "de": "Theoretische Perspektive"},
        {"en": "Abstract concept", "es": "Concepto abstracto", "pt": "Conceito abstrato",
         "fr": "Concept abstrait", "de": "Abstraktes Konzept"},
        {"en": "Theoretical approach", "es": "Enfoque teórico", "pt": "Abordagem teórica",
         "fr": "Approche théorique", "de": "Theoretischer Ansatz"},
        {"en": "Conceptual model", "es": "Modelo conceptual", "pt": "Modelo conceitual",
         "fr": "Modèle conceptuel", "de": "Konzeptmodell"}
    ],
    "Complex Opinions": [
        {"en": "In my considered opinion", "es": "En mi opinión considerada", "pt": "Na minha opinião ponderada",
         "fr": "À mon avis réfléchi", "de": "Nach reiflicher Überlegung"},
        {"en": "From my perspective", "es": "Desde mi perspectiva", "pt": "Da minha perspectiva",
         "fr": "De mon point de vue", "de": "Aus meiner Sicht"},
        {"en": "I would argue that", "es": "Yo argumentaría que", "pt": "Eu argumentaria que",
         "fr": "Je dirais que", "de": "Ich würde argumentieren, dass"},
        {"en": "Taking everything into account", "es": "Teniendo todo en cuenta", "pt": "Levando tudo em conta",
         "fr": "Tout bien considéré", "de": "Alles in Betracht ziehend"},
        {"en": "On deeper reflection", "es": "En una reflexión más profunda", "pt": "Numa reflexão mais profunda",
         "fr": "À y réfléchir plus profondément", "de": "Bei tieferer Betrachtung"},
        {"en": "It could be argued that", "es": "Se podría argumentar que", "pt": "Poderia se argumentar que",
         "fr": "On pourrait dire que", "de": "Man könnte argumentieren, dass"},
        {"en": "From a critical standpoint", "es": "Desde un punto de vista crítico", "pt": "De um ponto de vista crítico",
         "fr": "D'un point de vue critique", "de": "Aus kritischer Sicht"},
        {"en": "Upon careful analysis", "es": "Tras un análisis cuidadoso", "pt": "Após uma análise cuidadosa",
         "fr": "Après une analyse minutieuse", "de": "Nach sorgfältiger Analyse"},
        {"en": "In my assessment", "es": "En mi evaluación", "pt": "Na minha avaliação",
         "fr": "Selon mon évaluation", "de": "Nach meiner Einschätzung"},
        {"en": "Based on my understanding", "es": "Según mi entendimiento", "pt": "Com base no meu entendimento",
         "fr": "Selon ma compréhension", "de": "Nach meinem Verständnis"}
    ],
    "Hypothetical Scenarios": [
        {"en": "Let's imagine a scenario", "es": "Imaginemos un escenario", "pt": "Vamos imaginar um cenário",
         "fr": "Imaginons un scénario", "de": "Stellen wir uns ein Szenario vor"},
        {"en": "In a hypothetical situation", "es": "En una situación hipotética", "pt": "Em uma situação hipotética",
         "fr": "Dans une situation hypothétique", "de": "In einer hypothetischen Situation"},
        {"en": "Suppose that...", "es": "Supongamos que...", "pt": "Suponhamos que...",
         "fr": "Supposons que...", "de": "Angenommen, dass..."},
        {"en": "What if we considered...", "es": "¿Y si consideráramos...?", "pt": "E se considerássemos...?",
         "fr": "Et si nous considérions...?", "de": "Was wäre, wenn wir... betrachten würden?"},
        {"en": "In theory...", "es": "En teoría...", "pt": "Em teoria...",
         "fr": "En théorie...", "de": "Theoretisch..."},
        {"en": "Under different circumstances", "es": "Bajo diferentes circunstancias", "pt": "Sob diferentes circunstâncias",
         "fr": "Dans des circonstances différentes", "de": "Unter anderen Umständen"},
        {"en": "Assuming that...", "es": "Asumiendo que...", "pt": "Assumindo que...",
         "fr": "En supposant que...", "de": "Angenommen..."},
        {"en": "If we were to...", "es": "Si fuéramos a...", "pt": "Se fôssemos...",
         "fr": "Si nous devions...", "de": "Wenn wir... würden"},
        {"en": "In an ideal world", "es": "En un mundo ideal", "pt": "Em um mundo ideal",
         "fr": "Dans un monde idéal", "de": "In einer idealen Welt"},
        {"en": "Consider the possibility", "es": "Considera la posibilidad", "pt": "Considere a possibilidade",
         "fr": "Considérez la possibilité", "de": "Betrachten Sie die Möglichkeit"}
    ]
}

# Dictionary mapping day numbers to phrase dictionaries
all_phrases = {
    45: day45_phrases,
    46: day46_phrases,
    47: day47_phrases,
    48: day48_phrases,
    49: day49_phrases,
    50: day50_phrases
}

def generate_text_file(day, language_code, language_name):
    """Generate a text file with all phrases for a specific day"""
    print(f"Generating Day {day} {language_name} text file...")
    
    phrases_dict = all_phrases[day]
    
    with open(f"text_files/day{day}_{language_code}.txt", "w", encoding="utf-8") as f:
        for category, phrase_list in phrases_dict.items():
            f.write(f"\n{category}\n")
            f.write("-" * len(category) + "\n")
            for phrase in phrase_list:
                f.write(f"{phrase[language_code]}\n")
    
    print(f"✓ Saved to text_files/day{day}_{language_code}.txt")

def generate_audio(day, language_code, language_name):
    """Generate audio file for a specific day and language"""
    print(f"\nGenerating Day {day} {language_name} audio file...")
    start_time = time.time()
    
    phrases_dict = all_phrases[day]
    
    # Generate text for the entire language
    text = ""
    for category, phrase_list in phrases_dict.items():
        for phrase in phrase_list:
            text += phrase[language_code] + ". "
    
    # Generate audio using gTTS
    tts = gTTS(text=text, lang=language_code)
    tts.save(f"audio_files/day{day}_{language_code}.mp3")
    
    elapsed = time.time() - start_time
    print(f"✓ Saved to audio_files/day{day}_{language_code}.mp3 ({elapsed:.2f}s)")

def main():
    parser = argparse.ArgumentParser(description="Generate advanced language learning files (Days 45-50)")
    parser.add_argument("--day", "-d", type=int, choices=list(range(45, 51)), default=None,
                        help="Day number to generate (45-50). If not specified, generates all days.")
    parser.add_argument("--languages", "-l", nargs="+", choices=["es", "pt", "en", "fr", "de"], 
                        default=["es", "pt"], help="Languages to generate (es=Spanish, pt=Portuguese, en=English, fr=French, de=German)")
    parser.add_argument("--text-only", "-t", action="store_true", 
                        help="Generate only text files (no audio)")
    args = parser.parse_args()
    
    language_names = {"es": "Spanish", "pt": "Portuguese", "en": "English", "fr": "French", "de": "German"}
    
    # Check available days
    available_days = list(all_phrases.keys())
    if not available_days:
        print("No content available yet. Please add content for days 45-50.")
        return
    
    # Determine which days to process
    if args.day:
        if args.day not in all_phrases:
            print(f"Content for day {args.day} is not available yet.")
            return
        days_to_process = [args.day]
    else:
        days_to_process = available_days
    
    # Process each day
    for day in days_to_process:
        print(f"\n=== Processing Day {day} ===")
        
        # Generate text files for all selected languages
        for lang in args.languages:
            generate_text_file(day, lang, language_names[lang])
        
        # Generate audio files if not in text-only mode
        if not args.text_only:
            for lang in args.languages:
                generate_audio(day, lang, language_names[lang])
    
    print("\nAll files generated successfully!")
    print("\nUsage examples:")
    print("  - Generate text files only: python language_phrases_advanced_additional_extended.py --text-only")
    print("  - Generate files for just Day 45: python language_phrases_advanced_additional_extended.py --day 45")
    print("  - Generate files for just Spanish: python language_phrases_advanced_additional_extended.py --languages es")
    print("  - Generate Day 48 Portuguese text only: python language_phrases_advanced_additional_extended.py --day 48 --languages pt --text-only")
    print("  - Generate all available days: python language_phrases_advanced_additional_extended.py")

if __name__ == "__main__":
    main()
