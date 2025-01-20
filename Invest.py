import pandas as pd
import streamlit as st

st.title("Analyse des Investissements en Cryptomonnaies")

# Permettre à l'utilisateur de télécharger un fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is None:
    # Exemple de tableau CSV
    example_data = {
        "Cryptomonnaie": ["BTC", "ETH", "XRP"],
        "Date d'achat": ["01/01/2022", "02/01/2022", "03/01/2022"],
        "Quantite": [0.1, 0.5, 100],
        "Montant total d'achat(EUR)": [3000, 1500, 200],
        "Prix d'achat": [30000, 3000, 2],
        "Frais": [10, 5, 1]
    }
    example_df = pd.DataFrame(example_data)

    st.header("Exemple de format de fichier CSV")
    st.dataframe(example_df)
else:
    try:
        # Lire le fichier CSV téléchargé avec l'encodage correct
        df = pd.read_csv(uploaded_file, delimiter=';', decimal=',', encoding='ISO-8859-1')

        # Renommer la colonne pour éviter les problèmes d'apostrophe
        df.rename(columns={"Montant total d'achat(EUR)": "Montant_total_achat_EUR"}, inplace=True)

        # Convertir les colonnes en types numériques
        df['Montant_total_achat_EUR'] = pd.to_numeric(df['Montant_total_achat_EUR'], errors='coerce')
        df['Frais'] = pd.to_numeric(df['Frais'], errors='coerce')

        # Calculer le montant total investi par cryptomonnaie
        total_investi = df.groupby('Cryptomonnaie')['Montant_total_achat_EUR'].sum()

        # Calculer la quantité totale achetée par cryptomonnaie
        quantite_totale = df.groupby('Cryptomonnaie')['Quantite'].sum()

        # Calculer le montant total investi par cryptomonnaie en tenant compte des frais
        df['Montant_total_investi'] = df['Montant_total_achat_EUR'] + df['Frais']
        montant_total_investi = df.groupby('Cryptomonnaie')['Montant_total_investi'].sum()

        # Calculer le montant total d'argent investi
        total_argent_investi = montant_total_investi.sum()

        # Afficher le total d'argent investi en haut à gauche
        st.metric(label="Total d'argent investi (EUR)", value=f"{total_argent_investi:.2f}")

        st.header("Montant total investi par cryptomonnaie")
        st.bar_chart(total_investi)

        st.header("Quantité totale achetée par cryptomonnaie")
        st.bar_chart(quantite_totale)

        st.header("Montant total investi par cryptomonnaie (incluant les frais)")
        st.dataframe(montant_total_investi)
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier CSV ou du traitement des données : {e}")