import google.generativeai as genai
import os
import gradio as gr
import time
from google.api_core.exceptions import InvalidArgument
from home_assistant import set_light_values, intruder_alert, start_music, good_morning

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
            tools=[set_light_values, intruder_alert, start_music, good_morning],
            system_instruction=initial_prompt
        )

# Inicie um chat sem parâmetros iniciais
chat = model.start_chat(
    enable_automatic_function_calling=True
)


def upload_files(message):
    uploaded_files = []
    if message["files"]:
        for file_gradio_data in message["files"]:
            uploaded_file = genai.upload_file(path=file_gradio_data["path"])
            while uploaded_file.state.name == "PROCESSING":
               time.sleep(5)
               uploaded_file = genai.get_file(uploaded_file.name)
            uploaded_files.append(uploaded_file)
    return uploaded_files


def assemble_prompt(message):
   prompt = [message["text"]]
   uploaded_files = upload_files(message)
   prompt.extend(uploaded_files)
   return prompt

def gradio_wrapper(message, _history):
    prompt = assemble_prompt(message)
    try:
        response = chat.send_message(prompt)
    except InvalidArgument as e:
        response = chat.send_message(
            f"Ocorreu um erro: {e}. "
            "Por favor, verifique o comando e tente novamente."
        )
    return response.text
    
 
# Criando a interface do chat e passando a funcao gradio_wrapper
chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Chatbot com Suporte a Arquivos 🤖",
    multimodal=True
    )

# Inicie a interface
chat_interface.launch()