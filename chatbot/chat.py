import google.generativeai as genai
import os

# Configure a chave de API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Escolha o modelo a ser usado
model = genai.GenerativeModel("gemini-1.5-flash")

# Inicie um chat sem parâmetros iniciais
chat = model.start_chat()

# Envie uma mensagem para o chat
response = chat.send_message("Bom dia? Como você está? Me diga algo sobre você.")
# Exiba a resposta
print(response.text)