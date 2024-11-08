import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

file = "docs/resume.txt"

with open(file, "r") as file:
    resume = file.read()

prompt = f"Aprimore o currículo para deixá-lo mais assertivo e enfatizando os pontos positivos.\n{resume}"

response = model.generate_content(prompt)

print(response.text)