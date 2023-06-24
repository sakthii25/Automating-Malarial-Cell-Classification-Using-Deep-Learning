import streamlit as st
from single_image_predictor import predict_single_image
from multiple_images_predictor import predict_multiple_images

# Page navigation
choice = st.sidebar.selectbox('MCC', ['Home', 'Single image classifier', 'Multiple image classifier'])

if choice == "Home":
    st.title("Malarial Cell Classifier")

elif choice == "Single image classifier":
    predict_single_image()

else:
    predict_multiple_images()
