# importação
import requests
import csv
import os
from openai import OpenAI

#extração
API_URL = "https://pousada-api.onrender.com/hospedes"

def extrair_hospedes():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()

# Transformação (com IA)
from openai import OpenAI

client = OpenAI()

def gerar_mensagem_com_ia(hospede):
    prompt = f"""
Você é um assistente de marketing de uma pousada.

Crie uma mensagem curta, educada e personalizada para o hóspede abaixo,
com foco em relacionamento, fidelização e experiência positiva.

Dados do hóspede:
- Nome: {hospede['nome']}
- Check-in: {hospede['checkin']}
- Check-out: {hospede['checkout']}
- Data de aniversário: {hospede['aniversario']}

Regras:
- Se o aniversário estiver próximo ou coincidir com a data atual, inclua felicitações.
- Caso contrário, crie uma mensagem de boas-vindas ou promocional.
- Use linguagem profissional e acolhedora.
- Limite a mensagem a no máximo 3 frases.
"""
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return resposta.choices[0].message.content.strip()

    except Exception as e:
        # Fallback sem IA (obrigatório em pipelines reais)
        return (
            f"Olá {hospede['nome']}! Foi um prazer recebê-lo(a) em nossa pousada. "
            "Esperamos revê-lo(a) em breve para mais uma excelente experiência conosco."
        )


# Carregamento
def salvar_csv(hospedes):
    os.makedirs("output", exist_ok=True)

    with open("output/mensagens.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["id", "nome", "mensagem"])

        for hospede in hospedes:
            mensagem = gerar_mensagem_com_ia(hospede)
            writer.writerow([hospede["id"], hospede["nome"], mensagem])


#desenvolvimento do pipline
def main():
    hospedes = extrair_hospedes()
    salvar_csv(hospedes)
    print("✅ Pipeline ETL com IA executado com sucesso!")
if __name__ == "__main__":
    main()

