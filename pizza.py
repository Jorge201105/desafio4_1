from ingrediente import Ingredientes


class Pizza():## Creando clases para crear objetos tipo Pizza
    precio = 10000
    tamaño = "familiar"

    

    @staticmethod ## creando elementos para validar dos argumentos
    def validador(elemento:str, lista:list[str]):
        if elemento in lista:
            ### print("El elemento es valido")
            return True
        else:
            print(" El elemento no es valido")
            return False
        
    def pedido(self):### método para reaizar pedido
        proteico = input("Ingrese ingrediente proteico : ")
        vegetal1 = input("Ingrese primer vegetal : ")
        vegetal2 = input("Ingrese segundo vegetal : ")
        masa = input("Ingrese tipo de masa : ")

        # usando atributo de clase ingredente se valida cada uno de los datos ingresados

        v1 = Pizza.validador(proteico,Ingredientes.proteicos)
        v2 = Pizza.validador(vegetal1,Ingredientes.vegetales)
        v3 = Pizza.validador(vegetal2,Ingredientes.vegetales)
        v4 = Pizza.validador(masa,Ingredientes.masas)

        self.proteico = proteico
        self.vegetal1 = vegetal1
        self.vegetal2 = vegetal2
        self.masa = masa

        if v1 and v2 and v3 and v4:  ### se asigna a un atributo el valor True o False 
            print(f"El pedido es {self.proteico} , {self.vegetal1} , {self.vegetal2} , {self.masa}")
            self.valida = True
        else:
            print("Ingreaste mal un elemento")
            self.valida = False





       



   
