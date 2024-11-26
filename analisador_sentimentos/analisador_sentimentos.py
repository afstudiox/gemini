import google.generativeai as genai
import os
import gradio as gr

# Configurar a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Definir o prompt inicial para o analisador de sentimentos
initial_prompt = (
    "Você é um assistente que analisa o sentimento de textos fornecidos, "
    "identificando se o sentimento é positivo, negativo ou neutro, e fornecendo um breve feedback."
)

# Criar o modelo com o prompt inicial
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)

# Iniciar o chat
chat = model.start_chat()

def extract_file_contents(files):
    file_contents = []
    erros = []  # Lista para armazenar mensagens de erro

    for file_info in files:
        # import pdb; pdb.set_trace()
        file_path = file_info["path"]
        if file_info["mime_type"] == "text/plain":
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            file_contents.append(content)
        else:
            erros.append(f"Arquivo ignorado: {file_info['orig_name']} (tipo não suportado)")

    return file_contents, erros


def gradio_wrapper(message, _history):
    user_text = message["text"]
    files = message.get("files", [])
    file_contents, erros = extract_file_contents(files)
    combined_text = user_text + "\n\n" + "\n\n".join(file_contents)
    prompt = f"Analise o sentimento do seguinte texto:\n{combined_text}"
    response = chat.send_message(prompt)
    
    feedback_message = "Análise concluída com sucesso."
    if erros:
        feedback_message += "\n" + "\n".join(erros)
    
    return feedback_message + "\n\n" + response.text


chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Analisador de Sentimentos 🎭",
    multimodal=True
)
chat_interface.launch()