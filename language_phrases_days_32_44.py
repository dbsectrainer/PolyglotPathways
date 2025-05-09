import argparse
import os
import time
from gtts import gTTS

# This file contains days 32-44 of advanced language phrases
# Following the same structure as previous files but with enhanced content
# focusing on Academic & Professional Communication, Literary & Cultural Mastery,
# and Advanced Social Interaction

# Day 32: Academic Writing and Research
day32_phrases = {
    "Academic Writing Style": [
        {"en": "Based on the findings of this study", "es": "Según los hallazgos de este estudio", "pt": "Com base nos resultados deste estudo",
         "fr": "D'après les résultats de cette étude", "de": "Basierend auf den Ergebnissen dieser Studie"},
        {"en": "The data suggests that", "es": "Los datos sugieren que", "pt": "Os dados sugerem que",
         "fr": "Les données suggèrent que", "de": "Die Daten deuten darauf hin, dass"},
        {"en": "Previous research has shown", "es": "Investigaciones previas han demostrado", "pt": "Pesquisas anteriores demonstraram",
         "fr": "Les recherches antérieures ont montré", "de": "Frühere Forschungen haben gezeigt"},
        {"en": "This paper argues that", "es": "Este trabajo sostiene que", "pt": "Este artigo argumenta que",
         "fr": "Cet article soutient que", "de": "Diese Arbeit argumentiert, dass"},
        {"en": "The methodology employed", "es": "La metodología empleada", "pt": "A metodologia empregada",
         "fr": "La méthodologie employée", "de": "Die verwendete Methodologie"},
        {"en": "Significant correlation between", "es": "Correlación significativa entre", "pt": "Correlação significativa entre",
         "fr": "Corrélation significative entre", "de": "Signifikante Korrelation zwischen"},
        {"en": "Further research is needed", "es": "Se necesita más investigación", "pt": "Mais pesquisas são necessárias",
         "fr": "Des recherches supplémentaires sont nécessaires", "de": "Weitere Forschung ist erforderlich"},
        {"en": "The results indicate that", "es": "Los resultados indican que", "pt": "Os resultados indicam que",
         "fr": "Les résultats indiquent que", "de": "Die Ergebnisse zeigen, dass"},
        {"en": "In conclusion", "es": "En conclusión", "pt": "Em conclusão",
         "fr": "En conclusion", "de": "Zusammenfassend"},
        {"en": "This study contributes to", "es": "Este estudio contribuye a", "pt": "Este estudo contribui para",
         "fr": "Cette étude contribue à", "de": "Diese Studie trägt bei zu"}
    ],
    "Research Terminology": [
        {"en": "Quantitative analysis", "es": "Análisis cuantitativo", "pt": "Análise quantitativa",
         "fr": "Analyse quantitative", "de": "Quantitative Analyse"},
        {"en": "Qualitative research", "es": "Investigación cualitativa", "pt": "Pesquisa qualitativa",
         "fr": "Recherche qualitative", "de": "Qualitative Forschung"},
        {"en": "Statistical significance", "es": "Significancia estadística", "pt": "Significância estatística",
         "fr": "Signification statistique", "de": "Statistische Signifikanz"},
        {"en": "Literature review", "es": "Revisión de literatura", "pt": "Revisão de literatura",
         "fr": "Revue de littérature", "de": "Literaturübersicht"},
        {"en": "Empirical evidence", "es": "Evidencia empírica", "pt": "Evidência empírica",
         "fr": "Preuve empirique", "de": "Empirische Evidenz"},
        {"en": "Theoretical framework", "es": "Marco teórico", "pt": "Referencial teórico",
         "fr": "Cadre théorique", "de": "Theoretischer Rahmen"},
        {"en": "Research methodology", "es": "Metodología de investigación", "pt": "Metodologia de pesquisa",
         "fr": "Méthodologie de recherche", "de": "Forschungsmethodik"},
        {"en": "Data collection", "es": "Recolección de datos", "pt": "Coleta de dados",
         "fr": "Collecte de données", "de": "Datenerhebung"},
        {"en": "Hypothesis testing", "es": "Prueba de hipótesis", "pt": "Teste de hipótese",
         "fr": "Test d'hypothèse", "de": "Hypothesentest"},
        {"en": "Peer review", "es": "Revisión por pares", "pt": "Revisão por pares",
         "fr": "Évaluation par les pairs", "de": "Peer-Review"}
    ],
    "Academic Presentations": [
        {"en": "Let me begin by introducing", "es": "Permítanme comenzar presentando", "pt": "Permitam-me começar apresentando",
         "fr": "Permettez-moi de commencer par présenter", "de": "Lassen Sie mich damit beginnen"},
        {"en": "The key objectives are", "es": "Los objetivos principales son", "pt": "Os objetivos principais são",
         "fr": "Les objectifs principaux sont", "de": "Die Hauptziele sind"},
        {"en": "Moving on to the next point", "es": "Pasando al siguiente punto", "pt": "Passando ao próximo ponto",
         "fr": "Passons au point suivant", "de": "Kommen wir zum nächsten Punkt"},
        {"en": "As shown in this graph", "es": "Como se muestra en este gráfico", "pt": "Como mostrado neste gráfico",
         "fr": "Comme le montre ce graphique", "de": "Wie in dieser Grafik gezeigt"},
        {"en": "To illustrate this concept", "es": "Para ilustrar este concepto", "pt": "Para ilustrar este conceito",
         "fr": "Pour illustrer ce concept", "de": "Um dieses Konzept zu veranschaulichen"},
        {"en": "Let me emphasize that", "es": "Permítanme enfatizar que", "pt": "Deixem-me enfatizar que",
         "fr": "Permettez-moi de souligner que", "de": "Lassen Sie mich betonen, dass"},
        {"en": "In summary", "es": "En resumen", "pt": "Em resumo",
         "fr": "En résumé", "de": "Zusammenfassend"},
        {"en": "Are there any questions?", "es": "¿Hay alguna pregunta?", "pt": "Há alguma pergunta?",
         "fr": "Y a-t-il des questions ?", "de": "Gibt es Fragen?"},
        {"en": "Thank you for your attention", "es": "Gracias por su atención", "pt": "Obrigado pela atenção",
         "fr": "Merci de votre attention", "de": "Danke für Ihre Aufmerksamkeit"},
        {"en": "I'd be happy to elaborate", "es": "Me complacería elaborar más", "pt": "Terei prazer em elaborar",
         "fr": "Je serai ravi d'élaborer", "de": "Ich erläutere das gerne näher"}
    ],
    "Citations and References": [
        {"en": "According to [Author]", "es": "Según [Autor]", "pt": "De acordo com [Autor]",
         "fr": "Selon [Auteur]", "de": "Laut [Autor]"},
        {"en": "As cited in", "es": "Como se cita en", "pt": "Como citado em",
         "fr": "Comme cité dans", "de": "Wie zitiert in"},
        {"en": "Et al.", "es": "Et al.", "pt": "Et al.",
         "fr": "Et al.", "de": "Et al."},
        {"en": "In reference to", "es": "En referencia a", "pt": "Em referência a",
         "fr": "En référence à", "de": "In Bezug auf"},
        {"en": "Bibliography", "es": "Bibliografía", "pt": "Bibliografia",
         "fr": "Bibliographie", "de": "Bibliografie"},
        {"en": "Works cited", "es": "Obras citadas", "pt": "Obras citadas",
         "fr": "Ouvrages cités", "de": "Zitierte Werke"},
        {"en": "Primary source", "es": "Fuente primaria", "pt": "Fonte primária",
         "fr": "Source primaire", "de": "Primärquelle"},
        {"en": "Secondary source", "es": "Fuente secundaria", "pt": "Fonte secundária",
         "fr": "Source secondaire", "de": "Sekundärquelle"},
        {"en": "In-text citation", "es": "Cita en el texto", "pt": "Citação no texto",
         "fr": "Citation dans le texte", "de": "Textzitat"},
        {"en": "Reference list", "es": "Lista de referencias", "pt": "Lista de referências",
         "fr": "Liste de références", "de": "Literaturverzeichnis"}
    ]
}

