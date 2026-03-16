
# Importando métodos necesarios
from validaciones import *


# creación de la clase Padre y clases hijas.

class Cliente():
    def __init__(self,rut, nombre, email, telefono, direccion):
        self._rut = rut   # incluyo el rut para utilizarlo como id.
        self._nombre = nombre
        self._email= validar_email(email)
        self._telefono =  validar_telefono(telefono)
        self._direccion = direccion

    # método especial para imprimir los valores:
    def __str__(self):
        return f"RUT: {self._rut} | Nombre: {self._nombre} | Teléfono: {self._telefono} | Beneficio: {self.beneficio()}"



    # incluir método para vlaidar rut y datos en general.

# POR MOTIVO DE SIMPLICIDAD EN ARAS DEL TIEMPO PREVISTO PARA EL PROYECTO,  LAS VALIDACIONES SON MUY BÁSICAS. 
    def set_rut(self, nuevo_rut):  
        self._rut= nuevo_rut

    def set_nombre(self, nuevo_nombre): 
        self._nombre= nuevo_nombre

    def set_email(self, nuevo_email): 
        self._email= nuevo_email

        self._email= nuevo_email

    def set_telefono(self, nuevo_telefono):
        self._telefono= nuevo_telefono

    def set_direccion(self, nueva_direccion):  
        self._direccion = nueva_direccion

    def get_rut(self):
        return self._rut

    def beneficio(self):
        pass


    