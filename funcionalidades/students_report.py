import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Obter o caminho absoluto para o arquivo
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "docs", "students_enem.csv")

model = genai.GenerativeModel("gemini-1.5-flash")

# Verificar se o arquivo existe antes de tentar usá-lo
if not os.path.exists(file_path):
    raise FileNotFoundError(f"O arquivo não foi encontrado: {file_path}")

students_spreadsheet = genai.upload_file(path=file_path, display_name="Notas do ENEM")

prompt = f"Gere um relatório de dois ou três parágrafos baseado nesses dados. Fale de tendências nos grupos de estudantes."

response = model.generate_content([students_spreadsheet, prompt])

print(response.text)