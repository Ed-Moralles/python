dias = int(input('Quantos dias foram alugados: '))
km = float(input('Quantos quilometros foram rodados: '))
valor = ( dias * 60) + ( km * 0.15)
print('O total a pagar é R$ {:.2f} reais! '.format(valor))