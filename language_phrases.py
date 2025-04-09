import argparse
import os
import time
from gtts import gTTS

# Define phrases by day and category

# Day 1: Basic Greetings, Travel Phrases, Numbers, and Emergency Phrases
day1_phrases = {
    "Basic Greetings & Common Phrases": [
        {"en": "Hello", "es": "Hola", "pt": "Olá", "fr": "Bonjour", "de": "Hallo"},
        {"en": "Good morning", "es": "Buenos días", "pt": "Bom dia", "fr": "Bonjour", "de": "Guten Morgen"},
        {"en": "Good afternoon", "es": "Buenas tardes", "pt": "Boa tarde", "fr": "Bon après-midi", "de": "Guten Tag"},
        {"en": "Good evening/night", "es": "Buenas noches", "pt": "Boa noite", "fr": "Bonsoir", "de": "Guten Abend"},
        {"en": "How are you?", "es": "¿Cómo estás?", "pt": "Como você está?", "fr": "Comment ça va ?", "de": "Wie geht es dir?"},
        {"en": "I'm fine, thank you", "es": "Estoy bien, gracias", "pt": "Estou bem, obrigado/obrigada", "fr": "Je vais bien, merci", "de": "Mir geht es gut, danke"},
        {"en": "What's your name?", "es": "¿Cómo te llamas?", "pt": "Como você se chama?", "fr": "Comment tu t'appelles ?", "de": "Wie heißt du?"},
        {"en": "My name is…", "es": "Me llamo…", "pt": "Meu nome é…", "fr": "Je m'appelle…", "de": "Ich heiße…"},
        {"en": "Nice to meet you", "es": "Mucho gusto", "pt": "Prazer em conhecer", "fr": "Enchanté", "de": "Freut mich, dich kennenzulernen"},
        {"en": "Please", "es": "Por favor", "pt": "Por favor", "fr": "S'il vous plaît", "de": "Bitte"},
        {"en": "Thank you", "es": "Gracias", "pt": "Obrigado/Obrigada", "fr": "Merci", "de": "Danke"},
        {"en": "You're welcome", "es": "De nada", "pt": "De nada", "fr": "De rien", "de": "Gern geschehen"},
        {"en": "Excuse me", "es": "Perdón / Disculpe", "pt": "Com licença / Desculpe", "fr": "Excusez-moi", "de": "Entschuldigen Sie"},
        {"en": "I'm sorry", "es": "Lo siento", "pt": "Sinto muito", "fr": "Je suis désolé", "de": "Es tut mir leid"},
        {"en": "Yes", "es": "Sí", "pt": "Sim", "fr": "Oui", "de": "Ja"},
        {"en": "No", "es": "No", "pt": "Não", "fr": "Non", "de": "Nein"},
        {"en": "Maybe", "es": "Tal vez", "pt": "Talvez", "fr": "Peut-être", "de": "Vielleicht"},
        {"en": "I don't understand", "es": "No entiendo", "pt": "Não entendo", "fr": "Je ne comprends pas", "de": "Ich verstehe nicht"},
        {"en": "Can you help me?", "es": "¿Puedes ayudarme?", "pt": "Você pode me ajudar?", "fr": "Pouvez-vous m'aider ?", "de": "Kannst du mir helfen?"},
        {"en": "I need help", "es": "Necesito ayuda", "pt": "Preciso de ajuda", "fr": "J'ai besoin d'aide", "de": "Ich brauche Hilfe"}
    ],
    "Essential Travel Phrases": [
        {"en": "Where is the bathroom?", "es": "¿Dónde está el baño?", "pt": "Onde fica o banheiro?", "fr": "Où sont les toilettes ?", "de": "Wo ist die Toilette?"},
        {"en": "How much does it cost?", "es": "¿Cuánto cuesta?", "pt": "Quanto custa?", "fr": "Combien ça coûte ?", "de": "Wie viel kostet das?"},
        {"en": "I would like…", "es": "Me gustaría…", "pt": "Eu gostaria de…", "fr": "Je voudrais…", "de": "Ich hätte gerne…"},
        {"en": "I need…", "es": "Necesito…", "pt": "Eu preciso de…", "fr": "J'ai besoin de…", "de": "Ich brauche…"},
        {"en": "The check, please", "es": "La cuenta, por favor", "pt": "A conta, por favor", "fr": "L'addition, s'il vous plaît", "de": "Die Rechnung, bitte"},
        {"en": "Do you speak English?", "es": "¿Hablas inglés?", "pt": "Você fala inglês?", "fr": "Parlez-vous anglais ?", "de": "Sprechen Sie Englisch?"},
        {"en": "I don't speak Spanish/Portuguese well", "es": "No hablo bien español", "pt": "Não falo bem português", "fr": "Je ne parle pas bien espagnol/portugais", "de": "Ich spreche nicht gut Spanisch/Portugiesisch"},
        {"en": "What time is it?", "es": "¿Qué hora es?", "pt": "Que horas são?", "fr": "Quelle heure est-il ?", "de": "Wie spät ist es?"},
        {"en": "Where is…?", "es": "¿Dónde está…?", "pt": "Onde fica…?", "fr": "Où est… ?", "de": "Wo ist …?"},
        {"en": "I'm lost", "es": "Estoy perdido/a", "pt": "Estou perdido/a", "fr": "Je suis perdu", "de": "Ich habe mich verirrt"}
    ],
    "Numbers & Shopping": [
        {"en": "One", "es": "Uno", "pt": "Um", "fr": "Un", "de": "Eins"},
        {"en": "Two", "es": "Dos", "pt": "Dois", "fr": "Deux", "de": "Zwei"},
        {"en": "Three", "es": "Tres", "pt": "Três", "fr": "Trois", "de": "Drei"},
        {"en": "Four", "es": "Cuatro", "pt": "Quatro", "fr": "Quatre", "de": "Vier"},
        {"en": "Five", "es": "Cinco", "pt": "Cinco", "fr": "Cinq", "de": "Fünf"},
        {"en": "Ten", "es": "Diez", "pt": "Dez", "fr": "Dix", "de": "Zehn"},
        {"en": "Twenty", "es": "Veinte", "pt": "Vinte", "fr": "Vingt", "de": "Zwanzig"},
        {"en": "Fifty", "es": "Cincuenta", "pt": "Cinquenta", "fr": "Cinquante", "de": "Fünfzig"},
        {"en": "One hundred", "es": "Cien", "pt": "Cem", "fr": "Cent", "de": "Hundert"},
        {"en": "How much is this?", "es": "¿Cuánto cuesta esto?", "pt": "Quanto custa isso?", "fr": "Combien ça coûte ?", "de": "Wie viel kostet das?"}
    ],
    "Emergency Phrases": [
        {"en": "Help!", "es": "¡Ayuda!", "pt": "Socorro!", "fr": "À l'aide !", "de": "Hilfe!"},
        {"en": "Call the police!", "es": "¡Llame a la policía!", "pt": "Chame a polícia!", "fr": "Appelez la police !", "de": "Rufen Sie die Polizei!"},
        {"en": "I'm sick", "es": "Estoy enfermo/a", "pt": "Estou doente", "fr": "Je suis malade", "de": "Ich bin krank"},
        {"en": "I need a doctor", "es": "Necesito un médico", "pt": "Preciso de um médico", "fr": "J'ai besoin d'un médecin", "de": "Ich brauche einen Arzt"},
        {"en": "It's an emergency", "es": "Es una emergencia", "pt": "É uma emergência", "fr": "C'est une urgence", "de": "Es ist ein Notfall"},
        {"en": "I'm allergic to…", "es": "Soy alérgico/a a…", "pt": "Sou alérgico/a a…", "fr": "Je suis allergique à…", "de": "Ich bin allergisch gegen…"},
        {"en": "I lost my passport", "es": "Perdí mi pasaporte", "pt": "Perdi meu passaporte", "fr": "J'ai perdu mon passeport", "de": "Ich habe meinen Pass verloren"},
        {"en": "Where is the hospital?", "es": "¿Dónde está el hospital?", "pt": "Onde fica o hospital?", "fr": "Où est l'hôpital ?", "de": "Wo ist das Krankenhaus?"},
        {"en": "I need a taxi", "es": "Necesito un taxi", "pt": "Preciso de um táxi", "fr": "J'ai besoin d'un taxi", "de": "Ich brauche ein Taxi"},
        {"en": "Be careful!", "es": "¡Cuidado!", "pt": "Cuidado!", "fr": "Faites attention !", "de": "Sei vorsichtig!"}
    ]
}

