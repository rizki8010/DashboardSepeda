import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("dayCleaned.csv")
hour_df = pd.read_csv("hourCleaned.csv")

st.set_page_config(
    page_title="Dashboard Penyewaan Sepeda", page_icon="🚴", layout="wide"
)

st.title("🚴 Dashboard Penyewaan Sepeda")
st.markdown(
    '<p style="color:red; font-weight:bold;">Rizki Ilhamnuddin Muria mc009d5y1602</p>',
    unsafe_allow_html=True,
)

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
date_start = st.sidebar.date_input("Pilih Tanggal Awal:", pd.to_datetime("2011-01-01"))
date_end = st.sidebar.date_input("Pilih Tanggal Akhir:", pd.to_datetime("2012-12-31"))

# Filter musim dan cuaca berdasarkan tanggal yang dipilih
filtered_day_df = day_df[
    (day_df["date"] >= str(date_start)) & (day_df["date"] <= str(date_end))
]
filtered_hour_df = hour_df[
    (hour_df["date"] >= str(date_start)) & (hour_df["date"] <= str(date_end))
]

season_options = sorted(filtered_day_df["season"].unique())
season_selected = st.sidebar.multiselect(
    "Pilih Musim:", season_options, default=season_options
)

weather_options = sorted(filtered_hour_df["weathersit"].unique())
weather_selected = st.sidebar.multiselect(
    "Pilih Cuaca:", weather_options, default=weather_options
)

time_range = st.sidebar.slider("Pilih Rentang Jam:", 0, 23, (0, 23))

# Apply Filters
if season_selected:
    filtered_day_df = filtered_day_df[filtered_day_df["season"].isin(season_selected)]
    filtered_hour_df = filtered_hour_df[
        filtered_hour_df["season"].isin(season_selected)
    ]
if weather_selected:
    filtered_hour_df = filtered_hour_df[
        filtered_hour_df["weathersit"].isin(weather_selected)
    ]

filtered_hour_df = filtered_hour_df[
    filtered_hour_df["hr"].between(time_range[0], time_range[1])
]

# New Visualization Tabs
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🔄 Perbandingan Cuaca",
        "⏳ Distribusi Waktu",
        "📅 Analisis Hari",
        "📊 Tren Penyewaan",
    ]
)

with tab1:
    st.subheader("🔄 Total Penyewaan Sepeda Berdasarkan Cuaca")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x="weathersit",
        y="cnt",
        data=filtered_hour_df,
        estimator=sum,
        palette="coolwarm",
        ax=ax,
    )
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Total Penyewa")
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Cuaca")
    st.pyplot(fig)

with tab2:
    st.subheader("⏳ Total Penyewaan Berdasarkan Jam")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xticks(range(0, 24))
    sns.lineplot(
        x="hr",
        y="cnt",
        data=filtered_hour_df,
        estimator=sum,
        marker="o",
        color="purple",
        ax=ax,
    )
    ax.set_xlabel("Jam dalam Sehari")
    ax.set_ylabel("Total Penyewa")
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Jam")
    st.pyplot(fig)

with tab3:
    st.subheader("📅 Total Penyewaan Berdasarkan Hari")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x="weekday",
        y="cnt",
        data=filtered_hour_df,
        estimator=sum,
        palette="viridis",
        ax=ax,
    )
    ax.set_xlabel("Hari dalam Seminggu")
    ax.set_ylabel("Total Penyewa")
    ax.set_title("Total Penyewaan Sepeda Berdasarkan Hari")
    st.pyplot(fig)

with tab4:
    st.subheader("📊 Tren Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        x="date",
        y="cnt",
        data=filtered_day_df,
        estimator=sum,
        marker="o",
        color="blue",
        ax=ax,
    )
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Total Penyewa")
    ax.set_title("Tren Penyewaan Sepeda dari Waktu ke Waktu")
    plt.xticks(rotation=45)
    st.pyplot(fig)
