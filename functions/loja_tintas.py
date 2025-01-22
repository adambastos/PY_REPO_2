''' 
23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.

'''
lata = 18
price1 = 80

galao = 3.6
price2 = 25

tamanho = float(input('Quantos metros quadrados será pintado? '))
litros_usados = tamanho // 6
metros_falta = tamanho % 6

print('Serão utilizados {} litros de tintar para pintar {} metros quadrados'.format(litros_usados, tamanho))
print('Ficarão faltando {} metros para serem pintados' .format(metros_falta))

