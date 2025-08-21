# app2.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA Agricultura", layout="wide")

st.title("🌱 Análisis Exploratorio de Datos Agrícolas")

# Cargar el dataset directamente
df = pd.read_csv("dataset_agricultura.csv")

st.subheader("📋 Vista previa del dataset")
st.dataframe(df.head())

st.subheader("📊 Información general")
st.write(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
st.write("Columnas del dataset:", list(df.columns))

# Estadísticas
st.subheader("📈 Estadísticas descriptivas")
st.write(df.describe())

# Tipos de datos y nulos
st.subheader("🔍 Tipos de datos y valores faltantes")
st.write(df.dtypes)
st.write(df.isnull().sum())

# Histogramas
st.subheader("📉 Distribución de variables numéricas")
columnas_numericas = df.select_dtypes(include=['float64','int64']).columns
for col in columnas_numericas:
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    ax.set_title(f"Distribución de {col}")
    st.pyplot(fig)

# Boxplots
st.subheader("📦 Detección de valores atípicos (Boxplots)")
for col in columnas_numericas:
    fig, ax = plt.subplots()
    sns.boxplot(x=df[col], ax=ax)
    ax.set_title(f"Boxplot de {col}")
    st.pyplot(fig)

# Correlación
st.subheader("🔗 Matriz de correlación")
corr = df.corr(numeric_only=True)

if corr.empty:
    st.warning("⚠️ No se pudo calcular la matriz de correlación (no hay suficientes columnas numéricas).")
else:
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

# Relación con el cultivo
if "Cultivo" in df.columns:
    st.subheader("🌾 Relación entre variables y tipo de cultivo")
    for col in columnas_numericas:
        fig, ax = plt.subplots()
        sns.boxplot(x="Cultivo", y=col, data=df, ax=ax)
        ax.set_title(f"{col} por tipo de Cultivo")
        st.pyplot(fig)
