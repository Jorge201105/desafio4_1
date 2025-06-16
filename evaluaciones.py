from pizza import Pizza

print(Pizza.precio)## Metodo estatico se logra resultado sin instanciar
print(Pizza.validador("salsa de tomate", ["salsa de tomate","salsa bbq"])) ## se instancia para obtener resultados de metodo no estatico
c=Pizza() ##Instanciando la clase 
c.pedido()
print(c.valida)
print(Pizza.valida) ## Haciendo print sin instanciar la clase, 

