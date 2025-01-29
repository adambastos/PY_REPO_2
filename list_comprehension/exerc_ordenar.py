vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]
final_list = [(produto, vendas2019) for produto, vendas2019, vendas2020 in vendas_produtos]


maior_venda_2019 = 0
mais_vendido2019 = ''

for item in final_list:
    produto, valor = item
    if valor > maior_venda_2019:
        maior_venda_2019 = valor
        mais_vendido2019 = produto

print(maior_venda_2019)
print('{} foi o produto mais vendido em 2019 com R${} em vendas.' .format(mais_vendido2019, maior_venda_2019))




