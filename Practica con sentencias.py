
'''Construye un programa que lea un numero entero y determine si
el resultado de sumar sus dos ultimos 
es un numero de 1 digito '''
number = int(input("Put a number: "))
# intentando separar el digito
lastnumber= number % 100
# Ahora hay que separar los digitos
digit1 = lastnumber % 10
digit2 = lastnumber // 10
## ahora se pone la suma 
adition = digit1 + digit2

if adition <= 10:
     print("Your last digit plus your penultimate digit is shorter than 10")
else:
     print("Your last digit plus your penultimate digit is bigger than 10")

# '''
# Construir un programa que lea dos numeros enteros y determine si
# el primer numero leido es mayor que el segundo
# numero leido
# '''
# print("Hi :3")
# number = int(input("\nPut a number: ")) 
# number2 = int(input("\nPut a number: "))
# if number > number2:
#      print("Your first number is bigger than your second number ")
# elif number2 > number:
#      print("Your second number is bigger than your first number")
# else:
#      print(f"Ambos son iguales {number} = {number2}")