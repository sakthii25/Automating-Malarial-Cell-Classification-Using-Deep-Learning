import streamlit as st
from fpdf import FPDF
import base64


# Function to generate the PDF
def generate_pdf(name, age, gender, date, result):
    pdf = FPDF()
    pdf.add_page()

    # Add content to the PDF
    pdf.set_font("Arial", size=24, style="B")  # Set font and size for the title
    pdf.cell(0, 30, txt="Malarial Cell Classification Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(0, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(0, 10, txt=f"Gender: {gender}", ln=True)
    pdf.cell(0, 10, txt=f"Date: {date}",ln=True)
    pdf.cell(0, 10, txt=f"Test Results: {result}", ln=True)
    return pdf