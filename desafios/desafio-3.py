# Desafio
# Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

# Faça um programa para calcular isso.

# Entrada
# A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste. Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000),  respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia.

#definir a quantidade de testes
T = int(input()) 

#criar lista para guardar os valores de cada teste 
resultados = []

#iniciar os testes
for i in range(T):
  N, K = map(int, input().split())
  #definir o total de garrafas e o tanto que é necessário para trocar
  total_garrafas = N
  troca = K
  
  #para cada iteração, realizar o teste
  if N>=K:
    total_trocas = total_garrafas // troca
    sobra = total_garrafas % troca
    resultado = total_trocas + sobra
    resultados.append(resultado)
  else:
    resultados.append(total_garrafas)

#imprimir os resultados um por linha
for i in resultados:
  print(i, sep='\n')