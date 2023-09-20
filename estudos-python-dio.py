#        >formas de adicionar as variaveis para imprimir na string<
#
#   <Ultilisando o metodo old style %>
# nome = "Bruno"
# idade = 30
# profissao = "Desenvolvedo"
# Linguagem = "Python"

# print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade , profissao, Linguagem))
#
# %s: serve para projetar valores em strings
# %d: serve para projetar valores inteiros
# %f: serve para projetar valores flutuantes
# %(): colocar dentro dos parenteses na ordem que deseja que seja impresso
#   nao recomendado para strigs muito grandes
#
#   <Ultilizando o metodo format>
nome = "Bruno"
idade = 30
profissao = "desenvolvedor"
linguagem = "Python"
dados = {"nome": "Bruno", "idade": 30, "profissao": "desenvolvedor", "linguagem": "Python"}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem)) #{}: colocar chaves onde deseja projetar os valores

#                                  ou

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(nome, idade, profissao, linguagem)) # tambem pode ser adicionado a posição em que a variavel se encontra dentro de .format()

#                                  ou

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem)) # tambem é possivel adicionar um parametro dentro de chaves, e em .format passar o valor para cada parametro.

#                                  ou

print("Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**dados)) # esse metodo foi a um dicionario que se encontra na variavel 'dados'

# .format(): serve para imprimir as variaveis na ordem que deseja na posição onde adicionou as chaves.
#   esse metodo e menos recomendado que o anterior
#
#   <Ultilizando o metodo f-string>
# nome = "Bruno"
# idade = 30
# profissao = "desenvolvedor"
# linguagem = "Python"

# print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.") # esse formato é o mais recomendado atualmente, e usando esse metodo ja pode ser adicionado dentro das chaves diretamente a variavel criada.
#
#   <Formatar strings com f-string>
# PI = 3.14159

# print(f"valor de PI: {PI:.2f}") # imprime apenas duas casas flutuantes.
# print(f"valor de PI: {PI:10.2f}") # imprime no primeiro parametro '10', 11 espaços vazios e no parametro '.2f' a quantidade de casas flutuantes que deseja.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#