num = float(input('Digite uma medida em metros: '))
cm = num * 100
mm = num * 1000
print('Ao obter um certo valor em metro {}m, obtemos ele em centímetro {:.0f}cm e em milímetros {:.0f}mm! '.format(num, cm, mm))