# Day 33: Professional Negotiations and Conflict Resolution
day33_phrases = {
    "Negotiation Techniques": [
        {"en": "Let's find a mutually beneficial solution", "es": "Busquemos una solución mutuamente beneficiosa", "pt": "Vamos encontrar uma solução mutuamente benéfica",
         "fr": "Trouvons une solution mutuellement bénéfique", "de": "Lassen Sie uns eine für beide Seiten vorteilhafte Lösung finden"},
        {"en": "I propose the following compromise", "es": "Propongo el siguiente compromiso", "pt": "Proponho o seguinte compromisso",
         "fr": "Je propose le compromis suivant", "de": "Ich schlage folgenden Kompromiss vor"},
        {"en": "From our perspective", "es": "Desde nuestra perspectiva", "pt": "Da nossa perspectiva",
         "fr": "De notre point de vue", "de": "Aus unserer Sicht"},
        {"en": "What are your main concerns?", "es": "¿Cuáles son sus principales preocupaciones?", "pt": "Quais são suas principais preocupações?",
         "fr": "Quelles sont vos principales préoccupations ?", "de": "Was sind Ihre Hauptbedenken?"},
        {"en": "Let's explore our options", "es": "Exploremos nuestras opciones", "pt": "Vamos explorar nossas opções",
         "fr": "Explorons nos options", "de": "Lassen Sie uns unsere Optionen erkunden"},
        {"en": "I understand your position", "es": "Entiendo su posición", "pt": "Entendo sua posição",
         "fr": "Je comprends votre position", "de": "Ich verstehe Ihre Position"},
        {"en": "Can we meet halfway?", "es": "¿Podemos llegar a un punto medio?", "pt": "Podemos chegar a um meio-termo?",
         "fr": "Pouvons-nous trouver un compromis ?", "de": "Können wir uns in der Mitte treffen?"},
        {"en": "What would you suggest?", "es": "¿Qué sugeriría usted?", "pt": "O que você sugeriria?",
         "fr": "Que suggéreriez-vous ?", "de": "Was würden Sie vorschlagen?"},
        {"en": "Let's review the terms", "es": "Revisemos los términos", "pt": "Vamos revisar os termos",
         "fr": "Revoyons les termes", "de": "Lassen Sie uns die Bedingungen überprüfen"},
        {"en": "I need time to consider this", "es": "Necesito tiempo para considerar esto", "pt": "Preciso de tempo para considerar isso",
         "fr": "J'ai besoin de temps pour réfléchir à cela", "de": "Ich brauche Zeit, das zu überdenken"}
    ],
    "Conflict Resolution": [
        {"en": "Let's address this issue directly", "es": "Abordemos este tema directamente", "pt": "Vamos abordar esta questão diretamente",
         "fr": "Abordons cette question directement", "de": "Lassen Sie uns dieses Problem direkt angehen"},
        {"en": "I value your perspective", "es": "Valoro su perspectiva", "pt": "Valorizo sua perspectiva",
         "fr": "Je valorise votre point de vue", "de": "Ich schätze Ihre Perspektive"},
        {"en": "How can we resolve this?", "es": "¿Cómo podemos resolver esto?", "pt": "Como podemos resolver isso?",
         "fr": "Comment pouvons-nous résoudre cela ?", "de": "Wie können wir das lösen?"},
        {"en": "Let's focus on solutions", "es": "Centrémonos en las soluciones", "pt": "Vamos focar nas soluções",
         "fr": "Concentrons-nous sur les solutions", "de": "Lassen Sie uns auf Lösungen fokussieren"},
        {"en": "I apologize if I misunderstood", "es": "Me disculpo si malinterpreté", "pt": "Desculpe se entendi mal",
         "fr": "Je m'excuse si j'ai mal compris", "de": "Ich entschuldige mich, falls ich etwas missverstanden habe"},
        {"en": "Can we start over?", "es": "¿Podemos empezar de nuevo?", "pt": "Podemos começar de novo?",
         "fr": "Pouvons-nous recommencer ?", "de": "Können wir von vorne anfangen?"},
        {"en": "Let's maintain professional courtesy", "es": "Mantengamos la cortesía profesional", "pt": "Vamos manter a cortesia profissional",
         "fr": "Gardons une courtoisie professionnelle", "de": "Lassen Sie uns professionelle Höflichkeit wahren"},
        {"en": "I appreciate your feedback", "es": "Agradezco sus comentarios", "pt": "Agradeço seu feedback",
         "fr": "J'apprécie vos commentaires", "de": "Ich schätze Ihr Feedback"},
        {"en": "Let's clarify our expectations", "es": "Aclaremos nuestras expectativas", "pt": "Vamos esclarecer nossas expectativas",
         "fr": "Clarifions nos attentes", "de": "Lassen Sie uns unsere Erwartungen klären"},
        {"en": "I'm committed to finding a solution", "es": "Estoy comprometido a encontrar una solución", "pt": "Estou comprometido em encontrar uma solução",
         "fr": "Je m'engage à trouver une solution", "de": "Ich bin entschlossen, eine Lösung zu finden"}
    ],
    "Professional Diplomacy": [
        {"en": "I respectfully disagree", "es": "Respetuosamente discrepo", "pt": "Respeitosamente discordo",
         "fr": "Je ne suis respectueusement pas d'accord", "de": "Ich bin respektvoll anderer Meinung"},
        {"en": "Perhaps we could consider", "es": "Tal vez podríamos considerar", "pt": "Talvez pudéssemos considerar",
         "fr": "Peut-être pourrions-nous envisager", "de": "Vielleicht könnten wir in Betracht ziehen"},
        {"en": "I appreciate your input", "es": "Aprecio su aporte", "pt": "Aprecio sua contribuição",
         "fr": "J'apprécie votre contribution", "de": "Ich schätze Ihren Beitrag"},
        {"en": "Let me clarify my position", "es": "Permítame aclarar mi posición", "pt": "Deixe-me esclarecer minha posição",
         "fr": "Permettez-moi de clarifier ma position", "de": "Lassen Sie mich meine Position klarstellen"},
        {"en": "I see merit in your argument", "es": "Veo mérito en su argumento", "pt": "Vejo mérito em seu argumento",
         "fr": "Je vois du mérite dans votre argument", "de": "Ich sehe den Wert in Ihrem Argument"},
        {"en": "Would you please elaborate?", "es": "¿Podría elaborar, por favor?", "pt": "Poderia elaborar, por favor?",
         "fr": "Pourriez-vous développer, s'il vous plaît ?", "de": "Könnten Sie das bitte näher ausführen?"},
        {"en": "That's an interesting perspective", "es": "Es una perspectiva interesante", "pt": "Essa é uma perspectiva interessante",
         "fr": "C'est une perspective intéressante", "de": "Das ist eine interessante Perspektive"},
        {"en": "Let's maintain open dialogue", "es": "Mantengamos un diálogo abierto", "pt": "Vamos manter um diálogo aberto",
         "fr": "Maintenons un dialogue ouvert", "de": "Lassen Sie uns einen offenen Dialog pflegen"},
        {"en": "I value your expertise", "es": "Valoro su experiencia", "pt": "Valorizo sua experiência",
         "fr": "Je valorise votre expertise", "de": "Ich schätze Ihre Expertise"},
        {"en": "Thank you for bringing this to my attention", "es": "Gracias por traer esto a mi atención", "pt": "Obrigado por trazer isso à minha atenção",
         "fr": "Merci d'avoir porté cela à mon attention", "de": "Danke, dass Sie mich darauf aufmerksam gemacht haben"}
    ]
}

# Day 34: Complex Business Proposals and Reports
day34_phrases = {
    "Business Proposals": [
        {"en": "Executive summary", "es": "Resumen ejecutivo", "pt": "Resumo executivo",
         "fr": "Résumé exécutif", "de": "Zusammenfassende Übersicht"},
        {"en": "Project scope", "es": "Alcance del proyecto", "pt": "Escopo do projeto",
         "fr": "Portée du projet", "de": "Projektumfang"},
        {"en": "Market analysis", "es": "Análisis de mercado", "pt": "Análise de mercado",
         "fr": "Analyse de marché", "de": "Marktanalyse"},
        {"en": "Financial projections", "es": "Proyecciones financieras", "pt": "Projeções financeiras",
         "fr": "Projections financières", "de": "Finanzprognosen"},
        {"en": "Implementation timeline", "es": "Cronograma de implementación", "pt": "Cronograma de implementação",
         "fr": "Calendrier de mise en œuvre", "de": "Implementierungszeitplan"},
        {"en": "Risk assessment", "es": "Evaluación de riesgos", "pt": "Avaliação de riscos",
         "fr": "Évaluation des risques", "de": "Risikobewertung"},
        {"en": "Cost-benefit analysis", "es": "Análisis costo-beneficio", "pt": "Análise custo-benefício",
         "fr": "Analyse coûts-bénéfices", "de": "Kosten-Nutzen-Analyse"},
        {"en": "Strategic objectives", "es": "Objetivos estratégicos", "pt": "Objetivos estratégicos",
         "fr": "Objectifs stratégiques", "de": "Strategische Ziele"},
        {"en": "Resource allocation", "es": "Asignación de recursos", "pt": "Alocação de recursos",
         "fr": "Allocation des ressources", "de": "Ressourcenzuweisung"},
        {"en": "Expected outcomes", "es": "Resultados esperados", "pt": "Resultados esperados",
         "fr": "Résultats attendus", "de": "Erwartete Ergebnisse"}
    ],
    "Report Writing": [
        {"en": "Key findings indicate", "es": "Los hallazgos clave indican", "pt": "As principais conclusões indicam",
         "fr": "Les principales conclusions indiquent", "de": "Die wichtigsten Erkenntnisse zeigen"},
        {"en": "Quarterly performance", "es": "Desempeño trimestral", "pt": "Desempenho trimestral",
         "fr": "Performance trimestrielle", "de": "Quartalsleistung"},
        {"en": "Trend analysis shows", "es": "El análisis de tendencias muestra", "pt": "A análise de tendências mostra",
         "fr": "L'analyse des tendances montre", "de": "Die Trendanalyse zeigt"},
        {"en": "Comparative data", "es": "Datos comparativos", "pt": "Dados comparativos",
         "fr": "Données comparatives", "de": "Vergleichsdaten"},
        {"en": "Recommendations include", "es": "Las recomendaciones incluyen", "pt": "As recomendações incluem",
         "fr": "Les recommandations incluent", "de": "Empfehlungen beinhalten"},
        {"en": "Statistical analysis", "es": "Análisis estadístico", "pt": "Análise estatística",
         "fr": "Analyse statistique", "de": "Statistische Analyse"},
        {"en": "Growth indicators", "es": "Indicadores de crecimiento", "pt": "Indicadores de crescimento",
         "fr": "Indicateurs de croissance", "de": "Wachstumsindikatoren"},
        {"en": "Market share", "es": "Cuota de mercado", "pt": "Participação de mercado",
         "fr": "Part de marché", "de": "Marktanteil"},
        {"en": "Budget allocation", "es": "Asignación presupuestaria", "pt": "Alocação orçamentária",
         "fr": "Allocation budgétaire", "de": "Budgetzuweisung"},
        {"en": "Performance metrics", "es": "Métricas de desempeño", "pt": "Métricas de desempenho",
         "fr": "Indicateurs de performance", "de": "Leistungskennzahlen"}
    ],
    "Business Strategy": [
        {"en": "Competitive advantage", "es": "Ventaja competitiva", "pt": "Vantagem competitiva",
         "fr": "Avantage concurrentiel", "de": "Wettbewerbsvorteil"},
        {"en": "Market positioning", "es": "Posicionamiento en el mercado", "pt": "Posicionamento no mercado",
         "fr": "Positionnement sur le marché", "de": "Marktpositionierung"},
        {"en": "Growth strategy", "es": "Estrategia de crecimiento", "pt": "Estratégia de crescimento",
         "fr": "Stratégie de croissance", "de": "Wachstumsstrategie"},
        {"en": "Target demographics", "es": "Demografía objetivo", "pt": "Demografia-alvo",
         "fr": "Démographie cible", "de": "Zielgruppe"},
        {"en": "Revenue streams", "es": "Fuentes de ingresos", "pt": "Fontes de receita",
         "fr": "Sources de revenus", "de": "Einnahmequellen"},
        {"en": "Market penetration", "es": "Penetración de mercado", "pt": "Penetração de mercado",
         "fr": "Pénétration du marché", "de": "Marktdurchdringung"},
        {"en": "Business model", "es": "Modelo de negocio", "pt": "Modelo de negócios",
         "fr": "Modèle d'affaires", "de": "Geschäftsmodell"},
        {"en": "Value proposition", "es": "Propuesta de valor", "pt": "Proposta de valor",
         "fr": "Proposition de valeur", "de": "Wertversprechen"},
        {"en": "Core competencies", "es": "Competencias principales", "pt": "Competências principais",
         "fr": "Compétences principales", "de": "Kernkompetenzen"},
        {"en": "Strategic partnerships", "es": "Alianzas estratégicas", "pt": "Parcerias estratégicas",
         "fr": "Partenariats stratégiques", "de": "Strategische Partnerschaften"}
    ]
}

