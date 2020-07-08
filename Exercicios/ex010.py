p = float(input('Digite o preço de um produto: R$'))
desc = p - (p * 5 / 100) 
print('O produto que custava R${:.2f} reais, com desconto de 5 porcento ira custar R${:.2f} reais! '.format(p, desc))