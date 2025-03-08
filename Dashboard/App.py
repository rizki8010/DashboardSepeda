import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("Dashboard/dayCleaned.csv")
hour_df = pd.read_csv("Dashboard/hourCleaned.csv")

st.set_page_config(page_title="Dashboard Penyewaan Sepeda", page_icon="🚴", layout="wide")

st.title("🚴 Dashboard Penyewaan Sepeda")
st.markdown(""" """)
st.markdown('<p style="color:red; font-weight:bold;">Rizki Ilhamnuddin Muria mc009d5y1602</p>', unsafe_allow_html=True)

st.markdown("""
Selamat datang di dashboard analisis penyewaan sepeda!  
Dashboard ini menyajikan informasi mengenai tren penyewaan sepeda berdasarkan hari, jam, dan kondisi cuaca.
""")

menu = st.radio(
    "Pilih Tampilan:",
    ["🏠 Beranda", "📆 Visualisasi Harian", "🕒 Visualisasi Per Jam", "⛅ Visualisasi Berdasarkan Cuaca", "📊 Statistik Data"]
)

content = st.container()
with content:
    if menu == "🏠 Beranda":
        st.subheader("🏠 Beranda")
        st.markdown("""
        **Fitur utama:**
        - 📆 Analisis penyewaan berdasarkan hari kerja vs libur  
        - 🕒 Tren penyewaan berdasarkan jam dan kondisi cuaca  
        - ⛅ Pengaruh cuaca terhadap penyewaan  
        - 📊 Statistik ringkasan data  
        """)

    elif menu == "📆 Visualisasi Harian":
        st.subheader("📆 Tren Penyewaan Sepeda Berdasarkan Hari")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x="workingday", y="cnt", data=day_df, estimator=sum, palette="Blues", ax=ax)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Hari Libur", "Hari Kerja"])
        plt.xlabel("Tipe Hari")
        plt.ylabel("Total Penyewaan")
        plt.title("Perbandingan Penyewaan Sepeda pada Hari Kerja vs Libur")
        st.pyplot(fig)

    elif menu == "🕒 Visualisasi Per Jam":
        st.subheader("🕒 Penyewaan Sepeda Berdasarkan Jam")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(x="hr", y="cnt", data=hour_df, ci=None, palette="Set2", ax=ax)
        plt.xlabel("Jam dalam Sehari")
        plt.ylabel("Jumlah Penyewa")
        plt.title("Jumlah Penyewaan Sepeda Berdasarkan Jam")
        st.pyplot(fig)

    elif menu == "⛅ Visualisasi Berdasarkan Cuaca":
        st.subheader("⛅ Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="weathersit", y="cnt", data=day_df, estimator=sum, ci=None, palette="coolwarm", ax=ax)
        plt.xticks(ticks=[0, 1, 2, 3], labels=["Cerah", "Berkabut", "Hujan Ringan", "Hujan Lebat"])
        plt.xlabel("Kondisi Cuaca")
        plt.ylabel("Jumlah Penyewa")
        plt.title("Jumlah Penyewaan Sepeda Berdasarkan Cuaca")
        st.pyplot(fig)

    elif menu == "📊 Statistik Data":
        st.subheader("📊 Statistik Data Penyewaan Sepeda")
        st.write("### Data Penyewaan Harian")
        st.dataframe(day_df.describe())
        st.write("### Data Penyewaan Per Jam")
        st.dataframe(hour_df.describe())
