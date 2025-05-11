import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analyse Crypto", layout="wide")
st.title("📊 Analyse des Investissements en Cryptomonnaies")

def afficher_exemple():
    example_data = {
        "Cryptomonnaie": ["BTC", "ETH", "XRP"],
        "Date d'achat": ["01/01/2022", "02/01/2022", "03/01/2022"],
        "Quantite": [0.1, 0.5, 100],
        "Montant total d'achat(EUR)": [3000, 1500, 200],
        "Prix d'achat": [30000, 3000, 2],
        "Frais": [10, 5, 1]
    }
    st.subheader("📁 Exemple de format CSV attendu")
    st.dataframe(pd.DataFrame(example_data))

def charger_donnees(fichier):
    try:
        df = pd.read_csv(fichier, delimiter=';', decimal=',', encoding='ISO-8859-1')
        df = df.rename(columns={"Montant total d'achat(EUR)": "Montant_total_achat_EUR"})  # évite le bug d'apostrophe
        return df
    except Exception as e:
        st.error(f"❌ Erreur de lecture du fichier : {e}")
        return None

def traiter_donnees(df):
    try:
        df["Montant_total_achat_EUR"] = pd.to_numeric(df["Montant_total_achat_EUR"], errors='coerce')
        df["Frais"] = pd.to_numeric(df["Frais"], errors='coerce')
        df["Quantite"] = pd.to_numeric(df["Quantite"], errors='coerce')
        df["Montant total investi"] = df["Montant_total_achat_EUR"] + df["Frais"]
        return df
    except Exception as e:
        st.error(f"❌ Erreur de traitement des données : {e}")
        return None

def afficher_resultats(df):
    total_investi = df.groupby("Cryptomonnaie")["Montant_total_achat_EUR"].sum()
    quantite_totale = df.groupby("Cryptomonnaie")["Quantite"].sum()
    montant_total_investi = df.groupby("Cryptomonnaie")["Montant total investi"].sum()
    total_general = montant_total_investi.sum()

    st.metric(label="💰 Total investi (EUR)", value=f"{total_general:,.2f}")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💸 Montant investi par cryptomonnaie")
        st.bar_chart(total_investi)
    with col2:
        st.subheader("📦 Quantité totale par cryptomonnaie")
        st.bar_chart(quantite_totale)

    st.subheader("🧾 Détail du montant investi avec frais")
    st.dataframe(montant_total_investi.reset_index().rename(columns={"Montant total investi": "Montant (EUR)"}))

    with st.expander("📊 Voir en camembert"):
        fig, ax = plt.subplots()
        montant_total_investi.plot.pie(autopct='%1.1f%%', ax=ax, ylabel='', title="Répartition des investissements")
        st.pyplot(fig)

# --- Application principale ---
uploaded_file = st.file_uploader("📤 Téléversez un fichier CSV", type="csv")

if uploaded_file is None:
    afficher_exemple()
else:
    df = charger_donnees(uploaded_file)
    if df is not None:
        df = traiter_donnees(df)
        if df is not None:
            afficher_resultats(df)
