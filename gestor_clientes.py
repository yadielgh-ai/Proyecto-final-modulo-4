


# Este gestor se encargará de gestionar todos los clientes, clasificar por tipo etc..
# NOTA: Me parece muy largo este archivo, debería hacerlo una clase como hizo el profe.


from cliente import *
from tipos_clientes import *



# voy a trabajar con 1 lista de clientes, la cual va a tener los 3 tipos de objetos.
# A los objetos específicos dentro de la lista, puedo identificarlos mediante: isinstance

clientes=[]   # lista que va a contener todos los objetos creados.

# Función que se encarga de pedir los datos para poder crear el cliente, además ejecuta validaciones simples

def pedir_datos_cliente():                

    while True:                             # falta añadirle la opción para que cancele la emtrada de datos si no quiere continuar
        rut = input ("Introduzca el rut")
        
        try:
            rut_validado = validar_rut(rut)
            break
        except ValueError as e:
            print(e)
    
    nombre = input ("Introduzca el nombre")

    while True:    
        email = input ("Introduzca el email")
        try:
            email_validado= validar_email(email)
            break
        except ValueError as e:
            print(e)

    while True:    
        telefono = input ("Introduzca el número de teléfono")
        try:
            telefono_validado= validar_telefono(telefono)
            break
        except ValueError as e:
            print(e)

    direccion= input ("Introduzca la dirección")


    return  rut_validado, nombre, email_validado, telefono_validado, direccion  


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
        

# Una vez introducidos los datos de la clase cliente ( rut, teléfono etc..) y definido el tipo de cliente,
# se instancia para crear el objeto específico.
# Función para crear los clientes y guardar en listas en dependencia del tipo de cliente


def crear_cliente():

    rut, nombre, email, telefono, direccion = pedir_datos_cliente()    # llama a la función para pedir datos

    tipo = consultar_tipo_cliente()     # se llama a la función para conocer el tipo de cliente
    tipo_cliente= ["Regular", "Premium", "Corporativo"]  # lista solo para escribir (print) el tipo de cliente que se creó

    if tipo == "1":
        cliente_new= ClienteRegular(rut, nombre, email, telefono, direccion)
        
    elif tipo == "2":
        cliente_new= ClientePremium(rut, nombre, email, telefono, direccion)

    elif tipo == "3":
        cliente_new= ClienteCorporativo(rut, nombre, email, telefono, direccion)

    clientes.append(cliente_new)

    print(f"Cliente {tipo_cliente[int(tipo)-1]} creado correctamente")   # lo que aparece entre corchetes es para que salga el nombre del tipo de clientes creado


# NOTA: En aras del tiempo, las funciones se dejan muy simples.

# Devuelve el objeto en la lista, si no lo encuentra, devolver que no existe.

#-------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def buscar_cliente():    # no se valida el rut porque no interesa de momento, lo pero que puede pasar es que busque en vano.
    rut_a_buscar = input ("introduzca el rut del cliente")    
    
    for cliente in clientes:

        if cliente.guet_rut() == rut_a_buscar:    
            return cliente
    
    return None   # devuelve None si no encuentra el rut  

# ------------------------------------------------------------------------
#----------------------------------------------------------------------------

#Función para editar un cliente según su número de teléfono

def editar_cliente():  
    cliente = buscar_cliente()   # Primero busca el cliente

    if cliente:
        while True:
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            try:
                telefono_validado = validar_telefono(nuevo_telefono)
                cliente.set_telefono(telefono_validado)
                print("Teléfono actualizado correctamente")
                break
            except ValueError as e:
                print(e)
    else:
        print("Rut no encontrado")

#-----------------------------------------------------------------
#   ELIMIMNAR CLIENTE (primero lo busco y después lo elimino si existe)
#-----------------------------------------------------------------

def eliminar_cliente():

    cliente = buscar_cliente()   # llamada a funcion para buscar cliente
    if cliente:
        clientes.remove(cliente)
        print("Cliente eliminado")
    else:
        print("Cliente no encontrado")


#-----------------------------------------------------------------
#   MOSTRAR TODOS LOS CLIENTE
#-----------------------------------------------------------------

def mostrar_clientes():                # esta se pudiera dividir en 3 funciones para mostrar los específicos. Dejar para próxima versión.

    cliente_regular=[]
    cliente_premium=[]
    cliente_corporativo=[]
    for cliente in clientes:
        if isinstance(cliente, ClienteRegular):
            cliente_regular.append(cliente)
        elif isinstance(cliente, ClientePremium):
            cliente_premium.append(cliente)
        else:
            cliente_corporativo.append(cliente)
    
    print("Clientes Regulares:  ")
    for cliente in cliente_regular:
        print(cliente)

    print("Clientes Premium:  ")
    for cliente in cliente_premium:
        print(cliente)

    print("Clientes Corporativos:  ")
    for cliente in cliente_corporativo:
        print(cliente)

    