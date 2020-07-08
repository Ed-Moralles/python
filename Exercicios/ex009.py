alt = float(input('Digite altura: '))
comp = float(input('Digite o comprimento: '))
area = alt * comp
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {} m2! '.format(alt, comp, area))
print('Para pintarmos esta parede precisaremos de {} litros de tinta! '.format(tinta))
