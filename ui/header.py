import gradio as gr

def create_header():
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
