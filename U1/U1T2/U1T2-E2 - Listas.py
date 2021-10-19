# Ejercicio 2:
# Concatenar dos listas por índice

# Dado:
# lista1 = ["M", "nom", "e", "Che"]
# lista2 = ["i", "bre", "s", "ma"]

# Resultado esperado:
# ['Mi nombre es Chema']

lista1 = ["M", "nom", "e", "Che", "jajajajaj"]
lista2 = ["i", "bre", "s", "ma"]
lista3 = ""


if len(lista1) < len(lista2):
    for i in range(len(lista1)-1):
        lista3 = lista3+lista1[i]+lista2[i]+" "
    lista3.concat(lista2[len(lista1)-1:])
else:
    for i in range(len(lista2)):
        lista3 = lista3+lista1[i]+lista2[i]+" "
    lista3.concat(lista1[len(lista2)-1:])


print(lista3)