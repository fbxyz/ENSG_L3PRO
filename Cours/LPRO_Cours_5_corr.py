#!/usr/bin/env python3
"""
L3_Cours 4_corrélation
Analyse de données
Cours n°4- La corrélation
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
    'subtitle': 'Cours n°4- La corrélation',
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

content_rappels = markdown("""
Lors du précédent cours, nous avons vu comment décrire une série de données.

L'analyse de données commence cependant à prendre tout sons sens lorsque l'on regarde comment se comporte une série par rapport à une autre, voir plusieurs.

Pour mesurer **l'intensité de la relation** entre deux caractères quantitatifs continus, on utilise le **coefficient de corrélation**.

Il est complémentaire à la **régression linéaire** et à la régression multiple qui visent à résumer et/ou **modéliser** un phénomène par une ou plusieurs variables.
""")

content_geographie = markdown("""
En géographie, **identifier** puis **modéliser** des **relations** permet de comprendre un phénomène sur un espace donné, de prévoir la survenue de ce phénomène ou encore de déterminer les variables qui manquent à notre explication.
""")

slide2.add_content([content_rappels], columns=[12], styles=[css_styles['text-60']])
slide2.add_content([content_geographie], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - La corrélation
# =============================================================================

slide3 = Slide(center=True, **{
    'class': 'inverse animated fadeIn',
    'data-background-image': './assets/css/graticules.png',
    'data-background-size': 'cover',
    'data-background-position': 'bottom right'
})

slide3.add_title("1- La corrélation", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Relation et dépendance
# =============================================================================

slide4 = Slide(**{'class': 'animated fadeIn'})

slide4.add_title("Relation et dépendance")

content_relation = markdown("""
Une relation entre deux caractères quantitatifs x et y peut-être mesurée si l'attribution des valeurs de y *dépendent* des valeurs de x ou inversement.

Par exemple, lorsque x augmente de 1, y augmente aussi de 1. Autrement dit, il y a une **relation** si les valeurs de x ne sont font pas au hasard par rapport au valeurs de y.

**Types de relations :**

- **Relation linéaire positive** : quand x augmente, y augmente
- **Relation linéaire négative** : quand x augmente, y diminue
- **Absence de relation** : les variations de x et y sont indépendantes
- **Relation non-linéaire** : la relation existe mais n'est pas linéaire
""")

slide4.add_content([content_relation], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Le coefficient de corrélation
# =============================================================================

slide5 = Slide(**{'class': 'animated fadeIn'})

slide5.add_title("Le coefficient de corrélation")

content_coefficient = markdown("""
Le **coefficient de corrélation de Pearson** (r) mesure l'intensité et le sens de la relation linéaire entre deux variables quantitatives.

**Formule :**

r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]

**Propriétés :**

- -1 ≤ r ≤ +1
- r = 0 : absence de relation linéaire
- r = +1 : relation linéaire positive parfaite
- r = -1 : relation linéaire négative parfaite
- r est sans unité (indépendant des unités de mesure)
""")

# Tableau d'interprétation
interpretation_table = markdown_with_tables("""
| Valeur de |r| | Interprétation |
|-------------|----------------|
| 0.0 - 0.2   | Très faible |
| 0.2 - 0.4   | Faible |
| 0.4 - 0.6   | Modérée |
| 0.6 - 0.8   | Forte |
| 0.8 - 1.0   | Très forte |
""")

slide5.add_content([content_coefficient], columns=[7], styles=[css_styles['text-60']])
slide5.add_content([interpretation_table], columns=[5], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Types de corrélations
# =============================================================================

slide6 = Slide(**{'class': 'animated fadeIn'})

slide6.add_title("Types de corrélations")

# Create cards for different correlation types
cards_correlation = [
    {
        'title': 'Corrélation positive forte',
        'text': markdown("""
r ≈ +0.8

Les deux variables évoluent dans le même sens. Quand l'une augmente, l'autre augmente également.

Exemple : taille et poids
""")
    },
    {
        'title': 'Corrélation négative forte',
        'text': markdown("""
r ≈ -0.8

Les deux variables évoluent en sens inverse. Quand l'une augmente, l'autre diminue.

Exemple : altitude et température
""")
    },
    {
        'title': 'Corrélation nulle',
        'text': markdown("""
r ≈ 0

Aucune relation linéaire entre les variables.

Les points sont dispersés aléatoirement.
""")
    }
]

styles_correlation = [
    {'class': ['bg-success', 'text-white']},
    {'class': ['bg-danger', 'text-white']},
    {'class': ['bg-secondary', 'text-white']}
]

slide6.add_card(cards_correlation, styles_correlation, title_size="h5", text_size="60%")

#%%
# =============================================================================
# Conditions d'utilisation
# =============================================================================

slide7 = Slide(**{'class': 'animated fadeIn'})

slide7.add_title("Conditions d'utilisation")

content_conditions = markdown("""
**Le coefficient de corrélation de Pearson nécessite :**