# Day 35: Scientific and Research Terminology
day35_phrases = {
    "Scientific Method": [
        {"en": "Hypothesis formulation", "es": "Formulación de hipótesis", "pt": "Formulação de hipótese",
         "fr": "Formulation d'hypothèse", "de": "Hypothesenformulierung"},
        {"en": "Experimental design", "es": "Diseño experimental", "pt": "Desenho experimental",
         "fr": "Conception expérimentale", "de": "Experimentelles Design"},
        {"en": "Control group", "es": "Grupo de control", "pt": "Grupo de controle",
         "fr": "Groupe de contrôle", "de": "Kontrollgruppe"},
        {"en": "Variable analysis", "es": "Análisis de variables", "pt": "Análise de variáveis",
         "fr": "Analyse des variables", "de": "Variablenanalyse"},
        {"en": "Data collection", "es": "Recolección de datos", "pt": "Coleta de dados",
         "fr": "Collecte de données", "de": "Datenerhebung"},
        {"en": "Statistical significance", "es": "Significancia estadística", "pt": "Significância estatística",
         "fr": "Signification statistique", "de": "Statistische Signifikanz"},
        {"en": "Methodology", "es": "Metodología", "pt": "Metodologia",
         "fr": "Méthodologie", "de": "Methodologie"},
        {"en": "Peer review", "es": "Revisión por pares", "pt": "Revisão por pares",
         "fr": "Évaluation par les pairs", "de": "Peer-Review"},
        {"en": "Research findings", "es": "Hallazgos de investigación", "pt": "Resultados da pesquisa",
         "fr": "Résultats de recherche", "de": "Forschungsergebnisse"},
        {"en": "Empirical evidence", "es": "Evidencia empírica", "pt": "Evidência empírica",
         "fr": "Preuve empirique", "de": "Empirische Evidenz"}
    ],
    "Research Process": [
        {"en": "Literature review", "es": "Revisión de literatura", "pt": "Revisão de literatura",
         "fr": "Revue de littérature", "de": "Literaturübersicht"},
        {"en": "Data analysis", "es": "Análisis de datos", "pt": "Análise de dados",
         "fr": "Analyse de données", "de": "Datenanalyse"},
        {"en": "Research objectives", "es": "Objetivos de investigación", "pt": "Objetivos de pesquisa",
         "fr": "Objectifs de recherche", "de": "Forschungsziele"},
        {"en": "Sampling methods", "es": "Métodos de muestreo", "pt": "Métodos de amostragem",
         "fr": "Méthodes d'échantillonnage", "de": "Stichprobenmethoden"},
        {"en": "Research design", "es": "Diseño de investigación", "pt": "Desenho de pesquisa",
         "fr": "Conception de recherche", "de": "Forschungsdesign"},
        {"en": "Data validation", "es": "Validación de datos", "pt": "Validação de dados",
         "fr": "Validation des données", "de": "Datenvalidierung"},
        {"en": "Research ethics", "es": "Ética de investigación", "pt": "Ética em pesquisa",
         "fr": "Éthique de la recherche", "de": "Forschungsethik"},
        {"en": "Pilot study", "es": "Estudio piloto", "pt": "Estudo piloto",
         "fr": "Étude pilote", "de": "Pilotstudie"},
        {"en": "Research methodology", "es": "Metodología de investigación", "pt": "Metodologia de pesquisa",
         "fr": "Méthodologie de recherche", "de": "Forschungsmethodik"},
        {"en": "Data interpretation", "es": "Interpretación de datos", "pt": "Interpretação de dados",
         "fr": "Interprétation des données", "de": "Dateninterpretation"}
    ],
    "Scientific Writing": [
        {"en": "Abstract submission", "es": "Presentación del resumen", "pt": "Submissão do resumo",
         "fr": "Soumission du résumé", "de": "Abstract-Einreichung"},
        {"en": "Research paper", "es": "Artículo de investigación", "pt": "Artigo de pesquisa",
         "fr": "Article de recherche", "de": "Forschungsarbeit"},
        {"en": "Methodology section", "es": "Sección de metodología", "pt": "Seção de metodologia",
         "fr": "Section méthodologie", "de": "Methodenteil"},
        {"en": "Results discussion", "es": "Discusión de resultados", "pt": "Discussão dos resultados",
         "fr": "Discussion des résultats", "de": "Ergebnisdiskussion"},
        {"en": "Literature cited", "es": "Literatura citada", "pt": "Literatura citada",
         "fr": "Littérature citée", "de": "Zitierte Literatur"},
        {"en": "Research proposal", "es": "Propuesta de investigación", "pt": "Proposta de pesquisa",
         "fr": "Proposition de recherche", "de": "Forschungsantrag"},
        {"en": "Peer review process", "es": "Proceso de revisión por pares", "pt": "Processo de revisão por pares",
         "fr": "Processus d'évaluation par les pairs", "de": "Peer-Review-Prozess"},
        {"en": "Publication guidelines", "es": "Pautas de publicación", "pt": "Diretrizes de publicação",
         "fr": "Directives de publication", "de": "Publikationsrichtlinien"},
        {"en": "Journal submission", "es": "Envío a revista", "pt": "Submissão a periódico",
         "fr": "Soumission à une revue", "de": "Zeitschrifteneinreichung"},
        {"en": "Manuscript formatting", "es": "Formato del manuscrito", "pt": "Formatação do manuscrito",
         "fr": "Formatage du manuscrit", "de": "Manuskriptformatierung"}
    ]
}

