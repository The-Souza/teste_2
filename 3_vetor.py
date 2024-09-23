import json

CAMINHO_ARQUIVO = 'dados.json'

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

l2 = []
for i in dados:
    l2.append(i['valor'])

menor_valor = min(l2)
maior_valor = max(l2)

print(f'Maior faturamento: R${maior_valor}')
print(f'Menor faturamento: R${menor_valor}')

media = sum(l2) / len(l2)    
dias_acima_da_media = len([f for f in l2 if f > media])

print('Quantidade de dias que tiveram o faturamento acima da média: ',dias_acima_da_media)
