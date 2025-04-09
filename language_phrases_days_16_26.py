import argparse
import os
import time
from gtts import gTTS

# This file contains days 16-26 of language phrases for PolyglotPathways
# It follows the same structure as previous scripts but includes content
# focusing on Living & Working in South America, including housing, jobs,
# banking, healthcare, cultural integration, daily life, and social integration

# Day 16: Essential Living Topics - Finding Housing and Accommodation
day16_phrases = {
    "Software Engineering & Tech Workplace": [
        {"en": "I'm a software engineer", "es": "Soy ingeniero/a de software", "pt": "Sou engenheiro/a de software",
         "fr": "Je suis ingénieur en logiciel", "de": "Ich bin Softwareentwickler"},
        {"en": "I work in web development", "es": "Trabajo en desarrollo web", "pt": "Trabalho com desenvolvimento web",
         "fr": "Je travaille dans le développement web", "de": "Ich arbeite in der Webentwicklung"},
        {"en": "I specialize in backend development", "es": "Me especializo en desarrollo backend", "pt": "Me especializo em desenvolvimento backend",
         "fr": "Je me spécialise dans le développement back-end", "de": "Ich spezialisiere mich auf Backend-Entwicklung"},
        {"en": "I'm a frontend developer", "es": "Soy desarrollador/a frontend", "pt": "Sou desenvolvedor/a frontend",
         "fr": "Je suis développeur front-end", "de": "Ich bin Frontend-Entwickler"},
        {"en": "I work with mobile applications", "es": "Trabajo con aplicaciones móviles", "pt": "Trabalho com aplicativos móveis",
         "fr": "Je travaille avec des applications mobiles", "de": "Ich arbeite mit mobilen Anwendungen"},
        {"en": "I'm working on a new feature", "es": "Estoy trabajando en una nueva funcionalidad", "pt": "Estou trabalhando em uma nova funcionalidade",
         "fr": "Je travaille sur une nouvelle fonctionnalité", "de": "Ich arbeite an einer neuen Funktion"},
        {"en": "We need to fix this bug", "es": "Necesitamos arreglar este error", "pt": "Precisamos corrigir este bug",
         "fr": "Nous devons corriger ce bug", "de": "Wir müssen diesen Fehler beheben"},
        {"en": "Let's schedule a code review", "es": "Programemos una revisión de código", "pt": "Vamos agendar uma revisão de código",
         "fr": "Planifions une revue de code", "de": "Lass uns einen Code-Review planen"},
        {"en": "I'm looking for a remote tech job", "es": "Estoy buscando un trabajo remoto en tecnología", "pt": "Estou procurando um trabalho remoto em tecnologia",
         "fr": "Je cherche un emploi technologique à distance", "de": "Ich suche einen Remote-Tech-Job"},
        {"en": "The tech industry is growing here", "es": "La industria tecnológica está creciendo aquí", "pt": "A indústria de tecnologia está crescendo aqui",
         "fr": "L'industrie technologique se développe ici", "de": "Die Technologiebranche wächst hier"}
    ],
    "Programming Languages & Concepts": [
        {"en": "I code in JavaScript/Python/Java", "es": "Programo en JavaScript/Python/Java", "pt": "Programo em JavaScript/Python/Java",
         "fr": "Je code en JavaScript/Python/Java", "de": "Ich programmiere in JavaScript/Python/Java"},
        {"en": "This function is not working", "es": "Esta función no está funcionando", "pt": "Esta função não está funcionando",
         "fr": "Cette fonction ne fonctionne pas", "de": "Diese Funktion funktioniert nicht"},
        {"en": "We need to refactor this code", "es": "Necesitamos refactorizar este código", "pt": "Precisamos refatorar este código",
         "fr": "Nous devons refactorer ce code", "de": "Wir müssen diesen Code refaktorieren"},
        {"en": "Let's implement this algorithm", "es": "Implementemos este algoritmo", "pt": "Vamos implementar este algoritmo",
         "fr": "Implémentons cet algorithme", "de": "Lass uns diesen Algorithmus implementieren"},
        {"en": "This is an object-oriented approach", "es": "Este es un enfoque orientado a objetos", "pt": "Esta é uma abordagem orientada a objetos",
         "fr": "C'est une approche orientée objet", "de": "Das ist ein objektorientierter Ansatz"},
        {"en": "We should use a design pattern here", "es": "Deberíamos usar un patrón de diseño aquí", "pt": "Deveríamos usar um padrão de design aqui",
         "fr": "Nous devrions utiliser un patron de conception ici", "de": "Wir sollten hier ein Designmuster verwenden"},
        {"en": "The API is not responding", "es": "La API no está respondiendo", "pt": "A API não está respondendo",
         "fr": "L'API ne répond pas", "de": "Die API reagiert nicht"},
        {"en": "We need to optimize this query", "es": "Necesitamos optimizar esta consulta", "pt": "Precisamos otimizar esta consulta",
         "fr": "Nous devons optimiser cette requête", "de": "Wir müssen diese Abfrage optimieren"},
        {"en": "Let's test this component", "es": "Probemos este componente", "pt": "Vamos testar este componente",
         "fr": "Testons ce composant", "de": "Lass uns diese Komponente testen"},
        {"en": "This is a recursive solution", "es": "Esta es una solución recursiva", "pt": "Esta é uma solução recursiva",
         "fr": "C'est une solution récursive", "de": "Das ist eine rekursive Lösung"}
    ],
    "Development Tools & Methodologies": [
        {"en": "We use Git for version control", "es": "Usamos Git para control de versiones", "pt": "Usamos Git para controle de versão",
         "fr": "Nous utilisons Git pour le contrôle de version", "de": "Wir verwenden Git für die Versionskontrolle"},
        {"en": "Let's create a pull request", "es": "Creemos una solicitud de extracción", "pt": "Vamos criar um pull request",
         "fr": "Créons une pull request", "de": "Lass uns einen Pull Request erstellen"},
        {"en": "We follow Agile methodology", "es": "Seguimos la metodología Ágil", "pt": "Seguimos a metodologia Ágil",
         "fr": "Nous suivons la méthodologie Agile", "de": "Wir folgen der agilen Methodik"},
        {"en": "We have daily stand-up meetings", "es": "Tenemos reuniones diarias de pie", "pt": "Temos reuniões diárias em pé",
         "fr": "Nous avons des réunions debout quotidiennes", "de": "Wir haben tägliche Stand-up-Meetings"},
        {"en": "Let's plan the next sprint", "es": "Planifiquemos el próximo sprint", "pt": "Vamos planejar o próximo sprint",
         "fr": "Planifions le prochain sprint", "de": "Lass uns den nächsten Sprint planen"},
        {"en": "We need to document this API", "es": "Necesitamos documentar esta API", "pt": "Precisamos documentar esta API",
         "fr": "Nous devons documenter cette API", "de": "Wir müssen diese API dokumentieren"},
        {"en": "I use VS Code as my IDE", "es": "Uso VS Code como mi IDE", "pt": "Uso VS Code como meu IDE",
         "fr": "J'utilise VS Code comme mon IDE", "de": "Ich benutze VS Code als meine IDE"},
        {"en": "Let's set up continuous integration", "es": "Configuremos la integración continua", "pt": "Vamos configurar a integração contínua",
         "fr": "Mettons en place l'intégration continue", "de": "Lass uns Continuous Integration einrichten"},
        {"en": "We should write unit tests", "es": "Deberíamos escribir pruebas unitarias", "pt": "Deveríamos escrever testes unitários",
         "fr": "Nous devrions écrire des tests unitaires", "de": "Wir sollten Unit-Tests schreiben"},
        {"en": "Let's deploy to production", "es": "Despleguemos a producción", "pt": "Vamos implantar em produção",
         "fr": "Déployons en production", "de": "Lass uns in Produktion deployen"}
    ],
    "Tech Problem Solving": [
        {"en": "I'm debugging this issue", "es": "Estoy depurando este problema", "pt": "Estou depurando este problema",
         "fr": "Je débogue ce problème", "de": "Ich debugge dieses Problem"},
        {"en": "Let's check the error logs", "es": "Revisemos los registros de errores", "pt": "Vamos verificar os logs de erro",
         "fr": "Vérifions les journaux d'erreurs", "de": "Lass uns die Fehlerprotokolle überprüfen"},
        {"en": "The server is down", "es": "El servidor está caído", "pt": "O servidor está fora do ar",
         "fr": "Le serveur est en panne", "de": "Der Server ist ausgefallen"},
        {"en": "We need to scale our infrastructure", "es": "Necesitamos escalar nuestra infraestructura", "pt": "Precisamos escalar nossa infraestrutura",
         "fr": "Nous devons faire évoluer notre infrastructure", "de": "Wir müssen unsere Infrastruktur skalieren"},
        {"en": "This is a performance bottleneck", "es": "Este es un cuello de botella de rendimiento", "pt": "Este é um gargalo de desempenho",
         "fr": "C'est un goulet d'étranglement de performance", "de": "Das ist ein Leistungsengpass"},
        {"en": "Let's implement a workaround", "es": "Implementemos una solución alternativa", "pt": "Vamos implementar uma solução alternativa",
         "fr": "Implémentons une solution de contournement", "de": "Lass uns eine Notlösung implementieren"},
        {"en": "We need to optimize for mobile", "es": "Necesitamos optimizar para móviles", "pt": "Precisamos otimizar para dispositivos móveis",
         "fr": "Nous devons optimiser pour mobile", "de": "Wir müssen für mobile optimieren"},
        {"en": "The database is running slow", "es": "La base de datos está funcionando lento", "pt": "O banco de dados está funcionando lentamente",
         "fr": "La base de données est lente", "de": "Die Datenbank ist langsam"},
        {"en": "Let's run a load test", "es": "Ejecutemos una prueba de carga", "pt": "Vamos executar um teste de carga",
         "fr": "Effectuons un test de charge", "de": "Lass uns einen Lasttest durchführen"},
        {"en": "We need to fix this security vulnerability", "es": "Necesitamos arreglar esta vulnerabilidad de seguridad", "pt": "Precisamos corrigir esta vulnerabilidade de segurança",
         "fr": "Nous devons corriger cette vulnérabilité de sécurité", "de": "Wir müssen diese Sicherheitslücke beheben"}
    ],
    "Tech Workplace Communication": [
        {"en": "Let's discuss this in the next meeting", "es": "Discutamos esto en la próxima reunión", "pt": "Vamos discutir isso na próxima reunião",
         "fr": "Discutons-en lors de la prochaine réunion", "de": "Lass uns das im nächsten Meeting besprechen"},
        {"en": "I'll share my screen to show you", "es": "Compartiré mi pantalla para mostrarte", "pt": "Vou compartilhar minha tela para te mostrar",
         "fr": "Je vais partager mon écran pour te montrer", "de": "Ich werde meinen Bildschirm teilen, um es dir zu zeigen"},
        {"en": "Can you review my code?", "es": "¿Puedes revisar mi código?", "pt": "Você pode revisar meu código?",
         "fr": "Peux-tu revoir mon code ?", "de": "Kannst du meinen Code überprüfen?"},
        {"en": "I'll send you the documentation", "es": "Te enviaré la documentación", "pt": "Vou te enviar a documentação",
         "fr": "Je t'enverrai la documentation", "de": "Ich schicke dir die Dokumentation"},
        {"en": "Let's set up a video call", "es": "Configuremos una videollamada", "pt": "Vamos configurar uma videochamada",
         "fr": "Organisons un appel vidéo", "de": "Lass uns einen Videoanruf einrichten"},
        {"en": "I need access to the repository", "es": "Necesito acceso al repositorio", "pt": "Preciso de acesso ao repositório",
         "fr": "J'ai besoin d'accéder au dépôt", "de": "Ich benötige Zugriff auf das Repository"},
        {"en": "What's the status of your task?", "es": "¿Cuál es el estado de tu tarea?", "pt": "Qual é o status da sua tarefa?",
         "fr": "Quel est le statut de ta tâche ?", "de": "Wie ist der Stand deiner Aufgabe?"},
        {"en": "I'll update the ticket", "es": "Actualizaré el ticket", "pt": "Vou atualizar o ticket",
         "fr": "Je mettrai à jour le ticket", "de": "Ich werde das Ticket aktualisieren"},
        {"en": "Let's create a new project board", "es": "Creemos un nuevo tablero de proyecto", "pt": "Vamos criar um novo quadro de projeto",
         "fr": "Créons un nouveau tableau de projet", "de": "Lass uns ein neues Projektboard erstellen"},
        {"en": "I'll add comments to explain this", "es": "Agregaré comentarios para explicar esto", "pt": "Vou adicionar comentários para explicar isso",
         "fr": "J'ajouterai des commentaires pour expliquer cela", "de": "Ich werde Kommentare hinzufügen, um das zu erklären"}
    ]
}

