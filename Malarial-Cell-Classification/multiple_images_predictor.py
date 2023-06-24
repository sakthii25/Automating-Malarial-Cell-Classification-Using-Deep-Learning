import streamlit as st
import numpy as np
import cv2
from keras.models import load_model

model = load_model("E:\projects\Malarial-Cell-Classification\model.h5")

def predict_multiple_images():

    st.title("Multiple Image Classifier ")

    files = st.file_uploader("Upload multiple images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    if st.button("Predict"):

        if files is not None and len(files) > 0:
            x = []
            for file in files:
                data = file.read()
                arr = np.frombuffer(data, np.uint8)
                img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
                img = cv2.resize(img, (150, 150))
                x.append(img)

            x = np.array(x)
            res = model.predict(x)
            # st.write(type(res))
            for i in np.nditer(res):
                if (np.isclose(i, 1)):
                    st.write("It is affected!")
                else:
                    st.write("It is not affected!")
            st.write("Number of Images:", len(x))

        else:
            st.error("Please upload at least one image.")