# Day 36: Literary Analysis and Criticism
day36_phrases = {
    "Literary Analysis": [
        {"en": "Character development", "es": "Desarrollo de personajes", "pt": "Desenvolvimento de personagens",
         "fr": "Développement des personnages", "de": "Charakterentwicklung"},
        {"en": "Plot structure", "es": "Estructura de la trama", "pt": "Estrutura do enredo",
         "fr": "Structure de l'intrigue", "de": "Handlungsstruktur"},
        {"en": "Narrative perspective", "es": "Perspectiva narrativa", "pt": "Perspectiva narrativa",
         "fr": "Perspective narrative", "de": "Erzählperspektive"},
        {"en": "Thematic analysis", "es": "Análisis temático", "pt": "Análise temática",
         "fr": "Analyse thématique", "de": "Thematische Analyse"},
        {"en": "Symbolism", "es": "Simbolismo", "pt": "Simbolismo",
         "fr": "Symbolisme", "de": "Symbolik"},
        {"en": "Literary devices", "es": "Recursos literarios", "pt": "Recursos literários",
         "fr": "Procédés littéraires", "de": "Literarische Stilmittel"},
        {"en": "Foreshadowing", "es": "Presagio", "pt": "Prenúncio",
         "fr": "Préfiguration", "de": "Vorausdeutung"},
        {"en": "Allegory", "es": "Alegoría", "pt": "Alegoria",
         "fr": "Allégorie", "de": "Allegorie"},
        {"en": "Narrative arc", "es": "Arco narrativo", "pt": "Arco narrativo",
         "fr": "Arc narratif", "de": "Erzählbogen"},
        {"en": "Character motivation", "es": "Motivación del personaje", "pt": "Motivação do personagem",
         "fr": "Motivation du personnage", "de": "Charaktermotivation"}
    ],
    "Literary Criticism": [
        {"en": "Critical interpretation", "es": "Interpretación crítica", "pt": "Interpretação crítica",
         "fr": "Interprétation critique", "de": "Kritische Interpretation"},
        {"en": "Textual analysis", "es": "Análisis textual", "pt": "Análise textual",
         "fr": "Analyse textuelle", "de": "Textanalyse"},
        {"en": "Literary theory", "es": "Teoría literaria", "pt": "Teoria literária",
         "fr": "Théorie littéraire", "de": "Literaturtheorie"},
        {"en": "Deconstructionism", "es": "Deconstructivismo", "pt": "Desconstrucionismo",
         "fr": "Déconstructionnisme", "de": "Dekonstruktivismus"},
        {"en": "Feminist criticism", "es": "Crítica feminista", "pt": "Crítica feminista",
         "fr": "Critique féministe", "de": "Feministische Kritik"},
        {"en": "Postcolonial reading", "es": "Lectura poscolonial", "pt": "Leitura pós-colonial",
         "fr": "Lecture postcoloniale", "de": "Postkoloniale Lesart"},
        {"en": "Marxist interpretation", "es": "Interpretación marxista", "pt": "Interpretação marxista",
         "fr": "Interprétation marxiste", "de": "Marxistische Interpretation"},
        {"en": "Psychoanalytic approach", "es": "Enfoque psicoanalítico", "pt": "Abordagem psicanalítica",
         "fr": "Approche psychanalytique", "de": "Psychoanalytischer Ansatz"},
        {"en": "Reader response", "es": "Respuesta del lector", "pt": "Resposta do leitor",
         "fr": "Réponse du lecteur", "de": "Leserreaktion"},
        {"en": "Comparative analysis", "es": "Análisis comparativo", "pt": "Análise comparativa",
         "fr": "Analyse comparative", "de": "Vergleichende Analyse"}
    ],
    "Literary Genres": [
        {"en": "Epic poetry", "es": "Poesía épica", "pt": "Poesia épica",
         "fr": "Poésie épique", "de": "Epische Dichtung"},
        {"en": "Magical realism", "es": "Realismo mágico", "pt": "Realismo mágico",
         "fr": "Réalisme magique", "de": "Magischer Realismus"},
        {"en": "Postmodern literature", "es": "Literatura posmoderna", "pt": "Literatura pós-moderna",
         "fr": "Littérature postmoderne", "de": "Postmoderne Literatur"},
        {"en": "Dystopian fiction", "es": "Ficción distópica", "pt": "Ficção distópica",
         "fr": "Fiction dystopique", "de": "Dystopische Fiktion"},
        {"en": "Bildungsroman", "es": "Novela de formación", "pt": "Romance de formação",
         "fr": "Roman d'apprentissage", "de": "Bildungsroman"},
        {"en": "Metafiction", "es": "Metaficción", "pt": "Metaficção",
         "fr": "Métafiction", "de": "Metafiktion"},
        {"en": "Stream of consciousness", "es": "Flujo de conciencia", "pt": "Fluxo de consciência",
         "fr": "Flux de conscience", "de": "Bewusstseinsstrom"},
        {"en": "Existentialist literature", "es": "Literatura existencialista", "pt": "Literatura existencialista",
         "fr": "Littérature existentialiste", "de": "Existentialistische Literatur"},
        {"en": "Absurdist fiction", "es": "Ficción absurdista", "pt": "Ficção absurdista",
         "fr": "Fiction absurde", "de": "Absurde Fiktion"},
        {"en": "Modernist poetry", "es": "Poesía modernista", "pt": "Poesia modernista",
         "fr": "Poésie moderniste", "de": "Modernistische Poesie"}
    ]
}

# Day 37: Poetry and Figurative Language
day37_phrases = {
    "Poetic Devices": [
        {"en": "Metaphor", "es": "Metáfora", "pt": "Metáfora",
         "fr": "Métaphore", "de": "Metapher"},
        {"en": "Simile", "es": "Símil", "pt": "Símile",
         "fr": "Comparaison", "de": "Vergleich"},
        {"en": "Personification", "es": "Personificación", "pt": "Personificação",
         "fr": "Personnification", "de": "Personifikation"},
        {"en": "Alliteration", "es": "Aliteración", "pt": "Aliteração",
         "fr": "Allitération", "de": "Alliteration"},
        {"en": "Assonance", "es": "Asonancia", "pt": "Assonância",
         "fr": "Assonance", "de": "Assonanz"},
        {"en": "Onomatopoeia", "es": "Onomatopeya", "pt": "Onomatopeia",
         "fr": "Onomatopée", "de": "Onomatopoesie"},
        {"en": "Hyperbole", "es": "Hipérbole", "pt": "Hipérbole",
         "fr": "Hyperbole", "de": "Hyperbel"},
        {"en": "Irony", "es": "Ironía", "pt": "Ironia",
         "fr": "Ironie", "de": "Ironie"},
        {"en": "Oxymoron", "es": "Oxímoron", "pt": "Oxímoro",
         "fr": "Oxymore", "de": "Oxymoron"},
        {"en": "Paradox", "es": "Paradoja", "pt": "Paradoxo",
         "fr": "Paradoxe", "de": "Paradoxon"}
    ],
    "Poetic Forms": [
        {"en": "Sonnet", "es": "Soneto", "pt": "Soneto",
         "fr": "Sonnet", "de": "Sonett"},
        {"en": "Haiku", "es": "Haiku", "pt": "Haicai",
         "fr": "Haïku", "de": "Haiku"},
        {"en": "Free verse", "es": "Verso libre", "pt": "Verso livre",
         "fr": "Vers libre", "de": "Freie Verse"},
        {"en": "Ballad", "es": "Balada", "pt": "Balada",
         "fr": "Ballade", "de": "Ballade"},
        {"en": "Ode", "es": "Oda", "pt": "Ode",
         "fr": "Ode", "de": "Ode"},
        {"en": "Elegy", "es": "Elegía", "pt": "Elegia",
         "fr": "Élégie", "de": "Elegie"},
        {"en": "Epic", "es": "Épica", "pt": "Épico",
         "fr": "Épopée", "de": "Epos"},
        {"en": "Limerick", "es": "Limerick", "pt": "Limerick",
         "fr": "Limerick", "de": "Limerick"},
        {"en": "Villanelle", "es": "Villanela", "pt": "Vilancete",
         "fr": "Villanelle", "de": "Villanelle"},
        {"en": "Sestina", "es": "Sextina", "pt": "Sextina",
         "fr": "Sestine", "de": "Sestine"}
    ],
    "Figurative Language": [
        {"en": "Extended metaphor", "es": "Metáfora extendida", "pt": "Metáfora estendida",
         "fr": "Métaphore filée", "de": "Erweiterte Metapher"},
        {"en": "Synecdoche", "es": "Sinécdoque", "pt": "Sinédoque",
         "fr": "Synecdoque", "de": "Synekdoche"},
        {"en": "Metonymy", "es": "Metonimia", "pt": "Metonímia",
         "fr": "Métonymie", "de": "Metonymie"},
        {"en": "Euphemism", "es": "Eufemismo", "pt": "Eufemismo",
         "fr": "Euphémisme", "de": "Euphemismus"},
        {"en": "Apostrophe", "es": "Apóstrofe", "pt": "Apóstrofe",
         "fr": "Apostrophe", "de": "Apostrophe"},
        {"en": "Imagery", "es": "Imaginería", "pt": "Imagética",
         "fr": "Imagerie", "de": "Bildsprache"},
        {"en": "Allusion", "es": "Alusión", "pt": "Alusão",
         "fr": "Allusion", "de": "Anspielung"},
        {"en": "Symbolism", "es": "Simbolismo", "pt": "Simbolismo",
         "fr": "Symbolisme", "de": "Symbolik"},
        {"en": "Understatement", "es": "Subestimación", "pt": "Eufemismo",
         "fr": "Litote", "de": "Untertreibung"},
        {"en": "Juxtaposition", "es": "Yuxtaposición", "pt": "Justaposição",
         "fr": "Juxtaposition", "de": "Gegenüberstellung"}
    ]
}

