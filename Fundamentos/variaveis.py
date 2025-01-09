# cometários
# você esta vendo um agora
# eles não afetam o texto
# no vscode, digite algo e pressione ctrl+/

# criando variáveis
# nome_da_variável = valor
nome = "nathan"
idade = 40
patrimônio = 5.98
administracao = True
posicao = 3+4j

# convenções
#   1.não usar nomes aleatórios
#   2.separe as palavras com _
#   3.não começar com simbolos especiais ou números
#       ex: #$%¨&&*()
#       ex: 10dias
#       ex: fruta#
#       ex: !volume
#   4.preferível não utilizar acentos

# tipos
# para determinar o tipo da variável use *type()*
print(type(nome)) # string
print(type(idade)) # int
print(type(patrimônio)) # float
print(type(administracao)) # boolean
print(type(posicao)) # complex

# também é possivel usar construtores para definir uma variáveis e realizar conversões
idade = int("40")
dinheiro = float("0.99")
administracao = bool(1)