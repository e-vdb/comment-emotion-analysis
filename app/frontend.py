import streamlit as st


# Set the app title
st.title("Emotion Analysis App")
st.write(
    "A simple machine learning app to predict the emotion from a user's comment."
)
# Declare a form to receive a comment
form = st.form(key="my_form")
review = form.text_input(label="Enter a comment describing your mood")
submit = form.form_submit_button(label="Make Prediction")