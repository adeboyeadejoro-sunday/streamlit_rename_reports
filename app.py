import streamlit as st
from datetime import datetime
from io import BytesIO

# Constants
TEST_OPTIONS = [
    "ICP", "Vitamins", "HM", "Pesticides", "Radioactivity", "Mibi", "Tryptophan",
    "Residualsolvents", "Chlorate", "PA", "Gluten", "ETO", "Aflatoxins", "Quercetin",
    "Selenium", "Iron", "Magnesium", "Aminoacids", "Catechins", "Actives", "PAH",
    "TA", "Mycotoxins", "Allergens", "Fattyacids", "Conformity", "GMO", "Cannabinoids",
    "MOH", "Microcystins", "ProteinContent"
]

st.title("📄 Labortest File Renamer")

# Step 1: File upload
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    # Step 2: Input fields
    sku = st.text_input("Enter SKU", max_chars=20)

    number = st.selectbox("Select Number", list(range(1, 10)))

    selected_tests = st.multiselect("Select Test Shorthands", TEST_OPTIONS)

    date_input = st.date_input("Select Date")

    if sku and selected_tests and date_input:
        # Step 3: Format the test shorthands
        if len(selected_tests) == 1:
            tests_str = selected_tests[0]
        elif len(selected_tests) == 2:
            tests_str = "$".join(selected_tests)
        else:
            tests_str = selected_tests[0] + "$@" + "$@".join(selected_tests[1:])

        # Step 4: Format the date
        date_str = date_input.strftime("%d.%m.%Y")

        # Step 5: Create new filename
        new_filename = f"{sku}_labortest_{number}_{tests_str}_{date_str}.pdf"

        st.markdown(f"### 🆕 New filename:\n`{new_filename}`")

        # Step 6: Download renamed file
        renamed_file = BytesIO(uploaded_file.read())
        st.download_button(
            label="📥 Download Renamed File",
            data=renamed_file,
            file_name=new_filename,
            mime="application/pdf"
        )
    else:
        st.info("Please fill all fields to generate the new filename.")
