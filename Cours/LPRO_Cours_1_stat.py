#!/usr/bin/env python3
"""
L3_Cours 1_stat
Analyse des données
Cours n°1- Les données en statistique
Florian Bayer
"""

#%%
from respysive import Slide, Presentation
from markdown import markdown
import os
from dotenv import load_dotenv
import pandas as pd

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
    'subtitle': 'Cours n°1- Les données en statistique',
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
Savoir caractériser et organiser les données est une étape essentielle de toute étude scientifique. Outre la méthode de représentation graphique, le type de données est très important en statistique :

les **méthodes** ne seront pas les mêmes pour
- **caractériser** le prénom le plus fréquemment données en 2019
- ou pour déterminer l'âge moyen de la population française.

Les objectifs de ce cours sont donc :

- de réviser le **vocabulaire** portant sur les données en cartographie et en statistique
- d'apprendre à **reconnaître** les différents types de données et de tableaux
""")

slide2.add_content([content_objectifs], columns=[12], styles=[css_styles['text-80']])

#%%
# =============================================================================
# L'information géographique
# =============================================================================

slide3 = Slide(**{'class': 'animated fadeIn'})

slide3.add_title("L'information géographique")

content_info_geo = markdown("""
Le géographe a pour particularité de s'intéresser aux **lieux** auxquels sont rattachés les données.

- Une information non localisable a donc peu d'intérêt pour le géographe

Le cartographe utilise donc de l'**information géographique**, c'est-à-dire localisable dans l'espace :

- Par des coordonnées
- Par une appartenance à un lieu, à un maillage

Ces appartenances ont un intérêt si elles peuvent être **caractériser** :

- À une commune peut être associée sa population totale ou sa densité

Si la collecte de l'information géographique peut parfois être laborieuse, son analyse peut se faire avec les mêmes outils qu'en statistique.
""")

slide3.add_content([content_info_geo], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Les données en cartographie
# =============================================================================

slide4 = Slide(**{'class': 'animated fadeIn'})

slide4.add_title("Les données en cartographie")

content_donnees_carto = markdown("""
Les données utilisées en cartographie et statistique proviennent de multiples sources (*recensement, sondage,images satellites etc.*) et peuvent être **caractérisées** (première partie du cours) :
""")

# URLs for images
quali_url = "./assets/images/2-Stat/Quali.png"
quanti_url = "./assets/images/2-Stat/Quanti.png"

slide4.add_content([content_donnees_carto], columns=[12],styles=[css_styles['text-60']])

# Add two column layout for qualitative and quantitative data
content_quali = markdown("**Données qualitatives**")
content_quanti = markdown("**Données quantitatives**")

slide4.add_content([content_quali, content_quanti], columns=[6, 6],
                  styles=[{'text-align': 'center', 'font-weight': 'bold', 'font-size': '60%'},
                         {'text-align': 'center', 'font-weight': 'bold', 'font-size': '60%'}])

slide4.add_content([quali_url, quanti_url], columns=[6, 6],
                  styles=[{**css_styles['center-img'], 'width': '80%'},
                         {**css_styles['center-img'], 'width': '60%'}])

#%%
# =============================================================================
# Les données en cartographie (suite)
# =============================================================================

slide5 = Slide(**{'class': 'animated fadeIn'})

slide5.add_title("Les données en cartographie")

content_donnees_suite = markdown("""
Les données peuvent être récupérées sous forme de tableaux (*i.e. INSEE*), ou bien issues de différentes sources (livres, articles, pixels).

Il est nécessaire de **restructurer** ces données, le plus souvent sous la forme d'un nouveau tableau. Les différents types de tableaux seront abordés dans la seconde partie du cours.
""")

slide5.add_content([content_donnees_suite], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Les données en cartographie
# =============================================================================

slide6 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide6.add_title("1- Les données en cartographie", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Rappels de vocabulaire : statistique
# =============================================================================

slide7 = Slide(**{'class': 'animated fadeIn'})

slide7.add_title("Rappels de vocabulaire : statistique")

content_vocab_stat = markdown("""
Avant de définir les grands types de données, il est nécessaire de rappeler le vocabulaire commun aux données

