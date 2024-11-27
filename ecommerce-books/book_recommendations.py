def recommend_fiction(user_id: int) -> str:
    return """
## Recomendações de Ficção
- **Duna** – Frank Herbert
- **O Senhor dos Anéis** – J.R.R. Tolkien
- **Fundação** – Isaac Asimov
"""

def recommend_non_fiction(user_id: int) -> str:
    return """
## Recomendações de Não Ficção

- **Sapiens** – Yuval Noah Harari
- **O Poder do Hábito** – Charles Duhigg
- **Pai Rico, Pai Pobre** – Robert Kiyosaki
"""

def recommend_science(user_id: int) -> str:
    return """
## Recomendações de Ciência
- **Cosmos** – Carl Sagan
- **Uma Breve História do Tempo** – Stephen Hawking
- **O Universo Elegante** – Brian Greene
"""

def recommend_technology(user_id: int) -> str:
    return """
## Recomendações de Tecnologia

- **Clean Code** – Robert C. Martin
- **Design Patterns** – Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
- **The Pragmatic Programmer** – Andrew Hunt, David Thomas
"""