# Day 38: Historical and Cultural References
day38_phrases = {
    "Historical Periods": [
        {"en": "Renaissance", "es": "Renacimiento", "pt": "Renascimento",
         "fr": "Renaissance", "de": "Renaissance"},
        {"en": "Enlightenment", "es": "Ilustración", "pt": "Iluminismo",
         "fr": "Siècle des Lumières", "de": "Aufklärung"},
        {"en": "Industrial Revolution", "es": "Revolución Industrial", "pt": "Revolução Industrial",
         "fr": "Révolution industrielle", "de": "Industrielle Revolution"},
        {"en": "Colonial period", "es": "Período colonial", "pt": "Período colonial",
         "fr": "Période coloniale", "de": "Kolonialzeit"},
        {"en": "Post-war era", "es": "Era de posguerra", "pt": "Era pós-guerra",
         "fr": "Ère d'après-guerre", "de": "Nachkriegszeit"},
        {"en": "Cold War", "es": "Guerra Fría", "pt": "Guerra Fria",
         "fr": "Guerre froide", "de": "Kalter Krieg"},
        {"en": "Belle Époque", "es": "Belle Époque", "pt": "Belle Époque",
         "fr": "Belle Époque", "de": "Belle Époque"},
        {"en": "Modernism", "es": "Modernismo", "pt": "Modernismo",
         "fr": "Modernisme", "de": "Moderne"},
        {"en": "Postmodernism", "es": "Posmodernismo", "pt": "Pós-modernismo",
         "fr": "Postmodernisme", "de": "Postmoderne"},
        {"en": "Digital age", "es": "Era digital", "pt": "Era digital",
         "fr": "Ère numérique", "de": "Digitales Zeitalter"}
    ],
    "Cultural Movements": [
        {"en": "Romanticism", "es": "Romanticismo", "pt": "Romantismo",
         "fr": "Romantisme", "de": "Romantik"},
        {"en": "Surrealism", "es": "Surrealismo", "pt": "Surrealismo",
         "fr": "Surréalisme", "de": "Surrealismus"},
        {"en": "Expressionism", "es": "Expresionismo", "pt": "Expressionismo",
         "fr": "Expressionnisme", "de": "Expressionismus"},
        {"en": "Impressionism", "es": "Impresionismo", "pt": "Impressionismo",
         "fr": "Impressionnisme", "de": "Impressionismus"},
        {"en": "Cubism", "es": "Cubismo", "pt": "Cubismo",
         "fr": "Cubisme", "de": "Kubismus"},
        {"en": "Dadaism", "es": "Dadaísmo", "pt": "Dadaísmo",
         "fr": "Dadaïsme", "de": "Dadaismus"},
        {"en": "Futurism", "es": "Futurismo", "pt": "Futurismo",
         "fr": "Futurisme", "de": "Futurismus"},
        {"en": "Minimalism", "es": "Minimalismo", "pt": "Minimalismo",
         "fr": "Minimalisme", "de": "Minimalismus"},
        {"en": "Realism", "es": "Realismo", "pt": "Realismo",
         "fr": "Réalisme", "de": "Realismus"},
        {"en": "Neoclassicism", "es": "Neoclasicismo", "pt": "Neoclassicismo",
         "fr": "Néoclassicisme", "de": "Neoklassizismus"}
    ],
    "Historical References": [
        {"en": "During the reign of", "es": "Durante el reinado de", "pt": "Durante o reinado de",
         "fr": "Pendant le règne de", "de": "Während der Herrschaft von"},
        {"en": "In the aftermath of", "es": "En las secuelas de", "pt": "Nas consequências de",
         "fr": "À la suite de", "de": "In der Folge von"},
        {"en": "At the height of", "es": "En el apogeo de", "pt": "No auge de",
         "fr": "Au sommet de", "de": "Auf dem Höhepunkt von"},
        {"en": "During the era of", "es": "Durante la era de", "pt": "Durante a era de",
         "fr": "Pendant l'ère de", "de": "Während der Ära von"},
        {"en": "In the context of", "es": "En el contexto de", "pt": "No contexto de",
         "fr": "Dans le contexte de", "de": "Im Kontext von"},
        {"en": "Against the backdrop of", "es": "Con el telón de fondo de", "pt": "Tendo como pano de fundo",
         "fr": "Sur fond de", "de": "Vor dem Hintergrund von"},
        {"en": "In the wake of", "es": "A raíz de", "pt": "Na esteira de",
         "fr": "À la suite de", "de": "Im Gefolge von"},
        {"en": "Throughout the period", "es": "A lo largo del período", "pt": "Ao longo do período",
         "fr": "Tout au long de la période", "de": "Während des gesamten Zeitraums"},
        {"en": "In the midst of", "es": "En medio de", "pt": "Em meio a",
         "fr": "Au milieu de", "de": "Inmitten von"},
        {"en": "On the eve of", "es": "En vísperas de", "pt": "Na véspera de",
         "fr": "À la veille de", "de": "Am Vorabend von"}
    ]
}

# Day 39: Film and Media Analysis
day39_phrases = {
    "Film Terminology": [
        {"en": "Cinematography", "es": "Cinematografía", "pt": "Cinematografia",
         "fr": "Cinématographie", "de": "Kameraführung"},
        {"en": "Mise-en-scène", "es": "Puesta en escena", "pt": "Mise-en-scène",
         "fr": "Mise en scène", "de": "Mise-en-scène"},
        {"en": "Montage", "es": "Montaje", "pt": "Montagem",
         "fr": "Montage", "de": "Montage"},
        {"en": "Diegetic sound", "es": "Sonido diegético", "pt": "Som diegético",
         "fr": "Son diégétique", "de": "Diegetischer Ton"},
        {"en": "Non-diegetic sound", "es": "Sonido no diegético", "pt": "Som não diegético",
         "fr": "Son non diégétique", "de": "Nicht-diegetischer Ton"},
        {"en": "Shot composition", "es": "Composición de plano", "pt": "Composição de plano",
         "fr": "Composition du plan", "de": "Bildkomposition"},
        {"en": "Tracking shot", "es": "Plano de seguimiento", "pt": "Plano de acompanhamento",
         "fr": "Plan de travelling", "de": "Kamerafahrt"},
        {"en": "Jump cut", "es": "Corte de salto", "pt": "Corte seco",
         "fr": "Jump cut", "de": "Sprungschnitt"},
        {"en": "Establishing shot", "es": "Plano de establecimiento", "pt": "Plano de estabelecimento",
         "fr": "Plan d'ensemble", "de": "Establishing Shot"},
        {"en": "Close-up", "es": "Primer plano", "pt": "Close-up",
         "fr": "Gros plan", "de": "Nahaufnahme"}
    ],
    "Media Analysis": [
        {"en": "Visual rhetoric", "es": "Retórica visual", "pt": "Retórica visual",
         "fr": "Rhétorique visuelle", "de": "Visuelle Rhetorik"},
        {"en": "Narrative structure", "es": "Estructura narrativa", "pt": "Estrutura narrativa",
         "fr": "Structure narrative", "de": "Erzählstruktur"},
        {"en": "Audience reception", "es": "Recepción del público", "pt": "Recepção do público",
         "fr": "Réception du public", "de": "Publikumsrezeption"},
        {"en": "Media representation", "es": "Representación mediática", "pt": "Representação midiática",
         "fr": "Représentation médiatique", "de": "Mediale Darstellung"},
        {"en": "Critical discourse", "es": "Discurso crítico", "pt": "Discurso crítico",
         "fr": "Discours critique", "de": "Kritischer Diskurs"},
        {"en": "Intertextuality", "es": "Intertextualidad", "pt": "Intertextualidade",
         "fr": "Intertextualité", "de": "Intertextualität"},
        {"en": "Semiotics", "es": "Semiótica", "pt": "Semiótica",
         "fr": "Sémiotique", "de": "Semiotik"},
        {"en": "Cultural context", "es": "Contexto cultural", "pt": "Contexto cultural",
         "fr": "Contexte culturel", "de": "Kultureller Kontext"},
        {"en": "Ideological analysis", "es": "Análisis ideológico", "pt": "Análise ideológica",
         "fr": "Analyse idéologique", "de": "Ideologische Analyse"},
        {"en": "Framing theory", "es": "Teoría del encuadre", "pt": "Teoria do enquadramento",
         "fr": "Théorie du cadrage", "de": "Framing-Theorie"}
    ],
    "Film Genres": [
        {"en": "Film noir", "es": "Cine negro", "pt": "Film noir",
         "fr": "Film noir", "de": "Film noir"},
        {"en": "Neorealism", "es": "Neorrealismo", "pt": "Neorrealismo",
         "fr": "Néoréalisme", "de": "Neorealismus"},
        {"en": "New Wave", "es": "Nueva Ola", "pt": "Nouvelle Vague",
         "fr": "Nouvelle Vague", "de": "Nouvelle Vague"},
        {"en": "Documentary", "es": "Documental", "pt": "Documentário",
         "fr": "Documentaire", "de": "Dokumentarfilm"},
        {"en": "Experimental film", "es": "Cine experimental", "pt": "Cinema experimental",
         "fr": "Cinéma expérimental", "de": "Experimentalfilm"},
        {"en": "Art house", "es": "Cine de autor", "pt": "Cinema de arte",
         "fr": "Cinéma d'art et d'essai", "de": "Arthouse-Film"},
        {"en": "Psychological thriller", "es": "Thriller psicológico", "pt": "Thriller psicológico",
         "fr": "Thriller psychologique", "de": "Psychothriller"},
        {"en": "Dystopian sci-fi", "es": "Ciencia ficción distópica", "pt": "Ficção científica distópica",
         "fr": "Science-fiction dystopique", "de": "Dystopische Science-Fiction"},
        {"en": "Social realism", "es": "Realismo social", "pt": "Realismo social",
         "fr": "Réalisme social", "de": "Sozialrealismus"},
        {"en": "Mockumentary", "es": "Falso documental", "pt": "Mockumentário",
         "fr": "Documenteur", "de": "Mockumentary"}
    ]
}

