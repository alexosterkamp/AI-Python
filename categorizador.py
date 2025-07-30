from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pergunta = input("Digite sua pergunta: ")
resposta = cliente.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": """  

            """
        },
        {
            "role": "user",
            "content": "Indique o procedimento correto para pedir um carro."
        }
    ]
)

print(resposta.choices[0].message.content)