# Day 2: Transportation, Hotel, Restaurant, Shopping, Small Talk, and Conversational Connectors
day2_phrases = {
    "Transportation & Directions": [
        {"en": "Where is the bus station?", "es": "¿Dónde está la estación de autobuses?", "pt": "Onde fica a estação de ônibus?", "fr": "Où est la station de bus ?", "de": "Wo ist die Bushaltestelle?"},
        {"en": "Where is the train station?", "es": "¿Dónde está la estación de tren?", "pt": "Onde fica a estação de trem?", "fr": "Où est la gare ?", "de": "Wo ist der Bahnhof?"},
        {"en": "Where is the airport?", "es": "¿Dónde está el aeropuerto?", "pt": "Onde fica o aeroporto?", "fr": "Où est l'aéroport ?", "de": "Wo ist der Flughafen?"},
        {"en": "I need a ticket to…", "es": "Necesito un boleto para…", "pt": "Preciso de uma passagem para…", "fr": "J'ai besoin d'un billet pour…", "de": "Ich brauche ein Ticket nach…"},
        {"en": "How much is a ticket to…?", "es": "¿Cuánto cuesta un boleto para…?", "pt": "Quanto custa uma passagem para…?", "fr": "Combien coûte un billet pour… ?", "de": "Wie viel kostet ein Ticket nach…?"},
        {"en": "What time does the bus leave?", "es": "¿A qué hora sale el autobús?", "pt": "A que horas o ônibus sai?", "fr": "À quelle heure part le bus ?", "de": "Wann fährt der Bus ab?"},
        {"en": "What time does the train arrive?", "es": "¿A qué hora llega el tren?", "pt": "A que horas o trem chega?", "fr": "À quelle heure arrive le train ?", "de": "Wann kommt der Zug an?"},
        {"en": "I want to go to…", "es": "Quiero ir a…", "pt": "Quero ir para…", "fr": "Je veux aller à…", "de": "Ich möchte nach … gehen"},
        {"en": "Does this bus go to…?", "es": "¿Este autobús va a…?", "pt": "Este ônibus vai para…?", "fr": "Ce bus va-t-il à… ?", "de": "Fährt dieser Bus nach …?"},
        {"en": "Stop here, please", "es": "Pare aquí, por favor", "pt": "Pare aqui, por favor", "fr": "Arrêtez-vous ici, s'il vous plaît", "de": "Bitte halten Sie hier an"}
    ],
    "At a Hotel": [
        {"en": "I have a reservation", "es": "Tengo una reserva", "pt": "Tenho uma reserva", "fr": "J'ai une réservation", "de": "Ich habe eine Reservierung"},
        {"en": "I would like a room", "es": "Me gustaría una habitación", "pt": "Gostaria de um quarto", "fr": "Je voudrais une chambre", "de": "Ich hätte gerne ein Zimmer"},
        {"en": "Do you have any available rooms?", "es": "¿Tiene habitaciones disponibles?", "pt": "Você tem quartos disponíveis?", "fr": "Avez-vous des chambres disponibles ?", "de": "Haben Sie freie Zimmer?"},
        {"en": "How much is a night?", "es": "¿Cuánto cuesta por noche?", "pt": "Quanto custa por noite?", "fr": "Combien coûte une nuit ?", "de": "Wie viel kostet eine Nacht?"},
        {"en": "I need a single/double room", "es": "Necesito una habitación individual/doble", "pt": "Preciso de um quarto individual/duplo", "fr": "J'ai besoin d'une chambre simple/double", "de": "Ich brauche ein Einzel-/Doppelzimmer"},
        {"en": "Does the room have Wi-Fi?", "es": "¿La habitación tiene Wi-Fi?", "pt": "O quarto tem Wi-Fi?", "fr": "La chambre a-t-elle le Wi-Fi ?", "de": "Hat das Zimmer WLAN?"},
        {"en": "Where is the elevator?", "es": "¿Dónde está el ascensor?", "pt": "Onde fica o elevador?", "fr": "Où est l'ascenseur ?", "de": "Wo ist der Aufzug?"},
        {"en": "Can I have a late checkout?", "es": "¿Puedo hacer el check-out tarde?", "pt": "Posso fazer o check-out mais tarde?", "fr": "Puis-je avoir un départ tardif ?", "de": "Kann ich einen späten Check-out haben?"},
        {"en": "The key, please", "es": "La llave, por favor", "pt": "A chave, por favor", "fr": "La clé, s'il vous plaît", "de": "Den Schlüssel, bitte"},
        {"en": "I need extra towels", "es": "Necesito toallas extra", "pt": "Preciso de toalhas extras", "fr": "J'ai besoin de serviettes supplémentaires", "de": "Ich brauche zusätzliche Handtücher"}
    ],
    "At a Restaurant": [
        {"en": "A table for one/two, please", "es": "Una mesa para uno/dos, por favor", "pt": "Uma mesa para um/dois, por favor", "fr": "Une table pour une/deux personnes, s'il vous plaît", "de": "Ein Tisch für eine/zwei Personen, bitte"},
        {"en": "What do you recommend?", "es": "¿Qué recomienda?", "pt": "O que você recomenda?", "fr": "Que recommandez-vous ?", "de": "Was empfehlen Sie?"},
        {"en": "I would like to order…", "es": "Me gustaría pedir…", "pt": "Gostaria de pedir…", "fr": "Je voudrais commander…", "de": "Ich möchte bestellen…"},
        {"en": "I'm vegetarian", "es": "Soy vegetariano/a", "pt": "Sou vegetariano/a", "fr": "Je suis végétarien(ne)", "de": "Ich bin Vegetarier/in"},
        {"en": "I don't eat meat", "es": "No como carne", "pt": "Não como carne", "fr": "Je ne mange pas de viande", "de": "Ich esse kein Fleisch"},
        {"en": "Is this spicy?", "es": "¿Esto es picante?", "pt": "Isso é apimentado?", "fr": "Est-ce épicé ?", "de": "Ist das scharf?"},
        {"en": "I need a menu", "es": "Necesito un menú", "pt": "Preciso de um cardápio", "fr": "J'ai besoin d'un menu", "de": "Ich brauche eine Speisekarte"},
        {"en": "The bill, please", "es": "La cuenta, por favor", "pt": "A conta, por favor", "fr": "L'addition, s'il vous plaît", "de": "Die Rechnung, bitte"},
        {"en": "Can I pay with a credit card?", "es": "¿Puedo pagar con tarjeta de crédito?", "pt": "Posso pagar com cartão de crédito?", "fr": "Puis-je payer avec une carte de crédit ?", "de": "Kann ich mit Kreditkarte bezahlen?"},
        {"en": "That was delicious", "es": "Estuvo delicioso", "pt": "Estava delicioso", "fr": "C'était délicieux", "de": "Das war köstlich"}
    ],
    "Shopping & Bargaining": [
        {"en": "I want to buy this", "es": "Quiero comprar esto", "pt": "Quero comprar isso", "fr": "Je veux acheter ceci", "de": "Ich möchte das kaufen"},
        {"en": "How much is this?", "es": "¿Cuánto cuesta esto?", "pt": "Quanto custa isso?", "fr": "Combien ça coûte ?", "de": "Wie viel kostet das?"},
        {"en": "It's too expensive", "es": "Es demasiado caro", "pt": "Está muito caro", "fr": "C'est trop cher", "de": "Es ist zu teuer"},
        {"en": "Can you lower the price?", "es": "¿Puede bajar el precio?", "pt": "Pode fazer um desconto?", "fr": "Pouvez-vous baisser le prix ?", "de": "Können Sie den Preis senken?"},
        {"en": "Do you have this in another color?", "es": "¿Tiene esto en otro color?", "pt": "Você tem isso em outra cor?", "fr": "L'avez-vous dans une autre couleur ?", "de": "Haben Sie das in einer anderen Farbe?"},
        {"en": "Do you have this in another size?", "es": "¿Tiene esto en otra talla?", "pt": "Você tem isso em outro tamanho?", "fr": "L'avez-vous dans une autre taille ?", "de": "Haben Sie das in einer anderen Größe?"},
        {"en": "I'm just looking", "es": "Solo estoy mirando", "pt": "Só estou olhando", "fr": "Je regarde seulement", "de": "Ich sehe mich nur um"},
        {"en": "Where is the fitting room?", "es": "¿Dónde está el probador?", "pt": "Onde fica o provador?", "fr": "Où est la cabine d'essayage ?", "de": "Wo ist die Umkleidekabine?"},
        {"en": "I'll take it", "es": "Me lo llevo", "pt": "Vou levar", "fr": "Je le prends", "de": "Ich nehme es"},
        {"en": "I want a refund", "es": "Quiero un reembolso", "pt": "Quero um reembolso", "fr": "Je veux un remboursement", "de": "Ich möchte eine Rückerstattung"}
    ],
    "Making Small Talk": [
        {"en": "Where are you from?", "es": "¿De dónde eres?", "pt": "De onde você é?", "fr": "D'où viens-tu ?", "de": "Woher kommst du?"},
        {"en": "I'm from…", "es": "Soy de…", "pt": "Eu sou de…", "fr": "Je viens de…", "de": "Ich komme aus…"},
        {"en": "How long have you been here?", "es": "¿Cuánto tiempo llevas aquí?", "pt": "Há quanto tempo você está aqui?", "fr": "Depuis combien de temps es-tu ici ?", "de": "Wie lange bist du schon hier?"},
        {"en": "What do you do for work?", "es": "¿A qué te dedicas?", "pt": "O que você faz?", "fr": "Que fais-tu dans la vie ?", "de": "Was machst du beruflich?"},
        {"en": "Do you like it here?", "es": "¿Te gusta aquí?", "pt": "Você gosta daqui?", "fr": "Aimes-tu cet endroit ?", "de": "Gefällt es dir hier?"},
        {"en": "It's beautiful here", "es": "Es hermoso aquí", "pt": "Aqui é lindo", "fr": "C'est beau ici", "de": "Es ist schön hier"},
        {"en": "The weather is nice today", "es": "Hoy hace buen tiempo", "pt": "O tempo está bom hoje", "fr": "Il fait beau aujourd'hui", "de": "Das Wetter ist heute schön"},
        {"en": "What do you like to do?", "es": "¿Qué te gusta hacer?", "pt": "O que você gosta de fazer?", "fr": "Qu'est-ce que tu aimes faire ?", "de": "Was machst du gerne?"},
        {"en": "Do you have Instagram?", "es": "¿Tienes Instagram?", "pt": "Você tem Instagram?", "fr": "As-tu Instagram ?", "de": "Hast du Instagram?"},
        {"en": "Let's keep in touch", "es": "Mantengamos el contacto", "pt": "Vamos manter contato", "fr": "Restons en contact", "de": "Lass uns in Kontakt bleiben"}
    ],
    "Conversational Connectors": [
        {"en": "And", "es": "Y", "pt": "E", "fr": "Et", "de": "Und"},
        {"en": "But", "es": "Pero", "pt": "Mas", "fr": "Mais", "de": "Aber"},
        {"en": "Because", "es": "Porque", "pt": "Porque", "fr": "Parce que", "de": "Weil"},
        {"en": "Maybe", "es": "Tal vez", "pt": "Talvez", "fr": "Peut-être", "de": "Vielleicht"},
        {"en": "I think that…", "es": "Creo que…", "pt": "Acho que…", "fr": "Je pense que…", "de": "Ich denke, dass…"},
        {"en": "I don't know", "es": "No sé", "pt": "Não sei", "fr": "Je ne sais pas", "de": "Ich weiß nicht"},
        {"en": "That's interesting", "es": "Eso es interesante", "pt": "Isso é interessante", "fr": "C'est intéressant", "de": "Das ist interessant"},
        {"en": "I agree", "es": "Estoy de acuerdo", "pt": "Eu concordo", "fr": "Je suis d'accord", "de": "Ich stimme zu"},
        {"en": "I disagree", "es": "No estoy de acuerdo", "pt": "Eu discordo", "fr": "Je ne suis pas d'accord", "de": "Ich stimme nicht zu"},
        {"en": "Can you repeat that?", "es": "¿Puedes repetir eso?", "pt": "Você pode repetir isso?", "fr": "Peux-tu répéter ?", "de": "Kannst du das wiederholen?"}
    ]
}