# Day 40: Art and Architecture Vocabulary
day40_phrases = {
    "Art Terminology": [
        {"en": "Composition", "es": "Composición", "pt": "Composição",
         "fr": "Composition", "de": "Komposition"},
        {"en": "Perspective", "es": "Perspectiva", "pt": "Perspectiva",
         "fr": "Perspective", "de": "Perspektive"},
        {"en": "Chiaroscuro", "es": "Claroscuro", "pt": "Claro-escuro",
         "fr": "Clair-obscur", "de": "Helldunkel"},
        {"en": "Brushwork", "es": "Pincelada", "pt": "Pincelada",
         "fr": "Coup de pinceau", "de": "Pinselführung"},
        {"en": "Color palette", "es": "Paleta de colores", "pt": "Paleta de cores",
         "fr": "Palette de couleurs", "de": "Farbpalette"},
        {"en": "Texture", "es": "Textura", "pt": "Textura",
         "fr": "Texture", "de": "Textur"},
        {"en": "Negative space", "es": "Espacio negativo", "pt": "Espaço negativo",
         "fr": "Espace négatif", "de": "Negativraum"},
        {"en": "Trompe-l'œil", "es": "Trampantojo", "pt": "Trompe-l'œil",
         "fr": "Trompe-l'œil", "de": "Trompe-l'œil"},
        {"en": "Sfumato", "es": "Esfumado", "pt": "Sfumato",
         "fr": "Sfumato", "de": "Sfumato"},
        {"en": "Impasto", "es": "Empaste", "pt": "Empasto",
         "fr": "Empâtement", "de": "Impasto"}
    ],
    "Architectural Elements": [
        {"en": "Façade", "es": "Fachada", "pt": "Fachada",
         "fr": "Façade", "de": "Fassade"},
        {"en": "Colonnade", "es": "Columnata", "pt": "Colunata",
         "fr": "Colonnade", "de": "Kolonnade"},
        {"en": "Buttress", "es": "Contrafuerte", "pt": "Contraforte",
         "fr": "Contrefort", "de": "Strebepfeiler"},
        {"en": "Cornice", "es": "Cornisa", "pt": "Cornija",
         "fr": "Corniche", "de": "Gesims"},
        {"en": "Pediment", "es": "Frontón", "pt": "Frontão",
         "fr": "Fronton", "de": "Giebel"},
        {"en": "Portico", "es": "Pórtico", "pt": "Pórtico",
         "fr": "Portique", "de": "Portikus"},
        {"en": "Cupola", "es": "Cúpula", "pt": "Cúpula",
         "fr": "Coupole", "de": "Kuppel"},
        {"en": "Frieze", "es": "Friso", "pt": "Friso",
         "fr": "Frise", "de": "Fries"},
        {"en": "Architrave", "es": "Arquitrabe", "pt": "Arquitrave",
         "fr": "Architrave", "de": "Architrav"},
        {"en": "Spandrel", "es": "Enjuta", "pt": "Tímpano",
         "fr": "Écoinçon", "de": "Zwickel"}
    ],
    "Architectural Styles": [
        {"en": "Gothic", "es": "Gótico", "pt": "Gótico",
         "fr": "Gothique", "de": "Gotik"},
        {"en": "Baroque", "es": "Barroco", "pt": "Barroco",
         "fr": "Baroque", "de": "Barock"},
        {"en": "Art Nouveau", "es": "Modernismo", "pt": "Art Nouveau",
         "fr": "Art nouveau", "de": "Jugendstil"},
        {"en": "Brutalism", "es": "Brutalismo", "pt": "Brutalismo",
         "fr": "Brutalisme", "de": "Brutalismus"},
        {"en": "Neoclassical", "es": "Neoclásico", "pt": "Neoclássico",
         "fr": "Néoclassique", "de": "Klassizismus"},
        {"en": "Modernism", "es": "Modernismo", "pt": "Modernismo",
         "fr": "Modernisme", "de": "Moderne"},
        {"en": "Postmodernism", "es": "Posmodernismo", "pt": "Pós-modernismo",
         "fr": "Postmodernisme", "de": "Postmoderne"},
        {"en": "Deconstructivism", "es": "Deconstructivismo", "pt": "Desconstrutivismo",
         "fr": "Déconstructivisme", "de": "Dekonstruktivismus"},
        {"en": "Art Deco", "es": "Art Déco", "pt": "Art Déco",
         "fr": "Art déco", "de": "Art déco"},
        {"en": "Bauhaus", "es": "Bauhaus", "pt": "Bauhaus",
         "fr": "Bauhaus", "de": "Bauhaus"}
    ]
}

# Day 41: Subtle Humor and Wordplay
day41_phrases = {
    "Wordplay": [
        {"en": "Pun", "es": "Juego de palabras", "pt": "Trocadilho",
         "fr": "Jeu de mots", "de": "Wortspiel"},
        {"en": "Double entendre", "es": "Doble sentido", "pt": "Duplo sentido",
         "fr": "Double sens", "de": "Doppeldeutigkeit"},
        {"en": "Spoonerism", "es": "Espunerismo", "pt": "Espoonerismo",
         "fr": "Contrepèterie", "de": "Schüttelreim"},
        {"en": "Anagram", "es": "Anagrama", "pt": "Anagrama",
         "fr": "Anagramme", "de": "Anagramm"},
        {"en": "Palindrome", "es": "Palíndromo", "pt": "Palíndromo",
         "fr": "Palindrome", "de": "Palindrom"},
        {"en": "Malapropism", "es": "Malapropismo", "pt": "Malapropismo",
         "fr": "Malapropisme", "de": "Malapropismus"},
        {"en": "Portmanteau", "es": "Palabra compuesta", "pt": "Palavra-valise",
         "fr": "Mot-valise", "de": "Kofferwort"},
        {"en": "Rhyming slang", "es": "Jerga rimada", "pt": "Gíria rimada",
         "fr": "Argot rimé", "de": "Reimslang"},
        {"en": "Paraprosdokian", "es": "Paraprosdokian", "pt": "Paraprosdokian",
         "fr": "Paraprosdokian", "de": "Paraprosdokian"},
        {"en": "Tom Swifty", "es": "Tom Swifty", "pt": "Tom Swifty",
         "fr": "Tom Swifty", "de": "Tom Swifty"}
    ],
    "Subtle Humor": [
        {"en": "Dry wit", "es": "Humor seco", "pt": "Humor seco",
         "fr": "Humour pince-sans-rire", "de": "Trockener Humor"},
        {"en": "Deadpan delivery", "es": "Expresión impasible", "pt": "Expressão impassível",
         "fr": "Expression impassible", "de": "Ausdruckslose Darbietung"},
        {"en": "Understatement", "es": "Subestimación", "pt": "Subestimação",
         "fr": "Litote", "de": "Untertreibung"},
        {"en": "Self-deprecating humor", "es": "Humor autodespreciativo", "pt": "Humor autodepreciativo",
         "fr": "Humour autodérisoire", "de": "Selbstironischer Humor"},
        {"en": "Innuendo", "es": "Insinuación", "pt": "Insinuação",
         "fr": "Sous-entendu", "de": "Anspielung"},
        {"en": "Tongue-in-cheek", "es": "Con ironía", "pt": "Com ironia",
         "fr": "Au second degré", "de": "Ironisch gemeint"},
        {"en": "Satire", "es": "Sátira", "pt": "Sátira",
         "fr": "Satire", "de": "Satire"},
        {"en": "Parody", "es": "Parodia", "pt": "Paródia",
         "fr": "Parodie", "de": "Parodie"},
        {"en": "Wit", "es": "Ingenio", "pt": "Sagacidade",
         "fr": "Esprit", "de": "Geist"},
        {"en": "Repartee", "es": "Réplica ingeniosa", "pt": "Resposta espirituosa",
         "fr": "Répartie", "de": "Schlagfertigkeit"}
    ],
    "Humorous Expressions": [
        {"en": "To pull someone's leg", "es": "Tomar el pelo a alguien", "pt": "Pegar no pé de alguém",
         "fr": "Faire marcher quelqu'un", "de": "Jemanden auf den Arm nehmen"},
        {"en": "To be a barrel of laughs", "es": "Ser muy divertido", "pt": "Ser muito divertido",
         "fr": "Être une vraie partie de plaisir", "de": "Ein Riesenspaß sein"},
        {"en": "To crack someone up", "es": "Hacer reír a carcajadas", "pt": "Fazer alguém morrer de rir",
         "fr": "Faire mourir de rire", "de": "Jemanden zum Lachen bringen"},
        {"en": "To have a field day", "es": "Pasarlo en grande", "pt": "Se divertir muito",
         "fr": "Se régaler", "de": "Sich einen schönen Tag machen"},
        {"en": "To be the life of the party", "es": "Ser el alma de la fiesta", "pt": "Ser a alma da festa",
         "fr": "Être l'âme de la fête", "de": "Die Stimmungskanone sein"},
        {"en": "To tickle someone's funny bone", "es": "Hacer mucha gracia a alguien", "pt": "Fazer alguém rir muito",
         "fr": "Chatouiller les côtes de quelqu'un", "de": "Jemandes Lachmuskeln reizen"},
        {"en": "To be in stitches", "es": "Morirse de risa", "pt": "Morrer de rir",
         "fr": "Se tordre de rire", "de": "Sich vor Lachen biegen"},
        {"en": "To split one's sides", "es": "Partirse de risa", "pt": "Rachar de rir",
         "fr": "Se fendre la poire", "de": "Sich vor Lachen kugeln"},
        {"en": "To see the funny side", "es": "Ver el lado gracioso", "pt": "Ver o lado engraçado",
         "fr": "Voir le côté amusant", "de": "Die lustige Seite sehen"},
        {"en": "To have a sense of humor", "es": "Tener sentido del humor", "pt": "Ter senso de humor",
         "fr": "Avoir le sens de l'humour", "de": "Sinn für Humor haben"}
    ]
}

