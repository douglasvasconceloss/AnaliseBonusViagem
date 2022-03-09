import pandas as pd
from twilio.rest import Client

account_sid = "AC9108f5e9b627d2c078813e424c0a24cf"
auth_token  = "7e0254d6d106c5cbdd38669c232b5614"

client = Client(account_sid, auth_token)

#passo a passo de solução

#abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas =tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0] 
        print(f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')         
        message = client.messages.create(
            to="+05548984947444", 
            from_="+12072233480",
            body=f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
        print(message.sid)






#verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

#se for maior que 55.000 -> envia um SMS com o nome, o mes e as vendas do vendedor


#caso nao seja maior do que 55.000 nao quero fazer nada
