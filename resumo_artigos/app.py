import google.generativeai as genai
import os
import PyPDF2

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

with open("The PageRank Citation Ranking- Bringing Order to the Web.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    texto = ""
    for page in reader.pages:
        texto += page.extract_text()

prompt = f"Por favor, faça um resumo conciso do seguinte artigo científico:\n{texto}"

response = model.generate_content(prompt)

print("Resumo do Artigo Científico:")
print(response.text)