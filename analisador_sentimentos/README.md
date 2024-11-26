
# Analisador de Sentimentos 🎭

Este é um projeto de análise de sentimentos desenvolvido em Python que utiliza a API Google Generative AI para analisar o sentimento (positivo, negativo ou neutro) de textos fornecidos pelo usuário. A aplicação permite enviar textos e arquivos de texto simples para serem processados, retornando um feedback com o sentimento detectado. A interface é construída usando Gradio, proporcionando uma experiência interativa e fácil de usar.

## Tecnologias e Recursos Utilizados

- **Linguagem**: Python
- **Bibliotecas**:
  - `google.generativeai`: Integração com a API Google Generative AI para análise de sentimentos
  - `gradio`: Construção da interface interativa
- **Outros**: Ambiente virtual Python para isolamento de dependências

## Pré-requisitos

- **Python 3.10 ou superior** deve estar instalado no sistema.
- Uma chave de API do Google Generative AI para configurar o ambiente (`GEMINI_API_KEY`).

## Configuração do Projeto

Siga as etapas abaixo para configurar e executar o projeto localmente.

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um ambiente virtual

Para garantir que todas as dependências estejam isoladas, crie um ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

- **Linux / MacOS**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

### 3. Instale as dependências

As dependências estão listadas no arquivo `requirements.txt`. Instale-as usando:

```bash
pip install -r requirements.txt
```

### 4. Configure a chave de API

Para utilizar a API do Google Generative AI, é necessário configurar a variável de ambiente `GEMINI_API_KEY` com sua chave de API. Você pode fazer isso da seguinte forma:

- No Linux / MacOS:
  ```bash
  export GEMINI_API_KEY="sua_chave_api_aqui"
  ```

- No Windows:
  ```bash
  set GEMINI_API_KEY="sua_chave_api_aqui"
  ```

### 5. Execute o Projeto

Para iniciar o projeto e abrir a interface Gradio, execute o seguinte comando:

```bash
python nome_do_seu_arquivo.py
```

A aplicação estará disponível no navegador no endereço `http://127.0.0.1:7860`.

## Estrutura do Código

- **`initial_prompt`**: Configura o prompt inicial para definir o papel do chatbot como analisador de sentimentos.
- **`extract_file_contents`**: Função responsável por ler o conteúdo dos arquivos anexados e ignorar arquivos que não são de texto simples.
- **`gradio_wrapper`**: Função principal que combina o texto do usuário e o conteúdo dos arquivos, enviando para a análise de sentimento e retornando o feedback ao usuário.
- **`ChatInterface`**: Interface construída com Gradio para interação com o usuário.

## Exemplo de Uso

1. Insira um texto ou envie um arquivo de texto para a análise.
2. A aplicação retornará o sentimento identificado (positivo, negativo ou neutro) junto com um feedback breve sobre o texto.

## Contribuição

Sinta-se à vontade para fazer um fork do projeto, criar issues ou enviar pull requests. Toda contribuição é bem-vinda!

---

**Observação**: Este projeto depende de uma chave de API válida da Google Generative AI para funcionar corretamente.
