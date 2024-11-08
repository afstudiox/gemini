import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

file = "docs/collie.png"

dog = genai.upload_file(path=file)

prompt = (
   "Identifique a raça do cachorro da foto e me dê duas ou três frases de informações a respeito dele. "
   "De preferência, alguma curiosidade interessante em português, citando a fonte da informação e sempre de um jeito leve e interessante."
)

response = model.generate_content([dog, prompt])

print(response.text)