# Day 3: Talking About Yourself, Weather & Nature, Giving Directions, Making Plans, Asking for Help, Flirting & Making Friends, At a Bar or Café, Handling Problems
day3_phrases = {
    "Talking About Yourself": [
        {"en": "I am… (your profession)", "es": "Soy…", "pt": "Eu sou…", "fr": "Je suis… (votre profession)", "de": "Ich bin… (Ihr Beruf)"},
        {"en": "I work as…", "es": "Trabajo como…", "pt": "Trabalho como…", "fr": "Je travaille comme…", "de": "Ich arbeite als…"},
        {"en": "I am learning Spanish/Portuguese", "es": "Estoy aprendiendo español/portugués", "pt": "Estou aprendendo espanhol/português", "fr": "J'apprends l'espagnol/le portugais", "de": "Ich lerne Spanisch/Portugiesisch"},
        {"en": "I am traveling for… (time)", "es": "Estoy viajando por…", "pt": "Estou viajando por…", "fr": "Je voyage pour… (temps)", "de": "Ich reise für… (Zeit)"},
        {"en": "I love to travel", "es": "Me encanta viajar", "pt": "Eu adoro viajar", "fr": "J'adore voyager", "de": "Ich liebe es zu reisen"},
        {"en": "I like to read", "es": "Me gusta leer", "pt": "Eu gosto de ler", "fr": "J'aime lire", "de": "Ich lese gern"},
        {"en": "I like music", "es": "Me gusta la música", "pt": "Eu gosto de música", "fr": "J'aime la musique", "de": "Ich mag Musik"},
        {"en": "I like sports", "es": "Me gustan los deportes", "pt": "Eu gosto de esportes", "fr": "J'aime le sport", "de": "Ich mag Sport"},
        {"en": "I have a dog/cat", "es": "Tengo un perro/gato", "pt": "Eu tenho um cachorro/gato", "fr": "J'ai un chien/chat", "de": "Ich habe einen Hund/eine Katze"},
        {"en": "I am married/single", "es": "Estoy casado/a – soltero/a", "pt": "Sou casado/a – solteiro/a", "fr": "Je suis marié(e)/célibataire", "de": "Ich bin verheiratet/alleinstehend"}
    ],
    "Weather & Nature": [
        {"en": "It's hot", "es": "Hace calor", "pt": "Está quente", "fr": "Il fait chaud", "de": "Es ist heiß"},
        {"en": "It's cold", "es": "Hace frío", "pt": "Está frio", "fr": "Il fait froid", "de": "Es ist kalt"},
        {"en": "It's sunny", "es": "Hace sol", "pt": "Está ensolarado", "fr": "Il fait beau", "de": "Es ist sonnig"},
        {"en": "It's raining", "es": "Está lloviendo", "pt": "Está chovendo", "fr": "Il pleut", "de": "Es regnet"},
        {"en": "It's windy", "es": "Hace viento", "pt": "Está ventando", "fr": "Il y a du vent", "de": "Es ist windig"},
        {"en": "It's cloudy", "es": "Está nublado", "pt": "Está nublado", "fr": "C'est nuageux", "de": "Es ist bewölkt"},
        {"en": "It's snowing", "es": "Está nevando", "pt": "Está nevando", "fr": "Il neige", "de": "Es schneit"},
        {"en": "The weather is nice", "es": "Hace buen tiempo", "pt": "O tempo está bom", "fr": "Il fait beau", "de": "Das Wetter ist schön"},
        {"en": "The weather is bad", "es": "Hace mal tiempo", "pt": "O tempo está ruim", "fr": "Il fait mauvais", "de": "Das Wetter ist schlecht"},
        {"en": "What's the weather like today?", "es": "¿Cómo está el clima hoy?", "pt": "Como está o tempo hoje?", "fr": "Quel temps fait-il aujourd'hui ?", "de": "Wie ist das Wetter heute?"}
    ],
    "Giving Directions": [
        {"en": "Turn right", "es": "Gire a la derecha", "pt": "Vire à direita", "fr": "Tournez à droite", "de": "Biegen Sie rechts ab"},
        {"en": "Turn left", "es": "Gire a la izquierda", "pt": "Vire à esquerda", "fr": "Tournez à gauche", "de": "Biegen Sie links ab"},
        {"en": "Go straight", "es": "Siga recto", "pt": "Siga em frente", "fr": "Allez tout droit", "de": "Gehen Sie geradeaus"},
        {"en": "Stop here", "es": "Pare aquí", "pt": "Pare aqui", "fr": "Arrêtez-vous ici", "de": "Halten Sie hier an"},
        {"en": "It's near", "es": "Está cerca", "pt": "Está perto", "fr": "C'est près", "de": "Es ist in der Nähe"},
        {"en": "It's far", "es": "Está lejos", "pt": "Está longe", "fr": "C'est loin", "de": "Es ist weit"},
        {"en": "Go up", "es": "Sube", "pt": "Suba", "fr": "Montez", "de": "Gehen Sie nach oben"},
        {"en": "Go down", "es": "Baja", "pt": "Desça", "fr": "Descendez", "de": "Gehen Sie nach unten"},
        {"en": "At the corner", "es": "En la esquina", "pt": "Na esquina", "fr": "Au coin", "de": "An der Ecke"},
        {"en": "How do I get to…?", "es": "¿Cómo llego a…?", "pt": "Como eu chego em…?", "fr": "Comment puis-je aller à… ?", "de": "Wie komme ich zu…?"}
    ],
    "Making Plans": [
        {"en": "What are you doing today?", "es": "¿Qué haces hoy?", "pt": "O que você vai fazer hoje?", "fr": "Que fais-tu aujourd'hui ?", "de": "Was machst du heute?"},
        {"en": "Do you want to go out?", "es": "¿Quieres salir?", "pt": "Você quer sair?", "fr": "Veux-tu sortir ?", "de": "Möchtest du ausgehen?"},
        {"en": "Let's go!", "es": "¡Vamos!", "pt": "Vamos!", "fr": "Allons-y !", "de": "Lass uns gehen!"},
        {"en": "What time?", "es": "¿A qué hora?", "pt": "A que horas?", "fr": "À quelle heure ?", "de": "Um wie viel Uhr?"},
        {"en": "Where should we meet?", "es": "¿Dónde nos encontramos?", "pt": "Onde nos encontramos?", "fr": "Où devrions-nous nous rencontrer ?", "de": "Wo sollen wir uns treffen?"},
        {"en": "I'll see you there", "es": "Te veo allí", "pt": "Te vejo lá", "fr": "On se voit là-bas", "de": "Wir sehen uns dort"},
        {"en": "I have to go", "es": "Tengo que irme", "pt": "Tenho que ir", "fr": "Je dois y aller", "de": "Ich muss gehen"},
        {"en": "I'm busy", "es": "Estoy ocupado/a", "pt": "Estou ocupado/a", "fr": "Je suis occupé(e)", "de": "Ich bin beschäftigt"},
        {"en": "Maybe another day", "es": "Tal vez otro día", "pt": "Talvez outro dia", "fr": "Peut-être un autre jour", "de": "Vielleicht ein andermal"},
        {"en": "That sounds fun", "es": "Suena divertido", "pt": "Parece divertido", "fr": "Ça a l'air amusant", "de": "Das klingt spaßig"}
    ],
    "Asking for Help": [
        {"en": "Can you help me?", "es": "¿Puedes ayudarme?", "pt": "Você pode me ajudar?", "fr": "Peux-tu m'aider ?", "de": "Kannst du mir helfen?"},
        {"en": "I need help", "es": "Necesito ayuda", "pt": "Preciso de ajuda", "fr": "J'ai besoin d'aide", "de": "Ich brauche Hilfe"},
        {"en": "I lost my phone", "es": "Perdí mi teléfono", "pt": "Perdi meu celular", "fr": "J'ai perdu mon téléphone", "de": "Ich habe mein Handy verloren"},
        {"en": "I lost my wallet", "es": "Perdí mi cartera", "pt": "Perdi minha carteira", "fr": "J'ai perdu mon portefeuille", "de": "Ich habe meine Geldbörse verloren"},
        {"en": "I don't feel well", "es": "No me siento bien", "pt": "Não estou me sentindo bem", "fr": "Je ne me sens pas bien", "de": "Mir geht es nicht gut"},
        {"en": "Call an ambulance", "es": "Llame una ambulancia", "pt": "Chame una ambulância", "fr": "Appelez une ambulance", "de": "Rufen Sie einen Krankenwagen"},
        {"en": "Where is the police station?", "es": "¿Dónde está la comisaría?", "pt": "Onde fica a delegacia?", "fr": "Où est le poste de police ?", "de": "Wo ist die Polizeistation?"},
        {"en": "Where is the nearest pharmacy?", "es": "¿Dónde está la farmacia más cercana?", "pt": "Onde fica a farmácia mais próxima?", "fr": "Où est la pharmacie la plus proche ?", "de": "Wo ist die nächste Apotheke?"},
        {"en": "I have an emergency", "es": "Tengo una emergencia", "pt": "Tenho uma emergência", "fr": "J'ai une urgence", "de": "Ich habe einen Notfall"},
        {"en": "My hotel is…", "es": "Mi hotel está en…", "pt": "Meu hotel fica em…", "fr": "Mon hôtel est…", "de": "Mein Hotel ist…"}
    ],
    "Flirting & Making Friends": [
        {"en": "You are very beautiful/handsome", "es": "Eres muy hermosa/guapo", "pt": "Você é muito bonita/bonito", "fr": "Tu es très belle/beau", "de": "Du bist sehr schön/gutaussehend"},
        {"en": "I like your smile", "es": "Me gusta tu sonrisa", "pt": "Eu gosto do seu sorriso", "fr": "J'aime ton sourire", "de": "Ich mag dein Lächeln"},
        {"en": "Can I buy you a drink?", "es": "¿Te puedo invitar a un trago?", "pt": "Posso te pagar uma bebida?", "fr": "Puis-je t'offrir un verre ?", "de": "Kann ich dir ein Getränk kaufen?"},
        {"en": "Do you want to dance?", "es": "¿Quieres bailar?", "pt": "Você quer dançar?", "fr": "Veux-tu danser ?", "de": "Möchtest du tanzen?"},
        {"en": "I had a great time with you", "es": "Me la pasé muy bien contigo", "pt": "Eu me diverti muito com você", "fr": "J'ai passé un bon moment avec toi", "de": "Ich hatte eine tolle Zeit mit dir"},
        {"en": "Can I have your number?", "es": "¿Me das tu número?", "pt": "Posso ter seu número?", "fr": "Puis-je avoir ton numéro ?", "de": "Kann ich deine Nummer haben?"},
        {"en": "Do you have WhatsApp?", "es": "¿Tienes WhatsApp?", "pt": "Você tem WhatsApp?", "fr": "As-tu WhatsApp ?", "de": "Hast du WhatsApp?"},
        {"en": "Let's go out sometime", "es": "Salgamos algún día", "pt": "Vamos sair algum dia", "fr": "Sortons ensemble un de ces jours", "de": "Lass uns mal ausgehen"},
        {"en": "You are very funny", "es": "Eres muy gracioso/a", "pt": "Você é muito engraçado/a", "fr": "Tu es très drôle", "de": "Du bist sehr lustig"},
        {"en": "I like spending time with you", "es": "Me gusta pasar tiempo contigo", "pt": "Eu gosto de passar tempo com você", "fr": "J'aime passer du temps avec toi", "de": "Ich verbringe gerne Zeit mit dir"}
    ],
    "At a Bar or Café": [
        {"en": "A beer, please", "es": "Una cerveza, por favor", "pt": "Uma cerveja, por favor", "fr": "Une bière, s'il vous plaît", "de": "Ein Bier, bitte"},
        {"en": "A glass of wine, please", "es": "Una copa de vino, por favor", "pt": "Uma taça de vinho, por favor", "fr": "Un verre de vin, s'il vous plaît", "de": "Ein Glas Wein, bitte"},
        {"en": "A coffee, please", "es": "Un café, por favor", "pt": "Um café, por favor", "fr": "Un café, s'il vous plaît", "de": "Einen Kaffee, bitte"},
        {"en": "Can I see the menu?", "es": "¿Puedo ver el menú?", "pt": "Posso ver o cardápio?", "fr": "Puis-je voir le menu ?", "de": "Kann ich die Speisekarte sehen?"},
        {"en": "I'll have the same", "es": "Tomaré lo mismo", "pt": "Vou querer o mesmo", "fr": "Je prendrai la même chose", "de": "Ich nehme das Gleiche"},
        {"en": "Cheers!", "es": "¡Salud!", "pt": "Saúde!", "fr": "Santé !", "de": "Prost!"},
        {"en": "This is delicious", "es": "Esto está delicioso", "pt": "Isso está delicioso", "fr": "C'est délicieux", "de": "Das ist köstlich"},
        {"en": "Another round, please", "es": "Otra ronda, por favor", "pt": "Outra rodada, por favor", "fr": "Une autre tournée, s'il vous plaît", "de": "Noch eine Runde, bitte"},
        {"en": "What do you recommend?", "es": "¿Qué recomienda?", "pt": "O que você recomenda?", "fr": "Que recommandez-vous ?", "de": "Was empfehlen Sie?"},
        {"en": "Can I have a receipt?", "es": "¿Me puede dar un recibo?", "pt": "Pode me dar um recibo?", "fr": "Puis-je avoir un reçu ?", "de": "Kann ich einen Beleg haben?"}
    ],
    "Handling Problems": [
        {"en": "This is a mistake", "es": "Esto es un error", "pt": "Isso é um erro", "fr": "C'est une erreur", "de": "Das ist ein Fehler"},
        {"en": "I need to speak to the manager", "es": "Necesito hablar con el gerente", "pt": "Preciso falar com o gerente", "fr": "J'ai besoin de parler au responsable", "de": "Ich muss mit dem Manager sprechen"},
        {"en": "This is not what I ordered", "es": "Esto no es lo que pedí", "pt": "Isso não é o que eu pedi", "fr": "Ce n'est pas ce que j'ai commandé", "de": "Das ist nicht, was ich bestellt habe"},
        {"en": "I lost my keys", "es": "Perdí mis llaves", "pt": "Perdi minhas chaves", "fr": "J'ai perdu mes clés", "de": "Ich habe meine Schlüssel verloren"},
        {"en": "I was overcharged", "es": "Me cobraron de más", "pt": "Me cobraram a mais", "fr": "On m'a surfacturé", "de": "Mir wurde zu viel berechnet"},
        {"en": "I want to file a complaint", "es": "Quiero presentar una queja", "pt": "Quero fazer uma reclamação", "fr": "Je souhaite déposer une plainte", "de": "Ich möchte eine Beschwerde einreichen"},
        {"en": "Someone stole my…", "es": "Alguien robó mi…", "pt": "Alguém roubou meu/minha…", "fr": "Quelqu'un a volé mon/ma …", "de": "Jemand hat mein(e) … gestohlen"},
        {"en": "Can you fix this?", "es": "¿Puedes arreglar esto?", "pt": "Você pode consertar isso?", "fr": "Pouvez-vous réparer cela ?", "de": "Kannst du das reparieren?"},
        {"en": "I need a refund", "es": "Necesito un reembolso", "pt": "Preciso de um reembolso", "fr": "J'ai besoin d'un remboursement", "de": "Ich brauche eine Rückerstattung"},
        {"en": "This place is dangerous", "es": "Este lugar es peligroso", "pt": "Este lugar é perigoso", "fr": "Cet endroit est dangereux", "de": "Dieser Ort ist gefährlich"}
    ]
}

