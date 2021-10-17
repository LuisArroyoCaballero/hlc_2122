# Ejercicio 2:
# Concatenar dos listas por índice

# Dado:
# lista1 = ["M", "nom", "e", "Che"]
# lista2 = ["i", "bre", "s", "ma"]

# Resultado esperado:
# ['Mi nombre es Chema']

lista1 = ["M", "nom", "e", "Che", "jajajajaj"]
lista2 = ["i", "bre", "s", "ma"]


if len(lista1) < len(lista2):
    for i in range(len(lista1)):
        lista3 = lista3+lista1[i]+lista2[i]+" "
        cont+=1
    lista3 = lista3+(lista2[cont:])
elif len(lista1) > len(lista2):
    for i in range(len(lista2)):
        lista3 = lista3+lista1[i]+lista2[i]+" "
        cont+=1
    lista3 = lista3+(lista1[cont:])
else:
    for i in range(len(lista1)):
        lista3 = lista3+lista1[i]+lista2[i]+" "

print(lista3)