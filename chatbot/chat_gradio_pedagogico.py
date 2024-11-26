import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument
import os
import gradio as gr
import time
import fitz


# Função para extrair o texto da BNCC
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")  # Extrai o texto de cada página
    return text

# Função para carregar o conteúdo da BNCC e dividir em seções
def load_bncc_content(pdf_path):
    bncc_text = extract_text_from_pdf(pdf_path)
    # Aqui você pode dividir o texto em seções para facilitar a busca (exemplo simples de divisão por parágrafos)
    bncc_sections = bncc_text.split("\n\n")  # Cada bloco de texto separando por duas quebras de linha
    return bncc_sections

# Carregando o conteúdo da BNCC (insira o caminho do seu arquivo PDF aqui)
bncc_content = load_bncc_content("docs/BNCC.pdf")

# Configure a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Criando um prompt inicial com o conteúdo da BNCC
initial_prompt = (
    "Você é um assistente virtual para professores e pedagogos, ajudando a desenvolver planos de aula e auxílios pedagógicos. "
    "Você tem acesso ao conteúdo da Base Nacional Comum Curricular (BNCC) para fornecer informações relevantes e apoio. "
    "Por favor, use o conteúdo da BNCC para responder às questões dos professores e orientá-los conforme necessário. "
    "Caso precise, consulte as seções da BNCC para fornecer detalhes mais precisos."
)

# Função para pesquisar e incluir informações da BNCC no prompt
def search_bncc_content(query):
    # Busca simples no conteúdo da BNCC (aqui procuramos por palavras-chave na BNCC)
    results = []
    for section in bncc_content:
        if query.lower() in section.lower():  # Busca insensível a maiúsculas/minúsculas
            results.append(section)
    return "\n".join(results) if results else "Desculpe, não encontrei informações relacionadas a isso na BNCC."

# Ajustando o modelo para usar a BNCC
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=initial_prompt
)

# Inicie um chat sem parâmetros iniciais
chat = model.start_chat(
    enable_automatic_function_calling=True
)


# Função de wrapper para o Gradio
def gradio_wrapper(message, _history):
    query = message["text"]
    # Procura informações na BNCC
    bncc_info = search_bncc_content(query)
    # Criar o prompt com o conteúdo da BNCC para dar contexto à IA
    prompt = f"{initial_prompt}\n\nInformações da BNCC:\n{bncc_info}\n\nPergunta: {query}"
    
    try:
        response = chat.send_message(prompt)
    except InvalidArgument as e:
        response = chat.send_message(
            f"Ocorreu um erro: {e}. Por favor, verifique o comando e tente novamente."
        )
    
    return response.text

# Interface Gradio
chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Assistente Pedagógico com Suporte à BNCC",
    multimodal=True
)

# Iniciar a interface
chat_interface.launch()