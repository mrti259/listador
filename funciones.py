# Funciones de archivo
import json

def cargar(archivo):
    try:
        with open(archivo+'.json', 'r') as file:
            dic = json.load(file)
        return dic, 0
    except:
        dic = {}
        return dic, 1

def guardar(archivo, dic):
    with open(archivo+'.json', 'w') as file:
        json.dump(dic, file, sort_keys=1, indent=2)
    return 0

# Funciones de diccionario

def crear_lista(dic, nombre):
    dic[nombre.title()] = []
    return 1

def eliminar_lista(dic, nombre):
    del(dic[nombre])
    return 1

def renombrar_lista(dic, lista, nombre):
    dic[nombre.title()] = dic[lista.title()]
    del(dic[lista.title()])
    return 1

# Funciones de lista

def agregar_elemento(dic, lista, elemento):
    dic[lista].append(elemento)
    return 1

def eliminar_elemento(dic, lista, elemento):
    dic[lista].remove(elemento)
    return 1

def renombrar_elemento(dic, lista, elemento0, elemento1):
    i = dic[lista].index(elemento0)
    dic[lista][i] = elemento1
    return 1
