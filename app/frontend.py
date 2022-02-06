import streamlit as st
from predictions import load_pickle, make_prediction
import sys
from streamlit import cli as stcli

st.set_page_config(layout="wide")


class App:
    def __init__(self):
        self.ML_model = load_pickle('finalized_model.sav')
        self.encoder = load_pickle('encoder.pickle')

    def show(self):
        # Set the app title
        st.title("Emotion Analysis App")
        st.write(
            "A simple machine learning app to predict the emotion from a user's comment."
        )
        self.get_comment()

    def get_comment(self):
        # Declare a form to receive a comment
        with st.form('test'):
            self.comment = st.text_input(label="How do you feel today?")
            if st.form_submit_button('Make prediction'):
                self.display_prediction()

    def display_prediction(self):
        output = make_prediction(self.ML_model, self.encoder, self.comment)
        # Display results of the NLP task
        st.header("Results")
        st.write(output)
        filename = 'pictures/' + output + '.jpg'
        st.image(filename, use_column_width=False)


def main():
    front = App()
    front.show()


if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
