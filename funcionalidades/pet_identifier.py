import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Obter o caminho absoluto para o arquivo
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "docs", "collie.png")

model = genai.GenerativeModel("gemini-1.5-flash")

# Verificar se o arquivo existe antes de tentar usá-lo
if not os.path.exists(file_path):
    raise FileNotFoundError(f"O arquivo não foi encontrado: {file_path}")

# Fazer upload do arquivo
image = genai.upload_file(path=file_path)

prompt = (
   "Identifique a raça do cachorro da foto e me dê duas ou três frases de informações a respeito dele. "
   "De preferência, alguma curiosidade interessante em português, citando a fonte da informação e sempre de um jeito leve e interessante."
)

response = model.generate_content([image, prompt])

print(response.text)