import google.generativeai as genai
import os
import markdown

from flask import Flask, render_template
from user_data import get_user_history
from book_recommendations import (
    recommend_fiction,
    recommend_non_fiction,
    recommend_science,
    recommend_technology
)

app = Flask(__name__)

# Configurar a chave de API
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Definir o modelo generativo com as funções disponíveis
magical_if = genai.GenerativeModel(
    "gemini-1.5-flash",
    tools=[
        recommend_fiction,
        recommend_non_fiction,
        recommend_science,
        recommend_technology
    ]
)


def ia_decision(user_id, history):
    business_rules = """
    1. Analise o histórico de compras do usuário e decida qual função chamar baseado na categoria que ele mais comprou.
    2. Retorne diretamente uma mensagem formatada em Markdown que possa ser exibida para o usuário.
    3. Não acrecente nenhuma formatação ou conteúdo adicional ao texto retornado pela IA.
    """

    # Inicia o chat com a IA
    user_decision = magical_if.start_chat(enable_automatic_function_calling=True)

    # Envia os dados e as regras de negócio para a IA
    response = user_decision.send_message(
        f"Histórico do usuário {user_id}: {history}; Regras de negócio: {business_rules}"
    )

    try:
        # Extrair e converter Markdown para HTML
        markdown_response = response.candidates[0].content.parts[0].text.strip()
        html_response = markdown.markdown(markdown_response, extensions=["extra", "nl2br"])
        return html_response
    except Exception as e:
        print(f"Erro ao processar a resposta: {e}")
        return "<p>Desculpe, houve um erro ao gerar as recomendações.</p>"

# Página de recomendação para o usuário
@app.route('/recommend/<int:user_id>')

def recommend(user_id):
    history = get_user_history(user_id)
    if not history:
        return "Usuário não encontrado", 404
    ia_response = ia_decision(user_id, history)
    return render_template('recommendation.html', user_id=user_id, message=ia_response)

if __name__ == '__main__':
    app.run(debug=True)