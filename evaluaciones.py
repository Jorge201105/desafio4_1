from pizza import Pizza


##print(Pizza.precio)## Metodo estatico se logra resultado sin instanciar
##print(Pizza.validador("salsa de tomate", ["salsa de tomate","salsa bbq"]))
  ## se instancia para obtener resultados de metodo no estatico
c=Pizza() ##Instanciando la clase , se solicitan los inredientes, 
c.pedido() ## Llamo el resultado del if en def pedido el que da el print, no pude colocar como variable el self.proteico porque esta fuera de la clase y arrogaba error.

print(f" La pizza es valida si el parametro siguiente es True y no valida si es False : {c.valida}")
print(Pizza.valida) ## Haciendo print sin instanciar la clase, 

