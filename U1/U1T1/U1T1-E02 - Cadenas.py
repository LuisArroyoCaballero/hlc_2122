# Ejercicio 2:
# Dadas dos cadenas, s1 y s2, cree una nueva cadena agregando s2 en medio de s1

# Dado :
# s1 = "Hola"
# s2 = "Adios"
# Resultado:

# HoAdiosla

str1 = input("Introduzca una primera palabra: ")
str2 = input("Introduzca una segunda palabra: ")

# Utilizamos la funcion slice ([x:y]) para coger la primera mitad de la cadena, introduciendo como segundo valor la mitad. 
# Mismo proceso para la parte final de la cadena, pero esta vez desde la mitad hasta el final [mitad:len] o [mitad:] (no es necesario
# especificar el final de la cadena, el propio python lo sabe)

print(str1[0:int(len(str1)/2)]+str2+str1[int(len(str1)/2):len(str1)])