import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

file = "docs/students_enem.csv"

students_spreadsheet = genai.upload_file(path=file, display_name="Notas do ENEM")

prompt = f"Gere um relatório de dois ou três parágrafos baseado nesses dados. Fale de tendências nos grupos de estudantes."

response = model.generate_content([students_spreadsheet, prompt])

print(response.text)