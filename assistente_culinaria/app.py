import google.generativeai as genai
import os
import gradio as gr

# Configurar a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Definir o prompt inicial para o assistente de receitas
initial_prompt = (
    "Você é um assistente de receitas culinárias. Você fornece receitas baseadas nos ingredientes fornecidos, "
    "dá dicas de culinária e responde a perguntas sobre preparação de pratos."
)

# Criar o modelo com o prompt inicial
model = genai.GenerativeModel("gemini-1.5-flash",
                              system_instruction=initial_prompt)

# Iniciar o chat
chat = model.start_chat()

# Definir a função de interação com o Gradio
def gradio_wrapper(message, _history):
    
    # Enviar a mensagem para o chat e obter a resposta
    response = chat.send_message(message)
    return response.text

# Criar e lançar a interface do chat com um título personalizado
chat_interface = gr.ChatInterface(gradio_wrapper, title="Assistente de Receitas Culinárias 🍳")
chat_interface.launch()