# Day 18: Essential Living Topics - Banking and Finance
day18_phrases = {
    "Digital Life & Tech Vocabulary": [
        {"en": "I need to update my software", "es": "Necesito actualizar mi software", "pt": "Preciso atualizar meu software",
         "fr": "J'ai besoin de mettre à jour mon logiciel", "de": "Ich muss meine Software aktualisieren"},
        {"en": "My battery is running low", "es": "Mi batería se está agotando", "pt": "Minha bateria está acabando",
         "fr": "Ma batterie est faible", "de": "Mein Akku wird schwach"},
        {"en": "I need to back up my data", "es": "Necesito hacer una copia de seguridad de mis datos", "pt": "Preciso fazer backup dos meus dados",
         "fr": "J'ai besoin de sauvegarder mes données", "de": "Ich muss meine Daten sichern"},
        {"en": "The internet connection is slow", "es": "La conexión a internet es lenta", "pt": "A conexão com a internet está lenta",
         "fr": "La connexion Internet est lente", "de": "Die Internetverbindung ist langsam"},
        {"en": "I'm streaming a movie", "es": "Estoy transmitiendo una película", "pt": "Estou transmitindo um filme",
         "fr": "Je suis en train de diffuser un film", "de": "Ich streame einen Film"},
        {"en": "I need to download this app", "es": "Necesito descargar esta aplicación", "pt": "Preciso baixar este aplicativo",
         "fr": "J'ai besoin de télécharger cette application", "de": "Ich muss diese App herunterladen"},
        {"en": "My screen is frozen", "es": "Mi pantalla está congelada", "pt": "Minha tela está congelada",
         "fr": "Mon écran est figé", "de": "Mein Bildschirm ist eingefroren"},
        {"en": "I need to restart my device", "es": "Necesito reiniciar mi dispositivo", "pt": "Preciso reiniciar meu dispositivo",
         "fr": "Je dois redémarrer mon appareil", "de": "Ich muss mein Gerät neu starten"},
        {"en": "The system is lagging", "es": "El sistema está retrasado", "pt": "O sistema está lento",
         "fr": "Le système est lent", "de": "Das System reagiert langsam"},
        {"en": "I need more storage space", "es": "Necesito más espacio de almacenamiento", "pt": "Preciso de mais espaço de armazenamento",
         "fr": "J'ai besoin de plus d'espace de stockage", "de": "Ich benötige mehr Speicherplatz"}
    ],
    "Social Media & Apps": [
        {"en": "I'll send you the link", "es": "Te enviaré el enlace", "pt": "Vou te enviar o link",
         "fr": "Je t'enverrai le lien", "de": "Ich schicke dir den Link"},
        {"en": "Let's video chat later", "es": "Hablemos por video más tarde", "pt": "Vamos conversar por vídeo mais tarde",
         "fr": "Discutons en vidéo plus tard", "de": "Lass uns später per Videochat sprechen"},
        {"en": "I'll share this post", "es": "Compartiré esta publicación", "pt": "Vou compartilhar esta postagem",
         "fr": "Je vais partager ce post", "de": "Ich teile diesen Beitrag"},
        {"en": "Did you see my story?", "es": "¿Viste mi historia?", "pt": "Você viu minha história?",
         "fr": "As-tu vu ma story ?", "de": "Hast du meine Story gesehen?"},
        {"en": "I'll tag you in the photo", "es": "Te etiquetaré en la foto", "pt": "Vou te marcar na foto",
         "fr": "Je vais te taguer sur la photo", "de": "Ich werde dich im Foto markieren"},
        {"en": "Let's create a group chat", "es": "Creemos un chat grupal", "pt": "Vamos criar um chat em grupo",
         "fr": "Créons un chat de groupe", "de": "Lass uns einen Gruppenchat erstellen"},
        {"en": "I'll follow you on Instagram", "es": "Te seguiré en Instagram", "pt": "Vou te seguir no Instagram",
         "fr": "Je te suivrai sur Instagram", "de": "Ich werde dir auf Instagram folgen"},
        {"en": "I need to update my profile", "es": "Necesito actualizar mi perfil", "pt": "Preciso atualizar meu perfil",
         "fr": "Je dois mettre à jour mon profil", "de": "Ich muss mein Profil aktualisieren"},
        {"en": "I'll send you a voice message", "es": "Te enviaré un mensaje de voz", "pt": "Vou te enviar uma mensagem de voz",
         "fr": "Je t'enverrai un message vocal", "de": "Ich schicke dir eine Sprachnachricht"},
        {"en": "Let's use this app to communicate", "es": "Usemos esta aplicación para comunicarnos", "pt": "Vamos usar este aplicativo para nos comunicar",
         "fr": "Utilisons cette application pour communiquer", "de": "Lass uns diese App zur Kommunikation nutzen"}
    ],
    "Digital Security & Privacy": [
        {"en": "I need a strong password", "es": "Necesito una contraseña fuerte", "pt": "Preciso de uma senha forte",
         "fr": "J'ai besoin d'un mot de passe fort", "de": "Ich benötige ein starkes Passwort"},
        {"en": "Enable two-factor authentication", "es": "Habilita la autenticación de dos factores", "pt": "Ative a autenticação de dois fatores",
         "fr": "Active la double authentification", "de": "Aktiviere die Zwei-Faktor-Authentifizierung"},
        {"en": "Be careful with phishing emails", "es": "Ten cuidado con los correos de phishing", "pt": "Tenha cuidado com e-mails de phishing",
         "fr": "Fais attention aux emails de phishing", "de": "Sei vorsichtig mit Phishing-E-Mails"},
        {"en": "Don't share personal information online", "es": "No compartas información personal en línea", "pt": "Não compartilhe informações pessoais online",
         "fr": "Ne partage pas d'informations personnelles en ligne", "de": "Teile keine persönlichen Daten online"},
        {"en": "Use a VPN for secure browsing", "es": "Usa una VPN para navegación segura", "pt": "Use uma VPN para navegação segura",
         "fr": "Utilise un VPN pour une navigation sécurisée", "de": "Nutze ein VPN für sicheres Surfen"},
        {"en": "I think my account was hacked", "es": "Creo que mi cuenta fue hackeada", "pt": "Acho que minha conta foi hackeada",
         "fr": "Je pense que mon compte a été piraté", "de": "Ich glaube, mein Konto wurde gehackt"},
        {"en": "Check the privacy settings", "es": "Revisa la configuración de privacidad", "pt": "Verifique as configurações de privacidade",
         "fr": "Vérifie les paramètres de confidentialité", "de": "Überprüfe die Datenschutzeinstellungen"},
        {"en": "Be careful on public Wi-Fi", "es": "Ten cuidado en Wi-Fi público", "pt": "Tenha cuidado em Wi-Fi público",
         "fr": "Fais attention au Wi-Fi public", "de": "Sei vorsichtig bei öffentlichem WLAN"},
        {"en": "Update your security software", "es": "Actualiza tu software de seguridad", "pt": "Atualize seu software de segurança",
         "fr": "Mets à jour ton logiciel de sécurité", "de": "Aktualisiere deine Sicherheitssoftware"},
        {"en": "Backup your important files", "es": "Haz copias de seguridad de tus archivos importantes", "pt": "Faça backup dos seus arquivos importantes",
         "fr": "Sauvegarde tes fichiers importants", "de": "Sichere deine wichtigen Dateien"}
    ],
    "Online Services": [
        {"en": "I need to book a ride", "es": "Necesito reservar un viaje", "pt": "Preciso reservar uma corrida",
         "fr": "Je dois réserver un trajet", "de": "Ich muss eine Fahrt buchen"},
        {"en": "Let's order food delivery", "es": "Pidamos comida a domicilio", "pt": "Vamos pedir comida para entrega",
         "fr": "Commandons une livraison de nourriture", "de": "Lass uns Essen liefern bestellen"},
        {"en": "I'm shopping online", "es": "Estoy comprando en línea", "pt": "Estou comprando online",
         "fr": "Je fais des achats en ligne", "de": "Ich kaufe online ein"},
        {"en": "I need to make an online payment", "es": "Necesito hacer un pago en línea", "pt": "Preciso fazer um pagamento online",
         "fr": "Je dois effectuer un paiement en ligne", "de": "Ich muss eine Online-Zahlung tätigen"},
        {"en": "Let's stream this movie", "es": "Transmitamos esta película", "pt": "Vamos transmitir este filme",
         "fr": "Diffusons ce film en streaming", "de": "Lass uns diesen Film streamen"},
        {"en": "I'm using a navigation app", "es": "Estoy usando una aplicación de navegación", "pt": "Estou usando um aplicativo de navegação",
         "fr": "J'utilise une application de navigation", "de": "Ich benutze eine Navigations-App"},
        {"en": "I need to book a hotel online", "es": "Necesito reservar un hotel en línea", "pt": "Preciso reservar um hotel online",
         "fr": "Je dois réserver un hôtel en ligne", "de": "Ich muss ein Hotel online buchen"},
        {"en": "Let's compare prices online", "es": "Comparemos precios en línea", "pt": "Vamos comparar preços online",
         "fr": "Comparons les prix en ligne", "de": "Lass uns die Preise online vergleichen"},
        {"en": "I'm tracking my package", "es": "Estoy rastreando mi paquete", "pt": "Estou rastreando meu pacote",
         "fr": "Je suis mon colis", "de": "Ich verfolge mein Paket"},
        {"en": "I need to renew my subscription", "es": "Necesito renovar mi suscripción", "pt": "Preciso renovar minha assinatura",
         "fr": "Je dois renouveler mon abonnement", "de": "Ich muss mein Abonnement erneuern"}
    ],
    "Tech Support & Troubleshooting": [
        {"en": "My device isn't working", "es": "Mi dispositivo no está funcionando", "pt": "Meu dispositivo não está funcionando",
         "fr": "Mon appareil ne fonctionne pas", "de": "Mein Gerät funktioniert nicht"},
        {"en": "I can't connect to the network", "es": "No puedo conectarme a la red", "pt": "Não consigo me conectar à rede",
         "fr": "Je ne peux pas me connecter au réseau", "de": "Ich kann keine Verbindung zum Netzwerk herstellen"},
        {"en": "The app keeps crashing", "es": "La aplicación sigue fallando", "pt": "O aplicativo continua travando",
         "fr": "L'application plante constamment", "de": "Die App stürzt ständig ab"},
        {"en": "I need to reset my password", "es": "Necesito restablecer mi contraseña", "pt": "Preciso redefinir minha senha",
         "fr": "Je dois réinitialiser mon mot de passe", "de": "Ich muss mein Passwort zurücksetzen"},
        {"en": "How do I install this software?", "es": "¿Cómo instalo este software?", "pt": "Como instalo este software?",
         "fr": "Comment installer ce logiciel ?", "de": "Wie installiere ich diese Software?"},
        {"en": "My screen is blank", "es": "Mi pantalla está en blanco", "pt": "Minha tela está em branco",
         "fr": "Mon écran est vide", "de": "Mein Bildschirm ist schwarz"},
        {"en": "I need to clear my cache", "es": "Necesito limpiar mi caché", "pt": "Preciso limpar meu cache",
         "fr": "Je dois vider mon cache", "de": "Ich muss meinen Cache leeren"},
        {"en": "How do I update my drivers?", "es": "¿Cómo actualizo mis controladores?", "pt": "Como atualizo meus drivers?",
         "fr": "Comment mettre à jour mes pilotes ?", "de": "Wie aktualisiere ich meine Treiber?"},
        {"en": "I'm getting an error message", "es": "Estoy recibiendo un mensaje de error", "pt": "Estou recebendo uma mensagem de erro",
         "fr": "Je reçois un message d'erreur", "de": "Ich erhalte eine Fehlermeldung"},
        {"en": "Let me try restarting it", "es": "Déjame intentar reiniciarlo", "pt": "Deixe-me tentar reiniciá-lo",
         "fr": "Laisse-moi essayer de le redémarrer", "de": "Lass mich versuchen, es neu zu starten"}
    ]
}

