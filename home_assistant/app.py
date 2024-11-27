import google.generativeai as genai
import os
import gradio as gr
import time
from google.api_core.exceptions import InvalidArgument
from home_assistant import set_light_values, intruder_alert, start_music, good_morning, set_thermostat_temperature, open_curtains

# Configure a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Criando um prompt inicial
initial_prompt = (
    "Você é um assistente virtual que pode controlar dispositivos domésticos. "
    "Você tem acesso a funções que controlam a casa da pessoa que está usando. "
    "Chame as funções quando achar que deve, mas nunca exponha o código delas. "
    "Assuma que a pessoa é amigável e ajude-a a entender o que aconteceu se algo der errado "
    "ou se você precisar de mais informações. Não esqueça de, de fato, chamar as funções."
)

# Escolha o modelo a ser usado
model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            tools=[set_light_values, intruder_alert, start_music, good_morning, set_thermostat_temperature, open_curtains],
            system_instruction=initial_prompt
        )

# Inicie um chat sem parâmetros iniciais
chat = model.start_chat(
    enable_automatic_function_calling=True
)


def gradio_wrapper(message, _history):
    try:
        response = chat.send_message(message)
    except InvalidArgument as e:
        response = chat.send_message(
            f"Ocorreu um erro: {e}. "
            "Por favor, verifique o comando e tente novamente."
        )
    return response.text
    
 
# Criando a interface do chat e passando a funcao gradio_wrapper
chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Home Assistant 🤖",
    multimodal=False
    )

# Inicie a interface
chat_interface.launch()