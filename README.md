# API_youtube
L'objectif est de créer une API permettant de dire si un commentaire fourni en entrée est positif ou négatif. 

Nous reprenons ici un travail d’analyse de sentiments à partir d’un dataset contenant des commentaires de restaurants et un fichier joblib contenant une pipeline de nature inconnue contenant un modèle.Ce projet s’inscrit dans le domaine du NLP (ou Natural Language Processing) qui est une discipline de l’Intelligence Artificielle dédiée à l’analyse et/ou la compréhension de données textuelles. Il consiste à faire de l’analyse de sentiments, autrement dit, à extraire des opinions et/ou des sentiments d’un texte. Dans notre cas, il s’agira de déterminer si chaque commentaire du dataset est soit positif ou négatif. 

La pipeline contenant le modèle chargé de faire les prédictions est constitué de deux algorithmes :
- Le TFIDFVectorizer qui s’occupe de mettre le texte en minuscule, de le tokenizer puis de le transformer en vecteur.
- Le SVM (Support Vector Machine), un algorithme de classification supervisé en Machine Learning, qui consiste à séparer des données en différents groupes selon la similarité entre les données par rapport à un plan.

Les différentes étapes du projet sont les suivantes : 
- Evaluer les prédictions du modèle de base et chercher à améliorer les résultats obtenus. 
- Assurer la transition du code initial sous Flask vers un code amélioré utilisant la librairie FastAPI. Intégrer des journaux d'évenements (logs) avec la librairie logging afin de pouvoir tracer l'utilisation de l'API par les différents utilisateurs et pouvoir ainsi assurer un débogage si besoin. 
- Programmer des tests unitaires pour permettre éventuellement à de futurs développeurs de pouvoir modifier les fonctions s'ils le souhaitent sans dénaturer les résultats qu'elles sont censées fournir. 
- Tester l'API avec une nouvelle pipeline issue de l'amélioration du modèle et vérifier que tout fonctionne. 
- En bonus, réfléchir à de nouvelles améliorations pour l'API à travers l'implantation par exemple de nouveux points de terminaison. 
