# Qlik CSV Analyzer – Streamlit App

Aplicación en **Streamlit** diseñada para cargar archivos `.csv` exportados desde Qlik, analizarlos y mostrar información filtrada mediante un panel de búsqueda.

## 🚀 Funcionalidades
- Carga de archivos CSV (separador `;`).
- Filtrado inteligente según:
  - Últimos 10 dígitos del Administrative Number
  - Customer Legal Name
  - Customer WAN IPv4 Address
  - Autonomous System
  - Circuit Number
- Visualización inmediata de resultados.
- Uso totalmente privado mediante Streamlit Cloud.

## 📌 Tecnología utilizada
- Python 3.9+
- Streamlit
- Pandas
- (Opcional) AWS S3 para almacenamiento seguro de CSV

## 🔒 Seguridad & Privacidad
- El repositorio es **privado**.
- Los CSV **no se suben al repositorio** (gracias al `.gitignore`).
- Las credenciales (ej. AWS) se deben almacenar en Streamlit Secrets.

## ▶ Ejecutar localmente
pip install -r requirements.txt
streamlit run app.py