# Day 20: Cultural Integration - Regional Cultural Nuances
day20_phrases = {
    "South American Geography": [
        {"en": "The Amazon Rainforest is the largest in the world", "es": "La Selva Amazónica es la más grande del mundo", "pt": "A Floresta Amazônica é a maior do mundo",
         "fr": "La forêt amazonienne est la plus grande au monde", "de": "Der Amazonas-Regenwald ist der größte der Welt"},
        {"en": "The Andes Mountains run through South America", "es": "La Cordillera de los Andes atraviesa Sudamérica", "pt": "A Cordilheira dos Andes atravessa a América do Sul",
         "fr": "Les montagnes des Andes traversent l'Amérique du Sud", "de": "Die Anden durchziehen Südamerika"},
        {"en": "The Atacama Desert is one of the driest places", "es": "El Desierto de Atacama es uno de los lugares más secos", "pt": "O Deserto do Atacama é um dos lugares mais secos",
         "fr": "Le désert d'Atacama est l'un des endroits les plus arides", "de": "Die Atacama-Wüste ist einer der trockensten Orte"},
        {"en": "The Pantanal is the world's largest wetland", "es": "El Pantanal es el humedal más grande del mundo", "pt": "O Pantanal é a maior área úmida do mundo",
         "fr": "Le Pantanal est la plus grande zone humide du monde", "de": "Der Pantanal ist das größte Feuchtgebiet der Welt"},
        {"en": "Lake Titicaca is the highest navigable lake", "es": "El Lago Titicaca es el lago navegable más alto", "pt": "O Lago Titicaca é o lago navegável mais alto",
         "fr": "Le lac Titicaca est le lac navigable le plus haut", "de": "Der Titicaca-See ist der höchstgelegene schiffbare See"},
        {"en": "The Patagonia region is known for its beauty", "es": "La región de la Patagonia es conocida por su belleza", "pt": "A região da Patagônia é conhecida por sua beleza",
         "fr": "La région de la Patagonie est connue pour sa beauté", "de": "Die Region Patagonien ist für ihre Schönheit bekannt"},
        {"en": "The Pampas are fertile lowlands", "es": "Las Pampas son tierras bajas fértiles", "pt": "Os Pampas são planícies férteis",
         "fr": "Les Pampas sont des plaines fertiles", "de": "Die Pampas sind fruchtbare Tieflandgebiete"},
        {"en": "The Galapagos Islands are unique ecosystems", "es": "Las Islas Galápagos son ecosistemas únicos", "pt": "As Ilhas Galápagos são ecossistemas únicos",
         "fr": "Les îles Galápagos sont des écosystèmes uniques", "de": "Die Galapagos-Inseln sind einzigartige Ökosysteme"},
        {"en": "The Amazon River is the largest by volume", "es": "El Río Amazonas es el más grande por volumen", "pt": "O Rio Amazonas é o maior em volume",
         "fr": "Le fleuve Amazone est le plus grand en termes de volume", "de": "Der Amazonas ist der volumenmäßig größte Fluss"},
        {"en": "Angel Falls is the world's highest waterfall", "es": "El Salto Ángel es la cascada más alta del mundo", "pt": "O Salto Angel é a cachoeira mais alta do mundo",
         "fr": "Les chutes d'Angel sont les plus hautes du monde", "de": "Der Angel Falls ist der höchste Wasserfall der Welt"}
    ],
    "Climate & Weather": [
        {"en": "The rainy season lasts from November to April", "es": "La temporada de lluvias dura de noviembre a abril", "pt": "A estação chuvosa dura de novembro a abril",
         "fr": "La saison des pluies dure de novembre à avril", "de": "Die Regenzeit dauert von November bis April"},
        {"en": "The dry season is from May to October", "es": "La temporada seca es de mayo a octubre", "pt": "A estação seca é de maio a outubro",
         "fr": "La saison sèche va de mai à octobre", "de": "Die Trockenzeit ist von Mai bis Oktober"},
        {"en": "It's very humid in the rainforest", "es": "Es muy húmedo en la selva", "pt": "É muito úmido na floresta tropical",
         "fr": "Il fait très humide dans la forêt tropicale", "de": "Im Regenwald ist es sehr feucht"},
        {"en": "The highlands have cooler temperatures", "es": "Las tierras altas tienen temperaturas más frescas", "pt": "As terras altas têm temperaturas mais frescas",
         "fr": "Les hautes terres ont des températures plus fraîches", "de": "In den Hochebenen ist es kühler"},
        {"en": "The coastal areas are often foggy", "es": "Las zonas costeras suelen ser neblinosas", "pt": "As áreas costeiras costumam ser nebulosas",
         "fr": "Les zones côtières sont souvent brumeuses", "de": "Die Küstengebiete sind oft neblig"},
        {"en": "We're expecting a thunderstorm", "es": "Esperamos una tormenta eléctrica", "pt": "Estamos esperando uma tempestade",
         "fr": "Nous prévoyons un orage", "de": "Wir erwarten ein Gewitter"},
        {"en": "The temperature varies greatly between day and night", "es": "La temperatura varía mucho entre el día y la noche", "pt": "A temperatura varia muito entre o dia e a noite",
         "fr": "La température varie considérablement entre le jour et la nuit", "de": "Die Temperatur schwankt stark zwischen Tag und Nacht"},
        {"en": "The altitude affects the climate", "es": "La altitud afecta el clima", "pt": "A altitude afeta o clima",
         "fr": "L'altitude influence le climat", "de": "Die Höhe beeinflusst das Klima"},
        {"en": "The El Niño phenomenon affects our weather", "es": "El fenómeno de El Niño afecta nuestro clima", "pt": "O fenômeno El Niño afeta nosso clima",
         "fr": "Le phénomène El Niño affecte notre climat", "de": "Das El Niño-Phänomen beeinflusst unser Wetter"},
        {"en": "The microclimates vary within short distances", "es": "Los microclimas varían en distancias cortas", "pt": "Os microclimas variam em curtas distâncias",
         "fr": "Les microclimats varient sur de courtes distances", "de": "Die Mikroklimata variieren über kurze Distanzen"}
    ],
    "Natural Landscapes": [
        {"en": "The valley is surrounded by mountains", "es": "El valle está rodeado de montañas", "pt": "O vale é cercado por montanhas",
         "fr": "La vallée est entourée de montagnes", "de": "Das Tal ist von Bergen umgeben"},
        {"en": "The canyon was formed by the river", "es": "El cañón fue formado por el río", "pt": "O cânion foi formado pelo rio",
         "fr": "Le canyon a été formé par la rivière", "de": "Der Canyon wurde vom Fluss geformt"},
        {"en": "The plateau extends for hundreds of miles", "es": "La meseta se extiende por cientos de millas", "pt": "O planalto se estende por centenas de quilômetros",
         "fr": "Le plateau s'étend sur des centaines de kilomètres", "de": "Das Plateau erstreckt sich über Hunderte von Meilen"},
        {"en": "The coastline has beautiful beaches", "es": "La costa tiene hermosas playas", "pt": "O litoral tem belas praias",
         "fr": "La côte possède de belles plages", "de": "Die Küste hat schöne Strände"},
        {"en": "The forest is home to diverse wildlife", "es": "El bosque alberga diversa fauna silvestre", "pt": "A floresta abriga uma vida selvagem diversificada",
         "fr": "La forêt abrite une faune diversifiée", "de": "Der Wald beherbergt eine vielfältige Tierwelt"},
        {"en": "The glacier is retreating due to climate change", "es": "El glaciar está retrocediendo debido al cambio climático", "pt": "A geleira está recuando devido às mudanças climáticas",
         "fr": "Le glacier recule à cause du changement climatique", "de": "Der Gletscher zieht sich aufgrund des Klimawandels zurück"},
        {"en": "The savanna is dry during this season", "es": "La sabana está seca durante esta temporada", "pt": "A savana está seca durante esta estação",
         "fr": "La savane est sèche pendant cette saison", "de": "Die Savanne ist in dieser Jahreszeit trocken"},
        {"en": "The lagoon has crystal clear water", "es": "La laguna tiene agua cristalina", "pt": "A lagoa tem água cristalina",
         "fr": "La lagune a une eau cristalline", "de": "Die Lagune hat kristallklares Wasser"},
        {"en": "The cave system extends underground", "es": "El sistema de cuevas se extiende bajo tierra", "pt": "O sistema de cavernas se estende pelo subsolo",
         "fr": "Le système de grottes s'étend sous terre", "de": "Das Höhlensystem erstreckt sich unterirdisch"},
        {"en": "The island is of volcanic origin", "es": "La isla es de origen volcánico", "pt": "A ilha é de origem vulcânica",
         "fr": "L'île est d'origine volcanique", "de": "Die Insel ist vulkanischen Ursprungs"}
    ],
    "Sustainability & Conservation": [
        {"en": "We need to protect endangered species", "es": "Necesitamos proteger las especies en peligro", "pt": "Precisamos proteger as espécies ameaçadas",
         "fr": "Nous devons protéger les espèces en danger", "de": "Wir müssen gefährdete Arten schützen"},
        {"en": "Deforestation is a serious problem", "es": "La deforestación es un problema grave", "pt": "O desmatamento é um problema sério",
         "fr": "La déforestation est un problème sérieux", "de": "Abholzung ist ein ernsthaftes Problem"},
        {"en": "Let's reduce plastic waste", "es": "Reduzcamos los residuos plásticos", "pt": "Vamos reduzir o lixo plástico",
         "fr": "Réduisons les déchets plastiques", "de": "Lass uns den Plastikmüll reduzieren"},
        {"en": "This area is a protected reserve", "es": "Esta área es una reserva protegida", "pt": "Esta área é uma reserva protegida",
         "fr": "Cette zone est une réserve protégée", "de": "Dieses Gebiet ist ein Schutzgebiet"},
        {"en": "Sustainable tourism helps local communities", "es": "El turismo sostenible ayuda a las comunidades locales", "pt": "O turismo sustentável ajuda as comunidades locais",
         "fr": "Le tourisme durable aide les communautés locales", "de": "Nachhaltiger Tourismus unterstützt lokale Gemeinschaften"},
        {"en": "We practice organic farming", "es": "Practicamos la agricultura orgánica", "pt": "Praticamos a agricultura orgânica",
         "fr": "Nous pratiquons l'agriculture biologique", "de": "Wir betreiben biologischen Landbau"},
        {"en": "Renewable energy is growing here", "es": "La energía renovable está creciendo aquí", "pt": "A energia renovável está crescendo aqui",
         "fr": "Les énergies renouvelables se développent ici", "de": "Erneuerbare Energien wachsen hier"},
        {"en": "Water conservation is essential", "es": "La conservación del agua es esencial", "pt": "A conservação da água é essencial",
         "fr": "La conservation de l'eau est essentielle", "de": "Wassereinsparung ist wesentlich"},
        {"en": "Biodiversity is crucial for ecosystems", "es": "La biodiversidad es crucial para los ecosistemas", "pt": "A biodiversidade é crucial para os ecossistemas",
         "fr": "La biodiversité est cruciale pour les écosystèmes", "de": "Biodiversität ist entscheidend für Ökosysteme"},
        {"en": "Climate change affects our region", "es": "El cambio climático afecta nuestra región", "pt": "As mudanças climáticas afetam nossa região",
         "fr": "Le changement climatique affecte notre région", "de": "Der Klimawandel beeinflusst unsere Region"}
    ],
    "Outdoor Activities": [
        {"en": "Let's go hiking in the mountains", "es": "Vamos a hacer senderismo en las montañas", "pt": "Vamos fazer uma caminhada nas montanhas",
         "fr": "Allons faire de la randonnée en montagne", "de": "Lass uns in den Bergen wandern gehen"},
        {"en": "I enjoy birdwatching in the wetlands", "es": "Disfruto observando aves en los humedales", "pt": "Gosto de observar pássaros nas áreas úmidas",
         "fr": "J'aime observer les oiseaux dans les zones humides", "de": "Ich genieße das Vogelbeobachten in den Feuchtgebieten"},
        {"en": "We can go rafting on this river", "es": "Podemos hacer rafting en este río", "pt": "Podemos fazer rafting neste rio",
         "fr": "Nous pouvons faire du rafting sur cette rivière", "de": "Wir können auf diesem Fluss rafting fahren"},
        {"en": "The trail leads to a waterfall", "es": "El sendero conduce a una cascada", "pt": "A trilha leva a uma cachoeira",
         "fr": "Le sentier mène à une cascade", "de": "Der Pfad führt zu einem Wasserfall"},
        {"en": "Let's camp under the stars", "es": "Acampemos bajo las estrellas", "pt": "Vamos acampar sob as estrelas",
         "fr": "Campons sous les étoiles", "de": "Lass uns unter den Sternen campen"},
        {"en": "This beach is perfect for surfing", "es": "Esta playa es perfecta para surfear", "pt": "Esta praia é perfeita para surfar",
         "fr": "Cette plage est parfaite pour le surf", "de": "Dieser Strand ist perfekt zum Surfen"},
        {"en": "We can see wildlife on this tour", "es": "Podemos ver vida silvestre en este tour", "pt": "Podemos ver vida selvagem neste passeio",
         "fr": "Nous pouvons observer la faune lors de cette visite", "de": "Auf dieser Tour können wir Wildtiere sehen"},
        {"en": "The view from the summit is amazing", "es": "La vista desde la cumbre es increíble", "pt": "A vista do cume é incrível",
         "fr": "La vue du sommet est incroyable", "de": "Die Aussicht vom Gipfel ist erstaunlich"},
        {"en": "Let's go fishing in the lake", "es": "Vamos a pescar en el lago", "pt": "Vamos pescar no lago",
         "fr": "Allons pêcher dans le lac", "de": "Lass uns im See angeln gehen"},
        {"en": "This area is great for mountain biking", "es": "Esta área es genial para ciclismo de montaña", "pt": "Esta área é ótima para mountain bike",
         "fr": "Cette région est idéale pour le VTT", "de": "Dieses Gebiet ist großartig zum Mountainbiken"}
    ]
}

