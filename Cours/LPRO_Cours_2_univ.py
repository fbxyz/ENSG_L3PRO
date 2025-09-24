#!/usr/bin/env python3
"""
L3_Cours 2_univ
Analyse des données
Cours n°2- l'analyse univariée
Florian Bayer
"""

#%%
from respysive import Slide, Presentation
from markdown import markdown
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Configure markdown with table extension
import markdown as md_module
def markdown_with_tables(text):
    return md_module.markdown(text, extensions=['tables'])

# Load environment variables
load_dotenv(".env")
annee = os.getenv("annee", "2024")

# Create a new presentation
p = Presentation()

# CSS styles dictionary for text sizing
css_styles = {
    'text-30': {'font-size': '30%'},
    'text-40': {'font-size': '40%'},
    'text-50': {'font-size': '50%'},
    'text-60': {'font-size': '60%'},
    'text-70': {'font-size': '70%'},
    'text-80': {'font-size': '80%'},
    'text-90': {'font-size': '90%'},
    'center-img': {'class': 'center-img'}
}

#%%
# =============================================================================
# Title Page
# =============================================================================

slide1 = Slide(center=True, **{
    'class': 'title-slide animated fadeIn inverse'
})

title_page_content = {
    'title': f'Analyse des données Licence Pro {annee}',
    'subtitle': 'Cours n°2- l\'analyse univariée',
    'authors': 'Florian Bayer',
}

title_styles = [
    {'color': 'white', 'class': 'r-fit-text'},  # title
    {'color': '#f8f9fa', 'font-size': '1.5em'},  # subtitle
    {'color': '#e9ecef', 'font-size': '1.2em'},  # authors
]

slide1.add_title_page(title_page_content, title_styles)

#%%
# =============================================================================
# Objectifs du cours
# =============================================================================

slide2 = Slide(**{'class': 'animated fadeIn'})

slide2.add_title("Objectifs du cours")

content_objectifs = markdown("""
L'analyse d'une série de données est une étape obligatoire de **toutes** productions scientifiques.

Si on s'intéresse aux caractères pris un à un, on parle d'analyse **univariée**.

Elle permet :

- De mieux **comprendre** les données les unes par rapport aux autres (série homogène ? Hétérogène ?).
- De mettre en évidence les **valeurs remarquables**.
- Elle permet **résumer** l'information.
- Elle donne les éléments scientifiques pour **justifier et reproduire** ses choix.
""")