# Day 42: Irony, Sarcasm, and Cultural Jokes
day42_phrases = {
    "Irony and Sarcasm": [
        {"en": "How ironic", "es": "Qué irónico", "pt": "Que irônico",
         "fr": "Quelle ironie", "de": "Wie ironisch"},
        {"en": "Just what I needed", "es": "Justo lo que necesitaba", "pt": "Exatamente o que eu precisava",
         "fr": "Exactement ce dont j'avais besoin", "de": "Genau das, was ich brauchte"},
        {"en": "Well, that's just perfect", "es": "Bueno, eso es simplemente perfecto", "pt": "Bem, isso é simplesmente perfeito",
         "fr": "Eh bien, c'est tout simplement parfait", "de": "Na, das ist ja perfekt"},
        {"en": "Oh, brilliant", "es": "Oh, brillante", "pt": "Oh, brilhante",
         "fr": "Oh, brillant", "de": "Oh, großartig"},
        {"en": "Thanks for nothing", "es": "Gracias por nada", "pt": "Obrigado por nada",
         "fr": "Merci pour rien", "de": "Danke für nichts"},
        {"en": "What a surprise", "es": "Qué sorpresa", "pt": "Que surpresa",
         "fr": "Quelle surprise", "de": "Was für eine Überraschung"},
        {"en": "I'm shocked, truly shocked", "es": "Estoy impactado, verdaderamente impactado", "pt": "Estou chocado, verdadeiramente chocado",
         "fr": "Je suis choqué, vraiment choqué", "de": "Ich bin schockiert, wirklich schockiert"},
        {"en": "Couldn't be better", "es": "No podría ser mejor", "pt": "Não poderia ser melhor",
         "fr": "Ça ne pourrait pas être mieux", "de": "Könnte nicht besser sein"},
        {"en": "I'm thrilled", "es": "Estoy emocionado", "pt": "Estou emocionado",
         "fr": "Je suis ravi", "de": "Ich bin begeistert"},
        {"en": "What a genius idea", "es": "Qué idea tan genial", "pt": "Que ideia genial",
         "fr": "Quelle idée géniale", "de": "Was für eine geniale Idee"}
    ],
    "Cultural Jokes": [
        {"en": "Inside joke", "es": "Broma interna", "pt": "Piada interna",
         "fr": "Private joke", "de": "Insiderwitz"},
        {"en": "Running gag", "es": "Broma recurrente", "pt": "Piada recorrente",
         "fr": "Gag récurrent", "de": "Running Gag"},
        {"en": "Cultural reference", "es": "Referencia cultural", "pt": "Referência cultural",
         "fr": "Référence culturelle", "de": "Kulturelle Referenz"},
        {"en": "Local humor", "es": "Humor local", "pt": "Humor local",
         "fr": "Humour local", "de": "Lokaler Humor"},
        {"en": "National stereotype", "es": "Estereotipo nacional", "pt": "Estereótipo nacional",
         "fr": "Stéréotype national", "de": "Nationales Stereotyp"},
        {"en": "Regional joke", "es": "Broma regional", "pt": "Piada regional",
         "fr": "Blague régionale", "de": "Regionaler Witz"},
        {"en": "Pop culture reference", "es": "Referencia a la cultura pop", "pt": "Referência à cultura pop",
         "fr": "Référence à la culture pop", "de": "Popkulturelle Referenz"},
        {"en": "Generational humor", "es": "Humor generacional", "pt": "Humor geracional",
         "fr": "Humour générationnel", "de": "Generationenhumor"},
        {"en": "Political satire", "es": "Sátira política", "pt": "Sátira política",
         "fr": "Satire politique", "de": "Politische Satire"},
        {"en": "Social commentary", "es": "Comentario social", "pt": "Comentário social",
         "fr": "Commentaire social", "de": "Sozialkritik"}
    ],
    "Humorous Responses": [
        {"en": "You can't be serious", "es": "No puedes hablar en serio", "pt": "Você não pode estar falando sério",
         "fr": "Tu ne peux pas être sérieux", "de": "Das kann nicht dein Ernst sein"},
        {"en": "You're pulling my leg", "es": "Me estás tomando el pelo", "pt": "Você está me gozando",
         "fr": "Tu me fais marcher", "de": "Du nimmst mich auf den Arm"},
        {"en": "Tell me you're joking", "es": "Dime que estás bromeando", "pt": "Me diga que você está brincando",
         "fr": "Dis-moi que tu plaisantes", "de": "Sag mir, dass du scherzt"},
        {"en": "That's hilarious", "es": "Eso es hilarante", "pt": "Isso é hilário",
         "fr": "C'est hilarant", "de": "Das ist urkomisch"},
        {"en": "I almost believed you", "es": "Casi te creo", "pt": "Quase acreditei em você",
         "fr": "J'ai failli te croire", "de": "Ich hätte dir fast geglaubt"},
        {"en": "Good one!", "es": "¡Buena esa!", "pt": "Essa foi boa!",
         "fr": "Bien joué !", "de": "Guter Witz!"},
        {"en": "You had me going there", "es": "Me la estaba creyendo", "pt": "Você quase me pegou",
         "fr": "Tu m'as bien eu", "de": "Du hast mich fast drangekriegt"},
        {"en": "Very funny", "es": "Muy gracioso", "pt": "Muito engraçado",
         "fr": "Très drôle", "de": "Sehr witzig"},
        {"en": "I see what you did there", "es": "Ya veo lo que hiciste ahí", "pt": "Entendi o que você fez",
         "fr": "Je vois ce que tu as fait là", "de": "Ich verstehe, was du da gemacht hast"},
        {"en": "That's a good one", "es": "Esa es buena", "pt": "Essa é boa",
         "fr": "Elle est bonne celle-là", "de": "Der ist gut"}
    ]
}

# Day 43: Complex Social Etiquette
day43_phrases = {
    "Formal Social Settings": [
        {"en": "I'm honored to make your acquaintance", "es": "Es un honor conocerle", "pt": "É uma honra conhecê-lo",
         "fr": "Je suis honoré de faire votre connaissance", "de": "Ich fühle mich geehrt, Ihre Bekanntschaft zu machen"},
        {"en": "May I introduce", "es": "Permítame presentarle", "pt": "Permita-me apresentar",
         "fr": "Puis-je vous présenter", "de": "Darf ich vorstellen"},
        {"en": "It's a pleasure to be in your company", "es": "Es un placer estar en su compañía", "pt": "É um prazer estar em sua companhia",
         "fr": "C'est un plaisir d'être en votre compagnie", "de": "Es ist mir ein Vergnügen, in Ihrer Gesellschaft zu sein"},
        {"en": "I trust you're well", "es": "Confío en que esté bien", "pt": "Espero que esteja bem",
         "fr": "J'espère que vous vous portez bien", "de": "Ich hoffe, es geht Ihnen gut"},
        {"en": "Would you be so kind as to", "es": "¿Sería tan amable de", "pt": "Seria tão gentil a ponto de",
         "fr": "Auriez-vous l'amabilité de", "de": "Wären Sie so freundlich"},
        {"en": "I'd be delighted to accept", "es": "Estaría encantado de aceptar", "pt": "Ficaria encantado em aceitar",
         "fr": "Je serais ravi d'accepter", "de": "Ich würde mich freuen, anzunehmen"},
        {"en": "With your permission", "es": "Con su permiso", "pt": "Com sua permissão",
         "fr": "Avec votre permission", "de": "Mit Ihrer Erlaubnis"},
        {"en": "I must respectfully decline", "es": "Debo declinar respetuosamente", "pt": "Devo respeitosamente declinar",
         "fr": "Je dois respectueusement décliner", "de": "Ich muss respektvoll ablehnen"},
        {"en": "If I may be so bold", "es": "Si me permite ser tan atrevido", "pt": "Se me permite ser tão ousado",
         "fr": "Si je peux me permettre", "de": "Wenn ich so kühn sein darf"},
        {"en": "I'm much obliged", "es": "Le estoy muy agradecido", "pt": "Estou muito agradecido",
         "fr": "Je vous suis très reconnaissant", "de": "Ich bin Ihnen sehr verbunden"}
    ],
    "Social Nuances": [
        {"en": "Reading between the lines", "es": "Leer entre líneas", "pt": "Ler nas entrelinhas",
         "fr": "Lire entre les lignes", "de": "Zwischen den Zeilen lesen"},
        {"en": "Saving face", "es": "Salvar las apariencias", "pt": "Salvar as aparências",
         "fr": "Sauver la face", "de": "Das Gesicht wahren"},
        {"en": "White lie", "es": "Mentira piadosa", "pt": "Mentira branca",
         "fr": "Mensonge pieux", "de": "Notlüge"},
        {"en": "Tactful refusal", "es": "Rechazo con tacto", "pt": "Recusa com tato",
         "fr": "Refus plein de tact", "de": "Taktvoll ablehnen"},
        {"en": "Polite disagreement", "es": "Desacuerdo educado", "pt": "Discordância educada",
         "fr": "Désaccord poli", "de": "Höfliche Meinungsverschiedenheit"},
        {"en": "Subtle hint", "es": "Indirecta sutil", "pt": "Indireta sutil",
         "fr": "Allusion subtile", "de": "Subtile Andeutung"},
        {"en": "Social cue", "es": "Señal social", "pt": "Sinal social",
         "fr": "Indice social", "de": "Soziales Signal"},
        {"en": "Graceful exit", "es": "Salida elegante", "pt": "Saída elegante",
         "fr": "Sortie gracieuse", "de": "Eleganter Abgang"},
        {"en": "Unspoken understanding", "es": "Entendimiento tácito", "pt": "Entendimento tácito",
         "fr": "Compréhension tacite", "de": "Unausgesprochenes Verständnis"},
        {"en": "Social grace", "es": "Cortesía social", "pt": "Cortesia social",
         "fr": "Bienséance sociale", "de": "Soziale Anmut"}
    ],
    "Diplomatic Language": [
        {"en": "I see your point, however", "es": "Entiendo su punto, sin embargo", "pt": "Entendo seu ponto, no entanto",
         "fr": "Je comprends votre point de vue, cependant", "de": "Ich verstehe Ihren Standpunkt, jedoch"},
        {"en": "Perhaps we might consider", "es": "Quizás podríamos considerar", "pt": "Talvez pudéssemos considerar",
         "fr": "Peut-être pourrions-nous envisager", "de": "Vielleicht könnten wir in Betracht ziehen"},
        {"en": "I appreciate your perspective", "es": "Aprecio su perspectiva", "pt": "Aprecio sua perspectiva",
         "fr": "J'apprécie votre perspective", "de": "Ich schätze Ihre Perspektive"},
        {"en": "Let's explore alternatives", "es": "Exploremos alternativas", "pt": "Vamos explorar alternativas",
         "fr": "Explorons des alternatives", "de": "Lassen Sie uns Alternativen erkunden"},
        {"en": "I understand your concerns", "es": "Entiendo sus preocupaciones", "pt": "Entendo suas preocupações",
         "fr": "Je comprends vos préoccupations", "de": "Ich verstehe Ihre Bedenken"},
        {"en": "That's an interesting approach", "es": "Es un enfoque interesante", "pt": "Essa é uma abordagem interessante",
         "fr": "C'est une approche intéressante", "de": "Das ist ein interessanter Ansatz"},
        {"en": "If I may offer a suggestion", "es": "Si me permite ofrecer una sugerencia", "pt": "Se me permite oferecer uma sugestão",
         "fr": "Si je peux me permettre une suggestion", "de": "Wenn ich einen Vorschlag machen darf"},
        {"en": "Let's find common ground", "es": "Busquemos un terreno común", "pt": "Vamos encontrar um terreno comum",
         "fr": "Trouvons un terrain d'entente", "de": "Lassen Sie uns eine gemeinsame Basis finden"},
        {"en": "I'd like to better understand", "es": "Me gustaría entender mejor", "pt": "Gostaria de entender melhor",
         "fr": "J'aimerais mieux comprendre", "de": "Ich würde gerne besser verstehen"},
        {"en": "That's certainly one way to look at it", "es": "Ciertamente es una forma de verlo", "pt": "Certamente é uma forma de ver isso",
         "fr": "C'est certainement une façon de voir les choses", "de": "Das ist sicherlich eine Möglichkeit, es zu betrachten"}
    ]
}

