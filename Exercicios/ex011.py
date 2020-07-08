sal = int(input('O salario de um individuo é: R$'))
reaj = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R${:.2f} reais com o reajuste de 15%, seu salario ficou em R${:.2f} reais! '.format(sal, reaj))
