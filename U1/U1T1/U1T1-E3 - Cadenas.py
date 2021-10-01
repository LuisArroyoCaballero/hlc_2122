# Ejercicio 3:
# Dadas dos cadenas, s1 y s2 devuelven una nueva cadena compuesta por el primer, el medio y el último carácter de cada cadena de entrada

# Dado :
# s1 = "Chema"
# s2 = "Duran"
# Resultado:

# CDeran

str1 = input("Introduzca una primera palabra: ")
str2 = input("Introduzca una segunda palabra: ")

# Puesto que python interpreta las cadenas como Arrays podemos coger la posición exacta de cada letra de la cadena. Se pueden usar
# posiciones negativas y empezaremos a buscarla desde el final (la ultima posicion es [-1])

print(str1[0]+str2[0]+str1[int(len(str1)/2)]+str2[int(len(str2)/2)]+str1[-1]+str2[-1])