import google.generativeai as genai
import os

# Configure a chave de API
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Criar o modelo com o prompt inicial
model = genai.GenerativeModel('gemini-1.5-flash')

# Ler o texto em português
with open("tradutor/portuguese_text.txt", "r", encoding="utf-8") as file:
    texto_portugues = file.read()

# Definir o prompt para o modelo
prompt = f"Por favor, traduza o seguinte texto para o inglês:\n{texto_portugues}"

# Gerar a tradução
response = model.generate_content(prompt)

# Salvar a tradução em um arquivo
with open("tradutor/english_text.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

# Imprimir uma mensagem de conclusão
print("Tradução concluída e salva em 'english_text.txt'.")