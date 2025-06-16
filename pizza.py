


class Pizza():
    precio = 10000
    tamaño = "familiar"

    

    @staticmethod
    def validador():
        lista = []
        while True:
            ingrediente = input("Ingrese un ingredeinete o tipo, escriba fin para terminar : ")
            if ingrediente =="fin":
                break
            lista.append(ingrediente)

        elemento = input("valide su ingrediente o tipo de masa : ")

        if elemento in lista:
            return True, print("el elemento es valido")
        else:
            return False, print ("ele elemento no es valido")
        



        
