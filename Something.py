# Construye un programa que lea un numero entero y determine si la 
# suma de sus dos ultimos digitos es igual a 7.

number = int(input("\nPut some number there: "))

lastnumber = number % 100
# Extraemos cada dígito por separado:
# El último dígito: número % 10
# El penúltimo dígito: (número % 100) // 10
digit1 = lastnumber % 10
digit2 = lastnumber // 10
# ahora se realiza la suma 
adition = (number % 10) + ((number % 100) // 10)
# Obtener los dos últimos dígitos y sumarlos directamente
if adition == 7:
     print("Your last digit is 7")
else: 
     print("Your last digit is not 7")