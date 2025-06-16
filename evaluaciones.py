from pizza import Pizza

print(Pizza.precio)
print(Pizza.validador("salsa de tomate", ["salsa de tomate","salsa bbq"]))
c=Pizza() ##Instanciando la clase 
c.pedido()
print(c.valida)
print(Pizza.valida) ## Haciendo print sin instanciar la clase, 

