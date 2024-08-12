import pandas as pd
import plotly.express as px
#apelido -> agora pandas se chama pd

dados = pd.read_excel("projeto3/vendas.xlsx")

#visualizando as primieras linhas - dados.head()
#visualizando as ultimas linhas - dados.tail()
# Formato da Tabela de Dados - dados.shape
# Visualizando informaçoes das Colunas - dados.info()
#Selecionando Colunas - dados[["id_pedido","cidade" ]]


dados.describe()
dados.head()
#Contagem de vendas por loja - dados[["loja"]].value_counts()
#Faturamento por loja - dados.groupby("loja")['preco'].sum().to_frame()

#faturamento por + de uma coluna e enviar gerar uma planilha em excel com os resultados

dados_agrupados = dados.groupby(['estado', "cidade", "loja","forma_pagamento"])['preco'].sum().to_frame()
dados_agrupados.to_excel('Faturamento.xlsx')

lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    grafico = px.histogram(dados, x = coluna,
                                y = 'preco',
                                text_auto=True,
                                title= 'Faturamento',
                                color="forma_pagamento")
    grafico.show()
    grafico.write_html(f"faturamento-{coluna}.html")