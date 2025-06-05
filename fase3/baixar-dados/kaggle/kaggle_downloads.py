# Primeiro deve instalar a Api do Kaggle
# pip install kaggle, depois gerar um novo API TOKEN
# baixar o arquivo kaggle.json
# e inserir o arquivo baixado no local esperado (ex: home/.kaggle/kaggle.json)

import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Autentica
api = KaggleApi()
api.authenticate()


menu = input('Digite c para baixar competições e d para datasets:').strip().lower()

identificador = input('Digite o identificador do dataset/competição a ser baixado:').strip()

if menu == 'd':
    
    pasta_destino = identificador.replace('/', '-')
    # Cria a pasta 'dados' caso ela não exista
    os.makedirs(f'datasets/{pasta_destino}', exist_ok=True)

    # Baixa o dataset
    api.dataset_download_files(f'{identificador}', path=f'datasets/{pasta_destino}', unzip=True)

    # Mensagem de sucesso
    print(f'Dataset {identificador} baixado com sucesso na pasta "datasets/{pasta_destino}"!')


elif menu == 'c':

    # Cria a pasta 'competicoes' se não existir
    os.makedirs(f'competicoes/', exist_ok=True)

    # Baixa os arquivos da competição
    api.competition_download_files(f'{identificador}', path=f'competicoes/')

    print(f'Competição {identificador} baixada com sucesso na pasta "competicoes/"!')
