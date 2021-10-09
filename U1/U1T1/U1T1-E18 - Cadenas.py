# Ejercicio 18:
# Reemplace cada puntuación con # en la siguiente cadena

# Dado :
# str1 = '/*Chema es @profesor & maker!!'

# Resultado:
# ##Chema es #profesor # maker##

str1 = "/*Chema es @profesor & maker!!"

for i in str1:
    if not i.isalnum() and i != " ":
        str1 = str1.replace(i, "#")
        
print(str1)