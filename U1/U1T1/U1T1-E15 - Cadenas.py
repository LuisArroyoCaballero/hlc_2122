# Ejercicio 15:
# Eliminar símbolos / puntuación especiales de una cadena determinada

# Dado :
# str1 = "/*Chema es @profesor & maker"

# Resultado esperado :
# "Chema es profesor maker"

str1 = "/*Chema es @profesor & maker"

for i in str1:
    if not i.isalnum() and i != " ":
        str1 = str1.replace(i, "")
        
print(str1)