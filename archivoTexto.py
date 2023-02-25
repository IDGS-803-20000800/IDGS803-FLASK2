""" 
f = open("alumnos.txt", "r")
nombres = f.read()
print(nombres)
f.seek(9)
nombres2 = f.read()
print(nombres2)
f.close() 
"""

"""
f = open("alumnos.txt", "r")
nombres = f.readlines() # Lee varias lineas y las pone en un arreglo
for item in nombres:
    print(item, end="")
f.close() 
"""

f = open("alumnos.txt", "a") #"w" sobreescribe el contenido, "a" añade
f.write("\n" + "!!!Hola mundo!!!")
f.close()