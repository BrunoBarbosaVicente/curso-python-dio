# 2. Calculadora Simples
# Crie um programa que permita ao usuário realizar operaçoes simples de calculadora, como adição, subtração, multoplicação e divisão.

numero1 = int(input('Digite um numero:'))
operador = input('Digite o operador:')
numero2 = int(input('Digite outro numero:'))
resultado = 0

if operador == '+':
    resultado = numero1 + numero2
    print(f'{numero1} + {numero2} = {resultado}')
elif operador == '-':
    resultado = numero1 - numero2
    print(f'{numero1} - {numero2} = {resultado}')
elif operador == '*':
    resultado = numero1 * numero2
    print(f'{numero1} * {numero2} = {resultado}')
elif operador == '/':
    resultado = numero1 / numero2
    print(f'{numero1} / {numero2} = {resultado}')

# -------------------- ou ---------------------

nome = input("Digite seu nome: ")
print(f"Seja bem vindo {nome}, esta é uma calculadora basica !!!")

numero1 = int(input("Digite o primeiro numero: "))
operador = str(input("Digite o operador: "))
numero2 = int(input("Digite o segundo numero: "))
resultado = 0
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "/":
    resultado = numero1 / numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "//":
    resultado = numero1 // numero2
elif operador == "%":
    resultado = numero1 % numero2
elif operador == "**":
    resultado = numero1 ** numero2

print(f"O resultado de {numero1} {operador} {numero2} é = {resultado}")