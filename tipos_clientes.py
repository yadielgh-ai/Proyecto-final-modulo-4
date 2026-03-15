
# En este módulo se muestran las clases hijas de cliente:


from cliente import *



class ClienteRegular(Cliente):
    def beneficio(self):
        return "cliente si beneficios especiales"
    

class ClientePremium(Cliente):
    def beneficio(self):
        return "Cliente con 10% de descuento"
    

class ClienteCorporativo(Cliente):
    def beneficio(self):
        return "cliente con facturación"
    
    
    