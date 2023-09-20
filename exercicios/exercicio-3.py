# 3. Verificador de Numeros Primos
# Peça ap usuário para inserir um número e determine se ele é um número primo ou não

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = int(input('Digite o número que deseja saber se é um Número Primo ou não:'))
if eh_primo(numero):
    print(f'{numero} é Primo')
else:
    print(f'{numero} não é Primo')