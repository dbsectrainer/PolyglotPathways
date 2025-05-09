import argparse
import os
import time
from gtts import gTTS

# This file contains days 16-26 of language phrases for PolyglotPathways
# It follows the same structure as previous scripts but includes content
# focusing on practical topics for living and working abroad, including housing, jobs,
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
    "Geography & Landscapes": [
        {"en": "This region has high mountains", "es": "Esta región tiene montañas altas", "pt": "Esta região tem montanhas altas",
         "fr": "Cette région a de hautes montagnes", "de": "Diese Region hat hohe Berge"},
        {"en": "A major river flows through the valley", "es": "Un río importante fluye por el valle", "pt": "Um rio importante flui pelo vale",
         "fr": "Une rivière majeure traverse la vallée", "de": "Ein großer Fluss fließt durch das Tal"},
        {"en": "The coastline features sandy beaches and rocky cliffs", "es": "La costa presenta playas de arena y acantilados rocosos", "pt": "A costa apresenta praias de areia e falésias rochosas",
         "fr": "Le littoral présente des plages de sable et des falaises rocheuses", "de": "Die Küste weist Sandstrände und felsige Klippen auf"},
        {"en": "There are vast forests in this area", "es": "Hay vastos bosques en esta área", "pt": "Existem vastas florestas nesta área",
         "fr": "Il y a de vastes forêts dans cette région", "de": "In dieser Gegend gibt es ausgedehnte Wälder"},
        {"en": "This large lake is popular for recreation", "es": "Este gran lago es popular para la recreación", "pt": "Este grande lago é popular para recreação",
         "fr": "Ce grand lac est populaire pour les loisirs", "de": "Dieser große See ist beliebt zur Erholung"},
        {"en": "The desert landscape extends for many kilometers", "es": "El paisaje desértico se extiende por muchos kilómetros", "pt": "A paisagem desértica se estende por muitos quilômetros",
         "fr": "Le paysage désertique s'étend sur de nombreux kilomètres", "de": "Die Wüstenlandschaft erstreckt sich über viele Kilometer"},
        {"en": "These islands have unique ecosystems", "es": "Estas islas tienen ecosistemas únicos", "pt": "Estas ilhas têm ecossistemas únicos",
         "fr": "Ces îles ont des écosystèmes uniques", "de": "Diese Inseln haben einzigartige Ökosysteme"},
        {"en": "The waterfall is a famous natural landmark", "es": "La cascada es un famoso hito natural", "pt": "A cachoeira é um famoso marco natural",
         "fr": "La cascade est un célèbre repère naturel", "de": "Der Wasserfall ist ein berühmtes Naturdenkmal"},
        {"en": "Fertile plains are used for agriculture", "es": "Las llanuras fértiles se utilizan para la agricultura", "pt": "As planícies férteis são usadas para a agricultura",
         "fr": "Les plaines fertiles sont utilisées pour l'agriculture", "de": "Fruchtbare Ebenen werden für die Landwirtschaft genutzt"},
        {"en": "Wetlands are important habitats for wildlife", "es": "Los humedales son hábitats importantes para la vida silvestre", "pt": "As zonas úmidas são habitats importantes para a vida selvagem",
         "fr": "Les zones humides sont des habitats importants pour la faune", "de": "Feuchtgebiete sind wichtige Lebensräume für Wildtiere"}
    ],
    "Climate & Weather": [
        {"en": "The climate varies depending on the region", "es": "El clima varía según la región", "pt": "O clima varia dependendo da região",
         "fr": "Le climat varie en fonction de la région", "de": "Das Klima variiert je nach Region"},
        {"en": "Some areas have distinct rainy and dry seasons", "es": "Algunas áreas tienen estaciones lluviosas y secas distintas", "pt": "Algumas áreas têm estações chuvosas e secas distintas",
         "fr": "Certaines régions ont des saisons des pluies et sèches distinctes", "de": "Einige Gebiete haben ausgeprägte Regen- und Trockenzeiten"},
        {"en": "It can be very humid in the dense forests", "es": "Puede ser muy húmedo en los bosques densos", "pt": "Pode ser muito úmido nas florestas densas",
         "fr": "Il peut faire très humide dans les forêts denses", "de": "In dichten Wäldern kann es sehr feucht sein"},
        {"en": "The highlands generally have cooler temperatures", "es": "Las tierras altas generalmente tienen temperaturas más frescas", "pt": "As terras altas geralmente têm temperaturas mais frescas",
         "fr": "Les hautes terres ont généralement des températures plus fraîches", "de": "Die Hochebenen haben im Allgemeinen kühlere Temperaturen"},
        {"en": "Coastal areas can experience fog", "es": "Las zonas costeras pueden experimentar niebla", "pt": "As áreas costeiras podem ter neblina",
         "fr": "Les zones côtières peuvent connaître du brouillard", "de": "Küstengebiete können Nebel erleben"},
        {"en": "We're expecting a thunderstorm later", "es": "Esperamos una tormenta eléctrica más tarde", "pt": "Estamos esperando uma tempestade mais tarde",
         "fr": "Nous prévoyons un orage plus tard", "de": "Wir erwarten später ein Gewitter"},
        {"en": "Temperature can vary greatly between day and night", "es": "La temperatura puede variar mucho entre el día y la noche", "pt": "A temperatura pode variar muito entre o dia e a noite",
         "fr": "La température peut varier considérablement entre le jour et la nuit", "de": "Die Temperatur kann zwischen Tag und Nacht stark variieren"},
        {"en": "Altitude significantly affects the local climate", "es": "La altitud afecta significativamente el clima local", "pt": "A altitude afeta significativamente o clima local",
         "fr": "L'altitude affecte considérablement le climat local", "de": "Die Höhe beeinflusst das lokale Klima erheblich"},
        {"en": "Weather patterns can influence daily activities", "es": "Los patrones climáticos pueden influir en las actividades diarias", "pt": "Os padrões climáticos podem influenciar as atividades diárias",
         "fr": "Les conditions météorologiques peuvent influencer les activités quotidiennes", "de": "Wettermuster können tägliche Aktivitäten beeinflussen"},
        {"en": "Microclimates can vary within short distances", "es": "Los microclimas pueden variar en distancias cortas", "pt": "Os microclimas podem variar em curtas distâncias",
         "fr": "Les microclimats peuvent varier sur de courtes distances", "de": "Mikroklimata können über kurze Distanzen variieren"}
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
    "Loanwords & Linguistic Influence": [
        {"en": "Many languages borrow words from others", "es": "Muchos idiomas toman prestadas palabras de otros", "pt": "Muitas línguas emprestam palavras de outras", "fr": "De nombreuses langues empruntent des mots à d'autres", "de": "Viele Sprachen leihen Wörter von anderen"},
        {"en": "'Ballet' comes from French", "es": "'Ballet' viene del francés", "pt": "'Ballet' vem do francês", "fr": "'Ballet' vient du français", "de": "'Ballett' kommt aus dem Französischen"},
        {"en": "'Algebra' has Arabic origins", "es": "'Álgebra' tiene orígenes árabes", "pt": "'Álgebra' tem origens árabes", "fr": "'Algèbre' a des origines arabes", "de": "'Algebra' hat arabische Ursprünge"},
        {"en": "'Schadenfreude' is a German loanword", "es": "'Schadenfreude' es un préstamo del alemán", "pt": "'Schadenfreude' é um empréstimo do alemão", "fr": "'Schadenfreude' est un emprunt de l'allemand", "de": "'Schadenfreude' ist ein deutsches Lehnwort"},
        {"en": "'Sofa' comes from Arabic 'suffah'", "es": "'Sofá' viene del árabe 'suffah'", "pt": "'Sofá' vem do árabe 'suffah'", "fr": "'Sofa' vient de l'arabe 'suffah'", "de": "'Sofa' kommt vom arabischen 'suffah'"},
        {"en": "'Café' is used in many languages", "es": "'Café' se usa en muchos idiomas", "pt": "'Café' é usado em muitas línguas", "fr": "'Café' est utilisé dans de nombreuses langues", "de": "'Café' wird in vielen Sprachen verwendet"},
        {"en": "'Tsunami' is a Japanese word", "es": "'Tsunami' es una palabra japonesa", "pt": "'Tsunami' é uma palavra japonesa", "fr": "'Tsunami' est un mot japonais", "de": "'Tsunami' ist ein japanisches Wort"},
        {"en": "'Guerilla' comes from Spanish", "es": "'Guerrilla' viene del español", "pt": "'Guerrilha' vem do espanhol", "fr": "'Guérilla' vient de l'espagnol", "de": "'Guerilla' kommt aus dem Spanischen"},
        {"en": "'Robot' was coined by a Czech writer", "es": "'Robot' fue acuñado por un escritor checo", "pt": "'Robot' foi cunhado por um escritor tcheco", "fr": "'Robot' a été inventé par un écrivain tchèque", "de": "'Roboter' wurde von einem tschechischen Schriftsteller geprägt"},
        {"en": "Understanding loanwords helps language learning", "es": "Entender los préstamos lingüísticos ayuda al aprendizaje de idiomas", "pt": "Entender empréstimos linguísticos ajuda no aprendizado de idiomas", "fr": "Comprendre les emprunts aide à l'apprentissage des langues", "de": "Das Verständnis von Lehnwörtern hilft beim Sprachenlernen"}
    ],
    "Historical & Cultural Heritage": [
        {"en": "Ancient ruins tell stories of past civilizations", "es": "Las ruinas antiguas cuentan historias de civilizaciones pasadas", "pt": "Ruínas antigas contam histórias de civilizações passadas", "fr": "Les ruines antiques racontent des histoires de civilisations passées", "de": "Antike Ruinen erzählen Geschichten vergangener Zivilisationen"},
        {"en": "Medieval castles are common in Europe", "es": "Los castillos medievales son comunes en Europa", "pt": "Castelos medievais são comuns na Europa", "fr": "Les châteaux médiévaux sont courants en Europe", "de": "Mittelalterliche Burgen sind in Europa verbreitet"},
        {"en": "Pre-Columbian sites reveal ancient American history", "es": "Los sitios precolombinos revelan la historia antigua de América", "pt": "Sítios pré-colombianos revelam a história antiga da América", "fr": "Les sites précolombiens révèlent l'histoire ancienne de l'Amérique", "de": "Präkolumbianische Stätten enthüllen die alte Geschichte Amerikas"},
        {"en": "Roman aqueducts are impressive engineering feats", "es": "Los acueductos romanos son impresionantes hazañas de ingeniería", "pt": "Os aquedutos romanos são impressionantes feitos de engenharia", "fr": "Les aqueducs romains sont d'impressionnantes prouesses d'ingénierie", "de": "Römische Aquädukte sind beeindruckende Ingenieursleistungen"},
        {"en": "Viking longships explored distant lands", "es": "Los drakkars vikingos exploraron tierras lejanas", "pt": "Os dracares vikings exploraram terras distantes", "fr": "Les drakkars vikings ont exploré des terres lointaines", "de": "Wikinger-Langschiffe erkundeten ferne Länder"},
        {"en": "Many cultures have complex mythologies", "es": "Muchas culturas tienen mitologías complejas", "pt": "Muitas culturas têm mitologias complexas", "fr": "De nombreuses cultures ont des mythologies complexes", "de": "Viele Kulturen haben komplexe Mythologien"},
        {"en": "Historical trade routes connected continents", "es": "Las rutas comerciales históricas conectaban continentes", "pt": "Rotas comerciais históricas conectavam continentes", "fr": "Les routes commerciales historiques reliaient les continents", "de": "Historische Handelsrouten verbanden Kontinente"},
        {"en": "Colonial architecture reflects historical influences", "es": "La arquitectura colonial refleja influencias históricas", "pt": "A arquitetura colonial reflete influências históricas", "fr": "L'architecture coloniale reflète les influences historiques", "de": "Kolonialarchitektur spiegelt historische Einflüsse wider"},
        {"en": "Archaeological sites offer glimpses into the past", "es": "Los sitios arqueológicos ofrecen vistazos al pasado", "pt": "Sítios arqueológicos oferecem vislumbres do passado", "fr": "Les sites archéologiques offrent des aperçus du passé", "de": "Archäologische Stätten bieten Einblicke in die Vergangenheit"},
        {"en": "Preserving cultural heritage is important", "es": "Preservar el patrimonio cultural es importante", "pt": "Preservar o patrimônio cultural é importante", "fr": "Préserver le patrimoine culturel est important", "de": "Die Bewahrung des Kulturerbes ist wichtig"}
    ],
    "Traditional Knowledge & Practices": [
        {"en": "Traditional medicine often uses local plants", "es": "La medicina tradicional suele usar plantas locales", "pt": "A medicina tradicional frequentemente usa plantas locais", "fr": "La médecine traditionnelle utilise souvent des plantes locales", "de": "Traditionelle Medizin verwendet oft lokale Pflanzen"},
        {"en": "Spiritual healers play roles in some cultures", "es": "Los sanadores espirituales juegan roles en algunas culturas", "pt": "Curandeiros espirituais desempenham papéis em algumas culturas", "fr": "Les guérisseurs spirituels jouent un rôle dans certaines cultures", "de": "Spirituelle Heiler spielen in einigen Kulturen eine Rolle"},
        {"en": "Weaving techniques are passed down generations", "es": "Las técnicas de tejido se transmiten por generaciones", "pt": "As técnicas de tecelagem são transmitidas por gerações", "fr": "Les techniques de tissage se transmettent de génération en génération", "de": "Webtechniken werden über Generationen weitergegeben"},
        {"en": "Terrace farming is an ancient agricultural method", "es": "La agricultura en terrazas es un método agrícola antiguo", "pt": "A agricultura em terraços é um método agrícola antigo", "fr": "L'agriculture en terrasses est une méthode agricole ancienne", "de": "Terrassenfeldbau ist eine alte landwirtschaftliche Methode"},
        {"en": "Traditional fishing methods can be sustainable", "es": "Los métodos tradicionales de pesca pueden ser sostenibles", "pt": "Os métodos tradicionais de pesca podem ser sustentáveis", "fr": "Les méthodes de pêche traditionnelles peuvent être durables", "de": "Traditionelle Fischfangmethoden können nachhaltig sein"},
        {"en": "Pottery techniques date back thousands of years", "es": "Las técnicas de cerámica datan de miles de años", "pt": "As técnicas de cerâmica datam de milhares de anos", "fr": "Les techniques de poterie remontent à des milliers d'années", "de": "Töpfertechniken reichen Tausende von Jahren zurück"},
        {"en": "Traditional navigation sometimes uses stars", "es": "La navegación tradicional a veces usa las estrellas", "pt": "A navegação tradicional às vezes usa as estrelas", "fr": "La navigation traditionnelle utilise parfois les étoiles", "de": "Traditionelle Navigation nutzt manchmal Sterne"},
        {"en": "Oral traditions preserve cultural knowledge", "es": "Las tradiciones orales preservan el conocimiento cultural", "pt": "As tradições orais preservam o conhecimento cultural", "fr": "Les traditions orales préservent le savoir culturel", "de": "Mündliche Überlieferungen bewahren kulturelles Wissen"},
        {"en": "Traditional architecture often uses local materials", "es": "La arquitectura tradicional suele usar materiales locales", "pt": "A arquitetura tradicional frequentemente usa materiais locais", "fr": "L'architecture traditionnelle utilise souvent des matériaux locaux", "de": "Traditionelle Architektur verwendet oft lokale Materialien"},
        {"en": "Ancestral farming practices are still used today", "es": "Las prácticas agrícolas ancestrales todavía se usan hoy", "pt": "As práticas agrícolas ancestrais ainda são usadas hoje", "fr": "Les pratiques agricoles ancestrales sont encore utilisées aujourd'hui", "de": "Alte landwirtschaftliche Praktiken werden heute noch angewendet"}
    ],
    "Cultural Celebrations & Festivals": [
        {"en": "Many cultures celebrate the New Year", "es": "Muchas culturas celebran el Año Nuevo", "pt": "Muitas culturas celebram o Ano Novo", "fr": "De nombreuses cultures célèbrent le Nouvel An", "de": "Viele Kulturen feiern das Neujahr"},
        {"en": "Carnival is a major celebration in many places", "es": "El Carnaval es una celebración importante en muchos lugares", "pt": "O Carnaval é uma celebração importante em muitos lugares", "fr": "Le Carnaval est une célébration majeure dans de nombreux endroits", "de": "Karneval ist an vielen Orten eine wichtige Feier"},
        {"en": "Oktoberfest is a famous German festival", "es": "El Oktoberfest es un famoso festival alemán", "pt": "A Oktoberfest é um famoso festival alemão", "fr": "L'Oktoberfest est un célèbre festival allemand", "de": "Das Oktoberfest ist ein berühmtes deutsches Fest"},
        {"en": "Traditional dances often tell stories", "es": "Las danzas tradicionales suelen contar historias", "pt": "As danças tradicionais frequentemente contam histórias", "fr": "Les danses traditionnelles racontent souvent des histoires", "de": "Traditionelle Tänze erzählen oft Geschichten"},
        {"en": "Harvest festivals celebrate agricultural abundance", "es": "Las fiestas de la cosecha celebran la abundancia agrícola", "pt": "Os festivais da colheita celebram a abundância agrícola", "fr": "Les fêtes des récoltes célèbrent l'abondance agricole", "de": "Erntedankfeste feiern die landwirtschaftliche Fülle"},
        {"en": "Midsummer is celebrated in Nordic countries", "es": "El solsticio de verano se celebra en los países nórdicos", "pt": "O solstício de verão é celebrado nos países nórdicos", "fr": "La Saint-Jean est célébrée dans les pays nordiques", "de": "Mittsommer wird in nordischen Ländern gefeiert"},
        {"en": "Music is central to many celebrations", "es": "La música es central en muchas celebraciones", "pt": "A música é central em muitas celebrações", "fr": "La musique est au cœur de nombreuses célébrations", "de": "Musik ist zentral für viele Feiern"},
        {"en": "Traditional costumes are worn during festivals", "es": "Se usan trajes tradicionales durante los festivales", "pt": "Roupas tradicionais são usadas durante os festivais", "fr": "Les costumes traditionnels sont portés pendant les festivals", "de": "Traditionelle Kostüme werden während Festivals getragen"},
        {"en": "Religious holidays are important in many cultures", "es": "Las festividades religiosas son importantes en muchas culturas", "pt": "Feriados religiosos são importantes em muitas culturas", "fr": "Les fêtes religieuses sont importantes dans de nombreuses cultures", "de": "Religiöse Feiertage sind in vielen Kulturen wichtig"},
        {"en": "Festivals often strengthen community bonds", "es": "Los festivales suelen fortalecer los lazos comunitarios", "pt": "Os festivais frequentemente fortalecem os laços comunitários", "fr": "Les festivals renforcent souvent les liens communautaires", "de": "Festivals stärken oft die Gemeinschaftsbande"}
    ],
    "Cultural Communities & Modern Issues": [
        {"en": "Many cultural communities face modern challenges", "es": "Muchas comunidades culturales enfrentan desafíos modernos", "pt": "Muitas comunidades culturais enfrentam desafios modernos", "fr": "De nombreuses communautés culturelles font face à des défis modernes", "de": "Viele Kulturgemeinschaften stehen vor modernen Herausforderungen"},
        {"en": "Minority rights are an important issue globally", "es": "Los derechos de las minorías son un tema importante a nivel mundial", "pt": "Os direitos das minorias são uma questão importante globalmente", "fr": "Les droits des minorités sont une question importante au niveau mondial", "de": "Minderheitenrechte sind weltweit ein wichtiges Thema"},
        {"en": "Regional languages are being revitalized", "es": "Las lenguas regionales están siendo revitalizadas", "pt": "As línguas regionais estão sendo revitalizadas", "fr": "Les langues régionales sont en cours de revitalisation", "de": "Regionalsprachen werden wiederbelebt"},
        {"en": "Cultural knowledge is valuable for society", "es": "El conocimiento cultural es valioso para la sociedad", "pt": "O conhecimento cultural é valioso para a sociedade", "fr": "Le savoir culturel est précieux pour la société", "de": "Kulturelles Wissen ist wertvoll für die Gesellschaft"},
        {"en": "Many communities work to maintain their traditions", "es": "Muchas comunidades trabajan para mantener sus tradiciones", "pt": "Muitas comunidades trabalham para manter suas tradições", "fr": "De nombreuses communautés s'efforcent de maintenir leurs traditions", "de": "Viele Gemeinschaften arbeiten daran, ihre Traditionen zu bewahren"},
        {"en": "Local art forms gain international recognition", "es": "Las formas de arte locales ganan reconocimiento internacional", "pt": "Formas de arte locais ganham reconhecimento internacional", "fr": "Les formes d'art locales obtiennent une reconnaissance internationale", "de": "Lokale Kunstformen gewinnen internationale Anerkennung"},
        {"en": "Education often includes cultural awareness", "es": "La educación a menudo incluye la conciencia cultural", "pt": "A educação frequentemente inclui a consciência cultural", "fr": "L'éducation inclut souvent la sensibilisation culturelle", "de": "Bildung beinhaltet oft kulturelles Bewusstsein"},
        {"en": "Sustainable tourism can support local communities", "es": "El turismo sostenible puede apoyar a las comunidades locales", "pt": "O turismo sustentável pode apoiar comunidades locais", "fr": "Le tourisme durable peut soutenir les communautés locales", "de": "Nachhaltiger Tourismus kann lokale Gemeinschaften unterstützen"},
        {"en": "Traditional practices can complement modern life", "es": "Las prácticas tradicionales pueden complementar la vida moderna", "pt": "Práticas tradicionais podem complementar a vida moderna", "fr": "Les pratiques traditionnelles peuvent compléter la vie moderne", "de": "Traditionelle Praktiken können das moderne Leben ergänzen"},
        {"en": "Community leaders advocate for cultural preservation", "es": "Los líderes comunitarios abogan por la preservación cultural", "pt": "Líderes comunitários defendem a preservação cultural", "fr": "Les dirigeants communautaires plaident pour la préservation culturelle", "de": "Gemeinschaftsführer setzen sich für den Kulturerhalt ein"}
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
    "Contemporary Slang in France": [
        {"en": "Cool/Awesome", "es": "Genial", "pt": "Legal",
         "fr": "Stylé/Kiffant", "de": "Cool/Spitze"},
        {"en": "Dude/Friend", "es": "Tío/Amigo", "pt": "Cara/Amigo",
         "fr": "Mec/Pote", "de": "Kumpel/Freund"},
        {"en": "What's up?", "es": "¿Qué pasa?", "pt": "E aí?",
         "fr": "Ça roule?/Quoi de neuf?", "de": "Was geht?"},
        {"en": "To hang out", "es": "Pasar el rato", "pt": "Sair",
         "fr": "Traîner/Se poser", "de": "Abhängen"},
        {"en": "Money", "es": "Dinero", "pt": "Dinheiro",
         "fr": "Thune/Fric/Blé", "de": "Kohle"},
        {"en": "Work", "es": "Trabajo", "pt": "Trabalho",
         "fr": "Boulot/Taf", "de": "Job"},
        {"en": "Annoying/Bothersome", "es": "Molesto", "pt": "Chato",
         "fr": "Relou/Chiante", "de": "Nervig"},
        {"en": "Crazy/Insane", "es": "Loco", "pt": "Louco",
         "fr": "Ouf/Dingue/Taré", "de": "Verrückt"},
        {"en": "Excellent/Great", "es": "Excelente", "pt": "Ótimo",
         "fr": "Nickel/Au top", "de": "Spitze"},
        {"en": "To be angry", "es": "Estar enfadado", "pt": "Estar zangado",
         "fr": "Avoir le seum/Être vénère", "de": "Sauer sein"}
    ],
    "Contemporary Slang in Germany": [
        {"en": "Cool/Awesome", "es": "Genial", "pt": "Legal",
         "fr": "Cool", "de": "Geil/Krass/Hammer"},
        {"en": "Dude/Friend", "es": "Tío/Amigo", "pt": "Cara/Amigo",
         "fr": "Mec", "de": "Alter/Digga/Kollege"},
        {"en": "What's up?", "es": "¿Qué pasa?", "pt": "E aí?",
         "fr": "Quoi de neuf?", "de": "Was geht?/Na?"},
        {"en": "To hang out", "es": "Pasar el rato", "pt": "Sair",
         "fr": "Traîner", "de": "Abhängen/Chillen"},
        {"en": "Money", "es": "Dinero", "pt": "Dinheiro",
         "fr": "Argent", "de": "Kohle/Knete/Asche"},
        {"en": "Work", "es": "Trabajo", "pt": "Trabalho",
         "fr": "Travail", "de": "Job/Arbeit"},
        {"en": "Annoying/Bothersome", "es": "Molesto", "pt": "Chato",
         "fr": "Ennuyeux", "de": "Nervig/Ätzend"},
        {"en": "Crazy/Insane", "es": "Loco", "pt": "Louco",
         "fr": "Fou", "de": "Verrückt/Irre/Bekloppt"},
        {"en": "Excellent/Great", "es": "Excelente", "pt": "Ótimo",
         "fr": "Excellent", "de": "Spitze/Super/Toll"},
        {"en": "To be angry", "es": "Estar enfadado", "pt": "Estar zangado",
         "fr": "Être en colère", "de": "Sauer sein/Angepisst sein"}
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
        {"en": "I need to pick your brain", "es": "Necesito tu opinión", "pt": "Preciso da sua opinión",
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

# Day 26: Social Integration - Dating, Safety, and Traditions
day26_phrases = {
    "Dating and Relationships": [
        {"en": "Would you like to go out sometime?", "es": "¿Te gustaría salir alguna vez?", "pt": "Gostaria de sair alguma vez?",
         "fr": "Voudrais-tu sortir un de ces jours?", "de": "Hättest du Lust, mal auszugehen?"},
        {"en": "I'm interested in getting to know you better", "es": "Estoy interesado/a en conocerte mejor", "pt": "Estou interessado/a em te conhecer melhor",
         "fr": "Je suis intéressé(e) à mieux te connaître", "de": "Ich bin daran interessiert, dich besser kennenzulernen"},
        {"en": "Are you seeing anyone?", "es": "¿Estás saliendo con alguien?", "pt": "Você está saindo com alguém?",
         "fr": "Est-ce que tu vois quelqu'un?", "de": "Triffst du dich mit jemandem?"},
        {"en": "I had a great time with you", "es": "La pasé muy bien contigo", "pt": "Passei um ótimo tempo com você",
         "fr": "J'ai passé un bon moment avec toi", "de": "Ich hatte eine tolle Zeit mit dir"},
        {"en": "What are your relationship expectations?", "es": "¿Cuáles son tus expectativas de relación?", "pt": "Quais são suas expectativas de relacionamento?",
         "fr": "Quelles sont tes attentes en matière de relation?", "de": "Was sind deine Beziehungserwartungen?"},
        {"en": "I'd like to take things slowly", "es": "Me gustaría tomar las cosas con calma", "pt": "Gostaria de ir devagar",
         "fr": "J'aimerais prendre les choses lentement", "de": "Ich würde gerne langsam vorgehen"},
        {"en": "Can I have your number?", "es": "¿Puedo tener tu número?", "pt": "Posso ter seu número?",
         "fr": "Puis-je avoir ton numéro?", "de": "Kann ich deine Nummer haben?"},
        {"en": "I'm looking for a serious relationship", "es": "Estoy buscando una relación seria", "pt": "Estou procurando um relacionamento sério",
         "fr": "Je cherche une relation sérieuse", "de": "Ich suche eine ernsthafte Beziehung"},
        {"en": "I'm just interested in friendship right now", "es": "Solo estoy interesado/a en amistad por ahora", "pt": "Estou apenas interessado/a em amizade no momento",
         "fr": "Je suis juste intéressé(e) par l'amitié en ce moment", "de": "Ich bin im Moment nur an Freundschaft interessiert"},
        {"en": "What do you like to do on dates?", "es": "¿Qué te gusta hacer en las citas?", "pt": "O que você gosta de fazer em encontros?",
         "fr": "Qu'aimes-tu faire lors des rendez-vous?", "de": "Was machst du gerne bei Dates?"}
    ],
    "Personal Safety": [
        {"en": "Is this neighborhood safe at night?", "es": "¿Este vecindario es seguro por la noche?", "pt": "Este bairro é seguro à noite?",
         "fr": "Ce quartier est-il sûr la nuit?", "de": "Ist diese Nachbarschaft nachts sicher?"},
        {"en": "Who should I contact in an emergency?", "es": "¿A quién debo contactar en una emergencia?", "pt": "Quem devo contatar em uma emergência?",
         "fr": "Qui dois-je contacter en cas d'urgence?", "de": "Wen sollte ich im Notfall kontaktieren?"},
        {"en": "What areas should I avoid?", "es": "¿Qué áreas debo evitar?", "pt": "Quais áreas devo evitar?",
         "fr": "Quelles zones dois-je éviter?", "de": "Welche Gebiete sollte ich meiden?"},
        {"en": "Is it safe to use public transportation at night?", "es": "¿Es seguro usar el transporte público por la noche?", "pt": "É seguro usar transporte público à noite?",
         "fr": "Est-il sûr d'utiliser les transports en commun la nuit?", "de": "Ist es sicher, nachts öffentliche Verkehrsmittel zu benutzen?"},
        {"en": "What's the emergency number here?", "es": "¿Cuál es el número de emergencia aquí?", "pt": "Qual é o número de emergência aqui?",
         "fr": "Quel est le numéro d'urgence ici?", "de": "Was ist hier die Notrufnummer?"},
        {"en": "I don't feel comfortable with this situation", "es": "No me siento cómodo/a con esta situación", "pt": "Não me sinto confortável com esta situação",
         "fr": "Je ne me sens pas à l'aise avec cette situation", "de": "Ich fühle mich in dieser Situation nicht wohl"},
        {"en": "Where is the nearest police station?", "es": "¿Dónde está la comisaría más cercana?", "pt": "Onde fica a delegacia mais próxima?",
         "fr": "Où se trouve le poste de police le plus proche?", "de": "Wo ist die nächste Polizeistation?"},
        {"en": "How can I report suspicious activity?", "es": "¿Cómo puedo reportar actividad sospechosa?", "pt": "Como posso relatar atividade suspeita?",
         "fr": "Comment puis-je signaler une activité suspecte?", "de": "Wie kann ich verdächtige Aktivitäten melden?"},
        {"en": "Are there safety apps you recommend?", "es": "¿Hay aplicaciones de seguridad que recomiendes?", "pt": "Existem aplicativos de segurança que você recomenda?",
         "fr": "Y a-t-il des applications de sécurité que tu recommandes?", "de": "Gibt es Sicherheits-Apps, die du empfiehlst?"},
        {"en": "I need help, please", "es": "Necesito ayuda, por favor", "pt": "Preciso de ajuda, por favor",
         "fr": "J'ai besoin d'aide, s'il te plaît", "de": "Ich brauche Hilfe, bitte"}
    ],
    "Local Traditions": [
        {"en": "What are the important holidays here?", "es": "¿Cuáles son las festividades importantes aquí?", "pt": "Quais são os feriados importantes aqui?",
         "fr": "Quelles sont les fêtes importantes ici?", "de": "Was sind die wichtigen Feiertage hier?"},
        {"en": "How do you celebrate this tradition?", "es": "¿Cómo celebran esta tradición?", "pt": "Como vocês celebram esta tradição?",
         "fr": "Comment célébrez-vous cette tradition?", "de": "Wie feiert ihr diese Tradition?"},
        {"en": "What's the significance of this ceremony?", "es": "¿Cuál es el significado de esta ceremonia?", "pt": "Qual é o significado desta cerimônia?",
         "fr": "Quelle est la signification de cette cérémonie?", "de": "Was ist die Bedeutung dieser Zeremonie?"},
        {"en": "Are there any local superstitions?", "es": "¿Hay alguna superstición local?", "pt": "Existem superstições locais?",
         "fr": "Y a-t-il des superstitions locales?", "de": "Gibt es lokale Aberglauben?"},
        {"en": "What traditional foods are important here?", "es": "¿Qué comidas tradicionales son importantes aquí?", "pt": "Quais alimentos tradicionais são importantes aqui?",
         "fr": "Quels aliments traditionnels sont importants ici?", "de": "Welche traditionellen Speisen sind hier wichtig?"},
        {"en": "Can I participate in this festival?", "es": "¿Puedo participar en este festival?", "pt": "Posso participar deste festival?",
         "fr": "Puis-je participer à ce festival?", "de": "Kann ich an diesem Festival teilnehmen?"},
        {"en": "What should I wear to this event?", "es": "¿Qué debo usar para este evento?", "pt": "O que devo vestir para este evento?",
         "fr": "Que dois-je porter pour cet événement?", "de": "Was soll ich zu dieser Veranstaltung anziehen?"},
        {"en": "What's the history behind this tradition?", "es": "¿Cuál es la historia detrás de esta tradición?", "pt": "Qual é a história por trás desta tradição?",
         "fr": "Quelle est l'histoire derrière cette tradition?", "de": "Was ist die Geschichte hinter dieser Tradition?"},
        {"en": "Are there any taboos I should know about?", "es": "¿Hay algún tabú que deba conocer?", "pt": "Existem tabus que eu deva conhecer?",
         "fr": "Y a-t-il des tabous que je devrais connaître?", "de": "Gibt es Tabus, die ich kennen sollte?"},
        {"en": "How has this tradition evolved over time?", "es": "¿Cómo ha evolucionado esta tradición con el tiempo?", "pt": "Como esta tradição evoluiu ao longo do tempo?",
         "fr": "Comment cette tradition a-t-elle évolué au fil du temps?", "de": "Wie hat sich diese Tradition im Laufe der Zeit entwickelt?"}
    ],
    "Social Customs": [
        {"en": "How do people typically greet each other?", "es": "¿Cómo se saludan típicamente las personas?", "pt": "Como as pessoas geralmente se cumprimentam?",
         "fr": "Comment les gens se saluent-ils généralement?", "de": "Wie begrüßen sich die Menschen typischerweise?"},
        {"en": "Is it customary to tip here?", "es": "¿Es costumbre dar propina aquí?", "pt": "É costume dar gorjeta aqui?",
         "fr": "Est-il coutumier de donner un pourboire ici?", "de": "Ist es hier üblich, Trinkgeld zu geben?"},
        {"en": "What's the proper way to address someone?", "es": "¿Cuál es la forma adecuada de dirigirse a alguien?", "pt": "Qual é a maneira adequada de se dirigir a alguém?",
         "fr": "Quelle est la bonne façon de s'adresser à quelqu'un?", "de": "Was ist die richtige Art, jemanden anzusprechen?"},
        {"en": "How do I show respect in this culture?", "es": "¿Cómo muestro respeto en esta cultura?", "pt": "Como demonstro respeito nesta cultura?",
         "fr": "Comment montrer du respect dans cette culture?", "de": "Wie zeige ich Respekt in dieser Kultur?"},
        {"en": "What gestures are considered rude?", "es": "¿Qué gestos se consideran groseros?", "pt": "Quais gestos são considerados rudes?",
         "fr": "Quels gestes sont considérés comme impolis?", "de": "Welche Gesten gelten als unhöflich?"},
        {"en": "How do people typically socialize here?", "es": "¿Cómo suele socializar la gente aquí?", "pt": "Como as pessoas geralmente socializam aqui?",
         "fr": "Comment les gens socialisent-ils généralement ici?", "de": "Wie pflegen Menschen hier typischerweise soziale Kontakte?"},
        {"en": "What's the etiquette for visiting someone's home?", "es": "¿Cuál es la etiqueta para visitar la casa de alguien?", "pt": "Qual é a etiqueta para visitar a casa de alguém?",
         "fr": "Quelle est l'étiquette pour visiter la maison de quelqu'un?", "de": "Was ist die Etikette für den Besuch bei jemandem zu Hause?"},
        {"en": "How do I politely refuse something?", "es": "¿Cómo rechazo algo educadamente?", "pt": "Como recuso algo educadamente?",
         "fr": "Comment refuser poliment quelque chose?", "de": "Wie lehne ich höflich etwas ab?"},
        {"en": "What's considered appropriate personal space?", "es": "¿Qué se considera un espacio personal apropiado?", "pt": "O que é considerado um espaço pessoal apropriado?",
         "fr": "Qu'est-ce qui est considéré comme un espace personnel approprié?", "de": "Was gilt als angemessener persönlicher Raum?"},
        {"en": "How important is eye contact in conversation?", "es": "¿Qué tan importante es el contacto visual en la conversación?", "pt": "Quão importante é o contato visual na conversa?",
         "fr": "Quelle est l'importance du contact visuel dans la conversation?", "de": "Wie wichtig ist Augenkontakt im Gespräch?"}
    ],
    "Cultural Sensitivity": [
        {"en": "I'd like to learn about your cultural values", "es": "Me gustaría aprender sobre tus valores culturales", "pt": "Gostaria de aprender sobre seus valores culturais",
         "fr": "J'aimerais en apprendre davantage sur vos valeurs culturelles", "de": "Ich würde gerne etwas über eure kulturellen Werte erfahren"},
        {"en": "Please let me know if I'm being inappropriate", "es": "Por favor, avísame si estoy siendo inapropiado/a", "pt": "Por favor, me avise se eu estiver sendo inapropriado/a",
         "fr": "S'il te plaît, fais-moi savoir si je suis inapproprié(e)", "de": "Bitte lass mich wissen, wenn ich mich unangemessen verhalte"},
        {"en": "I apologize if I've offended you", "es": "Me disculpo si te he ofendido", "pt": "Peço desculpas se te ofendi",
         "fr": "Je m'excuse si je t'ai offensé(e)", "de": "Ich entschuldige mich, wenn ich dich beleidigt habe"},
        {"en": "I'm trying to understand your perspective", "es": "Estoy tratando de entender tu perspectiva", "pt": "Estou tentando entender sua perspectiva",
         "fr": "J'essaie de comprendre ton point de vue", "de": "Ich versuche, deine Perspektive zu verstehen"},
        {"en": "What's the significance of this cultural practice?", "es": "¿Cuál es el significado de esta práctica cultural?", "pt": "Qual é o significado desta prática cultural?",
         "fr": "Quelle est la signification de cette pratique culturelle?", "de": "Was ist die Bedeutung dieser kulturellen Praxis?"},
        {"en": "I respect your cultural traditions", "es": "Respeto tus tradiciones culturales", "pt": "Respeito suas tradições culturais",
         "fr": "Je respecte tes traditions culturelles", "de": "Ich respektiere deine kulturellen Traditionen"},
        {"en": "How can I be more culturally aware?", "es": "¿Cómo puedo ser más consciente culturalmente?", "pt": "Como posso ser mais consciente culturalmente?",
         "fr": "Comment puis-je être plus conscient(e) culturellement?", "de": "Wie kann ich kulturell bewusster sein?"},
        {"en": "I'd like to avoid cultural misunderstandings", "es": "Me gustaría evitar malentendidos culturales", "pt": "Gostaria de evitar mal-entendidos culturais",
         "fr": "J'aimerais éviter les malentendus culturels", "de": "Ich möchte kulturelle Missverständnisse vermeiden"},
        {"en": "What's considered respectful behavior here?", "es": "¿Qué se considera un comportamiento respetuoso aquí?", "pt": "O que é considerado um comportamento respeitoso aqui?",
         "fr": "Qu'est-ce qui est considéré comme un comportement respectueux ici?", "de": "Was gilt hier als respektvolles Verhalten?"},
        {"en": "I appreciate you sharing your culture with me", "es": "Agradezco que compartas tu cultura conmigo", "pt": "Agradeço por compartilhar sua cultura comigo",
         "fr": "J'apprécie que tu partages ta culture avec moi", "de": "Ich schätze es, dass du deine Kultur mit mir teilst"}
    ]
}

# Day 25: Social Integration - Making Friends and Building Community
day25_phrases = {
    "Making Friends": [
        {"en": "Would you like to grab a coffee sometime?", "es": "¿Te gustaría tomar un café alguna vez?", "pt": "Gostaria de tomar um café qualquer dia?",
         "fr": "Ça te dirait de prendre un café un de ces jours?", "de": "Hättest du Lust, mal einen Kaffee trinken zu gehen?"},
        {"en": "I'm new to the area", "es": "Soy nuevo/a en la zona", "pt": "Sou novo/a na área",
         "fr": "Je suis nouveau dans le coin", "de": "Ich bin neu in der Gegend"},
        {"en": "Let's exchange contact information", "es": "Intercambiemos información de contacto", "pt": "Vamos trocar informações de contato",
         "fr": "Échangeons nos coordonnées", "de": "Lass uns Kontaktinformationen austauschen"},
        {"en": "I'd love to get to know you better", "es": "Me encantaría conocerte mejor", "pt": "Adoraria te conhecer melhor",
         "fr": "J'aimerais bien mieux te connaître", "de": "Ich würde dich gerne besser kennenlernen"},
        {"en": "Do you have any recommendations for local spots?", "es": "¿Tienes recomendaciones de lugares locales?", "pt": "Você tem recomendações de lugares locais?",
         "fr": "As-tu des recommandations d'endroits locaux?", "de": "Hast du Empfehlungen für lokale Orte?"},
        {"en": "Would you like to join our group?", "es": "¿Te gustaría unirte a nuestro grupo?", "pt": "Gostaria de se juntar ao nosso grupo?",
         "fr": "Voudrais-tu rejoindre notre groupe?", "de": "Möchtest du dich unserer Gruppe anschließen?"},
        {"en": "I'm looking to make new friends", "es": "Estoy buscando hacer nuevos amigos", "pt": "Estou procurando fazer novos amigos",
         "fr": "Je cherche à me faire de nouveaux amis", "de": "Ich suche nach neuen Freunden"},
        {"en": "What do you do in your free time?", "es": "¿Qué haces en tu tiempo libre?", "pt": "O que você faz no seu tempo livre?",
         "fr": "Que fais-tu pendant ton temps libre?", "de": "Was machst du in deiner Freizeit?"},
        {"en": "Let's plan to meet up again soon", "es": "Planeemos reunirnos de nuevo pronto", "pt": "Vamos planejar nos encontrar novamente em breve",
         "fr": "Prévoyons de nous revoir bientôt", "de": "Lass uns planen, uns bald wieder zu treffen"},
        {"en": "I'm interested in your culture", "es": "Estoy interesado/a en tu cultura", "pt": "Estou interessado/a na sua cultura",
         "fr": "Je m'intéresse à ta culture", "de": "Ich interessiere mich für deine Kultur"}
    ],
    "Community Activities": [
        {"en": "Is there a community center nearby?", "es": "¿Hay un centro comunitario cerca?", "pt": "Existe um centro comunitário por perto?",
         "fr": "Y a-t-il un centre communautaire à proximité?", "de": "Gibt es ein Gemeindezentrum in der Nähe?"},
        {"en": "I'd like to volunteer in the community", "es": "Me gustaría ser voluntario/a en la comunidad", "pt": "Gostaria de ser voluntário/a na comunidade",
         "fr": "J'aimerais faire du bénévolat dans la communauté", "de": "Ich würde gerne in der Gemeinschaft ehrenamtlich tätig sein"},
        {"en": "Are there any local festivals coming up?", "es": "¿Hay festivales locales próximamente?", "pt": "Existem festivais locais em breve?",
         "fr": "Y a-t-il des festivals locaux à venir?", "de": "Stehen lokale Festivals bevor?"},
        {"en": "I'm interested in joining a sports club", "es": "Estoy interesado/a en unirme a un club deportivo", "pt": "Estou interessado/a em me juntar a um clube esportivo",
         "fr": "Je suis intéressé(e) à rejoindre un club sportif", "de": "Ich bin daran interessiert, einem Sportverein beizutreten"},
        {"en": "Do you know of any community gardens?", "es": "¿Conoces algún jardín comunitario?", "pt": "Você conhece alguma horta comunitária?",
         "fr": "Connais-tu des jardins communautaires?", "de": "Kennst du Gemeinschaftsgärten?"},
        {"en": "I'd like to attend a local cooking class", "es": "Me gustaría asistir a una clase de cocina local", "pt": "Gostaria de participar de uma aula de culinária local",
         "fr": "J'aimerais assister à un cours de cuisine local", "de": "Ich würde gerne an einem lokalen Kochkurs teilnehmen"},
        {"en": "Are there any language exchange meetups?", "es": "¿Hay encuentros de intercambio de idiomas?", "pt": "Existem encontros de intercâmbio de idiomas?",
         "fr": "Y a-t-il des rencontres d'échange linguistique?", "de": "Gibt es Sprachaustauschtreffen?"},
        {"en": "I'm looking for a local book club", "es": "Estoy buscando un club de lectura local", "pt": "Estou procurando um clube do livro local",
         "fr": "Je cherche un club de lecture local", "de": "Ich suche einen lokalen Buchclub"},
        {"en": "When does the farmers' market take place?", "es": "¿Cuándo tiene lugar el mercado de agricultores?", "pt": "Quando ocorre a feira de produtores?",
         "fr": "Quand le marché fermier a-t-il lieu?", "de": "Wann findet der Bauernmarkt statt?"},
        {"en": "I'd like to join a dance class", "es": "Me gustaría unirme a una clase de baile", "pt": "Gostaria de me juntar a uma aula de dança",
         "fr": "J'aimerais rejoindre un cours de danse", "de": "Ich würde gerne einem Tanzkurs beitreten"}
    ],
    "Social Etiquette": [
        {"en": "What's the appropriate greeting here?", "es": "¿Cuál es el saludo apropiado aquí?", "pt": "Qual é a saudação apropriada aqui?",
         "fr": "Quelle est la salutation appropriée ici?", "de": "Was ist hier die angemessene Begrüßung?"},
        {"en": "Is it customary to bring a gift?", "es": "¿Es costumbre traer un regalo?", "pt": "É costume trazer um presente?",
         "fr": "Est-il coutumier d'apporter un cadeau?", "de": "Ist es üblich, ein Geschenk mitzubringen?"},
        {"en": "What time do people usually arrive?", "es": "¿A qué hora suele llegar la gente?", "pt": "A que horas as pessoas geralmente chegam?",
         "fr": "À quelle heure les gens arrivent-ils habituellement?", "de": "Wann kommen die Leute normalerweise an?"},
        {"en": "Should I take off my shoes when entering?", "es": "¿Debo quitarme los zapatos al entrar?", "pt": "Devo tirar os sapatos ao entrar?",
         "fr": "Dois-je enlever mes chaussures en entrant?", "de": "Soll ich beim Betreten die Schuhe ausziehen?"},
        {"en": "How do I politely decline an invitation?", "es": "¿Cómo rechazo educadamente una invitación?", "pt": "Como recusar educadamente um convite?",
         "fr": "Comment décliner poliment une invitation?", "de": "Wie lehne ich höflich eine Einladung ab?"},
        {"en": "Is it okay to ask personal questions?", "es": "¿Está bien hacer preguntas personales?", "pt": "É aceitável fazer perguntas pessoais?",
         "fr": "Est-il acceptable de poser des questions personnelles?", "de": "Ist es in Ordnung, persönliche Fragen zu stellen?"},
        {"en": "What topics should I avoid in conversation?", "es": "¿Qué temas debo evitar en la conversación?", "pt": "Quais tópicos devo evitar na conversa?",
         "fr": "Quels sujets dois-je éviter dans la conversation?", "de": "Welche Themen sollte ich im Gespräch vermeiden?"},
        {"en": "How do I show respect to elders?", "es": "¿Cómo muestro respeto a los mayores?", "pt": "Como demonstro respeito aos mais velhos?",
         "fr": "Comment montrer du respect aux aînés?", "de": "Wie zeige ich Respekt gegenüber Älteren?"},
        {"en": "Is punctuality important here?", "es": "¿Es importante la puntualidad aquí?", "pt": "A pontualidade é importante aqui?",
         "fr": "La ponctualité est-elle importante ici?", "de": "Ist Pünktlichkeit hier wichtig?"},
        {"en": "How long should I stay at a social gathering?", "es": "¿Cuánto tiempo debo quedarme en una reunión social?", "pt": "Quanto tempo devo ficar em um encontro social?",
         "fr": "Combien de temps dois-je rester lors d'une réunion sociale?", "de": "Wie lange sollte ich bei einer geselligen Zusammenkunft bleiben?"}
    ],
    "Networking": [
        {"en": "I'd like to expand my professional network", "es": "Me gustaría ampliar mi red profesional", "pt": "Gostaria de expandir minha rede profissional",
         "fr": "J'aimerais élargir mon réseau professionnel", "de": "Ich möchte mein berufliches Netzwerk erweitern"},
        {"en": "Are there any industry meetups here?", "es": "¿Hay encuentros de la industria aquí?", "pt": "Existem encontros da indústria aqui?",
         "fr": "Y a-t-il des rencontres industrielles ici?", "de": "Gibt es hier Branchentreffen?"},
        {"en": "Could you introduce me to your colleague?", "es": "¿Podrías presentarme a tu colega?", "pt": "Poderia me apresentar ao seu colega?",
         "fr": "Pourrais-tu me présenter à ton collègue?", "de": "Könntest du mich deinem Kollegen vorstellen?"},
        {"en": "I'm interested in collaborating on projects", "es": "Estoy interesado/a en colaborar en proyectos", "pt": "Estou interessado/a em colaborar em projetos",
         "fr": "Je suis intéressé(e) à collaborer sur des projets", "de": "Ich bin an einer Zusammenarbeit bei Projekten interessiert"},
        {"en": "Do you know of any coworking spaces?", "es": "¿Conoces espacios de coworking?", "pt": "Você conhece espaços de coworking?",
         "fr": "Connais-tu des espaces de coworking?", "de": "Kennst du Coworking-Spaces?"},
        {"en": "I'd like to attend professional workshops", "es": "Me gustaría asistir a talleres profesionales", "pt": "Gostaria de participar de workshops profissionais",
         "fr": "J'aimerais assister à des ateliers professionnels", "de": "Ich würde gerne an beruflichen Workshops teilnehmen"},
        {"en": "Can we exchange business cards?", "es": "¿Podemos intercambiar tarjetas de presentación?", "pt": "Podemos trocar cartões de visita?",
         "fr": "Pouvons-nous échanger nos cartes de visite?", "de": "Können wir Visitenkarten austauschen?"},
        {"en": "Are you on LinkedIn?", "es": "¿Estás en LinkedIn?", "pt": "Você está no LinkedIn?",
         "fr": "Es-tu sur LinkedIn?", "de": "Bist du auf LinkedIn?"},
        {"en": "I'm looking for mentorship opportunities", "es": "Estoy buscando oportunidades de mentoría", "pt": "Estou procurando oportunidades de mentoria",
         "fr": "Je cherche des opportunités de mentorat", "de": "Ich suche nach Mentoring-Möglichkeiten"},
        {"en": "What professional associations are active here?", "es": "¿Qué asociaciones profesionales están activas aquí?", "pt": "Quais associações profissionais estão ativas aqui?",
         "fr": "Quelles associations professionnelles sont actives ici?", "de": "Welche Berufsverbände sind hier aktiv?"}
    ],
    "Local Community Integration": [
        {"en": "How can I get involved in local initiatives?", "es": "¿Cómo puedo involucrarme en iniciativas locales?", "pt": "Como posso me envolver em iniciativas locais?",
         "fr": "Comment puis-je m'impliquer dans des initiatives locales?", "de": "Wie kann ich mich an lokalen Initiativen beteiligen?"},
        {"en": "What are the important local customs?", "es": "¿Cuáles son las costumbres locales importantes?", "pt": "Quais são os costumes locais importantes?",
         "fr": "Quelles sont les coutumes locales importantes?", "de": "Was sind die wichtigen lokalen Bräuche?"},
        {"en": "I'd like to learn about local history", "es": "Me gustaría aprender sobre la historia local", "pt": "Gostaria de aprender sobre a história local",
         "fr": "J'aimerais en apprendre davantage sur l'histoire locale", "de": "Ich würde gerne etwas über die lokale Geschichte erfahren"},
        {"en": "Are there neighborhood meetings?", "es": "¿Hay reuniones de vecindario?", "pt": "Existem reuniões de bairro?",
         "fr": "Y a-t-il des réunions de quartier?", "de": "Gibt es Nachbarschaftstreffen?"},
        {"en": "How do locals typically spend weekends?", "es": "¿Cómo suelen pasar los fines de semana los locales?", "pt": "Como os moradores locais geralmente passam os fins de semana?",
         "fr": "Comment les locaux passent-ils généralement les week-ends?", "de": "Wie verbringen Einheimische typischerweise Wochenenden?"},
        {"en": "What local causes need support?", "es": "¿Qué causas locales necesitan apoyo?", "pt": "Quais causas locais precisam de apoio?",
         "fr": "Quelles causes locales ont besoin de soutien?", "de": "Welche lokalen Anliegen brauchen Unterstützung?"},
        {"en": "I'd like to participate in community decisions", "es": "Me gustaría participar en decisiones comunitarias", "pt": "Gostaria de participar das decisões comunitárias",
         "fr": "J'aimerais participer aux décisions communautaires", "de": "Ich möchte an Gemeinschaftsentscheidungen teilnehmen"},
        {"en": "How can I support local businesses?", "es": "¿Cómo puedo apoyar a los negocios locales?", "pt": "Como posso apoiar os negócios locais?",
         "fr": "Comment puis-je soutenir les entreprises locales?", "de": "Wie kann ich lokale Unternehmen unterstützen?"},
        {"en": "Are there local newspapers or blogs?", "es": "¿Hay periódicos o blogs locales?", "pt": "Existem jornais ou blogs locais?",
         "fr": "Y a-t-il des journaux ou blogs locaux?", "de": "Gibt es lokale Zeitungen oder Blogs?"},
        {"en": "What community traditions should I know about?", "es": "¿Qué tradiciones comunitarias debería conocer?", "pt": "Que tradições comunitárias devo conhecer?",
         "fr": "Quelles traditions communautaires devrais-je connaître?", "de": "Welche Gemeinschaftstraditionen sollte ich kennen?"}
    ]
}

# Day 23: Banking and Bureaucracy
day23_phrases = {
    "Banking Services": [
        {"en": "I'd like to open a bank account", "es": "Me gustaría abrir una cuenta bancaria", "pt": "Gostaria de abrir uma conta bancária",
         "fr": "Je voudrais ouvrir un compte bancaire", "de": "Ich möchte ein Bankkonto eröffnen"},
        {"en": "What documents do I need?", "es": "¿Qué documentos necesito?", "pt": "Quais documentos preciso?",
         "fr": "Quels documents me faut-il?", "de": "Welche Dokumente benötige ich?"},
        {"en": "I need to make a deposit", "es": "Necesito hacer un depósito", "pt": "Preciso fazer um depósito",
         "fr": "Je dois faire un dépôt", "de": "Ich muss eine Einzahlung machen"},
        {"en": "I'd like to withdraw cash", "es": "Me gustaría retirar efectivo", "pt": "Gostaria de sacar dinheiro",
         "fr": "Je voudrais retirer de l'argent", "de": "Ich möchte Bargeld abheben"},
        {"en": "What's the exchange rate?", "es": "¿Cuál es la tasa de cambio?", "pt": "Qual é a taxa de câmbio?",
         "fr": "Quel est le taux de change?", "de": "Wie ist der Wechselkurs?"},
        {"en": "I need to transfer money abroad", "es": "Necesito transferir dinero al extranjero", "pt": "Preciso transferir dinheiro para o exterior",
         "fr": "Je dois transférer de l'argent à l'étranger", "de": "Ich muss Geld ins Ausland überweisen"},
        {"en": "Are there any fees for this transaction?", "es": "¿Hay alguna comisión por esta transacción?", "pt": "Existem taxas para esta transação?",
         "fr": "Y a-t-il des frais pour cette transaction?", "de": "Gibt es Gebühren für diese Transaktion?"},
        {"en": "I'd like to set up direct deposit", "es": "Me gustaría configurar un depósito directo", "pt": "Gostaria de configurar um depósito direto",
         "fr": "Je voudrais mettre en place un dépôt direct", "de": "Ich möchte eine Direkteinzahlung einrichten"},
        {"en": "Can I access my account online?", "es": "¿Puedo acceder a mi cuenta en línea?", "pt": "Posso acessar minha conta online?",
         "fr": "Puis-je accéder à mon compte en ligne?", "de": "Kann ich online auf mein Konto zugreifen?"},
        {"en": "I need to report a lost card", "es": "Necesito reportar una tarjeta perdida", "pt": "Preciso relatar um cartão perdido",
         "fr": "Je dois signaler une carte perdue", "de": "Ich muss eine verlorene Karte melden"}
    ],
    "Financial Terminology": [
        {"en": "What's the interest rate?", "es": "¿Cuál es la tasa de interés?", "pt": "Qual é a taxa de juros?",
         "fr": "Quel est le taux d'intérêt?", "de": "Wie hoch ist der Zinssatz?"},
        {"en": "I need to check my balance", "es": "Necesito verificar mi saldo", "pt": "Preciso verificar meu saldo",
         "fr": "Je dois vérifier mon solde", "de": "Ich muss meinen Kontostand überprüfen"},
        {"en": "What's the minimum deposit?", "es": "¿Cuál es el depósito mínimo?", "pt": "Qual é o depósito mínimo?",
         "fr": "Quel est le dépôt minimum?", "de": "Was ist die Mindesteinlage?"},
        {"en": "I'd like to apply for a loan", "es": "Me gustaría solicitar un préstamo", "pt": "Gostaria de solicitar um empréstimo",
         "fr": "Je voudrais demander un prêt", "de": "Ich möchte einen Kredit beantragen"},
        {"en": "What's the monthly fee?", "es": "¿Cuál es la tarifa mensual?", "pt": "Qual é a taxa mensal?",
         "fr": "Quels sont les frais mensuels?", "de": "Was ist die monatliche Gebühr?"},
        {"en": "I need to update my account information", "es": "Necesito actualizar la información de mi cuenta", "pt": "Preciso atualizar as informações da minha conta",
         "fr": "Je dois mettre à jour les informations de mon compte", "de": "Ich muss meine Kontoinformationen aktualisieren"},
        {"en": "What's the overdraft limit?", "es": "¿Cuál es el límite de sobregiro?", "pt": "Qual é o limite de cheque especial?",
         "fr": "Quelle est la limite de découvert?", "de": "Was ist das Überziehungslimit?"},
        {"en": "I'd like to set up automatic payments", "es": "Me gustaría configurar pagos automáticos", "pt": "Gostaria de configurar pagamentos automáticos",
         "fr": "Je voudrais mettre en place des paiements automatiques", "de": "Ich möchte automatische Zahlungen einrichten"},
        {"en": "What investment options do you offer?", "es": "¿Qué opciones de inversión ofrecen?", "pt": "Quais opções de investimento vocês oferecem?",
         "fr": "Quelles options d'investissement proposez-vous?", "de": "Welche Anlagemöglichkeiten bieten Sie an?"},
        {"en": "I need to close my account", "es": "Necesito cerrar mi cuenta", "pt": "Preciso encerrar minha conta",
         "fr": "Je dois fermer mon compte", "de": "Ich muss mein Konto schließen"}
    ],
    "Government Offices": [
        {"en": "Where is the immigration office?", "es": "¿Dónde está la oficina de inmigración?", "pt": "Onde fica o escritório de imigração?",
         "fr": "Où se trouve le bureau d'immigration?", "de": "Wo ist das Einwanderungsbüro?"},
        {"en": "I need to renew my visa", "es": "Necesito renovar mi visa", "pt": "Preciso renovar meu visto",
         "fr": "Je dois renouveler mon visa", "de": "Ich muss mein Visum verlängern"},
        {"en": "Where can I get a tax identification number?", "es": "¿Dónde puedo obtener un número de identificación fiscal?", "pt": "Onde posso obter um número de identificação fiscal?",
         "fr": "Où puis-je obtenir un numéro d'identification fiscale?", "de": "Wo kann ich eine Steueridentifikationsnummer bekommen?"},
        {"en": "I need to register my address", "es": "Necesito registrar mi dirección", "pt": "Preciso registrar meu endereço",
         "fr": "Je dois enregistrer mon adresse", "de": "Ich muss meine Adresse anmelden"},
        {"en": "Where is the nearest notary?", "es": "¿Dónde está el notario más cercano?", "pt": "Onde fica o cartório mais próximo?",
         "fr": "Où se trouve le notaire le plus proche?", "de": "Wo ist der nächste Notar?"},
        {"en": "I need to apply for a work permit", "es": "Necesito solicitar un permiso de trabajo", "pt": "Preciso solicitar uma autorização de trabalho",
         "fr": "Je dois demander un permis de travail", "de": "Ich muss eine Arbeitserlaubnis beantragen"},
        {"en": "What's the process for residency?", "es": "¿Cuál es el proceso para la residencia?", "pt": "Qual é o processo para residência?",
         "fr": "Quel est le processus pour la résidence?", "de": "Wie ist der Prozess für die Aufenthaltserlaubnis?"},
        {"en": "I need to file my taxes", "es": "Necesito presentar mis impuestos", "pt": "Preciso declarar meus impostos",
         "fr": "Je dois déposer mes impôts", "de": "Ich muss meine Steuern einreichen"},
        {"en": "Where is the social security office?", "es": "¿Dónde está la oficina de seguridad social?", "pt": "Onde fica o escritório da previdência social?",
         "fr": "Où se trouve le bureau de la sécurité sociale?", "de": "Wo ist das Sozialversicherungsamt?"},
        {"en": "I need to get my documents authenticated", "es": "Necesito autenticar mis documentos", "pt": "Preciso autenticar meus documentos",
         "fr": "Je dois faire authentifier mes documents", "de": "Ich muss meine Dokumente beglaubigen lassen"}
    ],
    "Bureaucratic Procedures": [
        {"en": "What forms do I need to fill out?", "es": "¿Qué formularios necesito completar?", "pt": "Quais formulários preciso preencher?",
         "fr": "Quels formulaires dois-je remplir?", "de": "Welche Formulare muss ich ausfüllen?"},
        {"en": "Do I need to make an appointment?", "es": "¿Necesito hacer una cita?", "pt": "Preciso marcar uma consulta?",
         "fr": "Dois-je prendre rendez-vous?", "de": "Muss ich einen Termin vereinbaren?"},
        {"en": "What's the processing time?", "es": "¿Cuál es el tiempo de procesamiento?", "pt": "Qual é o tempo de processamento?",
         "fr": "Quel est le délai de traitement?", "de": "Wie lange dauert die Bearbeitung?"},
        {"en": "Do I need to bring original documents?", "es": "¿Necesito traer documentos originales?", "pt": "Preciso trazer documentos originais?",
         "fr": "Dois-je apporter les documents originaux?", "de": "Muss ich Originaldokumente mitbringen?"},
        {"en": "Is there an online application?", "es": "¿Hay una solicitud en línea?", "pt": "Existe uma aplicação online?",
         "fr": "Y a-t-il une demande en ligne?", "de": "Gibt es eine Online-Bewerbung?"},
        {"en": "What's the status of my application?", "es": "¿Cuál es el estado de mi solicitud?", "pt": "Qual é o status da minha solicitação?",
         "fr": "Quel est le statut de ma demande?", "de": "Wie ist der Status meines Antrags?"},
        {"en": "Do I need to pay a fee?", "es": "¿Necesito pagar una tarifa?", "pt": "Preciso pagar uma taxa?",
         "fr": "Dois-je payer des frais?", "de": "Muss ich eine Gebühr bezahlen?"},
        {"en": "Where can I get certified copies?", "es": "¿Dónde puedo obtener copias certificadas?", "pt": "Onde posso obter cópias autenticadas?",
         "fr": "Où puis-je obtenir des copies certifiées?", "de": "Wo kann ich beglaubigte Kopien bekommen?"},
        {"en": "I need to submit these documents by the deadline", "es": "Necesito presentar estos documentos antes de la fecha límite", "pt": "Preciso enviar estes documentos até o prazo",
         "fr": "Je dois soumettre ces documents avant la date limite", "de": "Ich muss diese Dokumente bis zur Frist einreichen"},
        {"en": "Is there an appeal process?", "es": "¿Hay un proceso de apelación?", "pt": "Existe um processo de recurso?",
         "fr": "Y a-t-il un processus d'appel?", "de": "Gibt es ein Berufungsverfahren?"}
    ],
    "Legal and Administrative Terms": [
        {"en": "What does this clause mean?", "es": "¿Qué significa esta cláusula?", "pt": "O que significa esta cláusula?",
         "fr": "Que signifie cette clause?", "de": "Was bedeutet diese Klausel?"},
        {"en": "I need legal advice", "es": "Necesito asesoramiento legal", "pt": "Preciso de aconselhamento jurídico",
         "fr": "J'ai besoin de conseils juridiques", "de": "Ich brauche rechtlichen Rat"},
        {"en": "What are my rights in this situation?", "es": "¿Cuáles son mis derechos en esta situación?", "pt": "Quais são meus direitos nesta situação?",
         "fr": "Quels sont mes droits dans cette situation?", "de": "Was sind meine Rechte in dieser Situation?"},
        {"en": "I need to sign a contract", "es": "Necesito firmar un contrato", "pt": "Preciso assinar um contrato",
         "fr": "Je dois signer un contrat", "de": "Ich muss einen Vertrag unterschreiben"},
        {"en": "What are the terms and conditions?", "es": "¿Cuáles son los términos y condiciones?", "pt": "Quais são os termos e condições?",
         "fr": "Quelles sont les conditions générales?", "de": "Was sind die Geschäftsbedingungen?"},
        {"en": "I need to file a complaint", "es": "Necesito presentar una queja", "pt": "Preciso registrar uma reclamação",
         "fr": "Je dois déposer une plainte", "de": "Ich muss eine Beschwerde einreichen"},
        {"en": "What's the legal procedure for this?", "es": "¿Cuál es el procedimiento legal para esto?", "pt": "Qual é o procedimento legal para isso?",
         "fr": "Quelle est la procédure légale pour cela?", "de": "Was ist das rechtliche Verfahren dafür?"},
        {"en": "I need to get power of attorney", "es": "Necesito obtener un poder notarial", "pt": "Preciso obter uma procuração",
         "fr": "J'ai besoin d'obtenir une procuration", "de": "Ich muss eine Vollmacht bekommen"},
        {"en": "What are the penalties for non-compliance?", "es": "¿Cuáles son las sanciones por incumplimiento?", "pt": "Quais são as penalidades por não conformidade?",
         "fr": "Quelles sont les sanctions pour non-conformité?", "de": "Was sind die Strafen für Nichteinhaltung?"},
        {"en": "I need to understand my tax obligations", "es": "Necesito entender mis obligaciones fiscales", "pt": "Preciso entender minhas obrigações fiscais",
         "fr": "Je dois comprendre mes obligations fiscales", "de": "Ich muss meine steuerlichen Verpflichtungen verstehen"}
    ]
}

# Day 21: Workplace Language and Etiquette
day21_phrases = {
    "Office Communication": [
        {"en": "Could we schedule a meeting?", "es": "¿Podríamos programar una reunión?", "pt": "Poderíamos agendar uma reunião?",
         "fr": "Pourrions-nous planifier une réunion?", "de": "Könnten wir ein Meeting planen?"},
        {"en": "I'd like to discuss this project", "es": "Me gustaría discutir este proyecto", "pt": "Gostaria de discutir este projeto",
         "fr": "J'aimerais discuter de ce projet", "de": "Ich würde gerne dieses Projekt besprechen"},
        {"en": "Please let me know your availability", "es": "Por favor, hazme saber tu disponibilidad", "pt": "Por favor, me informe sua disponibilidade",
         "fr": "Veuillez me faire savoir votre disponibilité", "de": "Bitte teilen Sie mir Ihre Verfügbarkeit mit"},
        {"en": "I'll send you the agenda beforehand", "es": "Te enviaré la agenda con anticipación", "pt": "Enviarei a pauta com antecedência",
         "fr": "Je vous enverrai l'ordre du jour à l'avance", "de": "Ich sende Ihnen die Tagesordnung im Voraus"},
        {"en": "Could you share your screen?", "es": "¿Podrías compartir tu pantalla?", "pt": "Você poderia compartilhar sua tela?",
         "fr": "Pourriez-vous partager votre écran?", "de": "Könnten Sie Ihren Bildschirm teilen?"},
        {"en": "I'll follow up with an email", "es": "Haré seguimiento con un correo electrónico", "pt": "Farei um acompanhamento com um e-mail",
         "fr": "Je ferai un suivi par e-mail", "de": "Ich werde mit einer E-Mail nachfassen"},
        {"en": "Let's take this discussion offline", "es": "Continuemos esta discusión en privado", "pt": "Vamos continuar esta discussão em particular",
         "fr": "Continuons cette discussion en privé", "de": "Lassen Sie uns diese Diskussion offline fortsetzen"},
        {"en": "I need your input on this matter", "es": "Necesito tu opinión sobre este asunto", "pt": "Preciso da sua opinião sobre este assunto",
         "fr": "J'ai besoin de votre avis sur cette question", "de": "Ich brauche Ihre Meinung zu dieser Angelegenheit"},
        {"en": "Could you CC me on that email?", "es": "¿Podrías ponerme en copia en ese correo?", "pt": "Você poderia me colocar em cópia nesse e-mail?",
         "fr": "Pourriez-vous me mettre en copie de cet e-mail?", "de": "Könnten Sie mich in dieser E-Mail in CC setzen?"},
        {"en": "Let's set up a video call", "es": "Organicemos una videollamada", "pt": "Vamos organizar uma videochamada",
         "fr": "Organisons un appel vidéo", "de": "Lassen Sie uns einen Videoanruf einrichten"}
    ],
    "Workplace Etiquette": [
        {"en": "It's customary to arrive a few minutes early", "es": "Es costumbre llegar unos minutos antes", "pt": "É costume chegar alguns minutos antes",
         "fr": "Il est d'usage d'arriver quelques minutes en avance", "de": "Es ist üblich, ein paar Minuten früher anzukommen"},
        {"en": "Business attire is expected in this office", "es": "Se espera vestimenta formal en esta oficina", "pt": "Traje executivo é esperado neste escritório",
         "fr": "Une tenue professionnelle est attendue dans ce bureau", "de": "Geschäftskleidung wird in diesem Büro erwartet"},
        {"en": "Please knock before entering", "es": "Por favor, toca antes de entrar", "pt": "Por favor, bata antes de entrar",
         "fr": "Veuillez frapper avant d'entrer", "de": "Bitte klopfen Sie, bevor Sie eintreten"},
        {"en": "It's polite to greet everyone in the morning", "es": "Es cortés saludar a todos por la mañana", "pt": "É educado cumprimentar todos pela manhã",
         "fr": "Il est poli de saluer tout le monde le matin", "de": "Es ist höflich, jeden am Morgen zu begrüßen"},
        {"en": "Personal calls should be taken outside", "es": "Las llamadas personales deben hacerse afuera", "pt": "Ligações pessoais devem ser feitas fora",
         "fr": "Les appels personnels doivent être pris à l'extérieur", "de": "Persönliche Anrufe sollten draußen getätigt werden"},
        {"en": "Please keep the break room clean", "es": "Por favor, mantén limpia la sala de descanso", "pt": "Por favor, mantenha a sala de descanso limpa",
         "fr": "Veuillez garder la salle de pause propre", "de": "Bitte halten Sie den Pausenraum sauber"},
        {"en": "It's important to respect meeting times", "es": "Es importante respetar los horarios de reuniones", "pt": "É importante respeitar os horários das reuniões",
         "fr": "Il est important de respecter les horaires des réunions", "de": "Es ist wichtig, Besprechungszeiten einzuhalten"},
        {"en": "Avoid interrupting when someone is speaking", "es": "Evita interrumpir cuando alguien está hablando", "pt": "Evite interromper quando alguém está falando",
         "fr": "Évitez d'interrompre quand quelqu'un parle", "de": "Vermeiden Sie es, jemanden zu unterbrechen, wenn er spricht"},
        {"en": "Remember to silence your phone in meetings", "es": "Recuerda silenciar tu teléfono en las reuniones", "pt": "Lembre-se de silenciar seu telefone nas reuniões",
         "fr": "N'oubliez pas de mettre votre téléphone en silencieux lors des réunions", "de": "Denken Sie daran, Ihr Telefon in Besprechungen stumm zu schalten"},
        {"en": "It's customary to bring treats on your birthday", "es": "Es costumbre traer golosinas en tu cumpleaños", "pt": "É costume trazer guloseimas no seu aniversário",
         "fr": "Il est d'usage d'apporter des friandises le jour de votre anniversaire", "de": "Es ist üblich, an Ihrem Geburtstag Leckereien mitzubringen"}
    ],
    "Professional Relationships": [
        {"en": "I'd like to introduce my colleague", "es": "Me gustaría presentar a mi colega", "pt": "Gostaria de apresentar meu colega",
         "fr": "J'aimerais vous présenter mon collègue", "de": "Ich möchte meinen Kollegen vorstellen"},
        {"en": "It's a pleasure to work with you", "es": "Es un placer trabajar contigo", "pt": "É um prazer trabalhar com você",
         "fr": "C'est un plaisir de travailler avec vous", "de": "Es ist eine Freude, mit Ihnen zu arbeiten"},
        {"en": "I appreciate your feedback", "es": "Agradezco tus comentarios", "pt": "Agradeço seu feedback",
         "fr": "J'apprécie vos commentaires", "de": "Ich schätze Ihr Feedback"},
        {"en": "Let's collaborate on this project", "es": "Colaboremos en este proyecto", "pt": "Vamos colaborar neste projeto",
         "fr": "Collaborons sur ce projet", "de": "Lassen Sie uns bei diesem Projekt zusammenarbeiten"},
        {"en": "I value your opinion", "es": "Valoro tu opinión", "pt": "Valorizo sua opinião",
         "fr": "Je valorise votre opinion", "de": "Ich schätze Ihre Meinung"},
        {"en": "Could we discuss this privately?", "es": "¿Podríamos discutir esto en privado?", "pt": "Poderíamos discutir isso em particular?",
         "fr": "Pourrions-nous en discuter en privé?", "de": "Könnten wir das unter vier Augen besprechen?"},
        {"en": "I'd like to clarify our roles", "es": "Me gustaría aclarar nuestros roles", "pt": "Gostaria de esclarecer nossos papéis",
         "fr": "J'aimerais clarifier nos rôles", "de": "Ich möchte unsere Rollen klären"},
        {"en": "Let's maintain open communication", "es": "Mantengamos una comunicación abierta", "pt": "Vamos manter uma comunicação aberta",
         "fr": "Maintenons une communication ouverte", "de": "Lassen Sie uns eine offene Kommunikation pflegen"},
        {"en": "I'm looking forward to our partnership", "es": "Espero con interés nuestra colaboración", "pt": "Estou ansioso/a pela nossa parceria",
         "fr": "J'attends avec impatience notre partenariat", "de": "Ich freue mich auf unsere Partnerschaft"},
        {"en": "Thank you for your mentorship", "es": "Gracias por tu mentoría", "pt": "Obrigado/a pela sua mentoria",
         "fr": "Merci pour votre mentorat", "de": "Danke für Ihre Mentorschaft"}
    ],
    "Meetings and Presentations": [
        {"en": "Let's go through the agenda", "es": "Repasemos la agenda", "pt": "Vamos passar pela pauta",
         "fr": "Passons en revue l'ordre du jour", "de": "Lassen Sie uns die Tagesordnung durchgehen"},
        {"en": "I'd like to present our findings", "es": "Me gustaría presentar nuestros hallazgos", "pt": "Gostaria de apresentar nossas descobertas",
         "fr": "J'aimerais présenter nos résultats", "de": "Ich möchte unsere Ergebnisse präsentieren"},
        {"en": "Do you have any questions?", "es": "¿Tienen alguna pregunta?", "pt": "Vocês têm alguma pergunta?",
         "fr": "Avez-vous des questions?", "de": "Haben Sie irgendwelche Fragen?"},
        {"en": "Let's move on to the next point", "es": "Pasemos al siguiente punto", "pt": "Vamos passar para o próximo ponto",
         "fr": "Passons au point suivant", "de": "Lassen Sie uns zum nächsten Punkt übergehen"},
        {"en": "Could you elaborate on that?", "es": "¿Podrías elaborar más sobre eso?", "pt": "Você poderia elaborar mais sobre isso?",
         "fr": "Pourriez-vous développer cela?", "de": "Könnten Sie das näher erläutern?"},
        {"en": "I'd like to add to that point", "es": "Me gustaría añadir a ese punto", "pt": "Gostaria de acrescentar a esse ponto",
         "fr": "J'aimerais ajouter à ce point", "de": "Ich möchte zu diesem Punkt etwas hinzufügen"},
        {"en": "Let's summarize what we've discussed", "es": "Resumamos lo que hemos discutido", "pt": "Vamos resumir o que discutimos",
         "fr": "Résumons ce que nous avons discuté", "de": "Lassen Sie uns zusammenfassen, was wir besprochen haben"},
        {"en": "We need to establish next steps", "es": "Necesitamos establecer los próximos pasos", "pt": "Precisamos estabelecer os próximos passos",
         "fr": "Nous devons établir les prochaines étapes", "de": "Wir müssen die nächsten Schritte festlegen"},
        {"en": "Let's set a deadline for this task", "es": "Establezcamos una fecha límite para esta tarea", "pt": "Vamos definir um prazo para esta tarefa",
         "fr": "Fixons une date limite pour cette tâche", "de": "Lassen Sie uns eine Frist für diese Aufgabe setzen"},
        {"en": "I'll prepare the presentation slides", "es": "Prepararé las diapositivas de la presentación", "pt": "Vou preparar os slides da apresentação",
         "fr": "Je préparerai les diapositives de la présentation", "de": "Ich werde die Präsentationsfolien vorbereiten"}
    ],
    "Workplace Conflict Resolution": [
        {"en": "I'd like to address a concern", "es": "Me gustaría abordar una preocupación", "pt": "Gostaria de abordar uma preocupação",
         "fr": "J'aimerais aborder une préoccupation", "de": "Ich möchte ein Anliegen ansprechen"},
        {"en": "Let's find a solution together", "es": "Encontremos una solución juntos", "pt": "Vamos encontrar uma solução juntos",
         "fr": "Trouvons une solution ensemble", "de": "Lassen Sie uns gemeinsam eine Lösung finden"},
        {"en": "I understand your perspective", "es": "Entiendo tu perspectiva", "pt": "Entendo sua perspectiva",
         "fr": "Je comprends votre point de vue", "de": "Ich verstehe Ihre Perspektive"},
        {"en": "Could we compromise on this?", "es": "¿Podríamos llegar a un compromiso en esto?", "pt": "Poderíamos chegar a um acordo sobre isso?",
         "fr": "Pourrions-nous faire un compromis sur ce point?", "de": "Könnten wir hier einen Kompromiss finden?"},
        {"en": "I'd like to clear up any misunderstandings", "es": "Me gustaría aclarar cualquier malentendido", "pt": "Gostaria de esclarecer quaisquer mal-entendidos",
         "fr": "J'aimerais dissiper tout malentendu", "de": "Ich möchte alle Missverständnisse klären"},
        {"en": "Let's focus on the issue, not the person", "es": "Centrémonos en el problema, no en la persona", "pt": "Vamos focar no problema, não na pessoa",
         "fr": "Concentrons-nous sur le problème, pas sur la personne", "de": "Lassen Sie uns auf das Problem konzentrieren, nicht auf die Person"},
        {"en": "I apologize if I've offended you", "es": "Me disculpo si te he ofendido", "pt": "Peço desculpas se te ofendi",
         "fr": "Je m'excuse si je vous ai offensé", "de": "Ich entschuldige mich, wenn ich Sie beleidigt habe"},
        {"en": "Let's discuss this with a mediator", "es": "Discutamos esto con un mediador", "pt": "Vamos discutir isso com um mediador",
         "fr": "Discutons-en avec un médiateur", "de": "Lassen Sie uns das mit einem Vermittler besprechen"},
        {"en": "I value our professional relationship", "es": "Valoro nuestra relación profesional", "pt": "Valorizo nossa relação profissional",
         "fr": "Je valorise notre relation professionnelle", "de": "Ich schätze unsere berufliche Beziehung"},
        {"en": "Let's agree to disagree respectfully", "es": "Acordemos discrepar respetuosamente", "pt": "Vamos concordar em discordar respeitosamente",
         "fr": "Convenons de ne pas être d'accord respectueusement", "de": "Lassen Sie uns respektvoll anderer Meinung sein"}
    ]
}

# Day 19: Healthcare Systems
day19_phrases = {
    "Medical Emergencies": [
        {"en": "I need a doctor urgently", "es": "Necesito un médico urgentemente", "pt": "Preciso de um médico urgentemente",
         "fr": "J'ai besoin d'un médecin de toute urgence", "de": "Ich brauche dringend einen Arzt"},
        {"en": "Please call an ambulance", "es": "Por favor, llame a una ambulancia", "pt": "Por favor, chame uma ambulância",
         "fr": "Veuillez appeler une ambulance", "de": "Bitte rufen Sie einen Krankenwagen"},
        {"en": "I'm having chest pain", "es": "Tengo dolor en el pecho", "pt": "Estou com dor no peito",
         "fr": "J'ai des douleurs thoraciques", "de": "Ich habe Brustschmerzen"},
        {"en": "I'm having difficulty breathing", "es": "Tengo dificultad para respirar", "pt": "Estou com dificuldade para respirar",
         "fr": "J'ai du mal à respirer", "de": "Ich habe Schwierigkeiten beim Atmen"},
        {"en": "I've had an accident", "es": "He tenido un accidente", "pt": "Sofri um acidente",
         "fr": "J'ai eu un accident", "de": "Ich hatte einen Unfall"},
        {"en": "I'm allergic to this medication", "es": "Soy alérgico/a a este medicamento", "pt": "Sou alérgico/a a este medicamento",
         "fr": "Je suis allergique à ce médicament", "de": "Ich bin allergisch gegen dieses Medikament"},
        {"en": "Where is the nearest emergency room?", "es": "¿Dónde está la sala de emergencias más cercana?", "pt": "Onde fica a sala de emergência mais próxima?",
         "fr": "Où se trouve les urgences les plus proches?", "de": "Wo ist der nächste Notfallraum?"},
        {"en": "I need immediate medical attention", "es": "Necesito atención médica inmediata", "pt": "Preciso de atenção médica imediata",
         "fr": "J'ai besoin de soins médicaux immédiats", "de": "Ich brauche sofortige ärztliche Hilfe"},
        {"en": "I'm feeling very dizzy", "es": "Me siento muy mareado/a", "pt": "Estou me sentindo muito tonto/a",
         "fr": "Je me sens très étourdi(e)", "de": "Mir ist sehr schwindelig"},
        {"en": "I have a high fever", "es": "Tengo fiebre alta", "pt": "Estou com febre alta",
         "fr": "J'ai une forte fièvre", "de": "Ich habe hohes Fieber"}
    ],
    "Healthcare Facilities": [
        {"en": "Where is the nearest hospital?", "es": "¿Dónde está el hospital más cercano?", "pt": "Onde fica o hospital mais próximo?",
         "fr": "Où se trouve l'hôpital le plus proche?", "de": "Wo ist das nächste Krankenhaus?"},
        {"en": "I need to find a clinic", "es": "Necesito encontrar una clínica", "pt": "Preciso encontrar uma clínica",
         "fr": "Je dois trouver une clinique", "de": "Ich muss eine Klinik finden"},
        {"en": "Is there a pharmacy open now?", "es": "¿Hay una farmacia abierta ahora?", "pt": "Há uma farmácia aberta agora?",
         "fr": "Y a-t-il une pharmacie ouverte maintenant?", "de": "Gibt es eine Apotheke, die jetzt geöffnet ist?"},
        {"en": "Do you have a family doctor?", "es": "¿Tiene un médico de familia?", "pt": "Você tem um médico de família?",
         "fr": "Avez-vous un médecin de famille?", "de": "Haben Sie einen Hausarzt?"},
        {"en": "I need to make an appointment with a specialist", "es": "Necesito hacer una cita con un especialista", "pt": "Preciso marcar uma consulta com um especialista",
         "fr": "J'ai besoin de prendre rendez-vous avec un spécialiste", "de": "Ich muss einen Termin bei einem Facharzt vereinbaren"},
        {"en": "Is there a medical center in this area?", "es": "¿Hay un centro médico en esta zona?", "pt": "Existe um centro médico nesta área?",
         "fr": "Y a-t-il un centre médical dans cette région?", "de": "Gibt es ein medizinisches Zentrum in dieser Gegend?"},
        {"en": "Where can I get a COVID test?", "es": "¿Dónde puedo hacerme una prueba de COVID?", "pt": "Onde posso fazer um teste de COVID?",
         "fr": "Où puis-je faire un test COVID?", "de": "Wo kann ich einen COVID-Test machen?"},
        {"en": "Is there a dentist nearby?", "es": "¿Hay un dentista cerca?", "pt": "Há um dentista por perto?",
         "fr": "Y a-t-il un dentiste à proximité?", "de": "Gibt es einen Zahnarzt in der Nähe?"},
        {"en": "I need to find an optometrist", "es": "Necesito encontrar un optometrista", "pt": "Preciso encontrar um optometrista",
         "fr": "Je dois trouver un optométriste", "de": "Ich muss einen Optiker finden"},
        {"en": "Where is the vaccination center?", "es": "¿Dónde está el centro de vacunación?", "pt": "Onde fica o centro de vacinação?",
         "fr": "Où se trouve le centre de vaccination?", "de": "Wo ist das Impfzentrum?"}
    ],
    "Health Insurance and Payments": [
        {"en": "Do you accept my health insurance?", "es": "¿Aceptan mi seguro de salud?", "pt": "Vocês aceitam meu seguro de saúde?",
         "fr": "Acceptez-vous mon assurance maladie?", "de": "Akzeptieren Sie meine Krankenversicherung?"},
        {"en": "How much does this treatment cost?", "es": "¿Cuánto cuesta este tratamiento?", "pt": "Quanto custa este tratamento?",
         "fr": "Combien coûte ce traitement?", "de": "Wie viel kostet diese Behandlung?"},
        {"en": "I need to register for public healthcare", "es": "Necesito registrarme para la atención médica pública", "pt": "Preciso me registrar para o sistema público de saúde",
         "fr": "Je dois m'inscrire aux soins de santé publics", "de": "Ich muss mich für die öffentliche Gesundheitsversorgung anmelden"},
        {"en": "Is this covered by insurance?", "es": "¿Esto está cubierto por el seguro?", "pt": "Isto está coberto pelo seguro?",
         "fr": "Est-ce couvert par l'assurance?", "de": "Wird das von der Versicherung übernommen?"},
        {"en": "Do I need to pay upfront?", "es": "¿Necesito pagar por adelantado?", "pt": "Preciso pagar adiantado?",
         "fr": "Dois-je payer d'avance?", "de": "Muss ich im Voraus bezahlen?"},
        {"en": "How do I claim reimbursement?", "es": "¿Cómo solicito el reembolso?", "pt": "Como solicito o reembolso?",
         "fr": "Comment demander un remboursement?", "de": "Wie beantrage ich eine Rückerstattung?"},
        {"en": "What documents do I need for health insurance?", "es": "¿Qué documentos necesito para el seguro de salud?", "pt": "Quais documentos preciso para o seguro de saúde?",
         "fr": "Quels documents me faut-il pour l'assurance maladie?", "de": "Welche Dokumente benötige ich für die Krankenversicherung?"},
        {"en": "Is there a co-payment?", "es": "¿Hay un copago?", "pt": "Existe um copagamento?",
         "fr": "Y a-t-il une quote-part?", "de": "Gibt es eine Zuzahlung?"},
        {"en": "How does the public healthcare system work?", "es": "¿Cómo funciona el sistema de salud público?", "pt": "Como funciona o sistema público de saúde?",
         "fr": "Comment fonctionne le système de santé publique?", "de": "Wie funktioniert das öffentliche Gesundheitssystem?"},
        {"en": "I need a receipt for my insurance", "es": "Necesito un recibo para mi seguro", "pt": "Preciso de um recibo para meu seguro",
         "fr": "J'ai besoin d'un reçu pour mon assurance", "de": "Ich brauche eine Quittung für meine Versicherung"}
    ],
    "Medical Consultations": [
        {"en": "I'd like to describe my symptoms", "es": "Me gustaría describir mis síntomas", "pt": "Gostaria de descrever meus sintomas",
         "fr": "J'aimerais décrire mes symptômes", "de": "Ich möchte meine Symptome beschreiben"},
        {"en": "When did the symptoms start?", "es": "¿Cuándo comenzaron los síntomas?", "pt": "Quando os sintomas começaram?",
         "fr": "Quand les symptômes ont-ils commencé?", "de": "Wann haben die Symptome begonnen?"},
        {"en": "I've been feeling unwell for a week", "es": "Me he sentido mal durante una semana", "pt": "Tenho me sentido mal por uma semana",
         "fr": "Je me sens mal depuis une semaine", "de": "Ich fühle mich seit einer Woche unwohl"},
        {"en": "Do I need any tests?", "es": "¿Necesito alguna prueba?", "pt": "Preciso de algum exame?",
         "fr": "Ai-je besoin de tests?", "de": "Benötige ich irgendwelche Tests?"},
        {"en": "What are the side effects of this medication?", "es": "¿Cuáles son los efectos secundarios de este medicamento?", "pt": "Quais são os efeitos colaterais deste medicamento?",
         "fr": "Quels sont les effets secondaires de ce médicament?", "de": "Was sind die Nebenwirkungen dieses Medikaments?"},
        {"en": "How often should I take this medicine?", "es": "¿Con qué frecuencia debo tomar este medicamento?", "pt": "Com que frequência devo tomar este remédio?",
         "fr": "À quelle fréquence dois-je prendre ce médicament?", "de": "Wie oft sollte ich dieses Medikament einnehmen?"},
        {"en": "Do I need a follow-up appointment?", "es": "¿Necesito una cita de seguimiento?", "pt": "Preciso de uma consulta de acompanhamento?",
         "fr": "Ai-je besoin d'un rendez-vous de suivi?", "de": "Benötige ich einen Folgetermin?"},
        {"en": "Can I get a medical certificate?", "es": "¿Puedo obtener un certificado médico?", "pt": "Posso obter um atestado médico?",
         "fr": "Puis-je obtenir un certificat médical?", "de": "Kann ich ein ärztliches Attest bekommen?"},
        {"en": "I need a prescription refill", "es": "Necesito una recarga de receta", "pt": "Preciso de uma renovação de receita",
         "fr": "J'ai besoin d'un renouvellement d'ordonnance", "de": "Ich brauche eine Nachfüllung meines Rezepts"},
        {"en": "What should I do if the symptoms persist?", "es": "¿Qué debo hacer si los síntomas persisten?", "pt": "O que devo fazer se os sintomas persistirem?",
         "fr": "Que dois-je faire si les symptômes persistent?", "de": "Was soll ich tun, wenn die Symptome anhalten?"}
    ],
    "Preventive Healthcare": [
        {"en": "I need to schedule a check-up", "es": "Necesito programar un chequeo", "pt": "Preciso agendar um check-up",
         "fr": "Je dois planifier un bilan de santé", "de": "Ich muss einen Check-up planen"},
        {"en": "When should I get vaccinated?", "es": "¿Cuándo debo vacunarme?", "pt": "Quando devo me vacinar?",
         "fr": "Quand dois-je me faire vacciner?", "de": "Wann sollte ich mich impfen lassen?"},
        {"en": "What vaccines do I need for this region?", "es": "¿Qué vacunas necesito para esta región?", "pt": "Quais vacinas preciso para esta região?",
         "fr": "De quels vaccins ai-je besoin pour cette région?", "de": "Welche Impfungen benötige ich für diese Region?"},
        {"en": "How often should I have a dental check-up?", "es": "¿Con qué frecuencia debo hacerme un chequeo dental?", "pt": "Com que frequência devo fazer um check-up odontológico?",
         "fr": "À quelle fréquence dois-je faire un contrôle dentaire?", "de": "Wie oft sollte ich eine zahnärztliche Untersuchung haben?"},
        {"en": "I'd like to get screened for common diseases", "es": "Me gustaría hacerme pruebas de detección de enfermedades comunes", "pt": "Gostaria de fazer exames para doenças comuns",
         "fr": "J'aimerais me faire dépister pour les maladies courantes", "de": "Ich möchte mich auf häufige Krankheiten untersuchen lassen"},
        {"en": "What are the recommended health screenings for my age?", "es": "¿Cuáles son los exámenes de salud recomendados para mi edad?", "pt": "Quais são os exames de saúde recomendados para minha idade?",
         "fr": "Quels sont les dépistages de santé recommandés pour mon âge?", "de": "Welche Gesundheitsuntersuchungen werden für mein Alter empfohlen?"},
        {"en": "How can I maintain a healthy lifestyle?", "es": "¿Cómo puedo mantener un estilo de vida saludable?", "pt": "Como posso manter um estilo de vida saudável?",
         "fr": "Comment puis-je maintenir un mode de vie sain?", "de": "Wie kann ich einen gesunden Lebensstil aufrechterhalten?"},
        {"en": "What are the signs of dehydration?", "es": "¿Cuáles son los signos de deshidratación?", "pt": "Quais são os sinais de desidratação?",
         "fr": "Quels sont les signes de déshydratation?", "de": "Was sind die Anzeichen von Dehydrierung?"},
        {"en": "How can I protect myself from mosquito-borne diseases?", "es": "¿Cómo puedo protegerme de enfermedades transmitidas por mosquitos?", "pt": "Como posso me proteger de doenças transmitidas por mosquitos?",
         "fr": "Comment puis-je me protéger des maladies transmises par les moustiques?", "de": "Wie kann ich mich vor durch Mücken übertragenen Krankheiten schützen?"},
        {"en": "What sunscreen should I use in this climate?", "es": "¿Qué protector solar debo usar en este clima?", "pt": "Que protetor solar devo usar neste clima?",
         "fr": "Quelle crème solaire dois-je utiliser dans ce climat?", "de": "Welchen Sonnenschutz sollte ich in diesem Klima verwenden?"}
    ]
}

# Day 17: Job Hunting Abroad
day17_phrases = {
    "Job Search Vocabulary": [
        {"en": "I'm looking for a job in tech", "es": "Estoy buscando trabajo en tecnología", "pt": "Estou procurando emprego em tecnologia",
         "fr": "Je cherche un emploi dans la technologie", "de": "Ich suche einen Job im Technologiebereich"},
        {"en": "Do you have any job openings?", "es": "¿Tienen alguna vacante?", "pt": "Vocês têm alguma vaga disponível?",
         "fr": "Avez-vous des postes vacants?", "de": "Haben Sie offene Stellen?"},
        {"en": "I'd like to submit my resume", "es": "Me gustaría presentar mi currículum", "pt": "Gostaria de enviar meu currículo",
         "fr": "J'aimerais soumettre mon CV", "de": "Ich möchte meinen Lebenslauf einreichen"},
        {"en": "I have experience in this field", "es": "Tengo experiencia en este campo", "pt": "Tenho experiência nesta área",
         "fr": "J'ai de l'expérience dans ce domaine", "de": "Ich habe Erfahrung in diesem Bereich"},
        {"en": "What skills are you looking for?", "es": "¿Qué habilidades están buscando?", "pt": "Quais habilidades vocês estão procurando?",
         "fr": "Quelles compétences recherchez-vous?", "de": "Welche Fähigkeiten suchen Sie?"},
        {"en": "Is this a full-time position?", "es": "¿Es un puesto a tiempo completo?", "pt": "Esta é uma posição de tempo integral?",
         "fr": "Est-ce un poste à temps plein?", "de": "Ist das eine Vollzeitstelle?"},
        {"en": "What's the application process?", "es": "¿Cuál es el proceso de solicitud?", "pt": "Qual é o processo de candidatura?",
         "fr": "Quel est le processus de candidature?", "de": "Wie läuft der Bewerbungsprozess ab?"},
        {"en": "I'm available for an interview", "es": "Estoy disponible para una entrevista", "pt": "Estou disponível para uma entrevista",
         "fr": "Je suis disponible pour un entretien", "de": "Ich bin für ein Vorstellungsgespräch verfügbar"},
        {"en": "What's the salary range?", "es": "¿Cuál es el rango salarial?", "pt": "Qual é a faixa salarial?",
         "fr": "Quelle est la fourchette de salaire?", "de": "Wie ist die Gehaltsspanne?"},
        {"en": "I'm interested in remote work", "es": "Estoy interesado/a en trabajo remoto", "pt": "Estou interessado/a em trabalho remoto",
         "fr": "Je suis intéressé(e) par le travail à distance", "de": "Ich bin an Fernarbeit interessiert"}
    ],
    "Resume and Qualifications": [
        {"en": "I have a degree in Computer Science", "es": "Tengo un título en Informática", "pt": "Tenho um diploma em Ciência da Computação",
         "fr": "J'ai un diplôme en informatique", "de": "Ich habe einen Abschluss in Informatik"},
        {"en": "I've worked for five years in this industry", "es": "He trabajado durante cinco años en esta industria", "pt": "Trabalhei por cinco anos nesta indústria",
         "fr": "J'ai travaillé pendant cinq ans dans cette industrie", "de": "Ich habe fünf Jahre in dieser Branche gearbeitet"},
        {"en": "My strengths are problem-solving and teamwork", "es": "Mis fortalezas son la resolución de problemas y el trabajo en equipo", "pt": "Meus pontos fortes são resolução de problemas e trabalho em equipe",
         "fr": "Mes points forts sont la résolution de problèmes et le travail d'équipe", "de": "Meine Stärken sind Problemlösung und Teamarbeit"},
        {"en": "I'm proficient in several programming languages", "es": "Soy competente en varios lenguajes de programación", "pt": "Sou proficiente em várias linguagens de programação",
         "fr": "Je maîtrise plusieurs langages de programmation", "de": "Ich bin in mehreren Programmiersprachen versiert"},
        {"en": "I have leadership experience", "es": "Tengo experiencia en liderazgo", "pt": "Tenho experiência em liderança",
         "fr": "J'ai une expérience de leadership", "de": "Ich habe Führungserfahrung"},
        {"en": "I'm certified in project management", "es": "Estoy certificado/a en gestión de proyectos", "pt": "Sou certificado/a em gestão de projetos",
         "fr": "Je suis certifié(e) en gestion de projet", "de": "Ich bin zertifiziert im Projektmanagement"},
        {"en": "I speak three languages fluently", "es": "Hablo tres idiomas con fluidez", "pt": "Falo três idiomas fluentemente",
         "fr": "Je parle couramment trois langues", "de": "Ich spreche fließend drei Sprachen"},
        {"en": "I have experience with international clients", "es": "Tengo experiencia con clientes internacionales", "pt": "Tenho experiência com clientes internacionais",
         "fr": "J'ai de l'expérience avec des clients internationaux", "de": "Ich habe Erfahrung mit internationalen Kunden"},
        {"en": "I'm adaptable to new environments", "es": "Me adapto a nuevos entornos", "pt": "Sou adaptável a novos ambientes",
         "fr": "Je m'adapte facilement à de nouveaux environnements", "de": "Ich bin anpassungsfähig an neue Umgebungen"},
        {"en": "I'm a quick learner", "es": "Aprendo rápido", "pt": "Aprendo rápido",
         "fr": "J'apprends vite", "de": "Ich lerne schnell"}
    ],
    "Job Interview Phrases": [
        {"en": "Thank you for this opportunity", "es": "Gracias por esta oportunidad", "pt": "Obrigado/a por esta oportunidade",
         "fr": "Merci pour cette opportunité", "de": "Vielen Dank für diese Gelegenheit"},
        {"en": "Let me tell you about my experience", "es": "Permítame contarle sobre mi experiencia", "pt": "Deixe-me contar sobre minha experiência",
         "fr": "Laissez-moi vous parler de mon expérience", "de": "Lassen Sie mich von meiner Erfahrung erzählen"},
        {"en": "I'm particularly interested in this role because...", "es": "Estoy particularmente interesado/a en este puesto porque...", "pt": "Estou particularmente interessado/a nesta função porque...",
         "fr": "Je suis particulièrement intéressé(e) par ce poste parce que...", "de": "Ich bin besonders an dieser Position interessiert, weil..."},
        {"en": "Could you tell me more about the team?", "es": "¿Podría contarme más sobre el equipo?", "pt": "Poderia me contar mais sobre a equipe?",
         "fr": "Pourriez-vous m'en dire plus sur l'équipe?", "de": "Könnten Sie mir mehr über das Team erzählen?"},
        {"en": "What would be my main responsibilities?", "es": "¿Cuáles serían mis principales responsabilidades?", "pt": "Quais seriam minhas principais responsabilidades?",
         "fr": "Quelles seraient mes principales responsabilités?", "de": "Was wären meine Hauptverantwortlichkeiten?"},
        {"en": "I handled a similar challenge in my previous job", "es": "Manejé un desafío similar en mi trabajo anterior", "pt": "Lidei com um desafio semelhante no meu emprego anterior",
         "fr": "J'ai géré un défi similaire dans mon emploi précédent", "de": "Ich habe eine ähnliche Herausforderung in meinem vorherigen Job bewältigt"},
        {"en": "I'm looking for growth opportunities", "es": "Estoy buscando oportunidades de crecimiento", "pt": "Estou procurando oportunidades de crescimento",
         "fr": "Je recherche des opportunités de croissance", "de": "Ich suche nach Wachstumsmöglichkeiten"},
        {"en": "What's the company culture like?", "es": "¿Cómo es la cultura de la empresa?", "pt": "Como é a cultura da empresa?",
         "fr": "Comment est la culture de l'entreprise?", "de": "Wie ist die Unternehmenskultur?"},
        {"en": "I have some questions about the position", "es": "Tengo algunas preguntas sobre el puesto", "pt": "Tenho algumas perguntas sobre a posição",
         "fr": "J'ai quelques questions sur le poste", "de": "Ich habe einige Fragen zur Position"},
        {"en": "When can I expect to hear back from you?", "es": "¿Cuándo puedo esperar tener noticias suyas?", "pt": "Quando posso esperar um retorno?",
         "fr": "Quand puis-je m'attendre à avoir de vos nouvelles?", "de": "Wann kann ich mit einer Rückmeldung von Ihnen rechnen?"}
    ],
    "Work Permits and Legal Requirements": [
        {"en": "I need information about work visas", "es": "Necesito información sobre visas de trabajo", "pt": "Preciso de informações sobre vistos de trabalho",
         "fr": "J'ai besoin d'informations sur les visas de travail", "de": "Ich benötige Informationen über Arbeitsvisa"},
        {"en": "What documents do I need to work legally?", "es": "¿Qué documentos necesito para trabajar legalmente?", "pt": "Quais documentos preciso para trabalhar legalmente?",
         "fr": "Quels documents me faut-il pour travailler légalement?", "de": "Welche Dokumente benötige ich, um legal zu arbeiten?"},
        {"en": "How long does the visa process take?", "es": "¿Cuánto tiempo toma el proceso de visa?", "pt": "Quanto tempo leva o processo de visto?",
         "fr": "Combien de temps prend le processus de visa?", "de": "Wie lange dauert der Visumsprozess?"},
        {"en": "Do I need to validate my foreign degree?", "es": "¿Necesito validar mi título extranjero?", "pt": "Preciso validar meu diploma estrangeiro?",
         "fr": "Dois-je valider mon diplôme étranger?", "de": "Muss ich meinen ausländischen Abschluss anerkennen lassen?"},
        {"en": "Can the company sponsor my work permit?", "es": "¿Puede la empresa patrocinar mi permiso de trabajo?", "pt": "A empresa pode patrocinar minha autorização de trabalho?",
         "fr": "L'entreprise peut-elle parrainer mon permis de travail?", "de": "Kann das Unternehmen meine Arbeitserlaubnis sponsern?"},
        {"en": "I need to register with tax authorities", "es": "Necesito registrarme en las autoridades fiscales", "pt": "Preciso me registrar nas autoridades fiscais",
         "fr": "Je dois m'inscrire auprès des autorités fiscales", "de": "Ich muss mich bei den Steuerbehörden anmelden"},
        {"en": "What's the process for obtaining a work permit?", "es": "¿Cuál es el proceso para obtener un permiso de trabajo?", "pt": "Qual é o processo para obter uma autorização de trabalho?",
         "fr": "Quel est le processus pour obtenir un permis de travail?", "de": "Wie ist der Prozess zur Erlangung einer Arbeitserlaubnis?"},
        {"en": "Are there any restrictions for foreign workers?", "es": "¿Hay alguna restricción para trabajadores extranjeros?", "pt": "Existem restrições para trabalhadores estrangeiros?",
         "fr": "Y a-t-il des restrictions pour les travailleurs étrangers?", "de": "Gibt es Einschränkungen für ausländische Arbeitnehmer?"},
        {"en": "I need to open a bank account for my salary", "es": "Necesito abrir una cuenta bancaria para mi salario", "pt": "Preciso abrir uma conta bancária para meu salário",
         "fr": "Je dois ouvrir un compte bancaire pour mon salaire", "de": "Ich muss ein Bankkonto für mein Gehalt eröffnen"},
        {"en": "What healthcare benefits are provided?", "es": "¿Qué beneficios de salud se proporcionan?", "pt": "Quais benefícios de saúde são fornecidos?",
         "fr": "Quels avantages de santé sont fournis?", "de": "Welche Gesundheitsleistungen werden angeboten?"}
    ],
    "Networking and Job Platforms": [
        {"en": "Are there any tech meetups in the city?", "es": "¿Hay encuentros tecnológicos en la ciudad?", "pt": "Existem encontros de tecnologia na cidade?",
         "fr": "Y a-t-il des rencontres technologiques dans la ville?", "de": "Gibt es Tech-Meetups in der Stadt?"},
        {"en": "Which job platforms are popular here?", "es": "¿Qué plataformas de empleo son populares aquí?", "pt": "Quais plataformas de emprego são populares aqui?",
         "fr": "Quelles plateformes d'emploi sont populaires ici?", "de": "Welche Jobplattformen sind hier beliebt?"},
        {"en": "I'd like to connect with professionals in my field", "es": "Me gustaría conectar con profesionales en mi campo", "pt": "Gostaria de me conectar com profissionais na minha área",
         "fr": "J'aimerais me connecter avec des professionnels dans mon domaine", "de": "Ich würde gerne mit Fachleuten in meinem Bereich in Kontakt treten"},
        {"en": "Do you know of any industry conferences?", "es": "¿Conoces alguna conferencia de la industria?", "pt": "Você conhece alguma conferência da indústria?",
         "fr": "Connaissez-vous des conférences de l'industrie?", "de": "Kennen Sie irgendwelche Branchenkonferenzen?"},
        {"en": "Can you recommend any professional associations?", "es": "¿Puede recomendar alguna asociación profesional?", "pt": "Pode recomendar alguma associação profissional?",
         "fr": "Pouvez-vous recommander des associations professionnelles?", "de": "Können Sie Berufsverbände empfehlen?"},
        {"en": "I'm updating my LinkedIn profile", "es": "Estoy actualizando mi perfil de LinkedIn", "pt": "Estou atualizando meu perfil do LinkedIn",
         "fr": "Je mets à jour mon profil LinkedIn", "de": "Ich aktualisiere mein LinkedIn-Profil"},
        {"en": "Are there any job fairs coming up?", "es": "¿Hay ferias de empleo próximamente?", "pt": "Existem feiras de emprego em breve?",
         "fr": "Y a-t-il des salons de l'emploi à venir?", "de": "Stehen Jobmessen bevor?"},
        {"en": "I'd like to build my professional network", "es": "Me gustaría construir mi red profesional", "pt": "Gostaria de construir minha rede profissional",
         "fr": "J'aimerais construire mon réseau professionnel", "de": "Ich möchte mein berufliches Netzwerk aufbauen"},
        {"en": "Do recruiters use this platform?", "es": "¿Los reclutadores usan esta plataforma?", "pt": "Os recrutadores usam esta plataforma?",
         "fr": "Les recruteurs utilisent-ils cette plateforme?", "de": "Nutzen Personalvermittler diese Plattform?"},
        {"en": "I'm looking for mentorship opportunities", "es": "Estoy buscando oportunidades de mentoría", "pt": "Estou procurando oportunidades de mentoria",
         "fr": "Je cherche des opportunités de mentorat", "de": "Ich suche nach Mentoring-Möglichkeiten"}
    ]
}

# Dictionary mapping day numbers to phrase dictionaries
all_phrases = {
    16: day16_phrases,  # Finding Housing and Accommodation
    17: day17_phrases,  # Job Hunting Abroad
    18: day18_phrases,  # Banking and Finance
    19: day19_phrases,  # Healthcare Systems
    20: day20_phrases,  # Geography and Environment
    21: day21_phrases,  # Workplace Language and Etiquette
    22: day22_phrases,  # Cultural Heritage and Influence
    23: day23_phrases,  # Banking and Bureaucracy
    24: day24_phrases,  # Transportation and Logistics
    25: day25_phrases,  # Social Integration - Making Friends and Building Community
    26: day26_phrases,  # Social Integration - Dating, Safety, and Traditions
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
    parser = argparse.ArgumentParser(description="Generate language learning files for Living & Working Abroad (Days 16-26)")
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
    print("  - Generate text files only: python language_phrases_days_16_26.py --text-only")
    print("  - Generate files for just Day 16: python language_phrases_days_16_26.py --day 16")
    print("  - Generate files for just Spanish: python language_phrases_days_16_26.py --languages es")
    print("  - Generate Day 22 Portuguese text only: python language_phrases_days_16_26.py --day 22 --languages pt --text-only")
    print("  - Generate all available days: python language_phrases_days_16_26.py")

if __name__ == "__main__":
    main()