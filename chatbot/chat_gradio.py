import google.generativeai as genai
import os
import gradio as gr

# Configure a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Escolha o modelo a ser usado
model = genai.GenerativeModel("gemini-1.5-flash")

# Inicie um chat sem parâmetros iniciais
chat = model.start_chat()

def gradio_wrapper(message, _history):
    #Envie mensagem para o chat e obtenha a resposta
    #O gradio pega a mensagem digitada no browser por quem o usa e o entrega para essa funcao
    response = chat.send_message(message)
    return response.text

# Criando a interface do chat e passando a funcao gradio_wrapper
chat_interface = gr.ChatInterface(gradio_wrapper)

# Inicie a interface
chat_interface.launch()