# Day 4: Expressing Opinions & Feelings, Talking About Plans & Future, Health & Medical Situations, Technology & Internet, Handling Money & Banking, Dealing with Authorities & Emergencies, Giving Compliments, Common Expressions & Idioms
day4_phrases = {
    "Expressing Opinions & Feelings": [
        {"en": "I like it", "es": "Me gusta", "pt": "Eu gosto", "fr": "J'aime ça", "de": "Ich mag es"},
        {"en": "I don't like it", "es": "No me gusta", "pt": "Eu não gosto", "fr": "Je n'aime pas ça", "de": "Ich mag es nicht"},
        {"en": "I love it", "es": "Me encanta", "pt": "Eu adoro", "fr": "Je l'adore", "de": "Ich liebe es"},
        {"en": "I hate it", "es": "Lo odio", "pt": "Eu odeio", "fr": "Je le déteste", "de": "Ich hasse es"},
        {"en": "I'm happy", "es": "Estoy feliz", "pt": "Estou feliz", "fr": "Je suis heureux/heureuse", "de": "Ich bin glücklich"},
        {"en": "I'm sad", "es": "Estoy triste", "pt": "Estou triste", "fr": "Je suis triste", "de": "Ich bin traurig"},
        {"en": "I'm tired", "es": "Estoy cansado/a", "pt": "Estou cansado/a", "fr": "Je suis fatigué(e)", "de": "Ich bin müde"},
        {"en": "I'm hungry", "es": "Tengo hambre", "pt": "Estou com fome", "fr": "J'ai faim", "de": "Ich habe Hunger"},
        {"en": "I'm thirsty", "es": "Tengo sed", "pt": "Estou com sede", "fr": "J'ai soif", "de": "Ich habe Durst"},
        {"en": "I'm bored", "es": "Estoy aburrido/a", "pt": "Estou entediado/a", "fr": "Je m'ennuie", "de": "Mir ist langweilig"}
    ],
    "Talking About Plans & Future": [
        {"en": "What are your plans?", "es": "¿Cuáles son tus planes?", "pt": "Quais são seus planos?", "fr": "Quels sont tes projets ?", "de": "Was hast du vor?"},
        {"en": "I have plans", "es": "Tengo planes", "pt": "Eu tenho planos", "fr": "J'ai des projets", "de": "Ich habe Pläne"},
        {"en": "I don't have plans", "es": "No tengo planes", "pt": "Eu não tenho planos", "fr": "Je n'ai pas de projets", "de": "Ich habe keine Pläne"},
        {"en": "I will travel", "es": "Voy a viajar", "pt": "Eu vou viajar", "fr": "Je vais voyager", "de": "Ich werde reisen"},
        {"en": "I am going to…", "es": "Voy a…", "pt": "Eu vou para…", "fr": "Je vais à…", "de": "Ich werde nach …"},
        {"en": "I want to…", "es": "Quiero…", "pt": "Eu quero…", "fr": "Je veux…", "de": "Ich möchte…"},
        {"en": "I have to…", "es": "Tengo que…", "pt": "Eu tenho que…", "fr": "Je dois…", "de": "Ich muss…"},
        {"en": "Maybe later", "es": "Tal vez más tarde", "pt": "Talvez mais tarde", "fr": "Peut-être plus tard", "de": "Vielleicht später"},
        {"en": "Let's meet tomorrow", "es": "Vamos a encontrarnos mañana", "pt": "Vamos nos encontrar amanhã", "fr": "Rencontrons-nous demain", "de": "Lass uns morgen treffen"},
        {"en": "What time should we meet?", "es": "¿A qué hora nos encontramos?", "pt": "A que horas nos encontramos?", "fr": "À quelle heure devrions-nous nous rencontrer ?", "de": "Um wie viel Uhr sollen wir uns treffen?"}
    ],
    "Health & Medical Situations": [
        {"en": "I don't feel well", "es": "No me siento bien", "pt": "Não me sinto bem", "fr": "Je ne me sens pas bien", "de": "Mir geht es nicht gut"},
        {"en": "I have a headache", "es": "Tengo dolor de cabeza", "pt": "Estou com dor de cabeça", "fr": "J'ai mal à la tête", "de": "Ich habe Kopfschmerzen"},
        {"en": "My stomach hurts", "es": "Me duele el estómago", "pt": "Meu estômago dói", "fr": "J'ai mal au ventre", "de": "Mein Magen tut weh"},
        {"en": "I have a fever", "es": "Tengo fiebre", "pt": "Estou com febre", "fr": "J'ai de la fièvre", "de": "Ich habe Fieber"},
        {"en": "I feel dizzy", "es": "Me siento mareado/a", "pt": "Estou tonto/a", "fr": "J'ai des vertiges", "de": "Mir ist schwindelig"},
        {"en": "I need a doctor", "es": "Necesito un médico", "pt": "Preciso de um médico", "fr": "J'ai besoin d'un médecin", "de": "Ich brauche einen Arzt"},
        {"en": "Is there a pharmacy nearby?", "es": "¿Hay una farmacia cerca?", "pt": "Tem uma farmácia por perto?", "fr": "Y a-t-il une pharmacie à proximité ?", "de": "Gibt es eine Apotheke in der Nähe?"},
        {"en": "I'm allergic to…", "es": "Soy alérgico/a a…", "pt": "Sou alérgico/a a…", "fr": "Je suis allergique à…", "de": "Ich bin allergisch gegen…"},
        {"en": "I need medicine", "es": "Necesito medicina", "pt": "Preciso de remédio", "fr": "J'ai besoin de médicaments", "de": "Ich brauche Medizin"},
        {"en": "It's an emergency", "es": "Es una emergencia", "pt": "É uma emergência", "fr": "C'est une urgence", "de": "Es ist ein Notfall"}
    ],
    "Technology & Internet": [
        {"en": "Do you have Wi-Fi?", "es": "¿Tienes Wi-Fi?", "pt": "Você tem Wi-Fi?", "fr": "Avez-vous du Wi-Fi ?", "de": "Haben Sie WLAN?"},
        {"en": "What's the Wi-Fi password?", "es": "¿Cuál es la contraseña del Wi-Fi?", "pt": "Qual é a senha do Wi-Fi?", "fr": "Quel est le mot de passe du Wi-Fi ?", "de": "Was ist das WLAN-Passwort?"},
        {"en": "My phone is out of battery", "es": "Mi teléfono está sin batería", "pt": "Meu celular está sem bateria", "fr": "Mon téléphone est déchargé", "de": "Mein Handy ist leer"},
        {"en": "I need a charger", "es": "Necesito un cargador", "pt": "Preciso de um carregador", "fr": "J'ai besoin d'un chargeur", "de": "Ich brauche ein Ladegerät"},
        {"en": "Where can I charge my phone?", "es": "¿Dónde puedo cargar mi teléfono?", "pt": "Onde posso carregar meu celular?", "fr": "Où puis-je charger mon téléphone ?", "de": "Wo kann ich mein Handy aufladen?"},
        {"en": "I can't connect to the internet", "es": "No puedo conectarme a Internet", "pt": "Não consigo me conectar à internet", "fr": "Je ne peux pas me connecter à Internet", "de": "Ich kann keine Verbindung zum Internet herstellen"},
        {"en": "I need to make a call", "es": "Necesito hacer una llamada", "pt": "Preciso fazer uma ligação", "fr": "Je dois passer un appel", "de": "Ich muss einen Anruf tätigen"},
        {"en": "Do you have an outlet?", "es": "¿Tienes un enchufe?", "pt": "Você tem uma tomada?", "fr": "Avez-vous une prise ?", "de": "Haben Sie eine Steckdose?"},
        {"en": "My phone isn't working", "es": "Mi teléfono no funciona", "pt": "Meu celular não está funcionando", "fr": "Mon téléphone ne fonctionne pas", "de": "Mein Handy funktioniert nicht"},
        {"en": "Can I use your phone?", "es": "¿Puedo usar tu teléfono?", "pt": "Posso usar seu telefone?", "fr": "Puis-je utiliser votre téléphone ?", "de": "Kann ich Ihr Telefon benutzen?"}
    ],
    "Handling Money & Banking": [
        {"en": "Where is the nearest ATM?", "es": "¿Dónde está el cajero automático más cercano?", "pt": "Onde fica o caixa eletrônico mais próximo?", "fr": "Où est le distributeur le plus proche ?", "de": "Wo ist der nächste Geldautomat?"},
        {"en": "I need to withdraw money", "es": "Necesito sacar dinero", "pt": "Preciso sacar dinheiro", "fr": "J'ai besoin de retirer de l'argent", "de": "Ich muss Geld abheben"},
        {"en": "Do you accept credit cards?", "es": "¿Aceptan tarjetas de crédito?", "pt": "Vocês aceitam cartão de crédito?", "fr": "Acceptez-vous les cartes de crédit ?", "de": "Akzeptieren Sie Kreditkarten?"},
        {"en": "Can I pay with cash?", "es": "¿Puedo pagar en efectivo?", "pt": "Posso pagar em dinheiro?", "fr": "Puis-je payer en espèces ?", "de": "Kann ich bar bezahlen?"},
        {"en": "I need to exchange money", "es": "Necesito cambiar dinero", "pt": "Preciso trocar dinheiro", "fr": "J'ai besoin de changer de l'argent", "de": "Ich muss Geld wechseln"},
        {"en": "What is the exchange rate?", "es": "¿Cuál es la tasa de cambio?", "pt": "Qual é a taxa de câmbio?", "fr": "Quel est le taux de change ?", "de": "Wie ist der Wechselkurs?"},
        {"en": "I lost my wallet", "es": "Perdí mi cartera", "pt": "Perdi minha carteira", "fr": "J'ai perdu mon portefeuille", "de": "Ich habe meine Geldbörse verloren"},
        {"en": "Someone stole my money", "es": "Alguien robó mi dinero", "pt": "Alguém roubou meu dinheiro", "fr": "Quelqu'un a volé mon argent", "de": "Jemand hat mein Geld gestohlen"},
        {"en": "My card isn't working", "es": "Mi tarjeta no funciona", "pt": "Meu cartão não está funcionando", "fr": "Ma carte ne fonctionne pas", "de": "Meine Karte funktioniert nicht"},
        {"en": "I need to go to the bank", "es": "Necesito ir al banco", "pt": "Preciso ir ao banco", "fr": "Je dois aller à la banque", "de": "Ich muss zur Bank gehen"}
    ],
    "Dealing with Authorities & Emergencies": [
        {"en": "I need help", "es": "Necesito ayuda", "pt": "Preciso de ajuda", "fr": "J'ai besoin d'aide", "de": "Ich brauche Hilfe"},
        {"en": "I need to report a crime", "es": "Necesito reportar un delito", "pt": "Preciso denunciar um crime", "fr": "Je dois signaler un crime", "de": "Ich muss ein Verbrechen melden"},
        {"en": "My passport was stolen", "es": "Me robaron el pasaporte", "pt": "Roubaram meu passaporte", "fr": "Mon passeport a été volé", "de": "Mein Pass wurde gestohlen"},
        {"en": "Where is the nearest police station?", "es": "¿Dónde está la comisaría más cercana?", "pt": "Onde fica a delegacia mais próxima?", "fr": "Où est le poste de police le plus proche ?", "de": "Wo ist die nächste Polizeistation?"},
        {"en": "I was attacked", "es": "Me atacaron", "pt": "Fui atacado/a", "fr": "J'ai été attaqué(e)", "de": "Ich wurde angegriffen"},
        {"en": "I need to contact my embassy", "es": "Necesito contactar con mi embajada", "pt": "Preciso entrar em contato com minha embaixada", "fr": "J'ai besoin de contacter mon ambassade", "de": "Ich muss meine Botschaft kontaktieren"},
        {"en": "Call the police", "es": "Llame a la policía", "pt": "Chame a polícia", "fr": "Appelez la police", "de": "Rufen Sie die Polizei"},
        {"en": "Call an ambulance", "es": "Llame una ambulancia", "pt": "Chame una ambulância", "fr": "Appelez une ambulance", "de": "Rufen Sie einen Krankenwagen"},
        {"en": "Is this area safe?", "es": "¿Es segura esta zona?", "pt": "Esta área é segura?", "fr": "Cette zone est-elle sûre ?", "de": "Ist dieses Gebiet sicher?"},
        {"en": "I am lost", "es": "Estoy perdido/a", "pt": "Estou perdido/a", "fr": "Je suis perdu(e)", "de": "Ich habe mich verirrt"}
    ],
    "Giving Compliments": [
        {"en": "You have a great smile", "es": "Tienes una gran sonrisa", "pt": "Você tem um lindo sorriso", "fr": "Tu as un beau sourire", "de": "Du hast ein tolles Lächeln"},
        {"en": "I love your style", "es": "Me encanta tu estilo", "pt": "Eu adoro seu estilo", "fr": "J'adore ton style", "de": "Ich liebe deinen Stil"},
        {"en": "You're very kind", "es": "Eres muy amable", "pt": "Você é muito gentil", "fr": "Tu es très gentil(le)", "de": "Du bist sehr freundlich"},
        {"en": "You're very funny", "es": "Eres muy gracioso/a", "pt": "Você é muito engraçado/a", "fr": "Tu es très drôle", "de": "Du bist sehr lustig"},
        {"en": "You have beautiful eyes", "es": "Tienes ojos hermosos", "pt": "Você tem olhos lindos", "fr": "Tu as de beaux yeux", "de": "Du hast schöne Augen"},
        {"en": "You're very talented", "es": "Eres muy talentoso/a", "pt": "Você é muito talentoso/a", "fr": "Tu es très talentueux/talentueuse", "de": "Du bist sehr talentiert"},
        {"en": "You have a great personality", "es": "Tienes una gran personalidad", "pt": "Você tem uma ótima personalidade", "fr": "Tu as une super personnalité", "de": "Du hast eine großartige Persönlichkeit"},
        {"en": "You're very interesting", "es": "Eres muy interesante", "pt": "Você é muito interesante", "fr": "Tu es très intéressant(e)", "de": "Du bist sehr interessant"},
        {"en": "I enjoy talking to you", "es": "Disfruto hablar contigo", "pt": "Gosto de conversar com você", "fr": "J'aime parler avec toi", "de": "Ich unterhalte mich gerne mit dir"},
        {"en": "You make me happy", "es": "Me haces feliz", "pt": "Você me faz feliz", "fr": "Tu me rends heureux/heureuse", "de": "Du machst mich glücklich"}
    ],
    "Common Expressions & Idioms": [
        {"en": "It's not a big deal", "es": "No es gran cosa", "pt": "Não é nada demais", "fr": "Ce n'est pas grave", "de": "Es ist keine große Sache"},
        {"en": "Don't worry", "es": "No te preocupes", "pt": "Não se preocupe", "fr": "Ne t'inquiète pas", "de": "Keine Sorge"},
        {"en": "It's up to you", "es": "Depende de ti", "pt": "Você que sabe", "fr": "C'est à toi de décider", "de": "Es liegt an dir"},
        {"en": "Take your time", "es": "Tómate tu tiempo", "pt": "Fique à vontade", "fr": "Prends ton temps", "de": "Lass dir Zeit"},
        {"en": "I don't believe it!", "es": "¡No lo creo!", "pt": "Não acredito!", "fr": "Je n'y crois pas !", "de": "Ich glaube es nicht!"},
        {"en": "That's amazing!", "es": "¡Eso es increíble!", "pt": "Isso é incrível!", "fr": "C'est incroyable !", "de": "Das ist erstaunlich!"},
        {"en": "Let's go for it!", "es": "¡Vamos a por ello!", "pt": "Vamos nessa!", "fr": "Allons-y !", "de": "Lass es uns machen!"},
        {"en": "It's my turn", "es": "Es mi turno", "pt": "É a minha vez", "fr": "C'est à moi", "de": "Ich bin dran"},
        {"en": "I changed my mind", "es": "Cambié de opinión", "pt": "Mudei de ideia", "fr": "J'ai changé d'avis", "de": "Ich habe meine Meinung geändert"},
        {"en": "That's how life is", "es": "Así es la vida", "pt": "Assim é a vida", "fr": "C'est comme ça la vie", "de": "So ist das Leben"}
    ]
}

