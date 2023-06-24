import streamlit as st
import numpy as np
import cv2
from keras.models import load_model
from pdf import generate_pdf
import base64

#load the model
model = load_model("E:\projects\Malarial-Cell-Classification\model.h5")

def predict_single_image():
    st.title("Single Image Classifier")

    c1, c2 = st.columns(2)
    name = c1.text_input("Enter name ")
    age = c2.text_input("Enter age ")
    gender = c1.selectbox("Select your gender", ["Male", "Female", "Other"])
    date = c2.date_input("Enter date ")
    file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    desc = st.text_area("Description (optional):")
    # necessary input from user

    if file is not None:
        x = []
        data = file.read()  # convert the image into byte file
        arr = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)  # decode the image
        img = cv2.resize(img, (150, 150))

        x.append(img)
        x = np.array(x)

        res = model.predict(x)  # predict the output for the image

        result = round(res[0, 0])

        if (res == 1):
            test_result = "The given cell of the person is infected by malaria."
        else:
            test_result = "The given cell of the person is not infected by malaria."
        # After predict the output we generate the report pdf using FPDF

        if st.button("Generate PDF"):

            if (not name or not age):
                st.error("Please fill all the details.")

            else:
                pdf = generate_pdf(name, age, gender, date, test_result, desc)
                pdf_output = pdf.output(dest="S").encode("latin-1")

                # Display PDF
                st.header(f"Displaying PDF: {name}'s Test Report")

                # Convert PDF data to base64 for embedding
                pdf_base64 = base64.b64encode(pdf_output).decode("latin-1")
                pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500" frameborder="0"></iframe>'
                st.write(pdf_display, unsafe_allow_html=True)

                # Download PDF
                href = f'<a href="data:application/pdf;base64,{pdf_base64}" download="output.pdf">Download PDF</a>'
                st.markdown(href, unsafe_allow_html=True)
