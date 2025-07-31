from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro ao ler o arquivo {nome_do_arquivo}: {e}")

prompt_usuário = input("Digite sua pergunta: ")

prompt = """Você é um consultor de processos internos.
Seu papel é fornecer orientações claras e precisas sobre procedimentos internos."""

resposta = cliente.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": "Indique o procedimento correto para pedir um carro."
        }
    ]
)

print(resposta.choices[0].message.content)


