# Desafio Cruso DIO
# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# Entrada
# A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

def encaixa(a, b):
    if len(b) > len(a):
        return "nao encaixa"
    elif a[-len(b):] == b:
        return "encaixa"
    else: 
        return "nao encaixa"
n = int(input())
while n > 0:
    a, b = input().split()
    result = encaixa(a, b)
    print(result)
    n -= 1

# ---------------- ou --------------

def encaixa(a, b):
    if len(b) > len(a):
        return "nao encaixa"
    elif a[-len(b):] == b:
        return "encaixa"
    else: 
        return "nao encaixa"
n = int(input())
cases = [input().split() for _ in range(n)]
for a, b in cases:
    result = encaixa(a, b)
    print(result)

# ------------- ou -------------

n = int(input())
sequencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def conferir_sequencia():
    while(n > 0):   
        if n in sequencia:
            return "Encaixa"
        else:
            return "Não encaixa"
print(conferir_sequencia())

# ----------------- ou -----------------

sequencia = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numero_procurado = int(input())
encontrado = False
indice = 0
while indice < len(sequencia[0:1000]):
    if sequencia[indice] == numero_procurado:
        encontrado = True
        break
    indice += 1
if encontrado:
    print("Encaixa")
else:
    print("nao encaixa")

# ------------- ou -------------

n = int(input("Digite o número de casos de teste: "))
def verifica_correspondencia(a, b):
    if len(b) > len(a):
        return "nao encaixa"
    last_digits_a = a[-len(b):]
    if last_digits_a == b:
        return "encaixa"
    else:
        return "nao encaixa"
def main():    
    while(n > 0):        
        a = input("Digite o valor de A: ")
        b = input("Digite o valor de B: ")       
        resultado = verifica_correspondencia(a, b)
        print(resultado)
if __name__ == "__main__":
    main()

# ------------ ou ------------

qt = int(input())
v = []
for i in range(qt):
  v = input().split(" ")
  a = v[0]
  b = v[1]
if len(b) > len(a):
    print("nao encaixa")
elif a.endswith(b):
    print("encaixa")
else:
    print("nao encaixa")  

# -------------- ou ----------------

valor_A = input("A -> ")
valor_B = input("B -> ")
teste = False
if str(valor_B) in str(valor_A):
  tamanho_A = len(valor_A);
  tamanho_B = len(valor_B);
  conta_iqualdade = 0;
  for i in range(tamanho_B -1, -1, -1):
    if valor_B[i] == valor_A[tamanho_A -1]:
        conta_iqualdade+=1;
        tamanho_A-=1;
  if conta_iqualdade == tamanho_B:
   teste = True;
print(teste)

# -------------- ou --------------

n = int(input("Digite o valor de N: "))
while(n >= 0):
    a = input("Informe o valor de A: ")
    b = input("Informe o valor de B: ")
    n = n > 1
    if len(a) >= len(b):
        if (a[(len(a) - len(b)):]) == b:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")

# ------------ ou ---------------
#passei com esse no desafio DIO

N = int(input())  # Lê o número de casos de teste

for i in range(N):
    A, B = input().split()  # Lê os valores A e B como strings
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")