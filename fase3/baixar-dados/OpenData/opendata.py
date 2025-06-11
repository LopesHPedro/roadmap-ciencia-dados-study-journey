import pandas as pd

path = 'dados_abertos_prppg_-_2024.2_cursos_pos.csv'

df_unifei = pd.read_csv(path)
part = pd.DataFrame(df_unifei[5:])


df_unifei = part.rename(columns={
    'Unnamed: 1' : 'Nome do Programa',
    'Unnamed: 3' : 'Situação',
    'Unnamed: 9' : 'Número de Discentes',
    'Unnamed: 10' : 'Número de Docentes'
})
columns_to_print = ['Nome do Programa', 'Situação', 'Número de Discentes', 'Número de Docentes']

print(df_unifei[columns_to_print])