# lists -> []
# listas são sequências ordenadas de elementos e podem ser modificadas

hobbies = ["ADM", "board games"]
info = ["Nathan", 40]
compras = list("maça", "laranja")
print(type(hobbies))

# tuples -> ()
# são sequencias ordenada imutáveis

hobbies = ("ADM", "board games")
info = ("Nathan", 40)
compras = tuple("maça", "laranja")
print(type(hobbies))

# sets -> {}
# não garantem a ordem dos itens e são mutáveis
# ponto principal: os itens não se repetem

carros = {"bmw", "ferrari", "maclaren"}
pilotos = set("senna", "botas")
print(type(my_set))

# dicts
# dicionarios são garantem a ordem e são mutáveis
# seus elementos são acessados por chaves

taça = {
    "Brasil": 5,
    "Uruguai": 2
}
camisa = dict(Neymar = 0, Vini_Junior=10)