slide2.add_content([content_objectifs], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Objectifs du cours (suite)
# =============================================================================

slide3 = Slide(**{'class': 'animated fadeIn'})

slide3.add_title("Objectifs du cours")

content_objectifs_suite = markdown("""
Ce qui se traduit aussi en cartographie par :

- Trouver le meilleur **compromis** entre information statistique et information géographique.
- **Résumer** l'information tout en conservant la **forme de la distribution**.
- Si besoin de mettre en évidence les **valeurs remarquables** et de les faire apparaître sur la carte.
- Choisir la méthode de **discrétisation** la plus adaptée à vos données.
""")

slide3.add_content([content_objectifs_suite], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Objectifs du cours (méthodes)
# =============================================================================

slide4 = Slide(**{'class': 'animated fadeIn'})

slide4.add_title("Objectifs du cours")

content_methodes = markdown("""
L'analyse univariée se fait à l'aide de la combinaison **graphiques** et **calculs** :

- Les graphiques permettent de visualiser instantanément les caractéristiques d'une ou de plusieurs séries.
- Les calculs statistiques donnent des éléments factuels et reproductibles.
""")

slide4.add_content([content_methodes], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Analyse univariée : les graphiques
# =============================================================================

slide5 = Slide(center=True, **{
    'class': 'inverse animated fadeIn',
    'data-background-image': './assets/css/graticules.png',
    'data-background-size': 'cover',
    'data-background-position': 'bottom right'
})

slide5.add_title("1- Analyse univariée : les graphiques", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Intérêt des graphiques
# =============================================================================

slide6 = Slide(**{'class': 'animated fadeIn'})

slide6.add_title("Intérêt")

quote_text = markdown("""
*« La représentation des données sous forme numérique n'a souvent qu'une assez faible lisibilité immédiate. Il est alors important de pouvoir utiliser des moyens qui améliorent l'appréhension, l'interprétation et la communication des données statistiques »* **[Dumolard et al.,2003]**
""")

slide6.add_content([quote_text], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Des graphiques en fonction des données
# =============================================================================

slide7 = Slide(**{'class': 'animated fadeIn'})

slide7.add_title("Des graphiques en fonction des données")

content_graphiques = markdown("""
Selon le type de données (qualitatives / quantitatives, discrètes ou continues), les outils permettant de décrire l'information statistique ne sont pas les mêmes.
""")

# Image showing different plot types
plots_url = "./assets/images/5-Stat/plotly-example-plots.png"

slide7.add_content([content_graphiques], columns=[12], styles=[css_styles['text-60']])
slide7.add_content([plots_url], columns=[12], styles=[{'class': 'center-img', 'width': '70%'}])

#%%
# =============================================================================
# Les diagrammes en bâton
# =============================================================================

slide8 = Slide(**{'class': 'animated fadeIn'})

slide8.add_title("Les diagrammes en bâton")

content_baton = markdown("""
On représente généralement les **données qualitatives discrètes / exhaustives** à l'aide d'un diagramme en bâton. Il faut réaliser un **dénombrage** à l'aide un tableau de contingence.

Le diagramme en bâton :

- La hauteur de chaque bâtons (y) est égale au nombre d'individus dans la modalité correspondante.
- Les variables discrètes sont en abscisse (x).

C'est donc la représentation d'une variable qualitative pondérée par le nombre d'occurence de la valeur dans le tableau.
""")

slide8.add_content([content_baton], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Histogramme
# =============================================================================

slide9 = Slide(**{'class': 'animated fadeIn'})

slide9.add_title("L'histogramme")

content_histogramme = markdown("""
L'**histogramme** est utilisé pour représenter des **données quantitatives continues**.

Caractéristiques :

- Les données sont regroupées en **classes** d'intervalles

- L'aire de chaque rectangle est proportionnelle à l'effectif de la classe

- Permet de visualiser la **distribution** des données

- Révèle la **forme** de la distribution (normale, asymétrique, bimodale...)
""")

slide9.add_content([content_histogramme], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Boîte à moustaches (boxplot)
# =============================================================================

slide10 = Slide(**{'class': 'animated fadeIn'})

slide10.add_title("La boîte à moustaches (boxplot)")

content_boxplot = markdown("""
La **boîte à moustaches** résume visuellement les principales caractéristiques d'une distribution :

- **Médiane** (trait central dans la boîte)
- **Quartiles Q1 et Q3** (limites de la boîte)
- **Valeurs extrêmes** (moustaches)
- **Valeurs aberrantes** (points isolés)

Avantages :

- Vision synthétique de la distribution

- Comparaison facile entre plusieurs groupes

- Détection des valeurs atypiques
""")

slide10.add_content([content_boxplot], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Analyse univariée : les calculs
# =============================================================================

slide11 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide11.add_title("2- Analyse univariée : les calculs", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Mesures de tendance centrale
# =============================================================================

slide12 = Slide(**{'class': 'animated fadeIn'})

slide12.add_title("Mesures de tendance centrale")

# Create cards for central tendency measures
cards_tendance = [
    {
        'title': 'Moyenne arithmétique',
        'text': markdown("""
**Formule :** x̄ = Σx/n

- Sensible aux valeurs extrêmes

- Pour données quantitatives

- Interprétation : centre de gravité
""")
    },
    {
        'title': 'Médiane',
        'text': markdown("""
**Définition :** valeur qui partage la série en deux effectifs égaux

- Robuste aux valeurs extrêmes

- Pour données ordinales/quantitatives

- 50% des valeurs sont inférieures
""")
    },
    {
        'title': 'Mode',
        'text': markdown("""
**Définition :** valeur la plus fréquente

- Pour tous types de données

- Peut être multimodal

- Utile pour données qualitatives
""")
    }
]

styles_tendance = [
    {'class': ['bg-primary', 'text-white']},
    {'class': ['bg-success', 'text-white']},
    {'class': ['bg-info', 'text-white']}
]

slide12.add_card(cards_tendance, styles_tendance, title_size="h5", text_size="60%")

#%%
# =============================================================================
# Mesures de dispersion
# =============================================================================

slide13 = Slide(**{'class': 'animated fadeIn'})

slide13.add_title("Mesures de dispersion")

# Create cards for dispersion measures
cards_dispersion = [
    {
        'title': 'Étendue (Range)',
        'text': markdown("""
**Formule :** R = Max - Min

- Très sensible aux valeurs extrêmes

- Simple à calculer

- Information limitée
""")
    },
    {
        'title': 'Écart-type',
        'text': markdown("""
**Formule :** σ = √(Σ(x-x̄)²/n)

- Mesure la dispersion autour de la moyenne

- Même unité que les données

- Sensible aux valeurs extrêmes
""")
    },
    {
        'title': 'Écart interquartile',
        'text': markdown("""
**Formule :** IQR = Q3 - Q1

- Robuste aux valeurs extrêmes

- Mesure la dispersion centrale

- Utilisé avec la médiane
""")
    }
]

styles_dispersion = [
    {'class': ['bg-warning', 'text-dark']},
    {'class': ['bg-danger', 'text-white']},
    {'class': ['bg-secondary', 'text-white']}
]

slide13.add_card(cards_dispersion, styles_dispersion, title_size="h5", text_size="60%")

#%%
# =============================================================================
# Mesures de forme
# =============================================================================

slide14 = Slide(**{'class': 'animated fadeIn'})

slide14.add_title("Mesures de forme")

content_forme = markdown("""
**Asymétrie (Skewness) :**
- Mesure la symétrie de la distribution

- Skewness = 0 : distribution symétrique

- Skewness > 0 : asymétrie positive (queue à droite)
- Skewness < 0 : asymétrie négative (queue à gauche)

**Aplatissement (Kurtosis) :**
- Mesure l'aplatissement de la distribution

- Kurtosis = 3 : distribution normale

- Kurtosis > 3 : distribution pointue (leptokurtique)
- Kurtosis < 3 : distribution aplatie (platykurtique)
""")

slide14.add_content([content_forme], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Applications pratiques
# =============================================================================

slide15 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide15.add_title("3- Applications pratiques", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Choix du graphique approprié
# =============================================================================

slide16 = Slide(**{'class': 'animated fadeIn'})

slide16.add_title("Choix du graphique approprié")

# Create decision table
table_choix = markdown_with_tables("""
| Type de variable | Graphique recommandé | Usage |
|------------------|---------------------|-------|
| Qualitative nominale | Diagramme en barres | Comparaison de fréquences |
| Qualitative ordinale | Diagramme en barres ordonnées | Progression ordonnée |
| Quantitative discrète | Diagramme en bâtons | Valeurs entières |
| Quantitative continue | Histogramme | Distribution des valeurs |
| Comparaison de groupes | Boîtes à moustaches | Analyse comparative |
""")

slide16.add_content([table_choix], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Interprétation des résultats
# =============================================================================

slide17 = Slide(**{'class': 'animated fadeIn'})

slide17.add_title("Interprétation des résultats")

content_interpretation = markdown("""
**Questions à se poser lors de l'analyse :**

1. **Distribution :** La distribution est-elle normale, asymétrique, bimodale ?
2. **Centre :** Quelle est la valeur typique (moyenne, médiane) ?
3. **Dispersion :** Les données sont-elles concentrées ou dispersées ?
4. **Valeurs atypiques :** Y a-t-il des valeurs aberrantes ?
5. **Comparaisons :** Comment cette série se compare-t-elle à d'autres ?

**Pour la cartographie :**
- Ces caractéristiques influencent le choix de la méthode de discrétisation

- Les valeurs atypiques peuvent nécessiter un traitement particulier

- La forme de la distribution guide le choix des seuils
""")

slide17.add_content([content_interpretation], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Exemple pratique
# =============================================================================

slide18 = Slide(**{'class': 'animated fadeIn'})

slide18.add_title("Exemple pratique")

content_exemple = markdown("""
**Analyse de la population des communes françaises :**

Données : Population de 100 communes

- **Moyenne :** 15 000 habitants

- **Médiane :** 8 000 habitants

- **Écart-type :** 25 000 habitants

- **Min :** 500 habitants

- **Max :** 200 000 habitants

**Interprétation :**
- Distribution asymétrique positive (moyenne > médiane)
- Forte dispersion (écart-type important)
- Présence probable de grandes villes (valeurs extrêmes)
- Pour la carte : discrétisation par quantiles ou seuils naturels
""")

slide18.add_content([content_exemple], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Conclusion
# =============================================================================

slide19 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide19.add_title("Conclusion", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Concepts-clés
# =============================================================================

slide20 = Slide(**{'class': 'animated fadeIn'})

slide20.add_title("Concepts-clés")

content_conclusion = markdown("""
**L'analyse univariée est fondamentale :**
- **Obligatoire** avant toute analyse plus complexe

- Combine **graphiques** et **calculs** statistiques

- Révèle les **caractéristiques** essentielles des données

**En cartographie :**
- Guide le choix de la **méthode de discrétisation**
- Permet d'identifier les **valeurs remarquables**
- Assure la **reproductibilité** des choix scientifiques

**Méthodologie :**
1. Identifier le type de variable
2. Choisir les graphiques et calculs appropriés
3. Interpréter les résultats
4. Adapter la représentation cartographique
""")

slide20.add_content([content_conclusion], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Generate Presentation
# =============================================================================

# Add all slides to the presentation
p.add_slide([slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8, slide9, slide10,
             slide11, slide12, slide13, slide14, slide15, slide16, slide17, slide18, slide19, slide20])

# Save the presentation
p.save_html("LPRO_Cours_2_univ_py.html",
           theme="moon",
           margin=0.1,
           center=True)

print("✅ Presentation 'LPRO_Cours_2_univ_py.html' has been created successfully!")