import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("Dashboard/dayCleaned.csv")
hour_df = pd.read_csv("Dashboard/hourCleaned.csv")

# Mapping manual
cuaca_mapping = {1: "Cerah", 2: "Berawan", 3: "Hujan Ringan", 4: "Hujan Lebat"}
hari_mapping = {0: "Senin", 1: "Selasa", 2: "Rabu", 3: "Kamis", 4: "Jum'at", 5: "Sabtu", 6: "Minggu"}
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}

# Apply mapping
day_df["weathersit"] = day_df["weathersit"].map(cuaca_mapping)
day_df["weekday"] = day_df["weekday"].map(hari_mapping)
day_df["season"] = day_df["season"].map(season_mapping)

# Order untuk visualisasi
cuaca_order = ["Cerah", "Berawan", "Hujan Ringan", "Hujan Lebat"]
hari_order = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
season_order = ["Spring", "Summer", "Fall", "Winter"]

st.set_page_config(page_title="Dashboard Penyewaan Sepeda", page_icon="🚴", layout="wide")
st.title("🚴 Dashboard Penyewaan Sepeda")

menu = st.radio("Pilih Tampilan:", ["🏠 Beranda", "📆 Cuaca & Hari", "❄️ Penyewaan Berdasarkan Musim", "🕒 Penyewaan Per Jam", "📊 Statistik Data"])

content = st.container()
with content:
    if menu == "🏠 Beranda":
        st.subheader("🏠 Beranda")
        st.markdown("""
        **Fitur utama:**
        - 📆 Pengaruh Cuaca dan Hari terhadap Penyewaan
        - ❄️ Tren Penyewaan Berdasarkan Musim
        - 🕒 Penyewaan Berdasarkan Jam
        - 📊 Statistik Data
        """)

    elif menu == "📆 Cuaca & Hari":
        st.subheader("📆 Penyewaan Sepeda Berdasarkan Cuaca dan Hari")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x="weathersit", y="cnt", hue="weekday", data=day_df,
                    order=cuaca_order, hue_order=hari_order, errorbar=None, ax=ax)
        plt.xlabel("Cuaca")
        plt.ylabel("Jumlah Penyewa")
        plt.title("Registrasi User Berdasarkan Hari dan Cuaca")
        plt.legend(title="Hari")
        st.pyplot(fig)
    
    elif menu == "❄️ Penyewaan Berdasarkan Musim":
        st.subheader("❄️ Penyewaan Sepeda Berdasarkan Musim")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="season", y="cnt", data=day_df, order=season_order, errorbar=None, ax=ax)
        plt.xlabel("Musim")
        plt.ylabel("Jumlah Penyewa")
        plt.title("Registrasi User Berdasarkan Musim")
        st.pyplot(fig)
    
    elif menu == "🕒 Penyewaan Per Jam":
        st.subheader("🕒 Penyewaan Sepeda Berdasarkan Jam")
        fig, ax = plt.subplots(figsize=(20, 8))
        sns.lineplot(x="hr", y="cnt", data=hour_df, estimator="sum", ax=ax)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.xlabel("Jam dalam Sehari")
        plt.ylabel("Jumlah Penyewaan")
        plt.title("Jumlah Penyewaan Sepeda Berdasarkan Jam")
        plt.xticks(range(24))
        st.pyplot(fig)
    elif menu == "📊 Statistik Data":
        st.subheader("📊 Statistik Data Penyewaan Sepeda")
        st.write("### Data Penyewaan Harian")
        st.dataframe(day_df.describe())
        st.write("### Data Penyewaan Per Jam")
        st.dataframe(hour_df.describe())
