import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# ===============================
# 1. CONFIGURACIÓN BÁSICA
# ===============================
st.set_page_config(page_title="EDA Deportivo", layout="wide")

st.title("🏅 Exploración de Datos Deportivos (EDA) con Streamlit")
st.markdown("Genera un conjunto de datos **sintético** sobre deportes y realiza un **EDA interactivo**.")

# ===============================
# 2. CREACIÓN DE DATOS SINTÉTICOS
# ===============================
def generar_datos(n_muestras, n_columnas):
    np.random.seed(42)
    deportes = ["Fútbol", "Baloncesto", "Tenis", "Natación", "Ciclismo", "Atletismo"]
    paises = ["Colombia", "Brasil", "EE.UU.", "España", "Argentina", "Francia"]

    data = {
        "Deporte": np.random.choice(deportes, n_muestras),
        "País": np.random.choice(paises, n_muestras),
        "Edad": np.random.randint(15, 40, n_muestras),
        "Altura_cm": np.random.normal(175, 10, n_muestras).astype(int),
        "Peso_kg": np.random.normal(70, 15, n_muestras).astype(int),
        "Puntaje": np.random.randint(0, 100, n_muestras),
    }

    df = pd.DataFrame(data)
    return df.iloc[:, :n_columnas]

# ===============================
# 3. CONTROLES DE USUARIO
# ===============================
st.sidebar.header("⚙️ Configuración de datos")

n_muestras = st.sidebar.slider("Número de muestras", min_value=50, max_value=500, value=200, step=50)
n_columnas = st.sidebar.slider("Número de columnas", min_value=2, max_value=6, value=4)

df = generar_datos(n_muestras, n_columnas)

# Selección de columnas
columnas = st.multiselect("Selecciona columnas a mostrar:", df.columns.tolist(), default=df.columns.tolist())
df_filtrado = df[columnas]

st.subheader("📊 Vista de la Tabla de Datos")
st.dataframe(df_filtrado)

# ===============================
# 4. ANÁLISIS DESCRIPTIVO
# ===============================
st.subheader("📈 Análisis Exploratorio")

st.write("**Estadísticas descriptivas (para variables numéricas):**")
st.write(df_filtrado.describe())

# ===============================
# 5. VISUALIZACIONES
# ===============================
st.subheader("🎨 Visualización de Datos")

tipo_grafico = st.selectbox(
    "Selecciona el tipo de gráfico",
    ["Histograma", "Barras", "Dispersión", "Tendencia (Línea)", "Pastel"]
)

col1, col2 = st.columns(2)

with col1:
    x_axis = st.selectbox("Eje X", columnas)
with col2:
    y_axis = st.selectbox("Eje Y (si aplica)", columnas)

fig, ax = plt.subplots(figsize=(8, 5))

if tipo_grafico == "Histograma":
    if pd.api.types.is_numeric_dtype(df_filtrado[x_axis]):
        sns.histplot(df_filtrado[x_axis], bins=20, kde=True, ax=ax)
        ax.set_title(f"Histograma de {x_axis}")
    else:
        st.warning("Selecciona una variable numérica para el histograma.")

elif tipo_grafico == "Barras":
    sns.countplot(x=x_axis, data=df_filtrado, ax=ax)
    ax.set_title(f"Gráfico de Barras de {x_axis}")

elif tipo_grafico == "Dispersión":
    if pd.api.types.is_numeric_dtype(df_filtrado[x_axis]) and pd.api.types.is_numeric_dtype(df_filtrado[y_axis]):
        sns.scatterplot(x=x_axis, y=y_axis, data=df_filtrado, ax=ax)
        ax.set_title(f"Diagrama de Dispersión {x_axis} vs {y_axis}")
    else:
        st.warning("Selecciona dos variables numéricas para dispersión.")

elif tipo_grafico == "Tendencia (Línea)":
    if pd.api.types.is_numeric_dtype(df_filtrado[x_axis]) and pd.api.types.is_numeric_dtype(df_filtrado[y_axis]):
        sns.lineplot(x=x_axis, y=y_axis, data=df_filtrado, ax=ax)
        ax.set_title(f"Gráfico de Tendencia {x_axis} vs {y_axis}")
    else:
        st.warning("Selecciona dos variables numéricas para tendencia.")

elif tipo_grafico == "Pastel":
    if df_filtrado[x_axis].nunique() < 10:  # Para no saturar
        df_filtrado[x_axis].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        ax.set_title(f"Gráfico de Pastel: {x_axis}")
    else:
        st.warning("Demasiadas categorías para pastel. Escoge una variable categórica con menos valores únicos.")

st.pyplot(fig)

# ===============================
# 6. FOOTER
# ===============================
st.markdown("---")
st.markdown("✅ Desarrollado para práctica de **EDA en Streamlit** con datos sintéticos deportivos.")
