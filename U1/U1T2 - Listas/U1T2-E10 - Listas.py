# Ejercicio 10
# Dada una lista, elimine todas las ocurrencias de 20 de la lista

# Dado:

# lista = [5, 20, 15, 20, 25, 50, 20]
# Resultado:

# [5, 15, 25, 50]

lista = [5, 20, 15, 20, 25, 50, 20]

lista = [value for value in lista if value != 20]

print(lista)