**1. Variables quantitatives continues**

- Les deux variables doivent être mesurées sur une échelle continue
- Pas applicable aux variables ordinales ou nominales

**2. Relation linéaire**

- Ne détecte que les relations linéaires
- Une corrélation faible peut masquer une relation non-linéaire forte

**3. Distribution normale (pour les tests)**

- Nécessaire pour tester la significativité
- Pas obligatoire pour le calcul du coefficient

**4. Absence de valeurs aberrantes**

- Les outliers peuvent fausser le coefficient
- Vérifier par analyse graphique préalable
""")

slide7.add_content([content_conditions], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Test de significativité
# =============================================================================

slide8 = Slide(**{'class': 'animated fadeIn'})

slide8.add_title("Test de significativité")

content_test = markdown("""
**Question :** La corrélation observée est-elle significativement différente de zéro ?

**Hypothèses :**

- H₀ : ρ = 0 (pas de corrélation dans la population)
- H₁ : ρ ≠ 0 (corrélation significative)

**Statistique de test :**

t = r√(n-2) / √(1-r²)

Suit une loi de Student à (n-2) degrés de liberté

**Décision :**

Si |t| > t_critique : rejet de H₀ → corrélation significative
""")

# Exemple pratique
exemple_test = markdown("""
**Exemple :**

- n = 50 observations
- r = 0.45
- t = 0.45 × √48 / √(1-0.45²) = 3.47
- t_critique (α=0.05) = 2.01
- Conclusion : corrélation significative
""")

slide8.add_content([content_test], columns=[7], styles=[css_styles['text-60']])
slide8.add_content([exemple_test], columns=[5], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Régression linéaire
# =============================================================================

slide9 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide9.add_title("2- Régression linéaire", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Principe de la régression
# =============================================================================

slide10 = Slide(**{'class': 'animated fadeIn'})

slide10.add_title("Principe de la régression")

content_regression = markdown("""
La **régression linéaire** permet de :

- **Modéliser** la relation entre deux variables
- **Prédire** la valeur d'une variable (Y) à partir d'une autre (X)
- **Quantifier** l'effet d'une variable explicative

**Modèle :**

Y = a + bX + ε

où :

- Y : variable à expliquer (dépendante)
- X : variable explicative (indépendante)
- a : ordonnée à l'origine (intercept)
- b : pente (coefficient de régression)
- ε : terme d'erreur
""")

content_objectif = markdown("""
**Objectif :** Trouver la droite qui minimise la somme des carrés des écarts entre les valeurs observées et prédites.

**Méthode des moindres carrés**
""")

slide10.add_content([content_regression], columns=[7], styles=[css_styles['text-60']])
slide10.add_content([content_objectif], columns=[5], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Calcul des paramètres
# =============================================================================

slide11 = Slide(**{'class': 'animated fadeIn'})

slide11.add_title("Calcul des paramètres")

content_calcul = markdown("""
**Coefficient de régression (pente) :**

b = Σ[(xi - x̄)(yi - ȳ)] / Σ(xi - x̄)²

ou

b = r × (sy / sx)

**Ordonnée à l'origine :**

a = ȳ - b × x̄

**Équation de régression :**

Ŷ = a + bX
""")

# Exemple de calcul
exemple_calcul = markdown_with_tables("""
**Exemple :**
| Variable | Valeur |
|----------|--------|
| x̄ | 10 |
| ȳ | 25 |
| sx | 3 |
| sy | 8 |
| r | 0.75 |

**Calculs :**
- b = 0.75 × (8/3) = 2.0
- a = 25 - 2.0 × 10 = 5.0
- **Équation : Ŷ = 5 + 2X**
""")

slide11.add_content([content_calcul], columns=[6], styles=[css_styles['text-60']])
slide11.add_content([exemple_calcul], columns=[6], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Qualité de l'ajustement
# =============================================================================

slide12 = Slide(**{'class': 'animated fadeIn'})

slide12.add_title("Qualité de l'ajustement")

content_qualite = markdown("""
**Coefficient de détermination (R²) :**

R² = r²

**Interprétation :**

- R² représente la proportion de variance de Y expliquée par X
- 0 ≤ R² ≤ 1
- R² = 0.64 signifie que 64% de la variance de Y est expliquée par X

**Variance résiduelle :**

