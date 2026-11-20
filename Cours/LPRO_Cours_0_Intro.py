#!/usr/bin/env python3
"""
Analyse des données - Introduction
Présentation du cours
Florian Bayer
"""

#%%
from respysive import Slide, Presentation
from markdown import markdown
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")
annee = os.getenv("annee", "2024")

# Create a new presentation
p = Presentation()

# CSS styles dictionary for text sizing
css_styles = {
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
    'class': 'title-slide animated fadeIn'
})

title_page_content = {
    'title': f'Analyse des données Licence Pro {annee}',
    'subtitle': 'Présentation du cours',
    'authors': 'Florian Bayer',
}

title_styles = [
    {'color': '#2c3e50', 'class': 'r-fit-text'},  # title
    {'color': '#34495e', 'font-size': '1.5em'},  # subtitle
    {'color': '#7f8c8d', 'font-size': '1.2em'},  # authors
]

slide1.add_title_page(title_page_content, title_styles)


#%%
# =============================================================================
# Déroulement des séances
# =============================================================================

slide2 = Slide(**{'class': 'animated fadeIn'})

slide2.add_title("Déroulement des séances")

content_deroulement = markdown("""
- 4 séances de 3 heures
- CM puis TD
- florian.bayer@gmail.com
""")

slide2.add_content([content_deroulement], columns=[12])

#%%
# =============================================================================
# Contenu de l'enseignement - Slide 1
# =============================================================================

slide3 = Slide(**{'class': 'animated fadeIn'})

slide3.add_title("Contenu de l'enseignement")

# First slide cards
cards_slide3 = [
    {
        'title': 'Démarche scientifique',
        'text': markdown("**Acquérir les bonnes pratiques de la démarche scientifique** : Introduction aux méthodes rigoureuses de recherche et d'analyse scientifique.")
    },
    {
        'title': 'Statistiques appliquées',
        'text': markdown("**Les statistiques appliquées à la cartographie** : Compréhension des concepts statistiques et de leur utilisation pour l'analyse et la représentation géographique des données.")
    },
    {
        'title': 'Traitement des données',
        'text': markdown("**Principes et méthodes de traitement en analyse de données** : Initiation aux bases de l'analyse de données et l'interprétation des résultats. La collecte des données n'est pas abordée.")
    }
]

styles_slide3 = [
    {'class': ['bg-primary', 'text-white']},
    {'class': ['bg-info', 'text-white']},
    {'class': ['bg-success', 'text-white']}
]

slide3.add_card(cards_slide3, styles_slide3, title_size="h5", text_size="50%")

#%%
# =============================================================================
# Contenu de l'enseignement - Slide 2
# =============================================================================

slide3b = Slide(**{'class': 'animated fadeIn'})

slide3b.add_title("Contenu de l'enseignement (2)")

# Second slide cards
cards_slide3b = [
    {
        'title': 'Analyse univariée et bivariée',
        'text': markdown("**Analyse univariée et bivariée** sur des données quantitatives : Exploration des techniques d'analyse de variables uniques et des relations entre deux variables (corrélation).")
    },
    {
        'title': 'Méthodes de discrétisation',
        'text': markdown("**Méthodes de discrétisation** : Techniques de regroupement des données en classes pour une meilleure interprétation visuelle.")
    },
    {
        'title': 'Séances de TD pratiques',
        'text': markdown("**Séances de TD pratiques** : Des travaux dirigés permettent aux étudiants de mettre en pratique les connaissances acquises à travers des exercices concrets.")
    }
]

styles_slide3b = [
    {'class': ['bg-warning', 'text-dark']},
    {'class': ['bg-secondary', 'text-white']},
    {'class': ['bg-dark', 'text-white']}
]

slide3b.add_card(cards_slide3b, styles_slide3b, title_size="h5", text_size="50%")

#%%
# =============================================================================
# Slide avec image de fond - Section divider
# =============================================================================

slide4 = Slide(center=True, **{
    'class': 'inverse animated fadeIn',
    'data-background-image': './assets/css/graticules.png',
    'data-background-size': 'cover',
    'data-background-position': 'bottom right'
})