# Day 22: Cultural Integration - Renting and Housing Vocabulary
day22_phrases = {
    "Indigenous Words in Spanish/Portuguese": [
        {"en": "Canoe (from Arawak 'canoa')", "es": "Canoa", "pt": "Canoa",
         "fr": "Canoë", "de": "Kanu"},
        {"en": "Hammock (from Taíno 'hamaca')", "es": "Hamaca", "pt": "Rede",
         "fr": "Hamac", "de": "Hängematte"},
        {"en": "Potato (from Quechua 'papa')", "es": "Papa", "pt": "Batata",
         "fr": "Pomme de terre", "de": "Kartoffel"},
        {"en": "Chocolate (from Nahuatl 'xocolatl')", "es": "Chocolate", "pt": "Chocolate",
         "fr": "Chocolat", "de": "Schokolade"},
        {"en": "Jaguar (from Tupi 'jaguara')", "es": "Jaguar", "pt": "Onça-pintada",
         "fr": "Jaguar", "de": "Jaguar"},
        {"en": "Avocado (from Nahuatl 'ahuacatl')", "es": "Aguacate", "pt": "Abacate",
         "fr": "Avocat", "de": "Avocado"},
        {"en": "Condor (from Quechua 'kuntur')", "es": "Cóndor", "pt": "Condor",
         "fr": "Condor", "de": "Kondor"},
        {"en": "Coca (from Aymara 'kuka')", "es": "Coca", "pt": "Coca",
         "fr": "Coca", "de": "Koka"},
        {"en": "Guava (from Arawak 'guayaba')", "es": "Guayaba", "pt": "Goiaba",
         "fr": "Goyave", "de": "Guave"},
        {"en": "Maize/Corn (from Taíno 'mahiz')", "es": "Maíz", "pt": "Milho",
         "fr": "Maïs", "de": "Mais"}
    ],
    "Indigenous Cultural Heritage": [
        {"en": "The Incas built Machu Picchu", "es": "Los Incas construyeron Machu Picchu", "pt": "Os Incas construíram Machu Picchu",
         "fr": "Les Incas ont construit le Machu Picchu", "de": "Die Inkas bauten Machu Picchu"},
        {"en": "The Mayans developed a complex calendar", "es": "Los Mayas desarrollaron un calendario complejo", "pt": "Os Maias desenvolveram um calendário complexo",
         "fr": "Les Mayas ont développé un calendrier complexe", "de": "Die Maya entwickelten einen komplexen Kalender"},
        {"en": "The Guaraní are known for their yerba mate", "es": "Los Guaraníes son conocidos por su yerba mate", "pt": "Os Guaranis são conhecidos por sua erva-mate",
         "fr": "Les Guaraní sont connus pour leur yerba maté", "de": "Die Guaraní sind bekannt für ihren Yerba Mate"},
        {"en": "The Mapuche resisted colonization", "es": "Los Mapuches resistieron la colonización", "pt": "Os Mapuches resistiram à colonização",
         "fr": "Les Mapuches ont résisté à la colonisation", "de": "Die Mapuche widersetzten sich der Kolonisation"},
        {"en": "The Quechua language is still widely spoken", "es": "La lengua quechua todavía se habla ampliamente", "pt": "A língua quéchua ainda é amplamente falada",
         "fr": "La langue quechua est encore largement parlée", "de": "Die Quechua-Sprache wird immer noch weit verbreitet gesprochen"},
        {"en": "The Aymara people live around Lake Titicaca", "es": "El pueblo Aymara vive alrededor del Lago Titicaca", "pt": "O povo Aymara vive ao redor do Lago Titicaca",
         "fr": "Le peuple aymara vit autour du lac Titicaca", "de": "Die Aymara leben rund um den Titicaca-See"},
        {"en": "The Yanomami inhabit the Amazon rainforest", "es": "Los Yanomami habitan la selva amazónica", "pt": "Os Yanomami habitam a floresta amazônica",
         "fr": "Les Yanomami habitent la forêt amazonienne", "de": "Die Yanomami bewohnen den Amazonas-Regenwald"},
        {"en": "The Nazca created the famous lines", "es": "Los Nazca crearon las famosas líneas", "pt": "Os Nazca criaram as famosas linhas",
         "fr": "Les Nazca ont créé les fameuses lignes", "de": "Die Nazca erschufen die berühmten Linien"},
        {"en": "The Wari preceded the Inca Empire", "es": "Los Wari precedieron al Imperio Inca", "pt": "Os Wari precederam o Império Inca",
         "fr": "Les Wari ont précédé l'Empire Inca", "de": "Die Wari gingen dem Inka-Reich voraus"},
        {"en": "The Tiwanaku civilization was advanced", "es": "La civilización Tiwanaku era avanzada", "pt": "A civilização Tiwanaku era avançada",
         "fr": "La civilisation Tiwanaku était avancée", "de": "Die Tiwanaku-Zivilisation war fortschrittlich"}
    ],
    "Traditional Knowledge & Practices": [
        {"en": "Traditional medicine uses local plants", "es": "La medicina tradicional usa plantas locales", "pt": "A medicina tradicional usa plantas locais",
         "fr": "La médecine traditionnelle utilise des plantes locales", "de": "Traditionelle Medizin verwendet einheimische Pflanzen"},
        {"en": "Shamans are spiritual healers", "es": "Los chamanes son sanadores espirituales", "pt": "Os xamãs são curandeiros espirituais",
         "fr": "Les chamans sont des guérisseurs spirituels", "de": "Schamanen sind spirituelle Heiler"},
        {"en": "Weaving techniques are passed down generations", "es": "Las técnicas de tejido se transmiten por generaciones", "pt": "As técnicas de tecelagem são transmitidas por gerações",
         "fr": "Les techniques de tissage se transmettent de génération en génération", "de": "Webtechniken werden von Generation zu Generation weitergegeben"},
        {"en": "Terrace farming was developed by the Incas", "es": "La agricultura en terrazas fue desarrollada por los Incas", "pt": "A agricultura em terraços foi desenvolvida pelos Incas",
         "fr": "L'agriculture en terrasses a été développée par les Incas", "de": "Die Terrassenlandwirtschaft wurde von den Inkas entwickelt"},
        {"en": "Traditional fishing methods are sustainable", "es": "Los métodos tradicionales de pesca son sostenibles", "pt": "Os métodos tradicionais de pesca são sustentáveis",
         "fr": "Les méthodes de pêche traditionnelles sont durables", "de": "Traditionelle Fischereimethoden sind nachhaltig"},
        {"en": "Pottery techniques date back thousands of years", "es": "Las técnicas de cerámica datan de miles de años", "pt": "As técnicas de cerâmica datam de milhares de anos",
         "fr": "Les techniques de poterie remontent à des milliers d'années", "de": "Töpfertechniken gibt es seit Tausenden von Jahren"},
        {"en": "Traditional navigation uses stars", "es": "La navegación tradicional usa las estrellas", "pt": "A navegação tradicional usa as estrelas",
         "fr": "La navigation traditionnelle utilise les étoiles", "de": "Traditionelle Navigation nutzt die Sterne"},
        {"en": "Oral traditions preserve cultural knowledge", "es": "Las tradiciones orales preservan el conocimiento cultural", "pt": "As tradições orais preservam o conhecimento cultural",
         "fr": "Les traditions orales préservent le savoir culturel", "de": "Mündliche Überlieferungen bewahren das kulturelle Wissen"},
        {"en": "Traditional architecture uses local materials", "es": "La arquitectura tradicional usa materiales locales", "pt": "A arquitetura tradicional usa materiais locais",
         "fr": "L'architecture traditionnelle utilise des matériaux locaux", "de": "Traditionelle Architektur verwendet lokale Materialien"},
        {"en": "Ancestral farming practices are still used", "es": "Las prácticas agrícolas ancestrales todavía se usan", "pt": "As práticas agrícolas ancestrais ainda são usadas",
         "fr": "Les pratiques agricoles ancestrales sont encore utilisées", "de": "Uralte landwirtschaftliche Praktiken werden immer noch angewendet"}
    ],
    "Cultural Celebrations": [
        {"en": "Inti Raymi celebrates the sun god", "es": "El Inti Raymi celebra al dios sol", "pt": "O Inti Raymi celebra o deus sol",
         "fr": "L'Inti Raymi célèbre le dieu soleil", "de": "Inti Raymi feiert den Sonnengott"},
        {"en": "Carnival is a major celebration", "es": "El Carnaval es una celebración importante", "pt": "O Carnaval é uma celebração importante",
         "fr": "Le Carnaval est une grande célébration", "de": "Karneval ist eine wichtige Feierlichkeit"},
        {"en": "Day of the Dead honors ancestors", "es": "El Día de los Muertos honra a los antepasados", "pt": "O Dia dos Mortos honra os antepassados",
         "fr": "Le Jour des Morts honore les ancêtres", "de": "Der Tag der Toten ehrt die Vorfahren"},
        {"en": "Traditional dances tell stories", "es": "Las danzas tradicionales cuentan historias", "pt": "As danças tradicionais contam histórias",
         "fr": "Les danses traditionnelles racontent des histoires", "de": "Traditionelle Tänze erzählen Geschichten"},
        {"en": "Pachamama rituals honor Mother Earth", "es": "Los rituales a la Pachamama honran a la Madre Tierra", "pt": "Os rituais à Pachamama honram a Mãe Terra",
         "fr": "Les rituels de Pachamama honorent la Terre Mère", "de": "Pachamama-Rituale ehren Mutter Erde"},
        {"en": "Festivals follow the agricultural calendar", "es": "Los festivales siguen el calendario agrícola", "pt": "Os festivais seguem o calendário agrícola",
         "fr": "Les festivals suivent le calendrier agricole", "de": "Festivals richten sich nach dem landwirtschaftlichen Kalender"},
        {"en": "Music is central to celebrations", "es": "La música es central en las celebraciones", "pt": "A música é central nas celebrações",
         "fr": "La musique est centrale dans les célébrations", "de": "Musik ist zentral für Feierlichkeiten"},
        {"en": "Traditional costumes are colorful", "es": "Los trajes tradicionales son coloridos", "pt": "As roupas tradicionais são coloridas",
         "fr": "Les costumes traditionnels sont colorés", "de": "Traditionelle Kostüme sind farbenfroh"},
        {"en": "Ceremonies often include offerings", "es": "Las ceremonias a menudo incluyen ofrendas", "pt": "As cerimônias frequentemente incluem oferendas",
         "fr": "Les cérémonies incluent souvent des offrandes", "de": "Zeremonien beinhalten oft Opfergaben"},
        {"en": "Festivals strengthen community bonds", "es": "Los festivales fortalecen los lazos comunitarios", "pt": "Os festivais fortalecem os laços comunitários",
         "fr": "Les festivals renforcent les liens communautaires", "de": "Festivals stärken die Gemeinschaftsbande"}
    ],
    "Indigenous Communities Today": [
        {"en": "Many indigenous communities face challenges", "es": "Muchas comunidades indígenas enfrentan desafíos", "pt": "Muitas comunidades indígenas enfrentam desafios",
         "fr": "De nombreuses communautés autochtones font face à des défis", "de": "Viele indigene Gemeinschaften stehen vor Herausforderungen"},
        {"en": "Land rights are an important issue", "es": "Los derechos a la tierra son un tema importante", "pt": "Os direitos à terra são uma questão importante",
         "fr": "Les droits fonciers sont une question importante", "de": "Landrechte sind ein wichtiges Thema"},
        {"en": "Traditional languages are being revitalized", "es": "Las lenguas tradicionales están siendo revitalizadas", "pt": "As línguas tradicionais estão sendo revitalizadas",
         "fr": "Les langues traditionnelles sont en cours de revitalisation", "de": "Traditionelle Sprachen werden revitalisiert"},
        {"en": "Indigenous knowledge is valuable for conservation", "es": "El conocimiento indígena es valioso para la conservación", "pt": "O conhecimento indígena é valioso para a conservação",
         "fr": "Le savoir indigène est précieux pour la conservation", "de": "Indigenes Wissen ist wertvoll für den Naturschutz"},
        {"en": "Many communities maintain their traditions", "es": "Muchas comunidades mantienen sus tradiciones", "pt": "Muitas comunidades mantêm suas tradições",
         "fr": "De nombreuses communautés préservent leurs traditions", "de": "Viele Gemeinschaften bewahren ihre Traditionen"},
        {"en": "Indigenous art is internationally recognized", "es": "El arte indígena es reconocido internacionalmente", "pt": "A arte indígena é reconhecida internacionalmente",
         "fr": "L'art indigène est reconnu internationalement", "de": "Indigene Kunst wird international anerkannt"},
        {"en": "Education often includes cultural teachings", "es": "La educación a menudo incluye enseñanzas culturales", "pt": "A educação frequentemente inclui ensinamentos culturais",
         "fr": "L'éducation inclut souvent des enseignements culturels", "de": "Bildung umfasst oft kulturelle Lehren"},
        {"en": "Tourism can support indigenous communities", "es": "El turismo puede apoyar a las comunidades indígenas", "pt": "O turismo pode apoiar comunidades indígenas",
         "fr": "Le tourisme peut soutenir les communautés autochtones", "de": "Tourismus kann indigene Gemeinschaften unterstützen"},
        {"en": "Traditional medicine complements modern healthcare", "es": "La medicina tradicional complementa la atención médica moderna", "pt": "A medicina tradicional complementa os cuidados de saúde modernos",
         "fr": "La médecine traditionnelle complète les soins de santé modernes", "de": "Traditionelle Medizin ergänzt die moderne Gesundheitsversorgung"},
        {"en": "Indigenous leaders advocate for their rights", "es": "Los líderes indígenas defienden sus derechos", "pt": "Os líderes indígenas defendem seus direitos",
         "fr": "Les dirigeants autochtones défendent leurs droits", "de": "Indigene Führer setzen sich für ihre Rechte ein"}
    ]
}

