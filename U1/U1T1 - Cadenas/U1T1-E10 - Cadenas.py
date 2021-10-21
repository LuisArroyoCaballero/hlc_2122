# Ejercicio 10:
# Dada una cadena de entrada, cuente las apariciones de todos los caracteres dentro de una cadena

# Dado :

# str1 = "Apple"
# Resultado:

# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "Apple"
dictionary = {}

for i in str1:
    dictionary[i] = str1.count(i)
    
print(dictionary)