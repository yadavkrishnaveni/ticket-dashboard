import streamlit as st
import pickle

st.title("Ticket Category Predictor")

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Text input
user_input = st.text_area("Enter ticket description:")

if st.button("Predict"):
    if user_input:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        st.success(f"Predicted Category: {prediction}")
                # Priority Logic
        text = user_input.lower()
        if "crash" in text or "down" in text or "urgent" in text or "not working" in text:
            priority = "High"
        elif "billing" in text or "invoice" in text or "payment" in text or "refund" in text:
            priority = "Medium"
        else:
            priority = "Low"
        
        st.info(f"Predicted Priority: {priority}")
    else:
        st.warning("Please enter a ticket description")