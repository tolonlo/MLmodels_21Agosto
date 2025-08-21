# 🚀 Modelos Supervisados de Machine Learning en Python con Streamlit

Este proyecto implementa modelos supervisados de *Machine Learning* (clasificación y regresión) en **Python**, y los despliega de forma interactiva con **Streamlit**.  
El objetivo es proporcionar una aplicación web sencilla donde el usuario pueda cargar datos, entrenar modelos y visualizar resultados directamente en su navegador.

---

## 📌 Características principales
- Entrenamiento de modelos supervisados:
  - **Regresión lineal**
  - **Regresión logística**
  - **Árboles de decisión**
  - **Random Forest**
  - **SVM**
- Carga de datasets en formato `.csv`.
- Preprocesamiento básico de datos (normalización, división train/test).
- Evaluación de métricas:
  - Para clasificación: *accuracy, precision, recall, f1-score, matriz de confusión.*
  - Para regresión: *RMSE, MAE, R².*
- Visualización interactiva de resultados.
- Despliegue con **Streamlit**.

---

## 🛠️ Tecnologías utilizadas
- [Python 3.9+](https://www.python.org/)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/) / [seaborn](https://seaborn.pydata.org/)
- [Streamlit](https://streamlit.io/)

---

## 📂 Estructura del proyecto
```bash
.
├── data/                 # Carpeta con datasets de ejemplo
├── models/               # Modelos entrenados (si se guardan con pickle/joblib)
├── app.py                # Aplicación principal de Streamlit
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
