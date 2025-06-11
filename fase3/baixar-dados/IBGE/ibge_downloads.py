import requests # vai requisitar o dado para a API(Application Programming Interface)
import pandas as pd # Organiza os dados em tabelas(DataFrame)


# URL da API SIDRA
url = "https://apisidra.ibge.gov.br/values/t/6579/p/2024/n6/3132404"

# Faz a requisição
res = requests.get(url)
res.raise_for_status()  # dispara erro se status != 200
data_json = res.json()

df_sidra = pd.DataFrame(data_json[1:])

df_sidra = df_sidra.rename(columns={
    'V' : 'Quantidade',
    'D1C' : 'Ano',
    'D2N' : 'Município',
    'D3N' : 'Objeto a ser estudado'
})

columns_to_print = ['Objeto a ser estudado', 'Quantidade', 'Município', 'Ano']

print(df_sidra[columns_to_print].head())