# Day 5: Advanced Conversational Phrases, Cultural Expressions & Slang, Asking for Clarification, Handling Travel Issues, Talking About Experiences, Social Situations & Networking, Fluent Conversations & Transitions, Solving Problems & Apologizing
day5_phrases = {
    "Advanced Conversational Phrases": [
        {"en": "What do you think about this?", "es": "¿Qué piensas de esto?", "pt": "O que você acha disso?", "fr": "Qu'en penses-tu ?", "de": "Was denkst du darüber?"},
        {"en": "That makes sense", "es": "Eso tiene sentido", "pt": "Isso faz sentido", "fr": "Ça a du sens", "de": "Das macht Sinn"},
        {"en": "I totally agree", "es": "Estoy totalmente de acuerdo", "pt": "Eu concordo totalmente", "fr": "Je suis tout à fait d'accord", "de": "Ich stimme völlig zu"},
        {"en": "I don't agree", "es": "No estoy de acuerdo", "pt": "Eu não concordo", "fr": "Je ne suis pas d'accord", "de": "Ich stimme nicht zu"},
        {"en": "In my opinion…", "es": "En mi opinión…", "pt": "Na minha opinião…", "fr": "À mon avis…", "de": "Meiner Meinung nach…"},
        {"en": "To be honest…", "es": "Para ser honesto/a…", "pt": "Para ser sincero/a…", "fr": "Pour être honnête…", "de": "Um ehrlich zu sein…"},
        {"en": "That depends", "es": "Eso depende", "pt": "Isso depende", "fr": "Cela dépend", "de": "Das kommt darauf an"},
        {"en": "I didn't expect that", "es": "No esperaba eso", "pt": "Eu não esperava isso", "fr": "Je ne m'y attendais pas", "de": "Das habe ich nicht erwartet"},
        {"en": "What a surprise!", "es": "¡Qué sorpresa!", "pt": "Que surpresa!", "fr": "Quelle surprise !", "de": "Was für eine Überraschung!"},
        {"en": "That's interesting", "es": "Eso es interesante", "pt": "Isso é interesante", "fr": "C'est intéressant", "de": "Das ist interessant"}
    ],
    "Cultural Expressions & Slang": [
        {"en": "What's up?", "es": "¿Qué tal? / ¿Qué onda?", "pt": "E aí? / Beleza?", "fr": "Quoi de neuf ?", "de": "Was geht?"},
        {"en": "No worries", "es": "No pasa nada", "pt": "Sem problema", "fr": "Pas de soucis", "de": "Kein Problem"},
        {"en": "Cool!", "es": "¡Qué genial!", "pt": "Que legal!", "fr": "Cool !", "de": "Cool!"},
        {"en": "Let's do it!", "es": "¡Vamos a hacerlo!", "pt": "Bora lá!", "fr": "Faisons-le !", "de": "Lass es uns tun!"},
        {"en": "I'm kidding", "es": "Estoy bromeando", "pt": "Estou brincando", "fr": "Je plaisante", "de": "Ich mache nur Spaß"},
        {"en": "It's crazy!", "es": "¡Es una locura!", "pt": "É uma loucura!", "fr": "C'est fou !", "de": "Das ist verrückt!"},
        {"en": "That's awesome!", "es": "¡Es increíble!", "pt": "Isso é demais!", "fr": "C'est génial !", "de": "Das ist toll!"},
        {"en": "I'm broke", "es": "Estoy sin dinero", "pt": "Estou sem grana", "fr": "Je suis fauché(e)", "de": "Ich bin pleite"},
        {"en": "Just chilling", "es": "Solo relajando", "pt": "Só de boa", "fr": "Je me détends", "de": "Ich chille"},
        {"en": "I had a blast", "es": "Me lo pasé genial", "pt": "Me diverti muito", "fr": "Je me suis éclaté(e)", "de": "Ich hatte viel Spaß"}
    ],
    "Asking for Clarification": [
        {"en": "Can you say that again?", "es": "¿Puedes repetir eso?", "pt": "Você pode repetir isso?", "fr": "Peux-tu répéter ?", "de": "Kannst du das nochmal sagen?"},
        {"en": "Could you speak slower?", "es": "¿Puedes hablar más despacio?", "pt": "Você pode falar mais devagar?", "fr": "Peux-tu parler plus lentement ?", "de": "Kannst du langsamer sprechen?"},
        {"en": "What does that mean?", "es": "¿Qué significa eso?", "pt": "O que isso significa?", "fr": "Qu'est-ce que cela signifie ?", "de": "Was bedeutet das?"},
        {"en": "I don't understand", "es": "No entiendo", "pt": "Não entendo", "fr": "Je ne comprends pas", "de": "Ich verstehe nicht"},
        {"en": "Can you write it down?", "es": "¿Puedes escribirlo?", "pt": "Você pode escrever isso?", "fr": "Peux-tu l'écrire ?", "de": "Kannst du es aufschreiben?"},
        {"en": "How do you say this in Spanish/Portuguese?", "es": "¿Cómo se dice esto en español/portugués?", "pt": "Como se diz isso em espanhol/português?", "fr": "Comment dit-on cela en espagnol/portugais ?", "de": "Wie sagt man das auf Spanisch/Portugiesisch?"},
        {"en": "I need more practice", "es": "Necesito más práctica", "pt": "Preciso praticar mais", "fr": "J'ai besoin de plus de pratique", "de": "Ich brauche mehr Übung"},
        {"en": "That's hard to pronounce", "es": "Es difícil de pronunciar", "pt": "Isso é difícil de pronunciar", "fr": "C'est difficile à prononcer", "de": "Das ist schwer auszusprechen"},
        {"en": "I'm still learning", "es": "Todavía estoy aprendiendo", "pt": "Ainda estou aprendendo", "fr": "J'apprends encore", "de": "Ich lerne noch"},
        {"en": "Let me think…", "es": "Déjame pensar…", "pt": "Deixe-me pensar…", "fr": "Laisse-moi réfléchir…", "de": "Lass mich nachdenken…"}
    ],
    "Handling Travel Issues": [
        {"en": "My flight was canceled", "es": "Mi vuelo fue cancelado", "pt": "Meu voo foi cancelado", "fr": "Mon vol a été annulé", "de": "Mein Flug wurde gestrichen"},
        {"en": "My luggage is lost", "es": "Mi equipaje está perdido", "pt": "Minha bagagem está perdida", "fr": "Mes bagages sont perdus", "de": "Mein Gepäck ist verloren"},
        {"en": "I missed my flight", "es": "Perdí mi vuelo", "pt": "Perdi meu voo", "fr": "J'ai raté mon vol", "de": "Ich habe meinen Flug verpasst"},
        {"en": "Where is my gate?", "es": "¿Dónde está mi puerta de embarque?", "pt": "Onde fica o meu portão de embarque?", "fr": "Où est ma porte ?", "de": "Wo ist mein Gate?"},
        {"en": "Can I change my ticket?", "es": "¿Puedo cambiar mi boleto?", "pt": "Posso trocar minha passagem?", "fr": "Puis-je changer mon billet ?", "de": "Kann ich mein Ticket ändern?"},
        {"en": "How long is the delay?", "es": "¿Cuánto dura el retraso?", "pt": "Quanto tempo de atraso?", "fr": "Combien de temps dure le retard ?", "de": "Wie lange ist die Verspätung?"},
        {"en": "I need a taxi", "es": "Necesito un taxi", "pt": "Preciso de um táxi", "fr": "J'ai besoin d'un taxi", "de": "Ich brauche ein Taxi"},
        {"en": "How much is the fare?", "es": "¿Cuánto cuesta la tarifa?", "pt": "Quanto custa a tarifa?", "fr": "Combien coûte la course ?", "de": "Wie viel kostet die Fahrt?"},
        {"en": "Do you have Uber here?", "es": "¿Tienen Uber aquí?", "pt": "Tem Uber aqui?", "fr": "Avez-vous Uber ici ?", "de": "Gibt es hier Uber?"},
        {"en": "I need a hotel for tonight", "es": "Necesito un hotel para esta noche", "pt": "Preciso de um hotel para esta noite", "fr": "J'ai besoin d'un hôtel pour ce soir", "de": "Ich brauche ein Hotel für heute Nacht"}
    ],
    "Talking About Experiences": [
        {"en": "I had an amazing time", "es": "Me lo pasé increíble", "pt": "Me diverti muito", "fr": "J'ai passé un moment incroyable", "de": "Ich hatte eine großartige Zeit"},
        {"en": "It was unforgettable", "es": "Fue inolvidable", "pt": "Foi inesquecível", "fr": "C'était inoubliable", "de": "Es war unvergesslich"},
        {"en": "I learned a lot", "es": "Aprendí mucho", "pt": "Aprendi muito", "fr": "J'ai beaucoup appris", "de": "Ich habe viel gelernt"},
        {"en": "I met great people", "es": "Conocí a gente increíble", "pt": "Conheci pessoas incríveis", "fr": "J'ai rencontré des gens formidables", "de": "Ich habe tolle Leute getroffen"},
        {"en": "I love this city", "es": "Me encanta esta ciudad", "pt": "Eu amo esta cidade", "fr": "J'adore cette ville", "de": "Ich liebe diese Stadt"},
        {"en": "The food was delicious", "es": "La comida estaba deliciosa", "pt": "A comida estava deliciosa", "fr": "La nourriture était délicieuse", "de": "Das Essen war köstlich"},
        {"en": "I want to come back", "es": "Quiero volver", "pt": "Quero voltar", "fr": "Je veux revenir", "de": "Ich möchte zurückkommen"},
        {"en": "I felt very welcome", "es": "Me sentí muy bienvenido/a", "pt": "Me senti muito bem-vindo/a", "fr": "Je me suis senti(e) très bien accueilli(e)", "de": "Ich fühlte mich sehr willkommen"},
        {"en": "The culture is fascinating", "es": "La cultura es fascinante", "pt": "A cultura é fascinante", "fr": "La culture est fascinante", "de": "Die Kultur ist faszinierend"},
        {"en": "It was a unique experience", "es": "Fue una experiencia única", "pt": "Foi uma experiência única", "fr": "C'était une expérience unique", "de": "Es war eine einzigartige Erfahrung"}
    ],
    "Social Situations & Networking": [
        {"en": "What do you do for a living?", "es": "¿A qué te dedicas?", "pt": "O que você faz da vida?", "fr": "Que fais-tu dans la vie ?", "de": "Was machst du beruflich?"},
        {"en": "I work in…", "es": "Trabajo en…", "pt": "Trabalho em…", "fr": "Je travaille dans…", "de": "Ich arbeite in…"},
        {"en": "That sounds interesting", "es": "Eso suena interesante", "pt": "Isso parece interessante", "fr": "Ça semble intéressant", "de": "Das klingt interessant"},
        {"en": "Do you have a business card?", "es": "¿Tienes una tarjeta de presentación?", "pt": "Você tem um cartão de visita?", "fr": "As-tu une carte de visite ?", "de": "Hast du eine Visitenkarte?"},
        {"en": "Let's keep in touch", "es": "Mantengámonos en contacto", "pt": "Vamos manter contato", "fr": "Restons en contact", "de": "Lass uns in Kontakt bleiben"},
        {"en": "Are you on LinkedIn?", "es": "¿Tienes LinkedIn?", "pt": "Você está no LinkedIn?", "fr": "Es-tu sur LinkedIn ?", "de": "Bist du auf LinkedIn?"},
        {"en": "I'm looking for opportunities", "es": "Estoy buscando oportunidades", "pt": "Estou buscando oportunidades", "fr": "Je cherche des opportunités", "de": "Ich suche nach Möglichkeiten"},
        {"en": "Do you have any recommendations?", "es": "¿Tienes alguna recomendación?", "pt": "Você tem alguma recomendação?", "fr": "As-tu des recommandations ?", "de": "Hast du Empfehlungen?"},
        {"en": "Let's collaborate", "es": "Colaboremos", "pt": "Vamos colaborar", "fr": "Collaborons", "de": "Lass uns zusammenarbeiten"},
        {"en": "It was great meeting you", "es": "Fue un placer conocerte", "pt": "Foi um prazer te conhecer", "fr": "Ce fut un plaisir de te rencontrer", "de": "Es war schön, dich kennenzulernen"}
    ],
    "Fluent Conversations & Transitions": [
        {"en": "By the way…", "es": "Por cierto…", "pt": "Aliás…", "fr": "Au fait…", "de": "Übrigens…"},
        {"en": "As I was saying…", "es": "Como decía…", "pt": "Como eu estava dizendo…", "fr": "Comme je disais…", "de": "Wie ich sagte…"},
        {"en": "That reminds me…", "es": "Eso me recuerda…", "pt": "Isso me lembra…", "fr": "Ça me rappelle…", "de": "Das erinnert mich daran…"},
        {"en": "Speaking of that…", "es": "Hablando de eso…", "pt": "Falando nisso…", "fr": "En parlant de cela…", "de": "Apropos…"},
        {"en": "Anyway…", "es": "De todos modos…", "pt": "Enfim…", "fr": "Bref…", "de": "Jedenfalls…"},
        {"en": "I was about to say…", "es": "Estaba a punto de decir…", "pt": "Eu estava prestes a dizer…", "fr": "J'étais sur le point de dire…", "de": "Ich wollte gerade sagen…"},
        {"en": "You know what I mean?", "es": "¿Sabes a qué me refiero?", "pt": "Sabe o que quero dizer?", "fr": "Tu vois ce que je veux dire ?", "de": "Weißt du, was ich meine?"},
        {"en": "Let's change the subject", "es": "Cambiemos de tema", "pt": "Vamos mudar de assunto", "fr": "Changeons de sujet", "de": "Lass uns das Thema wechseln"},
        {"en": "I completely forgot!", "es": "¡Se me olvidó por completo!", "pt": "Eu me esqueci completamente!", "fr": "J'ai complètement oublié !", "de": "Ich habe es völlig vergessen!"},
        {"en": "It slipped my mind", "es": "Se me pasó por alto", "pt": "Me fugiu da memória", "fr": "Ça m'a échappé", "de": "Es ist mir entfallen"}
    ],
    "Solving Problems & Apologizing": [
        {"en": "I made a mistake", "es": "Cometí un error", "pt": "Cometi um erro", "fr": "J'ai fait une erreur", "de": "Ich habe einen Fehler gemacht"},
        {"en": "I didn't mean to", "es": "No fue mi intención", "pt": "Não foi minha intenção", "fr": "Ce n'était pas intentionnel", "de": "Ich wollte das nicht"},
        {"en": "I'm really sorry", "es": "Lo siento mucho", "pt": "Sinto muito", "fr": "Je suis vraiment désolé", "de": "Es tut mir wirklich leid"},
        {"en": "Please forgive me", "es": "Por favor, perdóname", "pt": "Por favor, me perdoe", "fr": "S'il te plaît, pardonne-moi", "de": "Bitte vergib mir"},
        {"en": "Let's fix this", "es": "Arreglemos esto", "pt": "Vamos resolver isso", "fr": "Réglons cela", "de": "Lass uns das beheben"},
        {"en": "I take responsibility", "es": "Me hago responsable", "pt": "Eu assumo a responsabilidade", "fr": "J'assume la responsabilité", "de": "Ich übernehme die Verantwortung"},
        {"en": "How can I make it up to you?", "es": "¿Cómo puedo compensarte?", "pt": "Como posso compensar isso?", "fr": "Comment puis-je me faire pardonner ?", "de": "Wie kann ich es wiedergutmachen?"},
        {"en": "It won't happen again", "es": "No volverá a suceder", "pt": "Não vai acontecer de novo", "fr": "Ça ne se reproduira plus", "de": "Es wird nicht wieder vorkommen"},
        {"en": "Thank you for your patience", "es": "Gracias por tu paciencia", "pt": "Obrigado/a pela paciência", "fr": "Merci pour ta patience", "de": "Danke für deine Geduld"},
        {"en": "I appreciate your understanding", "es": "Aprecio tu comprensión", "pt": "Agradeço sua compreensão", "fr": "J'apprécie ta compréhension", "de": "Ich schätze dein Verständnis"}
    ]
}

