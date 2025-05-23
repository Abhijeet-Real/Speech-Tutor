import gradio as gr
from ui.theme import create_custom_theme
from ui.header import create_header
from ui.practice_tab import create_practice_tab
from ui.interview_tab import create_interview_tab
from ui.history_tab import create_history_tab

def create_ui(generate_question_and_answer, tutor_conversation, generate_interview_questions, load_history, save_history):
    with gr.Blocks(title="VaakShakti AI | Sanskrit-Inspired Speech Mastery", theme=create_custom_theme()) as app:
        create_header()
        create_practice_tab(generate_question_and_answer, tutor_conversation, save_history)
        create_interview_tab(generate_interview_questions)
        create_history_tab(load_history)
    return app
