# Montpellier-Weather

## But et Données 

l'Objectif de ce projet est de créer une application Web de prévision météo Pour la ville de Montpellier  dans laquelle , on pourra afficher principalement les températures hautes et basses , suivie de la moyenne du vent et la quantité de précipitation du vent 

```mermaid
flowchart TD
    A[carte Montpellier ] --> B[Température ]
    B --> D[Temp Hautes]
    B --> E[Temp Basses]
    B --> C[Moy_vent ]

    E --> G[carte Méteo ]
    D --> G
    C --> G
```
 Cette carte se met à jour automatiquement et accessible avec l'URL ... 


 ## Organisation 

 ### Traitement des données 

 Dans cette première partie du travail  je vais impérativement analyser , filtrer et organiser les données de manière à ce que notre dataframe soit soit utilisable , et ceci pour se faire à l'aide des packages suivants : pandas , numpy , scipy .

 ### Visualisation  




 ```mermaid
gantt
    title Montpellier_weather
    dateFormat YYYY-MM-DD
    section Phase 1
        Brainstrorming 1 :a1, 2023-10-10, 10d
        Brainstorming 2  :after a1, 10d
        Snpashot : 2023-10-22
    section Development
        filtrage des données  : a2, 2023-10-22, 10d
        Visualiation   : 2023-11-01, 10d
        Documentation : a3, after a2 , 5d
        Beamer : after a3, 5d
```

 Cette partie consiste à créer une carte graphique affichant la température d'une journée dans la ville de Montpellier en suivant differentes étapes : 





 
