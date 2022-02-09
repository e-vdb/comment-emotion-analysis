import streamlit as st
from predictions import load_pickle, make_prediction
import sys
from streamlit import cli as stcli
from constants import CHOICES, EMOTION_ANALYSIS
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
        st.markdown("## Emotion analysis")
        st.write(EMOTION_ANALYSIS)

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

            print(self.choice)
            print(map_actions_to_callables)
            # Calls the chosen function with relevant arguments
            map_actions_to_callables[self.choice](*args[0])

    def get_comment(self, *args):
        # Declare a form to receive a comment
        st.write("A machine learning application that predicts the emotion from a user's comment.")
        with st.form('test'):
            self.comment = st.text_input(label="💬 How do you feel today?")
            if st.form_submit_button('Make prediction'):
                self.display_prediction()

    def display_prediction(self):
        output = make_prediction(self.ML_model, self.encoder, self.comment)
        # Display results of the NLP task
        st.header("Result")
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
