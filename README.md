# API com recomendações de regras de qualidade de dados para o AWS Glue Data Quality

Este projeto fornece uma API para gerar regras de qualidade de dados para uma tabela específica usando a sintaxe DQDL do AWS Glue Data Quality.

## Requisitos

- Python
- API Key do Google Gemini
- Docker (Opcional)

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/hespius/glue-data-quality-recommendations.git
    ```

2. Crie arquivo com variaveis de ambiente

    Crie um arquivo [.env](http://_vscodecontentref_/1) contendo a variável GEMINI_API_KEY e o valor da sua API Key do Google Gemini
    ```env
    GEMINI_API_KEY=sua_chave_api_aqui
    ```

## Executando a API

### Utilizando somente Python

1. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

3. Execute o servidor FastAPI
    ```sh
    fastapi run main.py
    ```

A API estará disponível em `http://127.0.0.1:8000`

### Utilizando Docker

1. Faça o build da imagem Docker
    ```sh
    docker build -t glue-data-quality-recommendations-gemini-api .
    ```

2. Rode a imagem construída
    ```sh
    docker run -d -p 80:80 glue-data-quality-recommendations-gemini-api
    ```

A API estará disponível em `http://127.0.0.1`

## Endspoints da API

- **URL:** `/glue-data-quality-recommendations-rules`
- **Método:** `GET`
- **Parâmetros de Consulta:**
    - `model_name` (str, opcional) : O nome do modelo do Google Gemini que será utilizado. Valor padrão: `"gemini-2.0-flash-exp"`

## Testando a API

Para testar a API, você pode usar ferramentas como `curl`, `Postman`, `Insominia` ou qualquer outra ferramenta de teste de API. Aqui está um exemplo usando curl:

```sh
    curl -X 'GET' \
  'http://127.0.0.1:8000/glue-data-quality-recommendations-rules' \
  -H 'accept: application/json'
```
