#!/usr/bin/env python3
"""
L3_Cours 3 Chi²
Analyse de données
Mise en relation de deux caractères qualitatifs
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
    'title': f'Analyse de données L3 {annee}',
    'subtitle': 'Mise en relation de deux caractères qualitatifs',
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
# Rappels et objectifs du cours
# =============================================================================

slide2 = Slide(**{'class': 'animated fadeIn'})

slide2.add_title("Rappels et objectifs du cours")

content_objectifs = markdown("""
En partant du **tableau de contingence**, nous allons voir comment analyser les relations entre deux ou plusieurs séries de données **qualitatives.**

- Existe-t-il un lien entre le versant d'un massif (N,S,E,O) et le type de culture ?
- Les accidents aériens (oui/non) sont ils dépendant du type de piste des aéroports (tarmac/herbe/terre) ?
- La réussite à un concours (oui/non) est elle dépendante de l'enseignant ?
""")

content_suite = markdown("""
Mettre en évidence une relation n'est cependant pas suffisant. Il convient de savoir si le résultat peut être **validé avec certitude** ou non. Nous aborderons donc dans ce cours :

1. La démarche scientifique
2. Description d'une relation entre 2 caractères qualitatifs discrets
3. Test du Chi²
""")

slide2.add_content([content_objectifs], columns=[12], styles=[css_styles['text-60']])
slide2.add_content([content_suite], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - La démarche scientifique
# =============================================================================

slide3 = Slide(center=True, **{
    'class': 'inverse animated fadeIn',
    'data-background-image': './assets/css/graticules.png',
    'data-background-size': 'cover',
    'data-background-position': 'bottom right'
})

slide3.add_title("1- La démarche scientifique", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Les critères de scientificité
# =============================================================================

slide4 = Slide(**{'class': 'animated fadeIn'})

slide4.add_title("Les critères de scientificité")

content_criteres = markdown("""
La théorie scientifique comporte **3 composantes** :

- Objectivité
- Reproductibilité
- Falsifiabilité
""")

content_popper = markdown("""
K.R. Popper pose la question : *Existe-t-il un critère permettant d'établir la nature ou le statut scientifique d'une théorie ?*

Il introduit alors le principe de **falsifiabilité** : on ne peut accepter une théorie scientifique que s'il existe un moyen de **prouver qu'elle est erronée**. L'objectif est donc de pouvoir soumettre cette théorie à des expériences (des tests) afin de vérifier si la théorie et l'observé concorde.
""")

content_citation = markdown("""
*«Une théorie qui n'est réfutable par aucun événement qui se puisse concevoir est dépourvue de caractère scientifique. Pour les théories, l'irréfutabilité n'est pas vertu mais défaut »*. **Une théorie irréfutable est alors jugée comme méta-physique.**

