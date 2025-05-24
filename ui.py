import gradio as gr
import random
from pathlib import Path
from format_star_rating import format_star_rating
from create_custom_theme import create_custom_theme
from calculate_rating import calculate_rating 


def create_ui(generate_question_and_answer, tutor_conversation, generate_interview_questions, load_history, save_history, handle_custom_question=None):
    with gr.Blocks(title="VaakShakti AI | Sanskrit-Inspired Speech Mastery", theme=create_custom_theme()) as app:
        # User ID for history tracking (simple implementation)
        user_id = gr.State(value=f"user_{random.randint(1000, 9999)}")
        current_topic = gr.State(value="")
        
        # Header with logo and tagline
        gr.HTML("""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
            <img src="https://via.placeholder.com/80" alt="AI Logo" style="height: 80px; margin-right: 20px;">
            <div>
                <h1 style="text-align:center; font-size: 2.8em; background: linear-gradient(to right, #4F46E5, #2563EB); -webkit-background-clip: text; color: transparent; margin-bottom: 0;">VaakShakti AI</h1>
                <h3 style="text-align:center; margin-top: 5px; color: #475569; font-weight: 400;">Sanskrit-Inspired AI for Mastering the Art of Speech</h3>
            </div>
        </div>
        <div style="text-align: center; margin-bottom: 20px; padding: 10px; background: rgba(255, 255, 255, 0.7); border-radius: 10px;">
            <p style="margin: 0; color: #475569; font-style: italic;">"वाक्शक्ति (VaakShakti): The divine power of speech that transforms knowledge into wisdom"</p>
        </div>
        """)

        # Tabs for different features
        with gr.Tabs() as tabs:
            # Practice Tab
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
                            rating_display = gr.HTML(format_star_rating(0.0))
                        
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

            # Interview Prep Tab
            with gr.TabItem("Interview Preparation", id="interview"):
                with gr.Row():
                    with gr.Column(scale=1):
                        interview_topic = gr.Textbox(label="Interview Topic/Position", placeholder="e.g., Software Engineer, Data Scientist, Marketing Manager")
                        personality_traits = gr.Textbox(label="Your Personality Traits", placeholder="e.g., analytical, creative, detail-oriented, team player")
                        technical_skills = gr.Textbox(label="Your Technical Skills", placeholder="e.g., Python, SQL, data analysis, project management")
                        interview_model = gr.Dropdown(
                            choices=["mistral:latest", "llama3.2:latest", "qwen3:32b"],
                            value="mistral:latest",
                            label="AI Model"
                        )
                        generate_interview_btn = gr.Button("Generate Interview Questions", variant="primary")
                    
                    with gr.Column(scale=1):
                        interview_questions = gr.Markdown("Your interview questions will appear here...")

            # History Tab
            with gr.TabItem("Your History", id="history"):
                with gr.Row():
                    with gr.Column(scale=1):
                        refresh_history_btn = gr.Button("Refresh History", variant="secondary")
                        history_display = gr.Markdown("Your practice history will appear here...")

        # States for tracking
        question_state = gr.State()
        ideal_answer_state = gr.State()
        difficulty_state = gr.State()
        rating_state = gr.State(0.0)

        # Event handlers
        topic_choice.change(
            fn=lambda mode: (
                gr.update(visible=(mode == "Select from list")), 
                gr.update(visible=(mode == "Enter custom topic")),
                gr.update(interactive=(mode == "Enter custom topic"))
            ),
            inputs=topic_choice,
            outputs=[topic_dropdown, custom_topic_box, question_box]
        )
        
        # Auto-copy custom topic to question field
        custom_topic_box.change(
            fn=lambda text: gr.update(value=text),
            inputs=custom_topic_box,
            outputs=question_box
        )

        # Generate question flow
        def update_current_topic(choice_mode, dropdown_value, custom_value):
            topic = custom_value.strip() if choice_mode == "Enter custom topic" and custom_value else dropdown_value
            return topic, topic
        
        # Use the provided handle_custom_question function if available, otherwise use local implementation
        def handle_question_generation(choice_mode, current_question, topic, difficulty, model):
            if handle_custom_question:
                return handle_custom_question(choice_mode, current_question, topic, difficulty, model)
            else:
                # Fallback to local implementation if not provided
                if choice_mode == "Enter custom topic" and current_question.strip():
                    return current_question, "This is a custom question. No ideal answer reference is available."
                else:
                    return generate_question_and_answer(topic, difficulty, model)
        
        generate_btn.click(
            fn=update_current_topic,
            inputs=[topic_choice, topic_dropdown, custom_topic_box],
            outputs=[custom_topic_box, current_topic]
        ).then(
            fn=handle_question_generation,
            inputs=[topic_choice, question_box, custom_topic_box, difficulty_selector, model_selector],
            outputs=[question_box, ideal_answer_box]
        ).then(
            lambda q, a, d: (q, a, d),
            inputs=[question_box, ideal_answer_box, difficulty_selector],
            outputs=[question_state, ideal_answer_state, difficulty_state]
        ).then(
            lambda: gr.update(visible=False),
            inputs=None,
            outputs=ideal_answer_box
        ).then(
            lambda a: a,
            inputs=ideal_answer_box,
            outputs=ideal_answer_display
        )

        # Enhanced tutor conversation with rating
        def enhanced_tutor_conversation(audio, question, ideal_answer, difficulty, model, user_id, topic):
            if not audio:
                return "No audio received", "", "", "", ideal_answer, 0.0, format_star_rating(0.0)

            transcript, grammar_output, feedback_output, comparison = tutor_conversation(audio, question, ideal_answer, difficulty, model)
            
            # Calculate rating
            rating = calculate_rating(transcript, grammar_output, feedback_output, comparison)
            
            # Save history
            save_history(user_id, topic, difficulty, question, transcript, grammar_output, feedback_output, comparison, rating)
            
            return transcript, grammar_output, feedback_output, comparison, ideal_answer, rating, format_star_rating(rating)

        submit_btn.click(
            enhanced_tutor_conversation,
            inputs=[audio_input, question_state, ideal_answer_state, difficulty_state, model_selector, user_id, current_topic],
            outputs=[transcript_output, grammar_output, feedback_output, comparison_output, ideal_answer_box, rating_state, rating_display]
        ).then(
            lambda a: a,
            inputs=ideal_answer_box,
            outputs=ideal_answer_display
        )

        # Interview questions generation
        def format_interview_questions(topic, personality, skills, model):
            if not topic or not personality or not skills:
                return "Please fill in all fields to generate interview questions."
            
            questions = generate_interview_questions(topic, personality, skills, model)
            
            # Format the response with Markdown for better readability
            formatted = f"## Interview Questions for: {topic}\n\n"
            formatted += questions
            
            return formatted

        generate_interview_btn.click(
            fn=format_interview_questions,
            inputs=[interview_topic, personality_traits, technical_skills, interview_model],
            outputs=interview_questions
        )

        # History display
        def format_history(user_id):
            history = load_history(user_id)
            if not history["sessions"]:
                return "You haven't completed any practice sessions yet."
            
            sessions = history["sessions"]
            sessions.reverse()  # Most recent first
            
            formatted = "# Your Practice History\n\n"
            
            for i, session in enumerate(sessions[:10]):  # Show last 10 sessions
                formatted += f"## Session {i+1}: {session['timestamp']}\n"
                formatted += f"**Topic:** {session['topic']} | **Difficulty:** {session['difficulty']}\n"
                formatted += f"**Rating:** {session['rating']}/5.0 stars\n"
                formatted += f"**Question:** {session['question']}\n"
                formatted += f"**Your Answer:** {session['transcript'][:100]}...\n"
                formatted += f"**Key Feedback:** {session['grammar_feedback'][:100]}...\n\n"
                formatted += "---\n\n"
            
            if len(sessions) > 10:
                formatted += f"*{len(sessions) - 10} more sessions not shown*"
            
            return formatted

        refresh_history_btn.click(
            fn=format_history,
            inputs=user_id,
            outputs=history_display
        )

        # Initialize history on load
        app.load(
            fn=format_history,
            inputs=user_id,
            outputs=history_display
        )

    return app
