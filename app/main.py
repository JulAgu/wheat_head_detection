import os
import streamlit as st
from PIL import Image
from inference_module import countWheatHeads

st.set_page_config(
    page_title="Compteur d'épis de blé",
    page_icon="🌾",
    layout="wide",
    )

IMAGES = ["app/temp/original_image.png", "app/temp/annotated_image.png"]

def main():
    """
    The main function
    """
    # Main page
    col01, col02 = st.columns([0.8, 0.2], gap='medium')
    with col01:
        st.title("Compteur d'épis de blé 🌾")
        st.header("Une application basée dans YoloV5")
        st.subheader("Service Agronomique - 12/2024")
    with col02:
        st.image("app/src/Logo_Agrial.png", width=250)

    uploaded_file = st.file_uploader("Sélectionnez l'image où vous souhaitez effectuer le comptage")
    comptage = False
    col1, col2, col3 = st.columns([0.3, 0.35, 0.3])
    with col1:
        st.write("")
    with col2:
        with st.container():
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                image.save("app/temp/original_image.png")
                specialImage = st.empty()
                specialImage.image(IMAGES[0], caption="Image originale", use_container_width=True)
                st.write(image.size)
                comptage = st.button("Compter", use_container_width=True)
            else:
                st.markdown("<h3 style='text-align: center; color: black;'>Veuillez télecharger une image</h3>", unsafe_allow_html=True)
            
    with col3:
        st.write("")
    
    if comptage:
        nHeads = countWheatHeads("app/temp/original_image.png")
        specialImage.image(IMAGES[1], caption="Image annotée", use_container_width=True)
        with col2:
            st.markdown(f"<h3 style='text-align: center; color: red;'>{nHeads} épis</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    #Create the two base images
    main()