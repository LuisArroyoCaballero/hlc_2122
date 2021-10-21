# Ejercicio 6
# Eliminar cadenas vacías de la lista de cadenas

# Dado:

# lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]
# Resultado:

# ["Chema", "Juan Diego", "Diana", "Alejandro"]

lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]

for i in lista:
    if not i:
        lista.remove(i) # Puedes introducir tambien una cadena vacía y se borrara "".
        
print(lista)