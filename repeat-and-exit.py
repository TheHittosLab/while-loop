frase = "Lo que escribas, lo repito:"
frase += "\nIntroduce el comando 'salir' para finalizar el programa.\n"

mensaje = ""

while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)

print("Se ha salido del bucle.")
