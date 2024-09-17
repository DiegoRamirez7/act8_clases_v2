print("clases version 2 el constructor")

class Perro:
    ## funcion constructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    # funciones creadas por el usuario
    def morder(self):
        print("chale el perro me mordio")
    def chatperro(mensaje):
        print(f"chat perro: {mensaje}")
    def chatperra(mensajep):
        print(f"chat perro: {mensajep}")
    def datos(self):
        print(f"color: {self.color} edad: {self.edad}")
##llamadas a funciones
chihuas=Perro("negro",2)
##llamadas a funciones 
chihuas.datos()
chihuas.morder()