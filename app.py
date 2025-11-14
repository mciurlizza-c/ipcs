import streamlit as st
import pandas as pd

# ============================================
# CONFIGURACIÓN DE PÁGINA
# ============================================
st.set_page_config(
    page_title="Análisis de Servicios",
    layout="wide"
)

st.title("🔍 Análisis de Servicios – CSV Viewer Inteligente")

# ============================================
# SUBIR ARCHIVO
# ============================================
uploaded_file = st.sidebar.file_uploader("📂 Cargar archivo CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, sep=";", encoding="latin1")
    except:
        df = pd.read_csv(uploaded_file, sep=";", encoding="ISO-8859-1")

    df.columns = [c.strip() for c in df.columns]

    # ============================================
    # PANEL DE BÚSQUEDA – SIDEBAR
    # ============================================
    st.sidebar.header("🔎 Buscador Inteligente")

    search_admin = st.sidebar.text_input("Buscar por últimos 10 dígitos del Administrative Number")
    search_circuit_number = st.sidebar.text_input("Circuit Number")
    search_wan_ipv4 = st.sidebar.text_input("Customer WAN IPv4 Address")
    search_asn = st.sidebar.text_input("Autonomous System")
    search_legal_name = st.sidebar.text_input("Customer Legal Name")
    search_nemonicne = st.sidebar.text_input("Nodo")

    # ============================================
    # FUNCIÓN DE FILTRO
    # ============================================
    def filter_data():
        filtered = df.copy()

        # FILTRO PRINCIPAL → últimos 10 dígitos
        if search_admin:
            filtered["Administrative number"] = filtered["Administrative number"].astype(str)
            filtered = filtered[
                filtered["Administrative number"].str[-10:] == search_admin
            ]

        # FILTROS SECUNDARIOS (solo si se ingresan)
        if search_circuit_number:
            filtered["Circuit Number"] = filtered["Circuit Number"].astype(str)
            filtered = filtered[
                filtered["Circuit Number"].str.contains(search_circuit_number, case=False, na=False)
            ]

        if search_wan_ipv4:
            filtered["Customer WAN IPv4 Address"] = filtered["Customer WAN IPv4 Address"].astype(str)
            filtered = filtered[
                filtered["Customer WAN IPv4 Address"].str.contains(search_wan_ipv4, na=False)
            ]

        if search_asn:
            filtered["Autonomous system"] = filtered["Autonomous system"].astype(str)
            filtered = filtered[
                filtered["Autonomous system"].str.contains(search_asn, na=False)
            ]

        if search_legal_name:
            filtered["Customer Legal Name"] = filtered["Customer Legal Name"].astype(str)
            filtered = filtered[
                filtered["Customer Legal Name"].str.contains(search_legal_name, case=False, na=False)
            ]

        if search_nemonicne:
            filtered["NEMONICNE"] = filtered["NEMONICNE"].astype(str)
            filtered = filtered[
                filtered["NEMONICNE"].str.contains(search_nemonicne, case=False, na=False)
            ]

        # ============================================
        # MOSTRAR SOLO LAS COLUMNAS SOLICITADAS
        # ============================================
        columnas_finales = [
            "Administrative number",
            "Customer Legal Name",
            "Customer WAN IPv4 Address",
            "Customer WAN IPv6 Address",
            "Autonomous system",
            "NEMONICNE",
            "Interface",
            "Circuit Number",
            "Building Owner"
        ]

        # Evitar error si falta alguna columna
        columnas_presentes = [col for col in columnas_finales if col in filtered.columns]

        return filtered[columnas_presentes]

    # ============================================
    # BOTÓN DE BÚSQUEDA
    # ============================================
    if st.sidebar.button("🔍 Buscar"):
        result = filter_data()

        st.subheader("📄 Resultados encontrados")
        st.write(f"Total de coincidencias: **{len(result)}**")

        if len(result) == 0:
            st.warning("No se encontraron resultados con los parámetros indicados.")
        else:
            st.dataframe(result, use_container_width=True)

    else:
        st.subheader("📄 Vista general del archivo (columnas filtradas)")
        columnas_finales = [
            "Administrative number",
            "Customer Legal Name",
            "Customer WAN IPv4 Address",
            "Customer WAN IPv6 Address",
            "Autonomous system",
            "NEMONICNE",
            "Interface",
            "Circuit Number",
            "Building Owner"
        ]
        columnas_presentes = [c for c in columnas_finales if c in df.columns]
        st.dataframe(df[columnas_presentes], use_container_width=True)

else:
    st.info("📌 Carga un archivo CSV para comenzar.")
