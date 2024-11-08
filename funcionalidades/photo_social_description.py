import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

file = "docs/viagem.png"

image = genai.upload_file(path=file)

prompt = (
   "Gere uma descrição dessa imagem para o Instagram. Fale na primeira pessoa e insira emojis e hashtags. "
)

response = model.generate_content([image, prompt])

print(response.text)