from funciones import *
from time import sleep
import os

if not os.path.exists('archivos'):
    os.system('mkdir archivos')

while True:
    os.system('clear')
    # Elegir archivo
    print('¿Qué archivo queres cargar? Deja vacío para salir')
    #print('Estos son los archivos disponibles:')
    #os.system('ls archivos')
    arc = input()
    archivo = 'archivos/' + arc
    if len(arc) == 0:
        break
    datos, nuevo = cargar(archivo)
    if nuevo:
        print('Se ha iniciado un nuevo archivo')
    else:
        print('Se cargó un archivo anterior.')
    print()
    
    # Menu de listas
    while True:
        print('Archivo: %s.json (%s lista%s)' %(archivo, len(datos), 's'*(not len(datos)==1)))
        print([lista for lista in datos], '\n')
        print('[1] Ver listas y elementos\n[2] Crear lista\n[3] Modificar\n[w] Guardar')
        menu = input()
        print()
        
        while menu == '1':
            
            print('Listas:')
            if not len(datos):
                print('No hay nada...')
            else:
                for lista in datos:
                    print(' %s (%s)' % (lista, len(datos[lista])))
                nombre = input('\nVer lista: ').title()
                if nombre in datos:
                    print(nombre)
                    if not len(datos[nombre]):
                        print('  No hay elementos...')
                    else:
                        for elemento in datos[nombre]:
                            print(' ', elemento)
                else:
                    if nombre == '':
                        break
                    else:
                        print('No existe esa lista')
            if input('Repetir o [x] para volver: ') == 'x':
                break
            print()
        if menu == '1':
            pass
        
        elif menu == '2':
            print('Nueva lista:')
            nombre = input('').title()
            if not nombre in datos and len(nombre):
                crear_lista(datos, nombre)
                print('Creada!')
            else:
                print('Esta lista ya existe.')
                print(datos[nombre])
        
        elif menu == '3':
            # Modificar lista
            print('Elige una lista:')
            lista = input().title()
            if not lista in datos:
                print('No se encuentra la lista.')
            else:
                print('Lista: %s (%s elemento%s)' % (lista, len(datos[lista]), 's'*(not len(datos[lista])==1)))
                print(datos[lista], '\n')
                print('[1] Agregar elementos\n[2] Eliminar elementos\n[3] Renombrar lista\n[4] Copiar\n[5] Eliminar')
                menu = input()
                if menu == '1':
                    elemento = input('Nuevo elemento: ')
                    while len(elemento) > 0:
                        if not elemento in datos[lista]:
                            agregar_elemento(datos, lista, elemento)
                            print('Añadido!')
                        else:
                            print('El elemento ya se encuentra en la lista')
                        elemento = input('Nuevo elemento: ')
                elif menu == '2':
                    elemento = input('Elemento a eliminar:')
                    if elemento in datos[lista]:
                        eliminar_elemento(datos, lista, elemento)
                        print('Eliminado!')
                    else:
                        print('No se encuentra en la lista.')
                elif menu == '3':
                    print('Nuevo nombre:')
                    lista1 = input().title()
                    if lista1 in datos:
                        print('La lista', lista1, 'ya existe. No se va a sobreescribir')
                    else:
                        renombrar_lista(datos, lista, lista1)
                        print('Renombrada!')
                elif menu == '4':
                    nombre = input('Nueva lista: ')
                    if nombre in datos:
                        print('Ya hay una lista con ese nombre')
                    else:
                        datos[nombre] = datos[lista]
                        print('Copiada!')
                elif menu == '5':
                    lista0 = input('Vuelve a ingresar el nombre de la lista: ')
                    if lista0 == lista:
                        eliminar_lista(datos, lista0)
                        print('Eliminada!')
                    else:
                        print('Cancelado')
                else:
                    print('Volver')
        
        elif menu == 'w':
            nuevo = guardar(archivo, datos)
            print('Datos guardados!')
        
        else:
            if not nuevo:
                with open(archivo+'.json', 'r') as file:
                    mod = json.load(file) != datos
            if nuevo or mod:
                print('Hay datos sin guardar')
                print('[x] Salir sin guardar')
                print('[w] Guardar y salir')
                print('o ignorar para cancelar')
                x = input()
                if x == 'x':
                    break
                elif x == 'w':
                    mod = guardar(archivo, datos)
                    break
            else:
                break
        print('...')
        sleep(1)
        os.system('clear')

print('Saliendo!')
sleep(1)
os.system('clear')
