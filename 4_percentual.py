sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp+rj+mg+es+outros
print(f'Faturamento mensal: {total}')
print()

def percentual(valor, total):
	porcentagem = valor / total * 100
	print(f'{porcentagem:.2f}%')

print('Percentual de SP: ', end='')
percentual(sp, total)
print('Percentual de RJ: ', end='')
percentual(rj, total)
print('Percentual de MG: ', end='')
percentual(mg, total)
print('Percentual de ES: ', end='')
percentual(es, total)
print('Percentual de Outros: ', end='')
percentual(outros, total)