# Day 24: Practical Daily Life - Transportation and Logistics
day24_phrases = {
    "Contemporary Slang in Argentina": [
        {"en": "Cool/Awesome", "es": "Zarpado/Re copado", "pt": "Maneiro/Muito legal",
         "fr": "Cool/Impressionnant", "de": "Cool/Spitze"},
        {"en": "Dude/Friend", "es": "Chabón/Pibe", "pt": "Cara/Mano",
         "fr": "Mec/Pote", "de": "Kumpel/Freund"},
        {"en": "What's up?", "es": "¿Qué onda?", "pt": "E aí?",
         "fr": "Quoi de neuf ?", "de": "Was geht?"},
        {"en": "To hang out", "es": "Juntarse/Salir de joda", "pt": "Dar um rolê",
         "fr": "Traîner", "de": "Abhängen"},
        {"en": "Money", "es": "Guita/Mango", "pt": "Grana/Bufunfa",
         "fr": "Pognon", "de": "Kohle"},
        {"en": "Work", "es": "Laburo", "pt": "Trampo",
         "fr": "Boulot", "de": "Job"},
        {"en": "Annoying/Bothersome", "es": "Embole/Bajón", "pt": "Chato/Um saco",
         "fr": "Relou", "de": "Nervig"},
        {"en": "Crazy/Insane", "es": "Flashero/Loco", "pt": "Pirado/Maluco",
         "fr": "Cinglé", "de": "Verrückt"},
        {"en": "Excellent/Great", "es": "De la hostia/Buenísimo", "pt": "Do caralho/Muito bom",
         "fr": "Génial", "de": "Spitze"},
        {"en": "To be angry", "es": "Estar caliente/Estar en llamas", "pt": "Estar puto/Estar pistola",
         "fr": "Être énervé", "de": "Sauer sein"}
    ],
    "Contemporary Slang in Brazil": [
        {"en": "Cool/Awesome", "es": "Legal/Massa", "pt": "Dahora/Maneiro",
         "fr": "Cool/Extra", "de": "Cool/Geil"},
        {"en": "Dude/Friend", "es": "Amigo/Compañero", "pt": "Mano/Parça",
         "fr": "Mec/Mon pote", "de": "Alter/Kumpel"},
        {"en": "What's up?", "es": "¿Qué pasa?", "pt": "Qual é?/E aí?",
         "fr": "Quoi de neuf ?", "de": "Was geht?"},
        {"en": "To hang out", "es": "Salir", "pt": "Dar um rolê/Curtir",
         "fr": "Traîner", "de": "Abhängen"},
        {"en": "Money", "es": "Dinero", "pt": "Grana/Bufunfa",
         "fr": "Pognon", "de": "Kohle"},
        {"en": "Work", "es": "Trabajo", "pt": "Trampo/Serviço",
         "fr": "Boulot", "de": "Job"},
        {"en": "Annoying/Bothersome", "es": "Molesto", "pt": "Chato/Um saco",
         "fr": "Relou", "de": "Nervig"},
        {"en": "Crazy/Insane", "es": "Loco", "pt": "Doido/Maluco",
         "fr": "Cinglé", "de": "Verrückt"},
        {"en": "Excellent/Great", "es": "Excelente", "pt": "Irado/Top",
         "fr": "Génial", "de": "Spitze"},
        {"en": "To be angry", "es": "Estar enojado", "pt": "Estar pistola/Estar bolado",
         "fr": "Être énervé", "de": "Sauer sein"}
    ],
    "Contemporary Slang in Colombia": [
        {"en": "Cool/Awesome", "es": "Chévere/Bacano", "pt": "Legal/Bacana",
         "fr": "Super", "de": "Prima"},
        {"en": "Dude/Friend", "es": "Parcero/Llave", "pt": "Parceiro/Amigo",
         "fr": "Pote", "de": "Kumpel"},
        {"en": "What's up?", "es": "¿Quiubo?/¿Qué más?", "pt": "E aí?/Como vai?",
         "fr": "Quoi de neuf ?", "de": "Was geht?"},
        {"en": "To hang out", "es": "Parchar/Rumbear", "pt": "Sair/Curtir",
         "fr": "Traîner", "de": "Abhängen"},
        {"en": "Money", "es": "Lucas/Plata", "pt": "Grana/Dinheiro",
         "fr": "Pognon", "de": "Kohle"},
        {"en": "Work", "es": "Camello", "pt": "Trabalho",
         "fr": "Boulot", "de": "Job"},
        {"en": "Annoying/Bothersome", "es": "Jartera/Mamera", "pt": "Chato/Irritante",
         "fr": "Chiant", "de": "Lästig"},
        {"en": "Crazy/Insane", "es": "Loco/Chiflado", "pt": "Louco/Maluco",
         "fr": "Cinglé", "de": "Verrückt"},
        {"en": "Excellent/Great", "es": "Áspero/Una chimba", "pt": "Excelente/Muito bom",
         "fr": "Génial", "de": "Spitze"},
        {"en": "To be angry", "es": "Estar emberracado/Estar ofendido", "pt": "Estar bravo/Estar irritado",
         "fr": "Être vénère", "de": "Sauer sein"}
    ],
    "Modern Workplace Slang": [
        {"en": "I'm swamped with work", "es": "Estoy hasta el cuello de trabajo", "pt": "Estou atolado de trabalho",
         "fr": "Je suis débordé au boulot", "de": "Ich bin mit Arbeit überhäuft"},
        {"en": "Let's touch base later", "es": "Hablemos más tarde", "pt": "Vamos nos alinhar mais tarde",
         "fr": "Retrouvons-nous plus tard", "de": "Lass uns später in Kontakt treten"},
        {"en": "I'm working remotely today", "es": "Hoy estoy trabajando remoto", "pt": "Estou trabalhando remotamente hoje",
         "fr": "Je travaille à distance aujourd'hui", "de": "Ich arbeite heute remote"},
        {"en": "Let's take this offline", "es": "Hablemos de esto en privado", "pt": "Vamos discutir isso em particular",
         "fr": "Parlons-en en privé", "de": "Lass uns das offline besprechen"},
        {"en": "I need to pick your brain", "es": "Necesito tu opinión", "pt": "Preciso da sua opinião",
         "fr": "J'ai besoin de ton avis", "de": "Ich muss deine Meinung einholen"},
        {"en": "Let's circle back on this", "es": "Volvamos a esto más tarde", "pt": "Vamos voltar a isso mais tarde",
         "fr": "Revenons à ce sujet plus tard", "de": "Lass uns später darauf zurückkommen"},
        {"en": "I'm multitasking", "es": "Estoy haciendo varias cosas a la vez", "pt": "Estou fazendo várias coisas ao mesmo tempo",
         "fr": "Je fais plusieurs choses à la fois", "de": "Ich mache mehrere Dinge gleichzeitig"},
        {"en": "That's not in my wheelhouse", "es": "Eso no es mi especialidad", "pt": "Isso não é minha especialidade",
         "fr": "Ce n'est pas vraiment mon domaine", "de": "Das liegt nicht in meinem Fachgebiet"},
        {"en": "Let's think outside the box", "es": "Pensemos de manera innovadora", "pt": "Vamos pensar fora da caixa",
         "fr": "Pensons en dehors des sentiers battus", "de": "Lass uns querdenken"},
        {"en": "I'll ping you later", "es": "Te aviso más tarde", "pt": "Te aviso mais tarde",
         "fr": "Je te contacte plus tard", "de": "Ich schreibe dir später"}
    ],
    "Digital Communication Slang": [
        {"en": "LOL (laughing out loud)", "es": "MDR (me da risa)", "pt": "RS (risos)",
         "fr": "MDR", "de": "LOL"},
        {"en": "OMG (oh my god)", "es": "¡Dios mío!", "pt": "OMG/Meu Deus!",
         "fr": "Oh mon dieu!", "de": "Oh mein Gott!"},
        {"en": "BTW (by the way)", "es": "Por cierto", "pt": "Por falar nisso",
         "fr": "Au fait", "de": "Übrigens"},
        {"en": "TBH (to be honest)", "es": "Para ser honesto", "pt": "Para ser sincero",
         "fr": "Pour être honnête", "de": "Um ehrlich zu sein"},
        {"en": "FOMO (fear of missing out)", "es": "Miedo a perderse algo", "pt": "Medo de estar perdendo algo",
         "fr": "Peur de rater quelque chose", "de": "Angst, etwas zu verpassen"},
        {"en": "Ghosting (disappearing from communication)", "es": "Fantasmear", "pt": "Dar um ghost",
         "fr": "Ghosting", "de": "Ghosting"},
        {"en": "Selfie", "es": "Selfie", "pt": "Selfie",
         "fr": "Selfie", "de": "Selfie"},
        {"en": "To Google something", "es": "Googlear algo", "pt": "Googlar algo",
         "fr": "Googler quelque chose", "de": "Etwas googeln"},
        {"en": "To tweet", "es": "Tuitear", "pt": "Tuitar",
         "fr": "Tweeter", "de": "Twittern"},
        {"en": "Influencer", "es": "Influencer", "pt": "Influenciador",
         "fr": "Influenceur", "de": "Influencer"}
    ]
}

