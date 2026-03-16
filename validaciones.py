# validar rut, dirección y teléfono
# estas validacionas las usaré en la clase (constructor) para proteger los datos de entrada.
# además la utilzaré de forma interctiva en la entrada de datos del usuario

# NOTA: Las validaciones son bastante básicas.

def validar_rut(rut):
    if not rut.isdigit():       # comprueba que solo se escriban números, si algún caracter no es número, se escribe 
        raise ValueError("Rut inválido, solo introducir números")
    
    return rut


def validar_email(email):

    if "@" not in email:
        raise ValueError("Email inválido")

    return email


def validar_telefono(telefono):    # proximamente se le pueden agregar verificacion de cantidad de números y utilizar bibliotecas

    if not telefono.isdigit():    # comprueba que solo se escriban números, si algún caracter no es número, se escribe 
        raise ValueError("El teléfono debe contener solo números")

    return telefono       