Variance non expliquée = (1 - R²) × variance totale de Y
""")

# Tableau d'interprétation de R²
interpretation_r2 = markdown_with_tables("""
| Valeur de R² | Interprétation |
|--------------|----------------|
| 0.0 - 0.2    | Très faible ajustement |
| 0.2 - 0.4    | Faible ajustement |
| 0.4 - 0.6    | Ajustement modéré |
| 0.6 - 0.8    | Bon ajustement |
| 0.8 - 1.0    | Très bon ajustement |
""")

slide12.add_content([content_qualite], columns=[6], styles=[css_styles['text-60']])
slide12.add_content([interpretation_r2], columns=[6], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Analyse des résidus
# =============================================================================

slide13 = Slide(**{'class': 'animated fadeIn'})

slide13.add_title("Analyse des résidus")

content_residus = markdown("""
**Résidu :** différence entre valeur observée et valeur prédite

ei = yi - ŷi

**Hypothèses à vérifier :**

1. **Linéarité** : relation linéaire entre X et Y
2. **Homoscédasticité** : variance constante des résidus
3. **Normalité** : distribution normale des résidus
4. **Indépendance** : résidus non corrélés

**Méthodes de vérification :**

- Graphique des résidus vs valeurs prédites
- Graphique quantile-quantile pour la normalité
- Tests statistiques (Shapiro-Wilk, Durbin-Watson...)
""")

slide13.add_content([content_residus], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Applications pratiques
# =============================================================================

slide14 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide14.add_title("3- Applications pratiques", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Exemple complet
# =============================================================================

slide15 = Slide(**{'class': 'animated fadeIn'})

slide15.add_title("Exemple complet")

content_exemple = markdown("""
**Problème :** Relation entre l'altitude (X) et la température (Y)

**Données :** 20 stations météorologiques
""")

donnees_exemple = markdown_with_tables("""
| Statistique | Altitude (m) | Température (°C) |
|-------------|--------------|------------------|
| Moyenne     | 1200         | 8.5              |
| Écart-type  | 400          | 3.2              |
| **Corrélation** | **r = -0.85** |            |
""")

resultats_exemple = markdown("""
**Résultats :**

- **Corrélation :** r = -0.85 (forte corrélation négative)
- **Test :** t = -6.2, p < 0.001 (significatif)
- **Régression :** T = 18.1 - 0.0068 × Altitude
- **R² = 0.72** : 72% de la variance expliquée
- **Interprétation :** La température diminue de 0.68°C par 100m d'altitude
""")

slide15.add_content([content_exemple], columns=[12], styles=[css_styles['text-60']])
slide15.add_content([donnees_exemple], columns=[6], styles=[css_styles['text-60']])
slide15.add_content([resultats_exemple], columns=[6], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Limites et précautions
# =============================================================================

slide16 = Slide(**{'class': 'animated fadeIn'})

slide16.add_title("Limites et précautions")

content_limites = markdown("""
**Attention :**

**1. Corrélation ≠ Causalité**

- Une forte corrélation n'implique pas une relation de cause à effet
- Peut être due à une troisième variable (variable confondante)

**2. Relations non-linéaires**

- Le coefficient de Pearson ne détecte que les relations linéaires
- Utiliser des graphiques pour détecter d'autres types de relations

**3. Valeurs aberrantes**

- Peuvent fortement influencer le coefficient
- Toujours vérifier graphiquement

**4. Extrapolation**

- Ne pas prédire au-delà de la plage des données observées
- Validité du modèle limitée aux conditions d'observation
""")

slide16.add_content([content_limites], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Conclusion
# =============================================================================

slide17 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide17.add_title("Conclusion", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Concepts-clés
# =============================================================================

slide18 = Slide(**{'class': 'animated fadeIn'})

slide18.add_title("Concepts-clés")

content_conclusion = markdown("""
**La corrélation :**

- **Mesure l'intensité** de la relation linéaire entre deux variables
- **Coefficient de Pearson** : -1 ≤ r ≤ +1
- **Test de significativité** : validation statistique
- **Conditions d'application** : variables continues, relation linéaire

**La régression linéaire :**

- **Modélise et prédit** une variable à partir d'une autre
- **Équation :** Y = a + bX
- **R² :** proportion de variance expliquée
- **Analyse des résidus** : validation des hypothèses

**Applications en géographie :**

- Modélisation de phénomènes spatiaux
- Prédiction et aide à la décision
- Identification de relations cachées
- Base pour analyses multivariées
""")

slide18.add_content([content_conclusion], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Generate Presentation
# =============================================================================

# Add all slides to the presentation
p.add_slide([slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8, slide9, slide10,
             slide11, slide12, slide13, slide14, slide15, slide16, slide17, slide18])

# Save the presentation
p.save_html("LPRO_Cours_4_corr_py.html",
           theme="moon",
           margin=0.1,
           center=True)

print("✅ Presentation 'LPRO_Cours_4_corr_py.html' has been created successfully!")