# Dictionary mapping day numbers to phrase dictionaries
all_phrases = {
    16: day16_phrases,  # Finding Housing and Accommodation
    # 17: day17_phrases,  # Job Hunting in South America
    18: day18_phrases,  # Banking and Finance
    # 19: day19_phrases,  # Healthcare Systems
    20: day20_phrases,  # Regional Cultural Nuances
    # 21: day21_phrases,  # Workplace Language and Etiquette
    22: day22_phrases,  # Renting and Housing Vocabulary
    # 23: day23_phrases,  # Banking and Bureaucracy
    24: day24_phrases,  # Transportation and Logistics
    # 25: day25_phrases,  # Social Integration - Making Friends and Building Community
    # 26: day26_phrases,  # Social Integration - Dating, Safety, and Traditions
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
    
    # Generate audio
    tts = gTTS(text=text, lang=language_code)
    tts.save(f"audio_files/day{day}_{language_code}.mp3")
    
    elapsed = time.time() - start_time
    print(f"✓ Saved to audio_files/day{day}_{language_code}.mp3 ({elapsed:.2f}s)")

def main():
    parser = argparse.ArgumentParser(description="Generate language learning files for Living & Working in South America (Days 16-26)")
    parser.add_argument("--day", "-d", type=int, choices=list(range(16, 27)), default=None,
                        help="Day number to generate (16-26). If not specified, generates all available days.")
    parser.add_argument("--languages", "-l", nargs="+", choices=["es", "pt", "en", "fr", "de"], 
                        default=["es", "pt"], help="Languages to generate (es=Spanish, pt=Portuguese, en=English, fr=French, de=German)")
    parser.add_argument("--text-only", "-t", action="store_true", 
                        help="Generate only text files (no audio)")
    args = parser.parse_args()
    
    language_names = {"es": "Spanish", "pt": "Portuguese", "en": "English", "fr": "French", "de": "German"}
    
    # Check if we have content for the requested days
    available_days = list(all_phrases.keys())
    if not available_days:
        print("No content available yet. Please add content for days 16-26.")
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
        
        # Generate audio files if not text-only mode
        if not args.text_only:
            for lang in args.languages:
                generate_audio(day, lang, language_names[lang])
    
    print("\nAll files generated successfully!")
    print("\nUsage examples for PolyglotPathways:")
    print("  - Generate text files only: python language_phrases_advanced_extended.py --text-only")
    print("  - Generate files for just Day 16: python language_phrases_advanced_extended.py --day 16")
    print("  - Generate files for just Spanish: python language_phrases_advanced_extended.py --languages es")
    print("  - Generate Day 22 Portuguese text only: python language_phrases_advanced_extended.py --day 22 --languages pt --text-only")
    print("  - Generate all available days: python language_phrases_advanced_extended.py")

if __name__ == "__main__":
    main()