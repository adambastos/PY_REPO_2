import math
''' 
23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.

'''
area = float(input('Qual a área em m² a ser pintada? '))
lata_pinta = 18 * 6
galao_pinta = 3.6 * 6
preco_lata = 80
preco_galao = 25 
qnt_latas = area / lata_pinta
custo = preco_lata * math.floor(qnt_latas)
area_excedente = area % lata_pinta
retira_excedente = area - area_excedente
galoes_excedentes = area_excedente / math.ceil(galao_pinta)
custo_galao_exc = math.ceil(galoes_excedentes) * preco_galao
custo_geral = custo + custo_galao_exc
if area > lata_pinta:
    print('Precisará de {} latas de tinta para pintar {}m² e ficará restando {}m² sem pintura, com um custo de R${}.' .format(math.floor(qnt_latas), retira_excedente, area_excedente, custo))
print('Vamos às opções:')
if area_excedente <= 43.2:
    print('Este excedente de {}m² podem ser pintados com {} galões, com um custo de R${} a mais, totalizando R${}' .format(area_excedente, math.ceil(galoes_excedentes), custo_galao_exc, custo_geral))


    









