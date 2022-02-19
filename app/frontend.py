import streamlit as st
from predictions import load_pickle, make_prediction
import sys
from streamlit import cli as stcli
from constants import CHOICES, EMOTION_ANALYSIS, LICENCE
st.set_page_config(layout="wide")


class App:
    def __init__(self):
        self.ML_model = load_pickle('finalized_model.sav')
        self.encoder = load_pickle('encoder.pickle')
        self.comment = ""


    def choose(self) -> None:
        """Display the different possible actions."""
        self.choice = st.sidebar.selectbox(
            label="What would you like to do?",
            options=CHOICES,
            help="You need to select what you'd like the application to do.",
        )

    def display_info(self):
        st.markdown(EMOTION_ANALYSIS)
        st.markdown(LICENCE)

    def show(self):
        # Set the app title
        st.title("Streamlit demo ")
        st.write(
            "A basic demo of streamlit web application "
        )
        self.choose()
        if self.choice is not None:
            callables = [self.display_info, self.get_comment]

            args = [[], []]
            possible_choices = CHOICES[1:]
            map_actions_to_callables = dict(zip(possible_choices, callables))

            # Calls the chosen function with relevant arguments
            map_actions_to_callables[self.choice](*args[0])

    def get_comment(self, *args):
        # Declare a form to receive a comment
        st.write("A machine learning application that predicts the emotion from a user's comment.")

        with st.form('test', clear_on_submit=True):
            self.comment = st.text_input(label="💬 How do you feel today?")
            submit = st.form_submit_button(' 👉 Make prediction')
        if submit:
            if self.comment == "":
                st.warning("Please enter a comment before submit")
            else:
                self.display_prediction()
        self.collect_contribution()

    def display_prediction(self):
        self.output = make_prediction(self.ML_model, self.encoder, self.comment)
        # Display results of the NLP task
        st.header("Result")
        st.write(self.output)
        filename = 'pictures/' + self.output + '.jpg'
        st.image(filename, use_column_width=False)
        st.session_state.output = self.output

    def collect_contribution(self):
        if 'output' in st.session_state:
            st.write("Contribute to improve the model's performances")
            true_feeling = st.selectbox(label="Which feeling was the most relevant?",
                             options=['sadness', 'joy', 'love', 'anger', 'surprised', 'fear'])
            row = {'Comment': self.comment, 'Prediction': st.session_state.output, 'True': true_feeling}
            button = st.button('submit')
            if button:
                st.write(row)
                del st.session_state['output']
                st.success("Thanks for your contribution!")



def main():
    front = App()
    front.show()


if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
