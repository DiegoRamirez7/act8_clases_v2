class informacion:

    def mi_lista(self):
        lista_Nomperros=["body","dollar","fany"]
        for x in lista_Nomperros:
            print(x)

    def mi_Dic(self):
        dicc_Alumnno = {
            "nombre" : "Diego Ramirez",
            "nac": 2007,
            "salon" : 29
        }
        for x,z in dicc_Alumnno.items():
            print(x,z)
        
                

    def mi_conjunto(self):
        lista_Nomcarros=["camaro","mustang","charger"]
        for x in lista_Nomcarros:
            print(x)

    def mi_tupla(self):
        lista_Nomcolores=["azul","rojo","gris"]
        for x in lista_Nomcolores:
            print(x)                
# creando el objeto

datos=informacion()
print("listado de nombre de perros")
datos.mi_lista()
print("--mi diccionario--")
datos.mi_Dic()
print("--mi conjunto--")
datos.mi_conjunto()
print("--mi tupla--")
datos.mi_tupla()


