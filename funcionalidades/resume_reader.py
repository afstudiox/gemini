import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Obter o caminho absoluto para o arquivo
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "docs", "resume.txt")

model = genai.GenerativeModel("gemini-1.5-flash")

# Verificar se o arquivo existe antes de tentar usá-lo
if not os.path.exists(file_path):
    raise FileNotFoundError(f"O arquivo não foi encontrado: {file_path}")

with open(file_path, "r") as file:
    resume = file.read()

prompt = f"Aprimore o currículo para deixá-lo mais assertivo e enfatizando os pontos positivos.\n{resume}"

response = model.generate_content(prompt)

print(response.text)