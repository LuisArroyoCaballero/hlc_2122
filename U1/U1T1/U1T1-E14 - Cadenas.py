# Ejercicio 14:
# Eliminar cadenas vacías de una lista de cadenas

# Dado :
# str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]

# Resultado esperado :

# # lista original
# ['Chema', 'Alejandro', '', 'Juan Diego', None, 'Diana', '']
# # Después de quitar cadenas vacías
# ['Chema', 'Alejandro', 'Juan Diego', 'Diana']

str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]
# str_final = [n if (n != "" and n != None) else continue for n in str_list]


# Con el metodo REMOVE

for i in range(str_list.count(None)):
    str_list = str_list.remove(None)
    
print(str_list.count(""))
for i in range(str_list.count("")):
    print(i)
    str_list = str_list.remove("")
    

print(str_list)