# Day 44: Diplomatic Language and Political Discourse
day44_phrases = {
    "Diplomatic Expressions": [
        {"en": "We acknowledge your position", "es": "Reconocemos su posición", "pt": "Reconhecemos sua posição",
         "fr": "Nous reconnaissons votre position", "de": "Wir erkennen Ihre Position an"},
        {"en": "In the spirit of cooperation", "es": "En el espíritu de cooperación", "pt": "No espírito de cooperação",
         "fr": "Dans un esprit de coopération", "de": "Im Geiste der Zusammenarbeit"},
        {"en": "We remain committed to", "es": "Seguimos comprometidos con", "pt": "Permanecemos comprometidos com",
         "fr": "Nous restons engagés à", "de": "Wir bleiben verpflichtet zu"},
        {"en": "Without prejudice to", "es": "Sin perjuicio de", "pt": "Sem prejuízo para",
         "fr": "Sans préjudice de", "de": "Unbeschadet"},
        {"en": "We express our deep concern", "es": "Expresamos nuestra profunda preocupación", "pt": "Expressamos nossa profunda preocupação",
         "fr": "Nous exprimons notre profonde préoccupation", "de": "Wir bringen unsere tiefe Besorgnis zum Ausdruck"},
        {"en": "We strongly condemn", "es": "Condenamos enérgicamente", "pt": "Condenamos veementemente",
         "fr": "Nous condamnons fermement", "de": "Wir verurteilen entschieden"},
        {"en": "We call upon all parties to", "es": "Hacemos un llamamiento a todas las partes para", "pt": "Apelamos a todas as partes para",
         "fr": "Nous appelons toutes les parties à", "de": "Wir rufen alle Parteien dazu auf"},
        {"en": "We reaffirm our commitment", "es": "Reafirmamos nuestro compromiso", "pt": "Reafirmamos nosso compromisso",
         "fr": "Nous réaffirmons notre engagement", "de": "Wir bekräftigen unser Engagement"},
        {"en": "We take note with appreciation", "es": "Tomamos nota con aprecio", "pt": "Tomamos nota com apreço",
         "fr": "Nous prenons note avec satisfaction", "de": "Wir nehmen mit Anerkennung zur Kenntnis"},
        {"en": "We reserve our position on", "es": "Reservamos nuestra posición sobre", "pt": "Reservamos nossa posição sobre",
         "fr": "Nous réservons notre position sur", "de": "Wir behalten uns unsere Position vor zu"}
    ],
    "Political Discourse": [
        {"en": "Policy implications", "es": "Implicaciones políticas", "pt": "Implicações políticas",
         "fr": "Implications politiques", "de": "Politische Implikationen"},
        {"en": "Bilateral relations", "es": "Relaciones bilaterales", "pt": "Relações bilaterais",
         "fr": "Relations bilatérales", "de": "Bilaterale Beziehungen"},
        {"en": "Strategic interests", "es": "Intereses estratégicos", "pt": "Interesses estratégicos",
         "fr": "Intérêts stratégiques", "de": "Strategische Interessen"},
        {"en": "Diplomatic channels", "es": "Canales diplomáticos", "pt": "Canais diplomáticos",
         "fr": "Canaux diplomatiques", "de": "Diplomatische Kanäle"},
        {"en": "International community", "es": "Comunidad internacional", "pt": "Comunidade internacional",
         "fr": "Communauté internationale", "de": "Internationale Gemeinschaft"},
        {"en": "Sovereign rights", "es": "Derechos soberanos", "pt": "Direitos soberanos",
         "fr": "Droits souverains", "de": "Souveräne Rechte"},
        {"en": "Multilateral framework", "es": "Marco multilateral", "pt": "Estrutura multilateral",
         "fr": "Cadre multilatéral", "de": "Multilateraler Rahmen"},
        {"en": "Diplomatic immunity", "es": "Inmunidad diplomática", "pt": "Imunidade diplomática",
         "fr": "Immunité diplomatique", "de": "Diplomatische Immunität"},
        {"en": "Foreign policy", "es": "Política exterior", "pt": "Política externa",
         "fr": "Politique étrangère", "de": "Außenpolitik"},
        {"en": "Geopolitical considerations", "es": "Consideraciones geopolíticas", "pt": "Considerações geopolíticas",
         "fr": "Considérations géopolitiques", "de": "Geopolitische Überlegungen"}
    ],
    "Negotiation Language": [
        {"en": "We propose the following", "es": "Proponemos lo siguiente", "pt": "Propomos o seguinte",
         "fr": "Nous proposons ce qui suit", "de": "Wir schlagen Folgendes vor"},
        {"en": "Subject to your agreement", "es": "Sujeto a su acuerdo", "pt": "Sujeito ao seu acordo",
         "fr": "Sous réserve de votre accord", "de": "Vorbehaltlich Ihrer Zustimmung"},
        {"en": "We are prepared to consider", "es": "Estamos dispuestos a considerar", "pt": "Estamos dispostos a considerar",
         "fr": "Nous sommes prêts à envisager", "de": "Wir sind bereit zu erwägen"},
        {"en": "In exchange for", "es": "A cambio de", "pt": "Em troca de",
         "fr": "En échange de", "de": "Im Austausch für"},
        {"en": "As a gesture of goodwill", "es": "Como gesto de buena voluntad", "pt": "Como gesto de boa vontade",
         "fr": "En signe de bonne volonté", "de": "Als Geste des guten Willens"},
        {"en": "We seek assurances that", "es": "Buscamos garantías de que", "pt": "Buscamos garantias de que",
         "fr": "Nous cherchons des assurances que", "de": "Wir suchen Zusicherungen, dass"},
        {"en": "This represents our final position", "es": "Esto representa nuestra posición final", "pt": "Isto representa nossa posição final",
         "fr": "Ceci représente notre position finale", "de": "Dies stellt unsere endgültige Position dar"},
        {"en": "We are willing to compromise on", "es": "Estamos dispuestos a ceder en", "pt": "Estamos dispostos a ceder em",
         "fr": "Nous sommes prêts à faire des compromis sur", "de": "Wir sind bereit, Kompromisse einzugehen bei"},
        {"en": "This is non-negotiable", "es": "Esto no es negociable", "pt": "Isto não é negociável",
         "fr": "Ceci n'est pas négociable", "de": "Dies ist nicht verhandelbar"},
        {"en": "We request clarification on", "es": "Solicitamos aclaración sobre", "pt": "Solicitamos esclarecimento sobre",
         "fr": "Nous demandons des éclaircissements sur", "de": "Wir bitten um Klärung zu"}
    ]
}

# Dictionary mapping day numbers to phrase dictionaries
all_phrases = {
    32: day32_phrases,
    33: day33_phrases,
    34: day34_phrases,
    35: day35_phrases,
    36: day36_phrases,
    37: day37_phrases,
    38: day38_phrases,
    39: day39_phrases,
    40: day40_phrases,
    41: day41_phrases,
    42: day42_phrases,
    43: day43_phrases,
    44: day44_phrases
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
    parser = argparse.ArgumentParser(description="Generate language learning files for Academic & Professional Communication (Days 32-44)")
    parser.add_argument("--day", "-d", type=int, choices=list(range(32, 45)), default=None,
                        help="Day number to generate (32-44). If not specified, generates all available days.")
    parser.add_argument("--languages", "-l", nargs="+", choices=["es", "pt", "en", "fr", "de"],
                        default=["es", "pt", "fr", "de"], help="Languages to generate (es=Spanish, pt=Portuguese, en=English, fr=French, de=German)")
    parser.add_argument("--text-only", "-t", action="store_true",
                        help="Generate only text files (no audio)")
    args = parser.parse_args()
    
    language_names = {"es": "Spanish", "pt": "Portuguese", "en": "English", "fr": "French", "de": "German"}
    
    # Check if we have content for the requested days
    available_days = list(all_phrases.keys())
    if not available_days:
        print("No content available yet. Please add content for days 32-44.")
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
    print("  - Generate text files only: python language_phrases_days_32_44.py --text-only")
    print("  - Generate files for just Day 32: python language_phrases_days_32_44.py --day 32")
    print("  - Generate files for just Spanish: python language_phrases_days_32_44.py --languages es")
    print("  - Generate Day 40 Portuguese text only: python language_phrases_days_32_44.py --day 40 --languages pt --text-only")
    print("  - Generate all available days: python language_phrases_days_32_44.py")

if __name__ == "__main__":
    main()
