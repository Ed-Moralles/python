nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
separar = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separar[0], len(separar[0])))

