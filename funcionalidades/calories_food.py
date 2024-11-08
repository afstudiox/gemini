import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

file = "docs/food.png"

food = genai.upload_file(path=file)

prompt = (
   "Identifique com cuidado o que é servido nesse prato e estime grosseiramente as suas calorias?"
)

response = model.generate_content([food, prompt])

print(response.text)