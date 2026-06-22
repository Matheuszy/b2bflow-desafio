# Desafio Estágio Python - b2bflow

Código em Python que lê contatos cadastrados no Supabase e envia a mensagem **"Olá, {nome} tudo bem com você?"** via Z-API no WhatsApp.

## Setup da tabela no Supabase

Crie uma tabela chamada `contacts` com as seguintes colunas:

| Coluna | Tipo |
|--------|------|
| id     | int8 |
| name   | text |
| phone  | text |

> O campo `phone` deve seguir o formato: `5511999999999` (55 + DDD + número, sem espaços ou símbolos)

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
SUPABASE_URL=https://sua-url.supabase.co
SUPABASE_KEY=sua-chave-anon-public

ZAPI_INSTANCE_ID=seu-instance-id
ZAPI_TOKEN=seu-token
```

## Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/Matheuszy/b2bflow-desafio.git
cd b2bflow-desafio
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o `.env` com suas credenciais e execute:

```bash
python main.py
```

## Tecnologias

- Python
- Supabase
- Z-API
- python-dotenv