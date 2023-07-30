dados = {}
dados['Nome'] = input('Digite o nome da pessoa física:  ')
dados['Nascimento'] = int(input('Digite o ano de nascimento:  '))
dados['Carteira'] = int(input('Digite o número da carteira de trabalho (0 para não tem):  '))
dados['Idade'] = 2023 - dados['Nascimento']
if dados['Carteira'] != 0:
    dados['Contratado'] = int(input('Digite o ano da sua contratação:  '))
    dados['Salario'] = int(input('Digite seu salário atual: R$ '))
for k, v in dados.items():
    if k == 'Carteira':
        if dados['Carteira'] == 0:
            print('Não tem carteira')
        else:
            print(f'{k}: {v}')
    else:
        print(f'{k}: {v}')
if dados['Carteira'] != 0:
    dados['Aposentadoria'] = (2023 - dados['Contratado']) + 35
    if dados['Idade'] >= dados['Aposentadoria']:
        print('Aposentadoria: Já aposentado')
    else:
        print(f'Aposentadoria: {dados["Aposentadoria"]} anos')
