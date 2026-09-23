# Géodata Paris : Cours de cartographie et statistiques, L3 PRO
<p align="center">
  <img src="Cours/assets/css/geodata.svg" alt="Logo Géodata Paris" width="260"/>
</p>

## Introduction

Ce cours est destiné aux étudiants de Géodata Paris (ex-ENSG), Licence Professionnelle, débutants dans le domaine des statistiques et de la cartographie. Il a pour objectif de leur fournir les bases solides pour comprendre et appliquer les statistiques dans un contexte cartographique.

## Objectifs du cours

- **Acquérir les bonnes pratiques de la démarche scientifique** : Introduction aux méthodes rigoureuses de recherche et d'analyse scientifique.
- **Les statistiques appliquées à la cartographie** : Compréhension des concepts statistiques et de leur utilisation pour l'analyse et la représentation géographique des données.
- **La sémiologie graphique** : Les règles du langage cartographique (implantation, figuration, variables visuelles) pour choisir la représentation adaptée à chaque type de données.
- **Principes et méthodes de traitement en analyse de données** : Initiation aux bases de l'analyse de données et l'interprétation des résultats. La collecte des données n'est pas abordée.
- **Analyse univariée et bivariée** sur des données quantitatives : Exploration des techniques d'analyse de variables uniques et des relations entre deux variables (corrélation).
- **Méthodes de discrétisation** : Techniques de regroupement des données en classes pour une meilleure interprétation visuelle.
- **Séances de TD pratiques** : Des travaux dirigés permettent aux étudiants de mettre en pratique les connaissances acquises à travers des exercices concrets.

## Plan du cours

### Introduction
   - [Cours : LPRO_Cours_0_Intro.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_Cours_0_Intro.pdf)

### 1. Rappel du vocabulaire en statistique
   - [Cours : LPRO_Cours_1_stat.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_Cours_1_stat.pdf)
   - [TD : LPRO_TD_1_stat.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_TD_1_stat.pdf)

### 2. Analyse univariée : Méthodes et outils
   - [Cours : LPRO_Cours_2_univ.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_Cours_2_univ.pdf)
   - [TD : LPRO_TD_2_univ.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_TD_2_univ.pdf)

### 3. La sémiologie graphique
   - [Cours : LPRO_Cours_3_semio.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_Cours_3_semio.pdf)
   - [TD : LPRO_TD_3_semio.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_TD_3_semio.pdf)

### 4. Méthodes de discrétisation en cartographie
   - [Cours : LPRO_Cours_4_disc.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_Cours_4_disc.pdf)
   - [TD : LPRO_TD_4_disc.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_TD_4_disc.pdf)

### 5. Analyse bivariée : test du chi2
   - [Cours : LPRO_Cours_5_chi2.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_Cours_5_chi2.pdf)
   - [TD : LPRO_TD_5_chi2.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_TD_5_chi2.pdf)
   - [TD : fichier Excel](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/data/TD4_chi2_donnee.xls)

### 5. Analyse bivariée : la corrélation
   - [Cours : LPRO_Cours_5_corr.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_Cours_5_corr.pdf)
   - [TD : LPRO_TD_5_corr.pdf](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/pdf/LPRO_TD_5_corr.pdf)

## Travaux Dirigés (TD) : Données et outils utilisés
### Données 
A télécharger (download raw file). La colonne `population` (estimations Natural Earth) a été ajoutée pour les cartes en symboles proportionnels.
  - [data Excel](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/data/hdi-edu.xlsx)
  - [data CSV](https://github.com/fbxyz/ENSG_L3PRO/blob/main/Cours/data/hdi-edu.csv)
  - [fond de carte](https://raw.githubusercontent.com/fbxyz/ENSG_L3PRO/refs/heads/main/Cours/data/monde_iso3.geojson)
    
### Orange Data Mining

Pour les TD 2 et 5, nous utiliserons **Orange Data Mining**, un logiciel d'exploration de données qui permet d'analyser et de visualiser les données de manière simple et intuitive.

- Téléchargez Orange ici : [Orange Data Mining - Download](https://orangedatamining.com/download/)

Ou, dans miniforge prompt / conda prompt :
```
conda create -n orange -y
conda activate orange
conda install orange3 -y
```

### Magrit

**Magrit** est un outil en ligne gratuit pour la cartographie statistique. Nous l'utiliserons dans les TD 3 (sémiologie graphique) et 4 (discrétisation) pour réaliser des cartes à partir de données statistiques.

- Accédez à Magrit ici : [Magrit](https://magrit.cnrs.fr/)


## Prérequis

Aucun prérequis particulier n'est nécessaire, le cours est conçu pour les débutants.

## Format

Le cours alterne entre des séances théoriques et des séances pratiques sous forme de TD afin de favoriser une approche concrète et appliquée.


## Bibliographie

### Statistique en géographie :
- Béguin, M., & Pumain, D. (2017). La représentation des données géographiques-4e éd.: Statistique et cartographie. Armand Colin.
- Lambert, N., & Zanin, C. (2016). Manuel de cartographie: principes, méthodes, applications. Armand Colin.
- Bertin, J. (1967). Sémiologie graphique. Les diagrammes, les réseaux, les cartes. Mouton / Gauthier-Villars.
- Dumolard, P., Dubus, N., & Charleux, L. L. (2003). Les statistiques en géographie (p. 240). Editions Belin.

### Statistique :
- Saporta, G. (2006). Probabilités, analyse des données et statistique. Editions technip.
- Sanders, L. (1990). L’analyse des données appliquées à la géographie, GIP RECLUS.
- Bouyer, J. (2009). Épidémiologie: principes et méthodes quantitatives. Lavoisier.

