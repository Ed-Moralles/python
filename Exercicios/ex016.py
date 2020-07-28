from math import sin, cos, tan, radians
ang = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f} '.format(ang, seno))
coss = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f} '.format(ang, coss))
tang = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f} '.format(ang, tang))