*«Le critère de la scientificité d'une théorie réside dans la possibilité de l'invalider, de la réfuter ou encore de la tester »* K.R. Popper, Conjecture et réfutation, Payot, Paris, pp. 58-65.
""")

slide4.add_content([content_criteres], columns=[12], styles=[css_styles['text-60']])
slide4.add_content([content_popper], columns=[12], styles=[css_styles['text-60']])
slide4.add_content([content_citation], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Tests de significativité : exemple 1
# =============================================================================

slide5 = Slide(**{'class': 'animated fadeIn'})

slide5.add_title("Tests de significativité : exemple 1")

content_test1 = markdown("""
Obtenir un résultat (un indicateur d'intensité de relation, une comparaison de deux moyennes) n'est pas suffisant. Il est obligatoire de déterminer si ce résultat est lié au hasard (fluctuations d'échantillonage, pas de relation, biais de sélection, effectifs insuffisants etc.) ou s'il peut être **validé** avec un certaine **marge d'erreur**. On parle de **test de significativité**.
""")

content_exemple1 = markdown("""
Exemple : un article démontre que la part estimée de diabétique dans la population d'un pays est de 20%. Un scientifique décide de vérifier si ce taux est égal à 20% dans sa région. Comme il ne peut pas faire un test sur toute la population régionale, il réalise une étude sur un groupe représentatif (**échantillon**) semblable à celle de l'étude du pays.

- Cas 1 : il obtient un taux de 5%. Dans ce cas il **rejete** son hypothèse du fait de l'écart important entre les deux.
- Cas 2 : il obtient un taux de 18 %. L'hypothèse peut être jugée raisonnable et **il n'y a pas de raison évidente de la rejeter**.
""")

content_formalisation = markdown("""
L'intuition qui conduit à cette conclusion doit être **formalisée** en une **règle précise** s'appliquant à chaque cas et en fonction de la taille de la population étudiée : **un test de significativité**.
""")

slide5.add_content([content_test1], columns=[12], styles=[css_styles['text-60']])
slide5.add_content([content_exemple1], columns=[12], styles=[css_styles['text-60']])
slide5.add_content([content_formalisation], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Tests de significativité : exemple 2
# =============================================================================

slide6 = Slide(**{'class': 'animated fadeIn'})

slide6.add_title("Tests de significativité : exemple 2")

content_test2 = markdown("""
Deux équipes de recherche décident de mesurer la relation entre la température et l'altitude.

- Par manque de moyen, l'équipe A n'a pu faire **que 5 mesures**, l'équipe B **100 mesures**.
- Les deux équipes obtiennent le même résultat : tous les 100 mètres, la température baisse environ de 0,6°C (environ car il y a des fluctuation de mesures : parfois de 0,5°, 0,65° etc.)
""")

content_validation = markdown("""
Pourtant, seul le résultat de l'équipe B peut être validé car les mesures de l'équipe A sont insuffisantes et **peuvent être liées au hasard**. Pour compenser ce manque, il faudrait que les mesures réelles de la température baissent exactement (ou quasi) de 0,6° tous les 100 mètres pour l'équipe A. A l'inverse, l'équipe B peut valider son modèle en dépit des éventuelles fluctuations des mesures de la température.

Dans cet exemple, c'est l'effectif qui est insuffisant (**manque de puissance**), mais l'intensité de la relation ou la rareté d'un phénomène peuvent également jouer.
""")

slide6.add_content([content_test2], columns=[12], styles=[css_styles['text-60']])
slide6.add_content([content_validation], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Analyse des relations entre caractères qualitatifs
# =============================================================================

slide7 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide7.add_title("2- Analyse des relations entre caractères qualitatifs", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Le tableau de contingence
# =============================================================================

slide8 = Slide(**{'class': 'animated fadeIn'})

slide8.add_title("Le tableau de contingence")

content_contingence = markdown("""
Le **tableau de contingence** est l'outil de base pour analyser les relations entre deux caractères qualitatifs.

Il présente les effectifs croisés des modalités de deux variables :

- En lignes : modalités de la première variable
- En colonnes : modalités de la seconde variable
- Dans les cellules : effectifs observés
- Marges : totaux par ligne et par colonne
""")

# Exemple de tableau de contingence
tableau_exemple = markdown_with_tables("""
| Sexe / Réussite | Admis | Recalé | Total |
|-----------------|-------|--------|-------|
| Homme           | 45    | 35     | 80    |
| Femme           | 55    | 25     | 80    |
| **Total**       | **100** | **60** | **160** |
""")

slide8.add_content([content_contingence], columns=[6], styles=[css_styles['text-60']])
slide8.add_content([tableau_exemple], columns=[6], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Analyse des profils
# =============================================================================

slide9 = Slide(**{'class': 'animated fadeIn'})

slide9.add_title("Analyse des profils")

content_profils = markdown("""
L'analyse des profils permet d'étudier les relations :

**Profils lignes :** pourcentages calculés par rapport aux totaux de lignes

**Profils colonnes :** pourcentages calculés par rapport aux totaux de colonnes

Ces profils permettent de comparer les distributions et d'identifier les écarts à l'indépendance.
""")

# Tableaux des profils
profil_lignes = markdown_with_tables("""
**Profils lignes (en %):**
| Sexe / Réussite | Admis | Recalé |
|-----------------|-------|--------|
| Homme           | 56.3  | 43.7   |
| Femme           | 68.8  | 31.2   |
""")

profil_colonnes = markdown_with_tables("""
**Profils colonnes (en %):**
| Sexe / Réussite | Admis | Recalé |
|-----------------|-------|--------|
| Homme           | 45.0  | 58.3   |
| Femme           | 55.0  | 41.7   |
""")

slide9.add_content([content_profils], columns=[12], styles=[css_styles['text-60']])
slide9.add_content([profil_lignes, profil_colonnes], columns=[6, 6], styles=[css_styles['text-60'], css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Test du Chi²
# =============================================================================

slide10 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide10.add_title("3- Test du Chi²", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Principe du test du Chi²
# =============================================================================

slide11 = Slide(**{'class': 'animated fadeIn'})

slide11.add_title("Principe du test du Chi²")

content_principe = markdown("""
Le test du Chi² (χ²) permet de tester l'**indépendance** entre deux variables qualitatives.

**Hypothèses :**

- H₀ (hypothèse nulle) : Les deux variables sont indépendantes
- H₁ (hypothèse alternative) : Les deux variables sont liées

**Principe :**

Compare les effectifs **observés** aux effectifs **théoriques** calculés sous l'hypothèse d'indépendance.
""")

content_formule = markdown("""
**Calcul des effectifs théoriques :**

Effectif théorique = (Total ligne × Total colonne) / Total général

**Statistique du Chi² :**

χ² = Σ [(Observé - Théorique)² / Théorique]
""")

slide11.add_content([content_principe], columns=[6], styles=[css_styles['text-60']])
slide11.add_content([content_formule], columns=[6], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Application du test
# =============================================================================

slide12 = Slide(**{'class': 'animated fadeIn'})

slide12.add_title("Application du test")

# Create cards for the test steps
cards_test = [
    {
        'title': '1. Conditions d\'application',
        'text': markdown("""
- Effectifs théoriques ≥ 5
- Variables qualitatives
- Observations indépendantes
""")
    },
    {
        'title': '2. Calcul de la statistique',
        'text': markdown("""
- Calculer les effectifs théoriques
- Appliquer la formule du χ²
- Comparer à la valeur critique
""")
    },
    {
        'title': '3. Décision',
        'text': markdown("""
- Si χ² > χ²critique : rejet de H₀
- Les variables sont liées
- Sinon : pas de liaison démontrée
""")
    }
]

styles_test = [
    {'class': ['bg-primary', 'text-white']},
    {'class': ['bg-success', 'text-white']},
    {'class': ['bg-warning', 'text-dark']}
]

slide12.add_card(cards_test, styles_test, title_size="h5", text_size="60%")

#%%
# =============================================================================
# Mesures d'association
# =============================================================================

slide13 = Slide(**{'class': 'animated fadeIn'})

slide13.add_title("Mesures d'association")

content_mesures = markdown("""
Lorsqu'une liaison est détectée, on peut mesurer son **intensité** :

**Coefficient de contingence de Cramer (V) :**

V = √(χ² / (n × min(r-1, c-1)))

où n = effectif total, r = nombre de lignes, c = nombre de colonnes

**Interprétation :**

- V = 0 : indépendance parfaite
- V = 1 : liaison parfaite
- 0 < V < 1 : intensité de la liaison
""")

tableau_interpretation = markdown_with_tables("""
| Valeur de V | Interprétation |
|-------------|----------------|
| 0.0 - 0.1   | Liaison très faible |
| 0.1 - 0.3   | Liaison faible |
| 0.3 - 0.5   | Liaison modérée |
| 0.5 - 0.7   | Liaison forte |
| 0.7 - 1.0   | Liaison très forte |
""")

slide13.add_content([content_mesures], columns=[6], styles=[css_styles['text-60']])
slide13.add_content([tableau_interpretation], columns=[6], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Exemple complet
# =============================================================================

slide14 = Slide(**{'class': 'animated fadeIn'})

slide14.add_title("Exemple complet")

content_exemple = markdown("""
**Problème :** Existe-t-il une relation entre le sexe et la réussite à un concours ?

**Données :**
""")

donnees_exemple = markdown_with_tables("""
| Sexe / Réussite | Admis | Recalé | Total |
|-----------------|-------|--------|-------|
| Homme           | 45    | 35     | 80    |
| Femme           | 55    | 25     | 80    |
| **Total**       | **100** | **60** | **160** |
""")

resultats_exemple = markdown("""
**Résultats :**

- χ² calculé = 2.67
- χ² critique (α=0.05) = 3.84
- Conclusion : χ² < χ²critique → Pas de liaison significative
- V de Cramer = 0.13 (liaison faible)
""")

slide14.add_content([content_exemple], columns=[12], styles=[css_styles['text-60']])
slide14.add_content([donnees_exemple], columns=[6], styles=[css_styles['text-60']])
slide14.add_content([resultats_exemple], columns=[6], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Conclusion
# =============================================================================

slide15 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide15.add_title("Conclusion", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Concepts-clés
# =============================================================================

slide16 = Slide(**{'class': 'animated fadeIn'})

slide16.add_title("Concepts-clés")

content_conclusion = markdown("""
**La démarche scientifique :**

- **Falsifiabilité** : critère de scientificité de Popper
- **Tests de significativité** : validation statistique des résultats
- **Objectivité, reproductibilité** : fondements de la science

**L'analyse des relations qualitatives :**

- **Tableau de contingence** : outil de base
- **Profils lignes/colonnes** : analyse des distributions
- **Test du Chi²** : test d'indépendance
- **Mesures d'association** : quantification de l'intensité

**Applications pratiques :**

- Validation des hypothèses de recherche
- Aide à la décision en géographie
- Fondement pour analyses plus complexes
""")

slide16.add_content([content_conclusion], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Generate Presentation
# =============================================================================

# Add all slides to the presentation
p.add_slide([slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8, slide9, slide10,
             slide11, slide12, slide13, slide14, slide15, slide16])

# Save the presentation
p.save_html("LPRO_Cours_4_chi2_py.html",
           theme="moon",
           margin=0.1,
           center=True)

print("✅ Presentation 'LPRO_Cours_4_chi2_py.html' has been created successfully!")