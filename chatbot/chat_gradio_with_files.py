import google.generativeai as genai
import os
import gradio as gr
import time
from google.api_core.exceptions import InvalidArgument

# Configure a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Criando um prompt inicial
initial_prompt = (
   "Você é um assistente virtual capaz de processar arquivos como imagens, textos e outros tipos. "
   "Sempre que alguém perguntar sobre um arquivo, verifique o histórico para encontrar o arquivo correspondente. "
   "Não diga que não é capaz de processar arquivos, pois você é."
)

# Escolha o modelo a ser usado
model = genai.GenerativeModel("gemini-1.5-flash",system_instruction=initial_prompt)

# Inicie um chat sem parâmetros iniciais
chat = model.start_chat()

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
            f"O usuário te enviou um arquivo para você ler e obteve o erro: {e}."
             "Pode explicar o que houve e dizer quais tipos de arquivos você "
             "dá suporte? Assuma que a pessoa não sabe programação e "
             "não quer ver o erro original. Explique de forma simples e concisa."
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