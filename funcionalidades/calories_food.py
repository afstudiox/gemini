import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Obter o caminho absoluto para o arquivo
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "docs", "food.png")

model = genai.GenerativeModel("gemini-1.5-flash")

# Verificar se o arquivo existe antes de tentar usá-lo
if not os.path.exists(file_path):
    raise FileNotFoundError(f"O arquivo não foi encontrado: {file_path}")

# Fazer upload do arquivo
image = genai.upload_file(path=file_path)

prompt = (
   "Identifique com cuidado o que é servido nesse prato e estime grosseiramente as suas calorias?"
)

response = model.generate_content([image, prompt])

print(response.text)