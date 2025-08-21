# app2.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA Agricultura", layout="wide")

st.title("🌱 Análisis Exploratorio de Datos Agrícolas con Limpieza Automática")

# Cargar dataset
df = pd.read_csv("dataset_agricultura.csv")

st.subheader("📋 Vista previa inicial del dataset (sin limpiar)")
st.dataframe(df.head())

# --- Limpieza automática ---
st.subheader("🧹 Limpieza automática del dataset")

# Guardar tamaño inicial
filas_iniciales = df.shape[0]
columnas_iniciales = df.shape[1]

# Eliminar duplicados
duplicados = df.duplicated().sum()
df = df.drop_duplicates()

# Eliminar filas con todos los valores NaN
filas_nan_completas = df[df.isnull().all(axis=1)].shape[0]
df = df.dropna(how="all")

# Rellenar valores nulos en columnas numéricas con la media
nulos_por_col = df.isnull().sum()
cols_con_nulos = nulos_por_col[nulos_por_col > 0].index.tolist()
for col in cols_con_nulos:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna("Desconocido")

filas_finales = df.shape[0]
columnas_finales = df.shape[1]

# Mostrar resumen de la limpieza
st.write("✔️ Limpieza realizada:")
st.write(f"- Filas iniciales: {filas_iniciales}, Filas finales: {filas_finales}")
st.write(f"- Columnas iniciales: {columnas_iniciales}, Columnas finales: {columnas_finales}")
st.write(f"- Filas duplicadas eliminadas: {duplicados}")
st.write(f"- Filas con todos los valores NaN eliminadas: {filas_nan_completas}")
if cols_con_nulos:
    st.write(f"- Columnas con valores nulos tratados: {', '.join(cols_con_nulos)}")

st.subheader("📋 Vista previa después de limpieza")
st.dataframe(df.head())

# --- Análisis exploratorio ---
st.subheader("📊 Información general")
st.write(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
st.write("Columnas del dataset:", list(df.columns))

# Estadísticas
st.subheader("📈 Estadísticas descriptivas")
st.write(df.describe())

# Tipos de datos
st.subheader("🔍 Tipos de datos")
st.write(df.dtypes)

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
