# Fixed File Format converter

## Présentation

Outil générique qui convertit un fichier d'entrée au format fixe en un fichier csv, en se basant sur un fichier de metadonnées décrivant sa structure.
Notre fichier d'entrée peut avoir n'importe quel nombre de colonnes
Une colonne peut-être d'un de ces 3 formats:
* date (format yyyy-mm-dd)
* numerique (séparateur décimal '.', peut être négatif)
* string

La structure du fichier est définie dans un fichier de métadonnées, au format csv, où chaque ligne décrit chaque colonne:
* nom de la colonne
* taille de la colonne
* type de la colonne

## Exemple

Fichier d'entrée :
```
1970-01-01John           Smith           81.5
1975-01-31Jane           Doe             61.1
1988-11-28Bob            Big            102.4
```

Fichier de métadonnées :
```
Birth date,10,date
First name,15,string
Last name,15,string
Weight,5,numeric
```

Fichier csv de sortie :
```
Birth date,First name,Last name,Weight
01/01/1970,John,Smith,81.5
31/01/1975,Jane,Doe,61.1
28/11/1988,Bob,Big,102.4
```

## Pré-requis

L'outil est codé en Python (version 3.8 utilisée), il faut donc que Python soit installé sur le poste.

## Installation

Création d'un environnement virtuel dans le dossier du projet.
Pour créer le venv, se mettre à la racine du projet et faire la commande :

```
python -m venv venv
```

Activer le venv

```
source venv/bin/activate
```

Installer les libs requises

```
pip install -r requirements.txt
```

## Utilisation

Se mettre à la racine du projet et lancer le script comme ceci :

```
python -m file_converter --input_data_file ./example/input/input_data.txt --input_metadata_file ./example/input/input_metadata.csv --output_file ./example/output/output_data.csv
```

* input_data_file est le fichier à traiter
* input_metadata_file est le fichier de métadonnées en entrée
* output_file est le fichier dans lequel écrire le résultat

## Tests

Pour lancer les tests, se mettre à la racine du projet et lancer :

```
python -m pytest tests
```