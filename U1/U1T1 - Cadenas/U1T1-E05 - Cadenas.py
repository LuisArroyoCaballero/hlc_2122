# Ejercicio 5:
# Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada

# Dado :
# str1 = "C@#he26ma^&Du5ran"

# Resultado esperado :
# Recuentos totales de caracteres, dígitos y símbolos 
# Caracteres = 10 
# Dígitos = 3 
# Símbolo = 4

str1 = "C@#he26ma^&Du5ran"
characters = 0
digits = 0
simbols = 0
mayus = 0
minus = 0

for i in str1:
    if (i.isdigit()):
        digits += 1
    elif (i.isalpha()):
        characters += 1
        if (i.islower()):
            minus += 1
        elif (i.isupper()):
            mayus += 1
    else:
        simbols += 1

print("Recuentos totales de caracteres, dígitos y simbolos")
print("Caracteres = "+str(characters)+" de los cuales "+str(mayus)+" son mayusculas y "+str(minus)+" son minusculas.")
print("Dígitos = "+str(digits))
print("Símbolos = "+str(simbols))