**La statistique** :
l'ensemble de techniques et d'outils mathématiques permettant d'analyser des données
""")

# Fisher quote and image
fisher_quote = markdown("""
« L'objet de la méthode statistique est la réduction des données. Une masse de données doit être remplacée par un petit nombre de quantités représentant correctement cette masse, et contenant autant que possible la totalité de l'information pertinente contenue dans les données d'origine. »
- Sir Ronald Aymler Fisher
""")

fisher_url = "./assets/images/2-Stat/Fisher.jpg"

content_statistiques = markdown("""
**Les statistiques** :
les données textes ou chiffres (alphanumériques) décrivant une population, un ensemble
""")

slide7.add_content([content_vocab_stat], columns=[12],styles=[css_styles['text-60']])
slide7.add_content([fisher_quote, fisher_url], columns=[8, 4],
                  styles=[css_styles['text-50'], {**css_styles['center-img'], 'width': '70%'}])
slide7.add_content([content_statistiques], columns=[12],styles=[css_styles['text-60']])

#%%
# =============================================================================
# Rappels de vocabulaire : population
# =============================================================================

slide8 = Slide(**{'class': 'animated fadeIn'})

slide8.add_title("Rappels de vocabulaire : population")

content_vocab_pop = markdown("""
La **population** ou **l'ensemble** :

