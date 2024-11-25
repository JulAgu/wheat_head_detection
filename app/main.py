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
        st.title("Compteur d'épis de blé 🌾- basée dans YoloV5")
        st.markdown("<h4 style='text-align: left; color: black;'>Service Agronomique - 12/2024</h4>", unsafe_allow_html=True)
    with col02:
        st.image("app/src/Logo_Agrial.png", width=200)

    uploaded_file = st.file_uploader("Sélectionnez l'image où vous souhaitez effectuer le comptage")
    comptage = False
    col1, col2, col3, col4, = st.columns([0.25, 0.25 ,0.25, 0.25])
    if uploaded_file is not None:
        with col2:
            with st.container():
                image = Image.open(uploaded_file)
                image.save("app/temp/original_image.png")
                specialImage = st.empty()
                specialImage.image(IMAGES[0], use_container_width=True)
        with col3:
            comptage = st.button("Compter", use_container_width=True)

    if comptage:
        nHeads = countWheatHeads("app/temp/original_image.png")
        specialImage.image(IMAGES[1], use_container_width=True)
        with col3:
            st.markdown(f"<p style='text-align: center; color: red; font-size: 30px;'>{nHeads} épis</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    #Create the two base images
    main()