import streamlit as st
from predictions import load_pickle, make_prediction

ML_model = load_pickle('app/finalized_model.sav')
encoder = load_pickle('app/encoder.pickle')

# Set the app title
st.title("Emotion Analysis App")
st.write(
    "A simple machine learning app to predict the emotion from a user's comment."
)
# Declare a form to receive a comment
form = st.form(key="my_form")
comment = form.text_input(label="Enter a comment describing your mood")
submit = form.form_submit_button(label="Make Prediction")
if submit:
    output = make_prediction(ML_model, encoder, comment)
    # Display results of the NLP task
    st.header("Results")
    st.write(output)
    filename = 'app/pictures/' + output + '.jpg'
    st.image(filename)