# Day 6: Telling Stories & Sharing Experiences, Debating & Expressing Opinions, Making Jokes & Being Playful, Describing People & Places, Describing Feelings & Emotions, Advanced Travel Phrases, Expressing Preferences & Comparing
day6_phrases = {
    "Telling Stories & Sharing Experiences": [
        {"en": "Let me tell you a story", "es": "Déjame contarte una historia", "pt": "Deixe-me te contar uma história", "fr": "Laisse-moi te raconter une histoire", "de": "Lass mich dir eine Geschichte erzählen"},
        {"en": "This happened to me once", "es": "Esto me pasó una vez", "pt": "Isso aconteceu comigo uma vez", "fr": "Cela m'est arrivé une fois", "de": "Das ist mir einmal passiert"},
        {"en": "You won't believe what happened", "es": "No vas a creer lo que pasó", "pt": "Você não vai acreditar no que aconteceu", "fr": "Tu ne croiras pas ce qui s'est passé", "de": "Du wirst nicht glauben, was passiert ist"},
        {"en": "It was so funny!", "es": "¡Fue tan gracioso!", "pt": "Foi tão engraçado!", "fr": "C'était tellement drôle !", "de": "Es war so lustig!"},
        {"en": "It was a crazy experience", "es": "Fue una experiencia loca", "pt": "Foi uma experiência louca", "fr": "C'était une expérience folle", "de": "Es war eine verrückte Erfahrung"},
        {"en": "And then…", "es": "Y luego…", "pt": "E então…", "fr": "Et puis…", "de": "Und dann…"},
        {"en": "The best part was…", "es": "La mejor parte fue…", "pt": "A melhor parte foi…", "fr": "La meilleure partie était…", "de": "Der beste Teil war…"},
        {"en": "In the end…", "es": "Al final…", "pt": "No final…", "fr": "Finalement…", "de": "Am Ende…"},
        {"en": "I was so embarrassed", "es": "Me dio mucha vergüenza", "pt": "Fiquei muito envergonhado/a", "fr": "J'étais tellement embarrassé(e)", "de": "Ich war so beschämt"},
        {"en": "It was unforgettable", "es": "Fue inolvidable", "pt": "Foi inesquecível", "fr": "C'était inoubliable", "de": "Es war unvergesslich"}
    ],
    "Debating & Expressing Opinions": [
        {"en": "I think that…", "es": "Creo que…", "pt": "Eu acho que…", "fr": "Je pense que…", "de": "Ich denke, dass…"},
        {"en": "In my opinion…", "es": "En mi opinión…", "pt": "Na minha opinião…", "fr": "À mon avis…", "de": "Meiner Meinung nach…"},
        {"en": "I see your point", "es": "Veo tu punto", "pt": "Entendo o seu ponto", "fr": "Je comprends ton point de vue", "de": "Ich verstehe deinen Standpunkt"},
        {"en": "That's a good argument", "es": "Es un buen argumento", "pt": "Esse é um bom argumento", "fr": "C'est un bon argument", "de": "Das ist ein gutes Argument"},
        {"en": "I completely disagree", "es": "No estoy de acuerdo en absoluto", "pt": "Eu discordo completamente", "fr": "Je suis complètement en désaccord", "de": "Ich stimme vollkommen nicht zu"},
        {"en": "I see it differently", "es": "Lo veo de otra manera", "pt": "Eu vejo de outra forma", "fr": "Je le vois différemment", "de": "Ich sehe es anders"},
        {"en": "That's not necessarily true", "es": "Eso no es necesariamente cierto", "pt": "Isso não é necessariamente verdade", "fr": "Ce n'est pas nécessairement vrai", "de": "Das ist nicht unbedingt wahr"},
        {"en": "Can I add something?", "es": "¿Puedo agregar algo?", "pt": "Posso acrescentar algo?", "fr": "Puis-je ajouter quelque chose ?", "de": "Kann ich etwas hinzufügen?"},
        {"en": "Let's agree to disagree", "es": "Acordemos en no estar de acuerdo", "pt": "Vamos concordar em discordar", "fr": "Acceptons de ne pas être d'accord", "de": "Lass uns zustimmen, dass wir nicht übereinstimmen"},
        {"en": "Let's keep an open mind", "es": "Mantengamos la mente abierta", "pt": "Vamos manter a mente aberta", "fr": "Gardons l'esprit ouvert", "de": "Lass uns offen bleiben"}
    ],
    "Making Jokes & Being Playful": [
        {"en": "Just kidding!", "es": "¡Es broma!", "pt": "Tô brincando!", "fr": "Je plaisante !", "de": "Nur Spaß!"},
        {"en": "That was a good one!", "es": "¡Esa fue buena!", "pt": "Essa foi boa!", "fr": "C'était une bonne blague !", "de": "Das war ein guter Witz!"},
        {"en": "You're so funny!", "es": "¡Eres muy gracioso/a!", "pt": "Você é muito engraçado/a!", "fr": "Tu es tellement drôle !", "de": "Du bist so lustig!"},
        {"en": "I can't stop laughing", "es": "No puedo parar de reír", "pt": "Não consigo parar de rir", "fr": "Je n'arrête pas de rire", "de": "Ich kann nicht aufhören zu lachen"},
        {"en": "That joke was terrible!", "es": "¡Ese chiste fue terrible!", "pt": "Essa piada foi péssima!", "fr": "Cette blague était terrible !", "de": "Dieser Witz war schrecklich!"},
        {"en": "You have a great sense of humor", "es": "Tienes un gran sentido del humor", "pt": "Você tem um ótimo senso de humor", "fr": "Tu as un super sens de l'humour", "de": "Du hast einen großartigen Sinn für Humor"},
        {"en": "That's hilarious!", "es": "¡Eso es divertidísimo!", "pt": "Isso é hilário!", "fr": "C'est hilarant !", "de": "Das ist urkomisch!"},
        {"en": "I love silly jokes", "es": "Me encantan los chistes tontos", "pt": "Eu adoro piadas bobas", "fr": "J'adore les blagues idiotes", "de": "Ich liebe alberne Witze"},
        {"en": "You're making me laugh", "es": "Me estás haciendo reír", "pt": "Você está me fazendo rir", "fr": "Tu me fais rire", "de": "Du bringst mich zum Lachen"},
        {"en": "Laughter is the best medicine", "es": "La risa es el mejor remedio", "pt": "O riso é o melhor remédio", "fr": "Le rire est le meilleur remède", "de": "Lachen ist die beste Medizin"}
    ],
    "Describing People & Places": [
        {"en": "He/she is very kind", "es": "Es muy amable", "pt": "Ele/ela é muito gentil", "fr": "Il/elle est très gentil(le)", "de": "Er/sie ist sehr freundlich"},
        {"en": "They are very interesting", "es": "Son muy interesantes", "pt": "Eles/elas são muito interesantes", "fr": "Ils/elles sont très intéressants", "de": "Sie sind sehr interessant"},
        {"en": "This place is amazing", "es": "Este lugar es increíble", "pt": "Este lugar é incrível", "fr": "Cet endroit est incroyable", "de": "Dieser Ort ist erstaunlich"},
        {"en": "The city is beautiful", "es": "La ciudad es hermosa", "pt": "A cidade é linda", "fr": "La ville est belle", "de": "Die Stadt ist schön"},
        {"en": "It's very peaceful here", "es": "Es muy tranquilo aquí", "pt": "É muito tranquilo aqui", "fr": "C'est très paisible ici", "de": "Es ist hier sehr friedlich"},
        {"en": "The people are so friendly", "es": "La gente es muy amigable", "pt": "As pessoas são muito amigáveis", "fr": "Les gens sont si sympathiques", "de": "Die Leute sind so freundlich"},
        {"en": "The food is delicious", "es": "La comida es deliciosa", "pt": "A comida é deliciosa", "fr": "La nourriture est délicieuse", "de": "Das Essen ist köstlich"},
        {"en": "The architecture is stunning", "es": "La arquitectura es impresionante", "pt": "A arquitetura é impressionante", "fr": "L'architecture est époustouflante", "de": "Die Architektur ist atemberaubend"},
        {"en": "It's a vibrant place", "es": "Es un lugar vibrante", "pt": "É um lugar vibrante", "fr": "C'est un endroit vibrant", "de": "Es ist ein lebendiger Ort"},
        {"en": "I feel at home here", "es": "Me siento como en casa aquí", "pt": "Me sinto em casa aqui", "fr": "Je me sens chez moi ici", "de": "Ich fühle mich hier zu Hause"}
    ],
    "Describing Feelings & Emotions": [
        {"en": "I feel so happy", "es": "Me siento tan feliz", "pt": "Me sinto tão feliz", "fr": "Je me sens si heureux/heureuse", "de": "Ich fühle mich so glücklich"},
        {"en": "I'm really excited", "es": "Estoy muy emocionado/a", "pt": "Estou muito animado/a", "fr": "Je suis vraiment excité(e)", "de": "Ich bin wirklich aufgeregt"},
        {"en": "I'm a little nervous", "es": "Estoy un poco nervioso/a", "pt": "Estou um pouco nervoso/a", "fr": "Je suis un peu nerveux/nerveuse", "de": "Ich bin ein wenig nervös"},
        {"en": "I feel grateful", "es": "Me siento agradecido/a", "pt": "Me sinto grato/a", "fr": "Je me sens reconnaissant(e)", "de": "Ich bin dankbar"},
        {"en": "I'm frustrated", "es": "Estoy frustrado/a", "pt": "Estou frustrado/a", "fr": "Je suis frustré(e)", "de": "Ich bin frustriert"},
        {"en": "I'm overwhelmed", "es": "Estoy abrumado/a", "pt": "Estou sobrecarregado/a", "fr": "Je suis submergé(e)", "de": "Ich bin überwältigt"},
        {"en": "I'm feeling nostalgic", "es": "Me siento nostálgico/a", "pt": "Estou me sentindo nostálgico/a", "fr": "Je me sens nostalgique", "de": "Ich fühle mich nostalgisch"},
        {"en": "I'm in a great mood", "es": "Estoy de muy buen humor", "pt": "Estou de ótimo humor", "fr": "Je suis de très bonne humeur", "de": "Ich bin gut gelaunt"},
        {"en": "I'm feeling down", "es": "Me siento deprimido/a", "pt": "Estou me sentindo triste", "fr": "Je me sens déprimé(e)", "de": "Ich fühle mich niedergeschlagen"},
        {"en": "That made my day!", "es": "¡Eso me alegró el día!", "pt": "Isso fez o meu dia!", "fr": "Ça a illuminé ma journée !", "de": "Das hat meinen Tag gemacht!"}
    ],
    "Advanced Travel Phrases": [
        {"en": "Can I get a window seat?", "es": "¿Puedo tener un asiento junto a la ventana?", "pt": "Posso pegar um assento na janela?", "fr": "Puis-je avoir un siège côté fenêtre ?", "de": "Kann ich einen Fensterplatz bekommen?"},
        {"en": "Is there a direct flight?", "es": "¿Hay un vuelo directo?", "pt": "Tem um voo direto?", "fr": "Y a-t-il un vol direct ?", "de": "Gibt es einen Direktflug?"},
        {"en": "I need to book a room", "es": "Necesito reservar una habitación", "pt": "Preciso reservar um quarto", "fr": "J'ai besoin de réserver une chambre", "de": "Ich muss ein Zimmer buchen"},
        {"en": "Do you have recommendations for places to visit?", "es": "¿Tienes recomendaciones de lugares para visitar?", "pt": "Você tem recomendações de lugares para visitar?", "fr": "Avez-vous des recommandations de lieux à visiter ?", "de": "Haben Sie Empfehlungen für sehenswerte Orte?"},
        {"en": "I want to explore the city", "es": "Quiero explorar la ciudad", "pt": "Quero explorar a cidade", "fr": "Je veux explorer la ville", "de": "Ich möchte die Stadt erkunden"},
        {"en": "Can I rent a car here?", "es": "¿Puedo alquilar un coche aquí?", "pt": "Posso alugar um carro aqui?", "fr": "Puis-je louer une voiture ici ?", "de": "Kann ich hier ein Auto mieten?"},
        {"en": "Where is the tourist office?", "es": "¿Dónde está la oficina de turismo?", "pt": "Onde fica o escritório de turismo?", "fr": "Où est l'office de tourisme ?", "de": "Wo ist das Fremdenverkehrsamt?"},
        {"en": "What's the best way to get around?", "es": "¿Cuál es la mejor manera de moverse?", "pt": "Qual é a melhor maneira de se locomover?", "fr": "Quel est le meilleur moyen de se déplacer ?", "de": "Was ist der beste Weg, sich fortzubewegen?"},
        {"en": "I'd like to try local food", "es": "Me gustaría probar la comida local", "pt": "Gostaria de experimentar a comida local", "fr": "J'aimerais goûter la cuisine locale", "de": "Ich möchte die lokale Küche probieren"},
        {"en": "Do you know any hidden gems?", "es": "¿Conoces algún lugar secreto?", "pt": "Você conhece algum lugar escondido?", "fr": "Connais-tu des perles cachées ?", "de": "Kennst du versteckte Schätze?"}
    ],
    "Expressing Preferences & Comparing": [
        {"en": "I prefer this one", "es": "Prefiero este/a", "pt": "Eu prefiro este/a", "fr": "Je préfère celui-ci/celle-ci", "de": "Ich bevorzuge dieses"},
        {"en": "I like both", "es": "Me gustan ambos/as", "pt": "Eu gosto de ambos/as", "fr": "J'aime les deux", "de": "Ich mag beide"},
        {"en": "This is better than that", "es": "Esto es mejor que eso", "pt": "Isso é melhor do que aquilo", "fr": "C'est mieux que ça", "de": "Das ist besser als das"},
        {"en": "This is my favorite", "es": "Este es mi favorito/a", "pt": "Esse é o meu favorito/a", "fr": "C'est mon préféré", "de": "Das ist mein Favorit"},
        {"en": "That's a tough choice", "es": "Es una elección difícil", "pt": "Essa é uma escolha difícil", "fr": "C'est un choix difficile", "de": "Das ist eine schwierige Wahl"},
        {"en": "I don't care", "es": "No me importa", "pt": "Eu não me importo", "fr": "Ça m'est égal", "de": "Es ist mir egal"},
        {"en": "It depends on the situation", "es": "Depende de la situación", "pt": "Depende da situação", "fr": "Cela dépend de la situation", "de": "Es kommt auf die Situation an"},
        {"en": "I like simple things", "es": "Me gustan las cosas simples", "pt": "Eu gosto de coisas simples", "fr": "J'aime les choses simples", "de": "Ich mag einfache Dinge"},
        {"en": "I enjoy being outdoors", "es": "Disfruto estar al aire libre", "pt": "Eu gosto de estar ao ar livre", "fr": "J'aime être en plein air", "de": "Ich genieße es, draußen zu sein"},
        {"en": "I love learning new things", "es": "Me encanta aprender cosas nuevas", "pt": "Eu adoro aprender coisas novas", "fr": "J'adore apprendre de nouvelles choses", "de": "Ich liebe es, neue Dinge zu lernen"}
    ]
}

