import streamlit as st
import requests
import pandas as pd

API_URL = "http://10.43.101.108:8085/predict"

st.title("Modelo de Predicción del Tipo de Cobertura del Suelo")

url_fastapi = "http://10.43.101.108:8085/docs"
url_mlflow = "http://10.43.101.108:8084"
url_airflow = "http://10.43.101.108:8080"
url_minio = "http://10.43.101.108:8083"

col1, col2, col3 = st.columns(3)

with col1:
     elevation = st.number_input("Elevation", value=2596)
     aspect = st.number_input("Aspect", value=51)  
     slope = st.number_input("Slope", value=3)
     horizontal_distance_to_hydrology = st.number_input("Horizontal Distance To Hydrology", value=258)

with col2:
     vertical_distance_to_hydrology = st.number_input("Vertical Distance To Hydrology", value=0)
     horizontal_distance_to_roadways = st.number_input("Horizontal Distance To Roadways", value=510)
     hillshade_9am = st.number_input("Hillshade 9am", value=211)
     hillshade_noon = st.number_input("Hillshade Noon", value=232)

with col3:
     hillshade_3pm = st.number_input("Hillshade 3pm", value=148)
     horizontal_distance_to_fire_points = st.number_input("Horizontal Distance To Fire Points", value=6279)
     wilderness_area = st.text_input("Wilderness Area", value="Rawah")
     soil_type = st.text_input("Soil Type", value="C7745")

if st.button("Predecir"):
    input_dict = {
        "Elevation": elevation,
        "Aspect": aspect,
        "Slope": slope,
        "Horizontal_Distance_To_Hydrology": horizontal_distance_to_hydrology,
        "Vertical_Distance_To_Hydrology": vertical_distance_to_hydrology,
        "Horizontal_Distance_To_Roadways": horizontal_distance_to_roadways,
        "Hillshade_9am": hillshade_9am,
        "Hillshade_Noon": hillshade_noon,
        "Hillshade_3pm": hillshade_3pm,
        "Horizontal_Distance_To_Fire_Points": horizontal_distance_to_fire_points,
        "Wilderness_Area": wilderness_area,
        "Soil_Type": soil_type
    } 
    # Llamar a la API
    response = requests.post(API_URL, json=input_dict)
    
    if response.status_code == 200:
        prediction = response.json()["Prediction"]
        model_version = response.json()["Model Version"]
        st.success(f"La predicción es: {prediction}")
        st.write(f"Version del modelo: {model_version}")
    else:
        st.error("Error en la predicción")

# Sección de enlaces a herramientas
st.markdown("### Enlaces de aplicaciones o Herramientas a utilizar")
st.markdown(f"""
- **FastAPI Documentation**: [Acceder]({url_fastapi})
- **MLflow Tracking UI**: [Acceder]({url_mlflow})
- **Airflow Webserver**: [Acceder]({url_airflow})
- **MinIO Browser**: [Acceder]({url_minio})
""")