slide4.add_title("Contenu de l'enseignement", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Univarié
# =============================================================================

slide5 = Slide(**{'class': 'animated fadeIn'})

slide5.add_title("Univarié")

content_univarie = markdown("""
- Distinguer les types de **variables**, de **distributions**. **Décrire** une série de données, utiliser les **méthodes appropriées** à chaque type de données.
- Connaître les **principes** et **méthodes** de traitement et d'analyse de données.
- Maîtriser différentes méthodes de **représentation** de l'information statistique en géographie (notamment graphiques et cartographiques).
- N.B. L'analyse univariée est une étape obligatoire avant toutes les analyses statistiques les plus complexes.
""")

# Image URL for distribution
distrib_url = "./assets/images/1_Intro/distrib.png"

slide5.add_content([content_univarie], columns=[12], styles=[css_styles['text-60']])
slide5.add_content([distrib_url], columns=[12], styles=[{**css_styles['center-img'], 'width': '80%'}])

#%%
# =============================================================================
# Discrétisation
# =============================================================================

slide6 = Slide(**{'class': 'animated fadeIn'})

slide6.add_title("Discrétisation")

content_discretisation = markdown("""
En fonction de votre analyse univariée, de vos objectifs et de votre public :
- Appliquer la méthode de discrétisation la plus adaptée
""")

# Image URL for discretisation
discret_url = "./assets/images/1_Intro/discret.png"

slide6.add_content([content_discretisation], columns=[12])
slide6.add_content([discret_url], columns=[12], styles=[{'class': 'center-img', 'width': '100%'}])

#%%
# =============================================================================
# Bivarié
# =============================================================================

slide7 = Slide(**{'class': 'animated fadeIn'})

slide7.add_title("Bivarié")

content_bivarie = markdown("""
- Mesurer l'**intensité** de la **relation** entre deux variables *quantitatives* à l'aide de la corrélation.
- **Modéliser** la nature d'une relation entre deux variables à l'aide des analyses de régression linéaire.
""")

# Image URL for correlation
corr_url = "./assets/images/1_Intro/corr_dumb.jpg"

slide7.add_content([content_bivarie], columns=[12])
slide7.add_content([corr_url], columns=[12], styles=[{'class': 'center-img', 'width': '70%'}])

#%%
# =============================================================================
# Exemple d'application 1
# =============================================================================

slide8 = Slide(**{'class': 'animated fadeIn'})

slide8.add_title("Exemple d'application")

stat1_url = "./assets/images/1_Intro/stat1.png"

slide8.add_content([stat1_url], columns=[12], styles=[{'class': 'center-img', 'width': '100%'}])

#%%
# =============================================================================
# Exemple d'application 2
# =============================================================================

slide9 = Slide(**{'class': 'animated fadeIn'})

slide9.add_title("Exemple d'application")

stat2_url = "./assets/images/1_Intro/stat2.png"

slide9.add_content([stat2_url], columns=[12], styles=[{'class': 'center-img', 'width': '75%'}])

#%%
# =============================================================================
# Exemple (non abordé cette année) 1
# =============================================================================

slide10 = Slide(**{'class': 'animated fadeIn'})

slide10.add_title("Exemple (non abordé cette année)")

stat3_url = "./assets/images/1_Intro/stat3.png"

slide10.add_content([stat3_url], columns=[12], styles=[{'class': 'center-img', 'width': '100%'}])

#%%
# =============================================================================
# Exemples (non abordé cette année) 2
# =============================================================================

slide11 = Slide(**{'class': 'animated fadeIn'})

slide11.add_title("Exemples (non abordé cette année)")

bretagne_url = "./assets/images/1_Intro/bretagne_acp.png"

slide11.add_content([bretagne_url], columns=[12], styles=[{'class': 'center-img', 'width': '100%'}])

#%%
# =============================================================================
# Adding slides to presentation and saving
# =============================================================================

# Add all slides to the presentation
p.add_slide([slide1, slide2, slide3, slide3b, slide4, slide5, slide6, slide7, slide8, slide9, slide10, slide11])

# Save the presentation
p.save_html("LPRO_Cours_0_Intro_py.html",
           theme="moon",
           margin=0.1,
           center=True)

print("✅ Presentation 'LPRO_Cours_0_Intro_py.html' has been created successfully!")

