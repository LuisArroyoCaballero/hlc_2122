# Ejercicio 8:
# Busque todas las apariciones de "que" en una cadena dada, independientemente que esté o no en mayúsculas.


# Dado :

# str1 = "Lo que yo te diga. Que la vida es así"
# Resultado:

# El recuento de 'que' es: 2

str1 = "Lo que yo te diga. Que la vida es así"

contador = str1.lower().count("que")

print(contador)