- La collection (l'ensemble) des données qui vont servir à créer votre carte.
- En géographie cet ensemble est très rarement infini
- On parlera souvent de série statistique pour les données quantitatives
""")

# Images for examples
europe_url = "./assets/images/2-Stat/Europe.png"
solvay_url = "./assets/images/2-Stat/Solvay_conference_1927.jpg"

content_europe = markdown("Ensemble des unités statistiques étudiées : les pays européens")
content_solvay = markdown("Mais la population peut aussi correspondre à des personnes")

slide8.add_content([content_vocab_pop], columns=[12],styles=[css_styles['text-60']])
slide8.add_content([content_europe, content_solvay], columns=[6, 6],styles=[css_styles['text-60']]*2)
slide8.add_content([europe_url, solvay_url], columns=[6, 6],
                  styles=[{**css_styles['center-img'], 'width': '100%'},
                         {**css_styles['center-img'], 'width': '100%'}])

#%%
# =============================================================================
# Rappels de vocabulaire : élément
# =============================================================================

slide9 = Slide(**{'class': 'animated fadeIn'})

slide9.add_title("Rappels de vocabulaire : élément")

content_vocab_element = markdown("""
L'**élément** ou l'individu : un objet constitutif de l'ensemble
""")

# Create example table for Belgium
table_belgium = markdown_with_tables("""
| iso_a3 | Nom     | Continent |
|--------|---------|----------|
| AUT    | Austria | Europe   |
| BEL    | Belgium | Europe   |
| **BEL**| **Belgium** | **Europe** |
| BGR    | Bulgaria| Europe   |
| CYP    | Cyprus  | Europe   |
""")

content_belgium = markdown("La Belgique est un élément de l'ensemble des pays européens")
content_curie = markdown("Marie Curie est un individu de l'ensemble des participants du Congrès de Solvay")

curie_url = "./assets/images/2-Stat/Marie_Curie_c1920.jpg"

slide9.add_content([content_vocab_element], columns=[12],styles=[css_styles['text-60']])
slide9.add_content([content_belgium, content_curie], columns=[6, 6],styles=[css_styles['text-60']]*2)
slide9.add_content([table_belgium, curie_url], columns=[6, 6],
                  styles=[css_styles['text-70'], {'class': 'center-img', 'width': '60%', 'height': 'auto', 'max-width': '250px', 'text-align': 'center', 'display': 'block', 'margin': '0 auto'}])

#%%
# =============================================================================
# Rappels de vocabulaire : caractère
# =============================================================================

slide10 = Slide(**{'class': 'animated fadeIn'})

slide10.add_title("Rappels de vocabulaire : caractère")

content_vocab_caractere = markdown("""
Le **caractère** : les éléments d'un ensemble sont décrits par un caractère.
""")

content_pays = markdown("Chaque pays peut-être caractérisé par son code, son nom, sa superficie, sa population")
content_personnes = markdown("De même que des personnes (Nom, prénom, age, sexe, adresse etc.)")

# Create example tables
table_pays = markdown_with_tables("""
| iso_a3 | Nom | Continent | Superficie | Population |
|--------|-----|-----------|------------|------------|
|        |     |           |            |            |
""")

table_personnes = markdown_with_tables("""
| Nom | Prénom | Sexe | Adresse |
|-----|--------|------|--------|
|     |        |      |        |
""")

slide10.add_content([content_vocab_caractere], columns=[12] ,styles=[css_styles['text-60']])
slide10.add_content([content_pays, content_personnes], columns=[6, 6],styles=[css_styles['text-60']]*2)
slide10.add_content([table_pays, table_personnes], columns=[6, 6],
                   styles=[css_styles['text-40'], css_styles['text-40']])

#%%
# =============================================================================
# Rappels de vocabulaire : modalité / valeur
# =============================================================================

slide11 = Slide(**{'class': 'animated fadeIn'})

slide11.add_title("Rappels de vocabulaire : modalité / valeur")

content_vocab_modalite = markdown("""
La **modalité**, la **valeur** : la valeur descriptive du caractère
- * modalité pour les données qualitatives
- * valeur pour les données quantitatives
""")

content_belgique = markdown("La valeur de la population Belge est de 10,4 millions d'habitants. La modalité de son code iso est BEL")
content_marie = markdown("Marie Curie est une femme née en 1867. Elle a résidé au 36 quai de Béthune, 75004 Paris.")

# Create example tables with data
table_belgique = markdown_with_tables("""
| iso_a3 | Nom     | Continent | Superficie | Population |
|--------|---------|-----------|------------|------------|
| BEL    | Belgium | Europe    | 30528      | 10403000   |
""")

table_marie = markdown_with_tables("""
| Nom   | Prénom | Sexe | Adresse                      |
|-------|--------|------|------------------------------|
| Curie | Marie  | F    | 36 quai de Béthune, 75004 Paris |
""")

slide11.add_content([content_vocab_modalite], columns=[12],styles=[css_styles['text-60']])
slide11.add_content([content_belgique, content_marie], columns=[6, 6],styles=[css_styles['text-60']]*2)
slide11.add_content([table_belgique, table_marie], columns=[6, 6],
                   styles=[css_styles['text-40'], css_styles['text-40']])

#%%
# =============================================================================
# Données quantitatives et qualitatives
# =============================================================================

slide12 = Slide(**{'class': 'animated fadeIn'})

slide12.add_title("Données quantitatives et qualitatives")

intro_text = markdown("On peut caractériser les données en deux grands types, eux-mêmes disposant de sous-caractéristiques.")

# Create cards for qualitative and quantitative data
cards_data_types = [
    {
        'title': 'Données qualitatives',
        'text': markdown("""
- caractérise la nature de ce qui est décrit et non la quantité.
- Un nom
- Une couleur
- Le type de sol
""")
    },
    {
        'title': 'Données quantitatives',
        'text': markdown("""
- Caractérise une quantité, par définition mesurable
- Une population
- Un taux de chômage
- Une densité
- L'IDH
""")
    }
]

styles_data_types = [
    {'class': ['bg-info', 'text-white']},
    {'class': ['bg-success', 'text-white']}
]

slide12.add_content([intro_text], columns=[12],styles=[css_styles['text-60']])
slide12.add_card(cards_data_types, styles_data_types, title_size="h4", text_size="80%")

#%%
# =============================================================================
# Quantitatives et qualitatives ?
# =============================================================================

slide13 = Slide(**{'class': 'animated fadeIn'})

slide13.add_title("Quantitatives et qualitatives ?")

content_distinction = markdown("""
Il est important de pouvoir justifier le type de données :

- Si la moyenne est impossible ou absurde : qualitatif (code départementaux, numéro de téléphone)
- Si la moyenne a un sens : quantitatif (population, température)
""")

# Image URL for the meme
img = "./assets/images/1_Intro/quali_quanti.png"

slide13.add_content([content_distinction,img], columns=[6,6],styles=[css_styles['text-60'],{**css_styles['center-img'], 'width': '100%'}])


#%%
# =============================================================================
# Les sous types de données qualitatives
# =============================================================================

slide14 = Slide(**{'class': 'animated fadeIn'})

slide14.add_title("Les sous types de données qualitatives")

intro_qual = markdown("Les données qualitatives peuvent avoir d'autres propriétés, importantes en cartographie et en statistique")

# Create cards for qualitative subtypes
cards_qual = [
    {
        'title': 'Qualitatif nominal',
        'text': markdown("""
contient une notion de différence, aucun ordre
- Codes départementaux
- Des prénoms
- Des numéros étudiants
""")
    },
    {
        'title': 'Qualitatif ordinal',
        'text': markdown("""
contient une notion d'ordre sans être mesurable
- Une classification : grand > moyen > petit
""")
    }
]

cards_qual2 = [
    {
        'title': 'Qualitatif discret',
        'text': markdown("""
il y a moins de modalités que d'éléments.
- Le statut des hôpitaux : CHU, CHR, CH (3 statuts, 6 000 hôpitaux)
- Le statut des communes : Capitale, préfecture, sous préfecture
""")
    },
    {
        'title': 'Qualitatif exhaustif',
        'text': markdown("""
il y a autant de modalités que d'éléments
- Le nom des pays, des régions
- Un code
""")
    }
]

styles_qual = [
    {'class': ['bg-primary', 'text-white']},
    {'class': ['bg-info', 'text-white']}
]

slide14.add_content([intro_qual], columns=[12], styles=[css_styles['text-60']])
slide14.add_card(cards_qual, styles_qual, title_size="h5", text_size="60%")
slide14.add_card(cards_qual2, styles_qual, title_size="h5", text_size="60%")

#%%
# =============================================================================
# Les sous types de données quantitatives (1)
# =============================================================================

slide15 = Slide(**{'class': 'animated fadeIn'})

slide15.add_title("Les sous types de données quantitatives")

intro_quant = markdown("Les données **quantitatives** peuvent aussi avoir d'autres propriétés, toutes aussi importantes en cartographie et en statistique")

# Create cards for stock vs taux
cards_stock_taux = [
    {
        'title': 'Quantitatif de stock',
        'text': markdown("""
une quantité brute, un effectif.
- La population
- Une production en tonne
""")
    },
    {
        'title': 'Quantitatif de taux',
        'text': markdown("""
un rapport, un indice.
- La densité de population
- Le taux de chômage
- L'IDH
""")
    }
]

styles_quant = [
    {'class': ['bg-success', 'text-white']},
    {'class': ['bg-warning', 'text-dark']}
]

slide15.add_content([intro_quant], columns=[12], styles=[css_styles['text-60']])
slide15.add_card(cards_stock_taux, styles_quant, title_size="h5", text_size="70%")

#%%
# =============================================================================
# Stock ou taux ?
# =============================================================================

slide16 = Slide(**{'class': 'animated fadeIn'})

slide16.add_title("Stock ou taux ?")

content_stock_taux = markdown("""
Comment faire la différence entre stock et taux ?
- Si la somme a une signification : stock (la somme de la population des pays du monde = la population mondiale)
- Si la somme n'a pas de sens : taux (la somme du taux de chômage des pays du monde ne correspond pas au taux de chômage mondial)

Attention, ce n'est pas parce que la valeur contient une virgule qu'il s'agit d'une données de taux :
- la France à une population de 66,6 millions d'habitants en 2016
""")

# Image URL for the meme
img_url = "./assets/images/1_Intro/stock_taux.png"

slide16.add_content([content_distinction,img], columns=[6,6],styles=[css_styles['text-60'],{**css_styles['center-img'], 'width': '100%'}])


#%%
# =============================================================================
# Les sous types de données quantitatives (2)
# =============================================================================

slide17 = Slide(**{'class': 'animated fadeIn'})

slide17.add_title("Les sous types de données quantitatives")

# Create cards for additional quantitative subtypes
cards_quant2 = [
    {
        'title': 'Quantitatif repérable',
        'text': markdown("""
le zéro est conventionnel
- L'altitude
""")
    },
    {
        'title': 'Quantitatif mesurable',
        'text': markdown("""
le zéro signifie l'absence concrète
- Le taux de chômage
- La population
""")
    }
]

cards_quant3 = [
    {
        'title': 'Quantitatif discret',
        'text': markdown("""
une variable discrète a un nombre fini ou dénombrable de valeurs possibles. Elles sont distinctes et séparées :
- Le nombre d'étudiants dans cette salle
- Les pointures de chaussures
""")
    },
    {
        'title': 'Quantitatif continu',
        'text': markdown("""
il y a un nombre illimité de valeurs. Entre deux valeurs distinctes, il y a toujours une valeur intermédiaire possible :
- Le taux de chômage
- La vitesse du vent
""")
    }
]

styles_quant2 = [
    {'class': ['bg-secondary', 'text-white']},
    {'class': ['bg-dark', 'text-white']}
]

note_discretisation = markdown("On peut transformer une donnée continue en donnée discrète en classant les valeurs dans des classes → discrétisation")

slide17.add_card(cards_quant2, styles_quant2, title_size="h5", text_size="60%")
slide17.add_card(cards_quant3, styles_quant2, title_size="h5", text_size="50%")
slide17.add_content([note_discretisation], columns=[12], styles=[css_styles['text-70']])

#%%
# =============================================================================
# En résumé
# =============================================================================

slide18 = Slide(**{'class': 'animated fadeIn'})

slide18.add_title("En résumé")

# Schema image
schema_url = "./assets/images/2-Stat/Caractere.png"

slide18.add_content([schema_url], columns=[12],
                   styles=[{**css_styles['center-img'], 'width': '90%'}])

#%%
# =============================================================================
# Section divider - Les différents types de tableaux
# =============================================================================

slide19 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide19.add_title("2- Les différents types de tableaux", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Rappels
# =============================================================================

slide20 = Slide(**{'class': 'animated fadeIn'})

slide20.add_title("Rappels")

content_rappels = markdown("""
Il existe de nombreux type de tableaux en statistique. Leur forme peut dépendre entre autre:

- Du type de données en amont (comment ont-elles été recueillies ?)
- De la manière dont vous souhaitez analyser vos données (regroupements ?)
- La manière de mettre en forme les tableaux et les variables est un métier à part dans l'entreprise (data manager)
""")

slide20.add_content([content_rappels], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Tableau élémentaire de données
# =============================================================================

slide21 = Slide(**{'class': 'animated fadeIn'})

slide21.add_title("Tableau élémentaire de données")

content_tableau_elem = markdown("""
C'est le cas le plus courant. Il décrit un ensemble d'éléments (lignes du tableau) à l'aide d'un ensemble de caractères (colonnes du tableau).

- La première colonne est généralement réservée à un caractère servant d'identifiant.
- On note *i* un élément quelconque du tableau et *Xi* la " modalité prise par l'élément *i* pour le caractère *X*. "
- En géographie on parlera de **tableau d'information géographique**
""")

# Create example table
example_table = markdown_with_tables("""
| Etudiant | Groupe | UFR  |
|----------|--------|------|
| A        | 1      | GEO  |
| B        | 1      | GEO  |
| C        | 2      | GEO  |
| D        | 2      | HIST |
| E        | 3      | HIST |
| F        | 3      | GEO  |
| G        | 3      | HIST |
""")

slide21.add_content([content_tableau_elem, example_table], columns=[6, 6],
                   styles=[css_styles['text-50'], css_styles['text-70']])

#%%
# =============================================================================
# Tableau de contingence
# =============================================================================

slide22 = Slide(**{'class': 'animated fadeIn'})

slide22.add_title("Tableau de contingence")

content_contingence = markdown("""
C'est un cas particulier de tableau élémentaire :

- les lignes et les colonnes jouent un rôle symétrique
- le contenu des cases correspond à des effectifs qui peuvent être sommés en ligne et en colonne.
- On peut parfois calculer des moyennes ou tout autre indicateur statistique si les données le permettent

Tout tableau de contingence est le résultat de la transformation d'un tableau élémentaire constitués de deux caractères discrets X et Y décrivant le même ensemble E

Le nombre de ligne d'un tableau de contingence (k) correspond au nombre de modalités du premier caractère discret (X) et le nombre de colonnes (p) correspond au nombre de modalités du second caractère discret (Y)

L'effectif d'une case, noté Nij, correspond au " nombre d'éléments du tableau élémentaire E qui prennent simultanément la modalité i de X et la modalité j de Y ".
""")

slide22.add_content([content_contingence], columns=[12], styles=[css_styles['text-50']])

#%%
# =============================================================================
# Tableau de contingence - Exemple
# =============================================================================

slide23 = Slide(**{'class': 'animated fadeIn'})

slide23.add_title("Tableau de contingence")

content_elem_title = markdown("**Tableau élémentaire de données**")
content_contingence_title = markdown("**Transformé en tableau de contingence**")

# Example tables
table_elem = markdown_with_tables("""
| Etudiant | Groupe | UFR  |
|----------|--------|------|
| A        | 1      | GEO  |
| B        | 1      | GEO  |
| C        | 2      | GEO  |
| D        | 2      | HIST |
| E        | 3      | HIST |
| F        | 3      | GEO  |
| G        | 3      | HIST |
""")

table_contingence = markdown_with_tables("""
| UFR x Grp | GEO | HIST | Total |
|-----------|-----|------|-------|
| 1         | 2   | 0    | 2     |
| 2         | 1   | 1    | 2     |
| 3         | 1   | 2    | 3     |
| **Total** | **4** | **3** | **7** |
""")

slide23.add_content([content_elem_title, content_contingence_title], columns=[6, 6],styles=[css_styles['text-50'], css_styles['text-50']])
slide23.add_content([table_elem, table_contingence], columns=[6, 6],
                   styles=[css_styles['text-60'], css_styles['text-60']])

#%%
# =============================================================================
# Tableau disjonctif complet
# =============================================================================

slide24 = Slide(**{'class': 'animated fadeIn'})

slide24.add_title("Tableau disjonctif complet")

content_disjonctif = markdown("""
C'est le résultat de l'éclatement d'un tableau élémentaire contenant des modalités

- Les variables sont codées en 0 ou 1 pour l'absence/présence d'un caractère
- On l'utilise pour certaines analyses spécifiques (analyses factorielles)
- Ils sont de retour en grâce avec le machine learning
""")

content_elem_title2 = markdown("**Tableau élémentaire de données**")
content_disjonctif_title = markdown("**Transformé en tableau disjonctif complet**")

# Tables
table_elem2 = markdown_with_tables("""
| Etudiant | Groupe | UFR  |
|----------|--------|------|
| A        | 1      | GEO  |
| B        | 1      | GEO  |
| C        | 2      | GEO  |
| D        | 2      | HIST |
| E        | 3      | HIST |
| F        | 3      | GEO  |
| G        | 3      | HIST |
""")

table_disjonctif = markdown_with_tables("""
| Etudiant | groupe.1 | groupe.2 | groupe.3 | UFR.GEO | UFR.HIST |
|----------|----------|----------|----------|---------|----------|
| A        | 1        | 0        | 0        | 1       | 0        |
| B        | 1        | 0        | 0        | 1       | 0        |
| C        | 0        | 1        | 0        | 1       | 0        |
| D        | 0        | 1        | 0        | 0       | 1        |
| E        | 0        | 0        | 1        | 0       | 1        |
| F        | 0        | 0        | 1        | 1       | 0        |
| G        | 0        | 0        | 1        | 0       | 1        |
""")

slide24.add_content([content_disjonctif], columns=[12], styles=[css_styles['text-50']])
slide24.add_content([content_elem_title2, content_disjonctif_title], columns=[6, 6],
                    styles=[css_styles['text-60'], css_styles['text-50']])
slide24.add_content([table_elem2, table_disjonctif], columns=[6, 6],
                   styles=[css_styles['text-40'], css_styles['text-40']])

#%%
# =============================================================================
# Tableau d'échanges
# =============================================================================

slide25 = Slide(**{'class': 'animated fadeIn'})

slide25.add_title("Tableau d'échanges")

content_echanges = markdown("""
On parle aussi de matrice de flux

- Il contient des individus géographiques en ligne et en colonne, qui peuvent ou non être identiques
- Un tableau ne peut représenter qu'un seul caractère, par exemple les flux de population entre les individus
- Si le tableau d'échanges n'est pas symétrique, il se lit de la ligne vers la colonne
""")

# Example exchange table
table_echanges = markdown_with_tables("""
| Aéroports | Paris | Berlin | Londres |
|-----------|-------|--------|----------|
| Paris     | -     | 15     | 5        |
| Berlin    | 10    | -      | 20       |
| Londres   | 5     | 10     | -        |
""")

slide25.add_content([content_echanges,table_echanges], columns=[6,6],
                    styles=[css_styles['text-60'],css_styles['text-60']])

#%%
# =============================================================================
# Section divider - Conclusion
# =============================================================================

slide26 = Slide(center=True, **{
    'class': 'inverse animated fadeIn'
})

slide26.add_title("Conclusion", **{
    'color': 'white',
    'class': 'r-fit-text'
})

#%%
# =============================================================================
# Concepts-clés
# =============================================================================

slide27 = Slide(**{'class': 'animated fadeIn'})

slide27.add_title("Concepts-clés")

content_conclusion = markdown("""
Les géographes utilisent de **l'information géographique**, localisable dans l'espace.

- Il existe un vocabulaire propre aux données statistiques, qu'il est nécessaire de connaître.
- Les données peuvent être regroupées selon plusieurs **propriétés**
- Qu'il faut maîtriser, car les règles de la sémiologie graphique et les outils statistiques en **dépendent** !

Plusieurs types de tableaux existent et il est nécessaire de les reconnaître

- Les tableaux élémentaires de données sont les plus courants, avec en ligne les individus et en colonnes leurs caractères
- Les tableaux de contingence permettent de croiser des caractères
- Les tableaux d'échanges sont très appréciées des géographes
""")

slide27.add_content([content_conclusion], columns=[12], styles=[css_styles['text-60']])

#%%
# =============================================================================
# Generate Presentation
# =============================================================================

# Add all slides to the presentation
p.add_slide([slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8, slide9, slide10,
             slide11, slide12, slide13, slide14, slide15, slide16, slide17, slide18, slide19,
             slide20, slide21, slide22, slide23, slide24, slide25, slide26, slide27])

# Save the presentation
p.save_html("LPRO_Cours_1_stat_py.html",
           theme="moon",
           margin=0.1,
           center=True)

print("✅ Presentation 'LPRO_Cours_1_stat_py.html' has been created successfully!")