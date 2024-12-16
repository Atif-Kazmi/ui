import streamlit as st

# Title and Description
st.title("Healthcare Chatbot")
st.write("""
This chatbot helps you by taking symptoms as input and providing possible diagnoses 
along with suggested medicines. Please note that this is for informational purposes only and not a substitute for professional medical advice.
""")

# Symptom-Disease-Medicine Mapping (Predefined Data)
symptom_disease_medicine = {
    "fever": {"disease": "Flu", "medicines": ["Paracetamol", "Ibuprofen"]},
    "cough": {"disease": "Common Cold", "medicines": ["Cough Syrup", "Honey"]},
    "headache": {"disease": "Migraine", "medicines": ["Aspirin", "Ibuprofen"]},
    "runny nose": {"disease": "Allergy", "medicines": ["Antihistamines", "Decongestants"]},
    "chest pain": {"disease": "Angina", "medicines": ["Nitroglycerin", "Aspirin"]},
    "sore throat": {"disease": "Strep Throat", "medicines": ["Amoxicillin", "Ibuprofen"]},
}

# User Input
symptoms = st.text_input("Enter your symptoms (comma-separated, e.g., 'fever, cough'):")

if st.button("Diagnose"):
    if symptoms:
        # Process symptoms
        input_symptoms = [s.strip().lower() for s in symptoms.split(",")]
        diagnosis = []
        medicines = []

        # Match symptoms with data
        for symptom in input_symptoms:
            if symptom in symptom_disease_medicine:
                diagnosis.append(symptom_disease_medicine[symptom]["disease"])
                medicines.extend(symptom_disease_medicine[symptom]["medicines"])
        
        # Display Results
        if diagnosis:
            st.subheader("Possible Diagnosis:")
            st.write(", ".join(set(diagnosis)))

            st.subheader("Suggested Medicines:")
            st.write(", ".join(set(medicines)))
        else:
            st.warning("No matching diagnosis found. Please consult a healthcare professional.")
    else:
        st.warning("Please enter your symptoms!")

# Footer Disclaimer
st.write("---")
st.write("**Disclaimer:** This chatbot is for informational purposes only. Always consult a healthcare professional for medical advice.")
