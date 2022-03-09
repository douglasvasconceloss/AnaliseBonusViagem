import pandas as pd

#passo a passo de solução

#abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

tabela_vendas = pd.read_excel('janeiro.xlsx')

print(tabela_vendas)



#verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

#se for maior que 55.000 -> envia um SMS com o nome, o mes e as vendas do vendedor


#caso nao seja maior do que 55.000 nao quero fazer nada