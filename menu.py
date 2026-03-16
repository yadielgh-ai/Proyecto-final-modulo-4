# importando funciones:
from gestor_clientes import *

# menú de instrucciones

def menu():
    opcion = 0
    print(" Bienvenido al gestor de clientes")

    while True:
        print("""
        Escoja alguna de las siguientes opciones: 
        1: Crear Cliente  
        2: Editar Cliente    
        3: Eliminar Cliente
        4: Mostrar todos los clientes
        5: Mostrar un cliente
        4: Salir
        """)

        opcion = input("")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            editar_cliente()  # Se hará solo por teléfono en este caso.
        elif opcion == "3":
            eliminar_cliente()
        elif opcion== "4":
            mostrar_clientes()   # en este caso se mostrará la lista completa, queda pendiente mostrar clientes por categoría.
        elif opcion== "5":
            mostrar_cliente()
        elif opcion == "4":
            break
        else:
            print ("opcion no válida, inténtelo de nuevo")    