# Day 7: Business & Professional Conversations, Negotiation & Deals, Idiomatic Expressions & Common Sayings, Advanced Emotional Expressions, Handling Formal Situations, Dealing with Difficult Situations, Deep Conversations & Personal Growth
day7_phrases = {
    "Business & Professional Conversations": [
        {"en": "What do you do for work?", "es": "¿A qué te dedicas?", "pt": "O que você faz da vida?", "fr": "Que fais-tu dans la vie ?", "de": "Was machst du beruflich?"},
        {"en": "I work in…", "es": "Trabajo en…", "pt": "Trabalho em…", "fr": "Je travaille dans…", "de": "Ich arbeite in…"},
        {"en": "I'm looking for a job", "es": "Estoy buscando trabajo", "pt": "Estou procurando emprego", "fr": "Je cherche un emploi", "de": "Ich suche einen Job"},
        {"en": "I have experience in…", "es": "Tengo experiencia en…", "pt": "Tenho experiência em…", "fr": "J'ai de l'expérience dans…", "de": "Ich habe Erfahrung in…"},
        {"en": "I'm interested in this position", "es": "Estoy interesado/a en este puesto", "pt": "Estou interessado/a nesta vaga", "fr": "Je suis intéressé(e) par ce poste", "de": "Ich bin an dieser Position interessiert"},
        {"en": "Could you send me more details?", "es": "¿Podría enviarme más detalles?", "pt": "Você poderia me enviar mais detalhes?", "fr": "Pourriez-vous m'envoyer plus de détails ?", "de": "Können Sie mir mehr Details schicken?"},
        {"en": "I'd like to schedule a meeting", "es": "Me gustaría agendar una reunión", "pt": "Gostaria de agendar uma reunião", "fr": "J'aimerais planifier une réunion", "de": "Ich würde gerne ein Treffen vereinbaren"},
        {"en": "Let's discuss the details", "es": "Hablemos de los detalles", "pt": "Vamos discutir os detalhes", "fr": "Discutons des détails", "de": "Lass uns die Details besprechen"},
        {"en": "I'll send you an email", "es": "Te enviaré un correo", "pt": "Vou te enviar um e-mail", "fr": "Je t'enverrai un e-mail", "de": "Ich schicke dir eine E-Mail"},
        {"en": "When are you available?", "es": "¿Cuándo estás disponible?", "pt": "Quando você está disponível?", "fr": "Quand es-tu disponible ?", "de": "Wann bist du verfügbar?"}
    ],
    "Negotiation & Deals": [
        {"en": "What's your best price?", "es": "¿Cuál es su mejor precio?", "pt": "Qual é o seu melhor preço?", "fr": "Quel est votre meilleur prix ?", "de": "Was ist Ihr bester Preis?"},
        {"en": "Can we negotiate?", "es": "¿Podemos negociar?", "pt": "Podemos negociar?", "fr": "Pouvons-nous négocier ?", "de": "Können wir verhandeln?"},
        {"en": "That's too expensive", "es": "Eso es demasiado caro", "pt": "Isso é muito caro", "fr": "C'est trop cher", "de": "Das ist zu teuer"},
        {"en": "I need a discount", "es": "Necesito un descuento", "pt": "Preciso de um desconto", "fr": "J'ai besoin d'une réduction", "de": "Ich brauche einen Rabatt"},
        {"en": "Let's make a deal", "es": "Hagamos un trato", "pt": "Vamos fechar um acordo", "fr": "Faisons un accord", "de": "Lass uns einen Deal machen"},
        {"en": "I need more time to decide", "es": "Necesito más tiempo para decidir", "pt": "Preciso de mais tempo para decidir", "fr": "J'ai besoin de plus de temps pour décider", "de": "Ich brauche mehr Zeit, um zu entscheiden"},
        {"en": "I need an invoice", "es": "Necesito una factura", "pt": "Preciso de uma nota fiscal", "fr": "J'ai besoin d'une facture", "de": "Ich brauche eine Rechnung"},
        {"en": "Can I pay in installments?", "es": "¿Puedo pagar en cuotas?", "pt": "Posso pagar em parcelas?", "fr": "Puis-je payer en plusieurs fois ?", "de": "Kann ich in Raten bezahlen?"},
        {"en": "I'd like to see other options", "es": "Me gustaría ver otras opciones", "pt": "Gostaria de ver outras opções", "fr": "J'aimerais voir d'autres options", "de": "Ich möchte andere Optionen sehen"},
        {"en": "It's a fair price", "es": "Es un precio justo", "pt": "É um preço justo", "fr": "C'est un prix raisonnable", "de": "Das ist ein fairer Preis"}
    ],
    "Idiomatic Expressions & Common Sayings": [
        {"en": "It's raining cats and dogs", "es": "Está lloviendo a cántaros", "pt": "Está chovendo canivetes", "fr": "Il pleut des cordes", "de": "Es regnet in Strömen"},
        {"en": "Don't judge a book by its cover", "es": "No juzgues un libro por su portada", "pt": "Não julgue o livro pela capa", "fr": "Il ne faut pas juger un livre à sa couverture", "de": "Beurteile ein Buch nicht nach seinem Einband"},
        {"en": "The early bird catches the worm", "es": "A quien madruga, Dios lo ayuda", "pt": "Deus ajuda quem cedo madruga", "fr": "L'avenir sourit à ceux qui se lèvent tôt", "de": "Der frühe Vogel fängt den Wurm"},
        {"en": "Actions speak louder than words", "es": "Los hechos valen más que las palabras", "pt": "As ações falam mais alto que as palavras", "fr": "Les actions parlent plus fort que les mots", "de": "Taten sagen mehr als Worte"},
        {"en": "Better late than never", "es": "Más vale tarde que nunca", "pt": "Antes tarde do que nunca", "fr": "Mieux vaut tard que jamais", "de": "Besser spät als nie"},
        {"en": "Easier said than done", "es": "Es más fácil decirlo que hacerlo", "pt": "É mais fácil falar do que fazer", "fr": "C'est plus facile à dire qu'à faire", "de": "Leichter gesagt als getan"},
        {"en": "A piece of cake", "es": "Es pan comido", "pt": "É moleza", "fr": "C'est du gâteau", "de": "Das ist ein Kinderspiel"},
        {"en": "Kill two birds with one stone", "es": "Matar dos pájaros de un tiro", "pt": "Matar dois coelhos com uma cajadada só", "fr": "Faire d'une pierre deux coups", "de": "Zwei Fliegen mit einer Klappe schlagen"},
        {"en": "The ball is in your court", "es": "La pelota está en tu tejado", "pt": "A bola está no seu campo", "fr": "La balle est dans ton camp", "de": "Der Ball liegt bei dir"},
        {"en": "Let bygones be bygones", "es": "Lo pasado, pasado está", "pt": "O que passou, passou", "fr": "Laisse le passé au passé", "de": "Was geschehen ist, ist geschehen"}
    ],
    "Advanced Emotional Expressions": [
        {"en": "I feel overwhelmed", "es": "Me siento abrumado/a", "pt": "Me sinto sobrecarregado/a", "fr": "Je me sens submergé(e)", "de": "Ich fühle mich überfordert"},
        {"en": "I need some space", "es": "Necesito un poco de espacio", "pt": "Preciso de mais espaço", "fr": "J'ai besoin d'espace", "de": "Ich brauche etwas Freiraum"},
        {"en": "I'm trying to stay positive", "es": "Estoy tratando de mantenerme positivo/a", "pt": "Estou tentando manter o pensamento positivo", "fr": "J'essaie de rester positif(ve)", "de": "Ich versuche, positiv zu bleiben"},
        {"en": "That really hurt my feelings", "es": "Eso realmente me lastimó", "pt": "Isso realmente me magoou", "fr": "Ça m'a vraiment blessé", "de": "Das hat mir wirklich wehgetan"},
        {"en": "I'm deeply grateful", "es": "Estoy profundamente agradecido/a", "pt": "Estou profundamente grato/a", "fr": "Je suis profondément reconnaissant(e)", "de": "Ich bin zutiefst dankbar"},
        {"en": "I'm feeling nostalgic", "es": "Me siento nostálgico/a", "pt": "Estou me sentindo nostálgico/a", "fr": "Je me sens nostalgique", "de": "Ich fühle mich nostalgisch"},
        {"en": "I need to clear my mind", "es": "Necesito aclarar mi mente", "pt": "Preciso limpar minha mente", "fr": "J'ai besoin de clarifier mon esprit", "de": "Ich muss meinen Geist klären"},
        {"en": "I have mixed feelings", "es": "Tengo sentimientos encontrados", "pt": "Tenho sentimentos mistos", "fr": "J'ai des sentiments mitigés", "de": "Ich habe gemischte Gefühle"},
        {"en": "I'm at a crossroads", "es": "Estoy en una encrucijada", "pt": "Estou em uma encruzilhada", "fr": "Je suis à un carrefour", "de": "Ich stehe an einem Scheideweg"},
        {"en": "I just want to be understood", "es": "Solo quiero ser comprendido/a", "pt": "Só quero ser compreendido/a", "fr": "Je veux juste être compris(e)", "de": "Ich möchte einfach verstanden werden"}
    ],
    "Handling Formal Situations": [
        {"en": "Excuse me, may I ask you something?", "es": "Disculpe, ¿puedo preguntarle algo?", "pt": "Com licença, posso te perguntar algo?", "fr": "Excusez-moi, puis-je vous demander quelque chose ?", "de": "Entschuldigen Sie, darf ich Sie etwas fragen?"},
        {"en": "Could you repeat that, please?", "es": "¿Podría repetir eso, por favor?", "pt": "Você poderia repetir isso, por favor?", "fr": "Pourriez-vous répéter, s'il vous plaît ?", "de": "Könnten Sie das bitte wiederholen?"},
        {"en": "I apologize for the misunderstanding", "es": "Me disculpo por el malentendido", "pt": "Peço desculpas pelo mal-entendido", "fr": "Je m'excuse pour le malentendu", "de": "Ich entschuldige mich für das Missverständnis"},
        {"en": "May I introduce myself?", "es": "¿Puedo presentarme?", "pt": "Posso me apresentar?", "fr": "Puis-je me présenter ?", "de": "Darf ich mich vorstellen?"},
        {"en": "Thank you for your time", "es": "Gracias por su tiempo", "pt": "Obrigado/a pelo seu tempo", "fr": "Merci pour votre temps", "de": "Danke für Ihre Zeit"},
        {"en": "I appreciate your help", "es": "Aprecio su ayuda", "pt": "Agradeço sua ajuda", "fr": "Je vous remercie pour votre aide", "de": "Ich schätze Ihre Hilfe"},
        {"en": "I hope to hear from you soon", "es": "Espero saber de usted pronto", "pt": "Espero receber notícias suas em breve", "fr": "J'espère avoir de vos nouvelles bientôt", "de": "Ich hoffe, bald von Ihnen zu hören"},
        {"en": "Please let me know if you need anything else", "es": "Por favor, avíseme si necesita algo más", "pt": "Por favor, me avise se precisar de algo mais", "fr": "Faites-moi savoir si vous avez besoin de quelque chose d'autre", "de": "Bitte lassen Sie mich wissen, wenn Sie noch etwas brauchen"},
        {"en": "It was a pleasure meeting you", "es": "Fue un placer conocerte", "pt": "Foi um prazer te conhecer", "fr": "Ce fut un plaisir de vous rencontrer", "de": "Es war mir ein Vergnügen, Sie kennenzulernen"},
        {"en": "I hope we can collaborate in the future", "es": "Espero que podamos colaborar en el futuro", "pt": "Espero que possamos colaborar no futuro", "fr": "J'espère que nous pourrons collaborer à l'avenir", "de": "Ich hoffe, wir können in Zukunft zusammenarbeiten"}
    ],
    "Dealing with Difficult Situations": [
        {"en": "This is a misunderstanding", "es": "Esto es un malentendido", "pt": "Isso é um mal-entendido", "fr": "C'est un malentendu", "de": "Das ist ein Missverständnis"},
        {"en": "I need to speak to the manager", "es": "Necesito hablar con el gerente", "pt": "Preciso falar com o gerente", "fr": "J'ai besoin de parler au responsable", "de": "Ich muss mit dem Manager sprechen"},
        {"en": "I need a solution now", "es": "Necesito una solución ahora", "pt": "Preciso de uma solução agora", "fr": "J'ai besoin d'une solution maintenant", "de": "Ich brauche sofort eine Lösung"},
        {"en": "This is unacceptable", "es": "Esto es inaceptable", "pt": "Isso é inaceitável", "fr": "C'est inacceptable", "de": "Das ist inakzeptabel"},
        {"en": "I feel disrespected", "es": "Me siento irrespetado/a", "pt": "Me sinto desrespeitado/a", "fr": "Je me sens irrespecté(e)", "de": "Ich fühle mich respektlos behandelt"},
        {"en": "I need to report this", "es": "Necesito reportar esto", "pt": "Preciso relatar isso", "fr": "Je dois signaler cela", "de": "Ich muss das melden"},
        {"en": "I would like a refund", "es": "Me gustaría un reembolso", "pt": "Gostaria de um reembolso", "fr": "Je voudrais un remboursement", "de": "Ich hätte gerne eine Rückerstattung"},
        {"en": "I won't accept this", "es": "No aceptaré esto", "pt": "Não vou aceitar isso", "fr": "Je n'accepterai pas cela", "de": "Ich werde das nicht akzeptieren"},
        {"en": "I expect better service", "es": "Espero un mejor servicio", "pt": "Espero um serviço melhor", "fr": "Je m'attends à un meilleur service", "de": "Ich erwarte besseren Service"},
        {"en": "Can we find a compromise?", "es": "¿Podemos encontrar un compromiso?", "pt": "Podemos chegar a um acordo?", "fr": "Pouvons-nous trouver un compromis ?", "de": "Können wir einen Kompromiss finden?"}
    ],
    "Deep Conversations & Personal Growth": [
        {"en": "What inspires you?", "es": "¿Qué te inspira?", "pt": "O que te inspira?", "fr": "Qu'est-ce qui t'inspire ?", "de": "Was inspiriert dich?"},
        {"en": "I've been thinking a lot lately", "es": "He estado pensando mucho últimamente", "pt": "Tenho pensado muito ultimamente", "fr": "J'ai beaucoup réfléchi ces derniers temps", "de": "Ich habe in letzter Zeit viel nachgedacht"},
        {"en": "I'm trying to improve myself", "es": "Estoy tratando de mejorarme", "pt": "Estou tentando me melhorar", "fr": "J'essaie de m'améliorer", "de": "Ich versuche, mich zu verbessern"},
        {"en": "Life is full of surprises", "es": "La vida está llena de sorpresas", "pt": "A vida está cheia de surpresas", "fr": "La vie est pleine de surprises", "de": "Das Leben ist voller Überraschungen"},
        {"en": "I believe everything happens for a reason", "es": "Creo que todo pasa por una razón", "pt": "Eu acredito que tudo acontece por uma razão", "fr": "Je crois que tout arrive pour une raison", "de": "Ich glaube, alles geschieht aus einem bestimmten Grund"},
        {"en": "Growth comes from challenges", "es": "El crecimiento viene de los desafíos", "pt": "O crescimento vem dos desafios", "fr": "La croissance vient des défis", "de": "Wachstum kommt durch Herausforderungen"},
        {"en": "The past doesn't define you", "es": "El pasado no te define", "pt": "O passado não te define", "fr": "Le passé ne te définit pas", "de": "Die Vergangenheit definiert dich nicht"},
        {"en": "I want to make a difference", "es": "Quiero marcar la diferencia", "pt": "Quero fazer a diferença", "fr": "Je veux faire une différence", "de": "Ich will einen Unterschied machen"},
        {"en": "Happiness is a journey, not a destination", "es": "La felicidad es un viaje, no un destino", "pt": "A felicidade é uma jornada, não um destino", "fr": "Le bonheur est un voyage, pas une destination", "de": "Glück ist eine Reise, kein Ziel"},
        {"en": "We all have our own path", "es": "Todos tenemos nuestro propio camino", "pt": "Todos nós temos nosso próprio caminho", "fr": "Nous avons tous notre propre chemin", "de": "Wir alle haben unseren eigenen Weg"}
    ]
}

