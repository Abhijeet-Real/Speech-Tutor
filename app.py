import HuggingFaceLogin as HFL
import gen_QnA  
from tutor_conversation import tutor_conversation
from handle_custom_question import handle_custom_question
from ui import create_ui
from generate_interview_questions import generate_interview_questions
from history import save_history, load_history
HFL.login_to_huggingface()

# Create the UI and launch the app
app = create_ui(
    generate_question_and_answer=gen_QnA.generate_question_and_answer,
    tutor_conversation=tutor_conversation,
    generate_interview_questions=generate_interview_questions,
    load_history=load_history,
    save_history=save_history,
    handle_custom_question=handle_custom_question
)

if __name__ == "__main__":
    app.launch(server_port=7777, share=True)