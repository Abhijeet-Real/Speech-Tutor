import gradio as gr
from ui.rating_display import format_star_rating  # Import the function

def create_practice_tab(generate_question_and_answer, tutor_conversation, save_history):
    with gr.TabItem("Practice Speaking", id="practice"):
        with gr.Row():
            with gr.Column(scale=1):
                with gr.Box(style={"margin": "10px", "padding": "10px"}):
                    gr.Markdown("### Topic Selection")
                    topic_choice = gr.Radio(
                        ["Select from list", "Enter custom topic"], 
                        value="Select from list", 
                        label="Topic Input Mode"
                    )
                    topic_dropdown = gr.Dropdown(
                        choices=["Hobbies", "Travel", "Finance", "Technology", "Career Goals", 
                                 "Education", "Leadership", "Innovation", "Sustainability", 
                                 "Cultural Diversity", "Digital Transformation"],
                        label="Choose a Topic", 
                        visible=True
                    )
                    custom_topic_box = gr.Textbox(
                        label="Custom Topic", 
                        placeholder="Type any topic or question...", 
                        visible=False
                    )
                    
                    difficulty_selector = gr.Radio(
                        choices=["Easy", "Medium", "Hard"],
                        value="Medium",
                        label="Difficulty Level",
                        info="Select the complexity level of questions"
                    )
                    
                    model_selector = gr.Dropdown(
                        choices=[
                            "mistral-small3.1", "gemma3:27b", "qwq:latest", "llama3.2:latest",
                            "phi4-mini:latest", "qwen3:4b", "qwen3:32b", "llama2:latest", "mistral:latest"
                        ],
                        value="mistral:latest",
                        label="AI Model"
                    )
                    generate_btn = gr.Button("Generate Question", variant="primary")

                with gr.Box(style={"margin": "10px", "padding": "10px"}):
                    gr.Markdown("### Your Speaking Task")
                    question_box = gr.Textbox(label="Your Question", interactive=False, placeholder="Your question will appear here or type directly when custom topic is selected")
                    ideal_answer_box = gr.Textbox(label="Ideal Answer Reference", interactive=False, visible=False)
                    
                    audio_input = gr.Audio(source="microphone", type="filepath", label="Record Your Answer")
                    submit_btn = gr.Button("Analyze My Speech", variant="primary")

            with gr.Column(scale=1):
                with gr.Box(style={"margin": "10px", "padding": "10px"}):
                    gr.Markdown("### Performance Rating")
                    rating_display = gr.HTML(format_star_rating(0.0))  # Now this will work
                
                with gr.Accordion("Transcript", open=True):
                    transcript_output = gr.Textbox(label="What You Said")
                
                with gr.Accordion("Grammar Feedback", open=True):
                    grammar_output = gr.Textbox(label="Grammar Analysis")
                
                with gr.Accordion("Pronunciation Feedback", open=True):
                    feedback_output = gr.Textbox(label="Pronunciation Tips")
                
                with gr.Accordion("Content Evaluation", open=True):
                    comparison_output = gr.Textbox(label="Content Analysis")
                
                with gr.Accordion("Ideal Answer Reference", open=False):
                    ideal_answer_display = gr.Textbox(label="AI Reference Answer")

        # Add event handlers and logic for the practice tab here
        # ...
