# Analyse des Investissements en Cryptomonnaies

Ce projet permet d'analyser les investissements en cryptomonnaies à partir d'un fichier CSV. L'application utilise Streamlit pour afficher les résultats de l'analyse.

## Structure du projet

- `Invest.py`: Script principal pour l'analyse des investissements.
- `.gitignore`: Fichier pour ignorer certains fichiers dans le dépôt.

## Format du fichier CSV

Le fichier CSV doit contenir les colonnes suivantes :

- `Cryptomonnaie`: Nom de la cryptomonnaie (ex: BTC, ETH, XRP).
- `Date d'achat`: Date d'achat de la cryptomonnaie (format: JJ/MM/AAAA).
- `Quantite`: Quantité de cryptomonnaie achetée.
- `Montant total d'achat(EUR)`: Montant total de l'achat en euros.
- `Prix d'achat`: Prix d'achat de la cryptomonnaie.
- `Frais`: Frais associés à l'achat.
