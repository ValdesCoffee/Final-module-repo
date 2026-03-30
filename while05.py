# Crea un menú con while que permita al usuario elegir entre
# opciones (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y solo termine
# cuando elija la opción de salir.
chs= "1"
while chs!= 3:
    chs= int(input("1.Saludar\n2.Despedirse\n3.Salir"))
    if chs == 1:
        print("Hi :)")
    elif chs == 2:
        print("Chao")
    else:
        break
