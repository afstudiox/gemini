import google.generativeai as genai
import os
import gradio as gr

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

def gradio_wrapper(message, _history):
    
    # Extraia o texto da mensagem
    prompt = [message["text"]]
    
    # Lista para armazenar os arquivos uploadados
    uploaded_files = []
    
    # Iterar sobre cada arquivo recebido
    if message["files"]:
        for file_gradio_data in message["files"]:
            # Obter o caminho local do arquivo
            file_path = file_gradio_data["path"]
            # Fazer upload do arquivo para o Gemini
            uploaded_file_info = genai.upload_file(path=file_path)
            # Adicionar o arquivo uploadado à lista
            uploaded_files.append(uploaded_file_info)    
    
    # Envie o prompt para o chat e obtenha a resposta
    prompt.extend(uploaded_files)
    response = chat.send_message(prompt)
    return response.text
    
 

# Criando a interface do chat e passando a funcao gradio_wrapper
chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Chatbot com Suporte a Arquivos 🤖",
    multimodal=True
    )

# Inicie a interface
chat_interface.launch()