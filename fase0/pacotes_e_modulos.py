# Pacotes

"""
Pacotes emm Python são um meio de organizar e estruturar código através do agrupamento
de módulos relacionados em diretórios. Essa organização ajuda a manejar e reusar
código de maneira eficaz, especialmente em projetos grandes, pense em pacotes como
caixas de ferramentas, armazenando e organizando ferramentas(funções e classes),
para um acesso e reuso eficiente!
"""

# Componentes de um pacote:
"""
- módulo: Um único arquivo Python que contém código reutilizável (ex: math.py)
- pacote: Uma pasta que contém módulos e um arquivo especial chamado __init__.py
- subpacotes: Pacotes dentro de outros pacotes para organizar em níveis mais profundos.
"""

# Como criar e acessar pacotes:
"""
    1. Crie um diretório, ele vai servir como a pasta raiz
    2. Adicione arquivos python(módulos), cada um representando uma funcionalidade específica
    3. Inclua  no diretório __init__.py (pode estar vazio), isso vai marcá-lo como um pacote
    4. Adicione subpacotes(opcional)
    5. Importe os módulos,  usando . exemplo: from meupacote.modulo1 import ola
"""

# Alguns exemplos de pacotes:
""" 
Para Análise Estatística:
 - NumPy
 - Pandas
 - SciPy
 - StatsModels

Para Visualização de dados:
 - Matplotlib
 - Seaborn
 - Plotly
 
Para Deep Learning:
 - Scikit-learn
 - TensorFlow
 - PyTorch
"""
# 🔗 Referências:
# https://www.geeksforgeeks.org/python-packages/