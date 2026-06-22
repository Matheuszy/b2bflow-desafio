import os
import requests
import logging
from dotenv import load_dotenv
from supabase import create_client

# Carrego as variáveis de ambiente do arquivo .env
# assim não preciso colocar senhas direto no código
load_dotenv()

# Configuro o log para ver o que está acontecendo no terminal enquanto o script roda
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def get_contacts():
    """Busca até 3 contatos cadastrados no Supabase."""

    # Pego as credenciais do .env para conectar no Supabase
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    # Crio o cliente do Supabase com a URL e a chave
    supabase = create_client(url, key)

    # Busco os campos name e phone da tabela contacts, limitando a 3 registros
    response = supabase.table("contacts").select("name, phone").limit(3).execute()

    # Retorno a lista de contatos
    return response.data


def send_whatsapp(phone: str, name: str):
    """Envia a mensagem de saudação via Z-API para um número de WhatsApp."""

    # Pego as credenciais da Z-API do .env
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token       = os.getenv("ZAPI_TOKEN")

    # Monto a URL do endpoint de envio de texto da Z-API
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"

    # Header padrão da Z-API
    headers = {
        "Content-Type": "application/json"
    }

    # Monto o corpo da requisição com o número e a mensagem personalizada
    payload = {
        "phone": phone,
        "message": f"Olá, {name} tudo bem com você?"
    }

    # Faço a requisição POST para a Z-API
    response = requests.post(url, json=payload, headers=headers)

    # Verifico se o envio foi bem-sucedido e registro no log
    if response.status_code == 200:
        logging.info(f"✅ Mensagem enviada para {name}")
    else:
        logging.error(f"❌ Falha ao enviar para {name}: {response.text}")


def main():
    logging.info("Buscando contatos no Supabase...")

    # Chamo a função que busca os contatos no banco
    contacts = get_contacts()

    # Se não encontrar nenhum contato, aviso e encerro o script
    if not contacts:
        logging.warning("Nenhum contato encontrado no banco.")
        return

    logging.info(f"{len(contacts)} contato(s) encontrado(s). Enviando mensagens...")

    # Para cada contato, chamo a função que envia a mensagem no WhatsApp
    for contact in contacts:
        send_whatsapp(contact["phone"], contact["name"])

    logging.info("Processo finalizado.")


# Ponto de entrada do script — só executa se rodar direto com python main.py
if __name__ == "__main__":
    main()