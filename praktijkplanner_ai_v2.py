import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Pagina-instellingen
st.set_page_config(page_title="PraktijkPlanner AI", layout="centered")

# Logo en header
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://i.imgur.com/3VQ5GXi.png" width="200">
        <h1 style="margin-bottom: 0.2em;">🦷 PraktijkPlanner AI</h1>
        <h4 style="color: gray;">Dental SpacePro – van idee naar succesvolle praktijk</h4>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)

# Intakeformulier
with st.form("intake_form"):
    st.markdown("### 📋 1. Praktijkinformatie")
    praktijk_type = st.selectbox("Type praktijk", ["Algemene tandartspraktijk", "Kindertandarts", "Implantologie"])

    st.markdown("### 🧮 2. Capaciteit")
    behandelkamers = st.number_input("Aantal behandelkamers", min_value=1, max_value=10, step=1)
    patienten_per_dag = st.number_input("Aantal patiënten per dag", min_value=1, max_value=200, step=1)

    st.markdown("### 📐 3. Afmetingen van de ruimte")
    lengte = st.number_input("Lengte (m)", min_value=1.0, max_value=100.0, step=0.5)
    breedte = st.number_input("Breedte (m)", min_value=1.0, max_value=100.0, step=0.5)
    oppervlakte = lengte * breedte
    st.info(f"Totale oppervlakte: {oppervlakte:.2f} m²")

    st.markdown("### 💶 4. Budget")
    budget = st.radio("Kies je budget", ["Onder €10.000", "€10.000 - €20.000", "Boven €20.000"])

    st.markdown("### 🎨 5. Stijlvoorkeur")
    stijl = st.selectbox("Welke uitstraling wil je?", ["Modern", "Functioneel", "Warm klassiek"])
