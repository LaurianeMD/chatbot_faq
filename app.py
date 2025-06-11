# app.py

import gradio as gr
from model import get_response  # importe ta fonction

def chatbot_interface(user_input):
    return get_response(user_input)

iface = gr.Interface(
    fn=chatbot_interface,
    inputs="text",
    outputs="text",
    title="💬 Chatbot FAQ - Jumia Sénégal",
    description="Posez une question liée aux paiements Jumia (ex : 'Quels sont les moyens de paiement ?')"
)

iface.launch(server_name="0.0.0.0", server_port=10000)

