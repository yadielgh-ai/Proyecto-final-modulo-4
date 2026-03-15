


# este gestor se encargará de gestionar todos los clientes, clasificar por tipo etc..

from cliente import *



# voy a trabajar por 1 lista de clientes, la cual va a tener los 3 tipos de objetos.
# A los objetos específicos dentro de la lista, puedo identificarlos mediante: isinstance

clientes=[]

# Funcion que se encarga de pedir los datos para porder crear el cliente

def pedir_datos_cliente():

    while True:  # los while creo se pueden poner en las validaciones
        rut = input ("Introduzca el rut")
        #validar Rut_ crear funciones de validació en otro archivo, de esa forma lo puedo utilizar cuando quiera
        # si el rut está ok, continuar, si no, rut inválido
        # para mejorar puedo icluir que si comete 3 errores se cierra la función y tiene que comenzar de nuevo.
    nombre = input ("Introduzca el nombre")
    while True:    
        email = input ("Introduzca el email")
        # validar email
        pass
    while True:    
        telefono = input ("Introduzca el número de teléfono")
        # validar teléfono
        pass
    while True:    
        direccion= input ("Introduzca la dirección")
        # validar dirección
        pass

    return  rut, nombre, email, telefono, direccion  


# Función que permite elegir el tipo de cliente, devuelve el tipo de cliente.
def consultar_tipo_cliente():
    while True:         # en este bucle queda pendiente implementar la opción de cancelar.
        
        tipo_cliente=0
        
        print("""  
        Indique el tipo de cliente introduciendo el número de la opción:
        1: Regular
        2: Premium
        3: Corporativo
        """)
        tipo_cliente= input( )
        
        if tipo_cliente in ["1", "2", "3"]:  # comprueba si el valor está contenido en la lista
            return tipo_cliente
        else:
            print("opción inválida, inténtelo de nuevo")
        

# Función para crear los clientes y guardar en listas en dependencia del tipo de cliente


def crear_cliente():

    rut, nombre, email, telefono, direccion = pedir_datos_cliente()

    tipo = consultar_tipo_cliente()
    tipo_cliente= ["Regular", "Premium", "Corporativo"]

    if tipo == "1":
        cliente_new= ClienteRegular(rut, nombre, email, telefono, direccion)
        
    elif tipo == "2":
        cliente_new= ClientePremium(rut, nombre, email, telefono, direccion)

    elif tipo == "3":
        cliente_new= ClienteCorporativo(rut, nombre, email, telefono, direccion)

    clientes.append(cliente_new)

    print(f"Cliente {tipo_cliente[int(tipo)-1]} creado correctamente")   # lo que aparece entre corchetes es para que salga el nombre del tipo de clientes creado


# EN PROCESO DE CREACIÓN

# Puede devolver la posición del cliente en la lista, si no lo encuentra, devolver que no existe.

def buscar_cliente():
    rut_a_buscar = input ("introduzca el rut del cliente")
    
    for i, cliente1 in enumerate(clientes):  # enumerate va contando el índice
        if cliente1.rut== rut_a_buscar:
            return i   # devuelve la posición en del objeto con el rut buscado
    
    return None   # devuelve None si no encuentra el rut  


#Función para editar un cliente según su número

def editar_cliente():  # en este caso se editará solamente el número de teléfono.
    resultado= buscar_cliente()
    if resultado != None:
        nuevo_telefono = input ("ingrese el nuevo número:  ")   # ver cómo coño valido el número y dónde
        clientes[resultado].cambiar_teléfono(nuevo_telefono)
    else:
        print("Rut no encontrado")