# Dictionary mapping day numbers to phrase dictionaries
all_phrases = {
    1: day1_phrases,
    2: day2_phrases,
    3: day3_phrases,
    4: day4_phrases,
    5: day5_phrases,
    6: day6_phrases,
    7: day7_phrases
}

def generate_text_file(day, language_code, language_name):
    """Generate a text file with all phrases for a specific day"""
    print(f"Generating Day {day} {language_name} text file...")
    
    phrases_dict = all_phrases[day]
    
    # Ensure the text_files directory exists
    os.makedirs("text_files", exist_ok=True)
    
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
    
    # Ensure the audio_files directory exists
    os.makedirs("audio_files", exist_ok=True)
    
    # Generate audio
    tts = gTTS(text=text, lang=language_code)
    tts.save(f"audio_files/day{day}_{language_code}.mp3")
    
    elapsed = time.time() - start_time
    print(f"✓ Saved to audio_files/day{day}_{language_code}.mp3 ({elapsed:.2f}s)")

def main():
    parser = argparse.ArgumentParser(description="Generate language learning files")
    parser.add_argument("--day", "-d", type=int, choices=[1, 2, 3, 4, 5, 6, 7], default=None,
                        help="Day number to generate (1-7). If not specified, generates all days.")
    parser.add_argument("--languages", "-l", nargs="+", choices=["es", "pt", "en", "fr", "de"], 
                        default=["es", "pt"], help="Languages to generate (es=Spanish, pt=Portuguese, en=English, fr=French, de=German)")
    parser.add_argument("--text-only", "-t", action="store_true", 
                        help="Generate only text files (no audio)")
    args = parser.parse_args()
    
    language_names = {"es": "Spanish", "pt": "Portuguese", "en": "English", "fr": "French", "de": "German"}
    
    # Determine which days to process
    days_to_process = [args.day] if args.day else [1, 2, 3, 4, 5, 6, 7]
    
    # Process each day
    for day in days_to_process:
        print(f"\n=== Processing Day {day} ===")
        
        # Generate text files for all selected languages
        for lang in args.languages:
            generate_text_file(day, lang, language_names[lang])
        
        # Generate audio files if not text-only mode
        if not args.text_only:
            for lang in args.languages:
                generate_audio(day, lang, language_names[lang])
    
    print("\nAll files generated successfully!")
    print("\nUsage examples:")
    print("  - Generate text files only: python language_phrases.py --text-only")
    print("  - Generate files for just Day 1: python language_phrases.py --day 1")
    print("  - Generate files for just Spanish: python language_phrases.py --languages es")
    print("  - Generate Day 2 Portuguese text only: python language_phrases.py --day 2 --languages pt --text-only")
    print("  - Generate Day 3 English audio: python language_phrases.py --day 3 --languages en")
    print("  - Generate Day 6 Spanish and Portuguese: python language_phrases.py --day 6")
    print("  - Generate Day 7 all languages: python language_phrases.py --day 7 --languages es pt en fr de")

if __name__ == "__main__":
    main()
