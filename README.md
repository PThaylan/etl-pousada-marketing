Pipeline ETL com IA para Marketing de Pousada

Este projeto implementa um pipeline ETL (Extract, Transform, Load) em Python, com uso de Inteligência Artificial Generativa (ChatGPT/OpenAI) para criação de mensagens personalizadas de marketing para hóspedes de uma pousada.

OBJETIVO DO PROJETO
- Extrair dados de hóspedes a partir de uma API REST
- Utilizar IA generativa para criar mensagens personalizadas
- Aplicar boas práticas de tratamento de falhas externas
- Gerar um arquivo CSV final para campanhas de marketing

ARQUITETURA DO PIPELINE
Extract (API REST)
Transform (IA Generativa / Fallback)
Load (Arquivo CSV)

ETAPAS DO ETL
1) Extract:
Os dados são obtidos via API REST.
Endpoint: GET /hospedes

2) Transform:
A IA gera mensagens personalizadas com base nos dados do hóspede.
Caso a API da OpenAI não esteja disponível, o sistema utiliza mensagens automáticas.

3) Load:
Os dados são salvos no arquivo output/mensagens.csv.

ESTRUTURA DO PROJETO
etl-pousada-marketing/
- etl.py
- requirements.txt
- output/mensagens.csv
- README.md

COMO EXECUTAR
1) Criar ambiente virtual
python -m venv .venv

2) Ativar ambiente
.venv\Scripts\Activate.ps1

3) Instalar dependências
python -m pip install -r requirements.txt

4) Executar
python etl.py

RESULTADO
Arquivo CSV com mensagens personalizadas geradas para cada hóspede.

TECNOLOGIAS
Python, Requests, OpenAI, FastAPI, CSV, GitHub

AUTOR
Pedro Thaylan Oliveira de Paula

