## Sentencias de condicionales

૮ ˶ᵔ ᵕ ᵔ˶ ა  
##### Las sentencias condicionales son estructuras que permiten que tu programa tome decisiones y ejecute diferentes fragmentos de código dependiendo de si una condición se cumple (True) o no (False)

##### Una sentencia condicional es un esquema de instrucciones que permite escoger uno de entre dos caminos lógicos o uno de entre varios caminos logicos, a partir de estas condiciones se validan datos. *¿Que significa esto?*, para que se cumplan determinadas condiciones que sean favorables a los programas que construyamos.

### Operadores lógicos:

#### Operador **and** que genera Verdadero en caso de que las dos condiciones que conecto son verdaderas.

#### Operador **or** que genera Verdadero si al menos **UNA** de las condiciones que conecte es *Verdadera*.

#### Operador **not** que invierte el sentido lógico de una expresión relacional; si es Verdadera la vuelva Falsa y viceversa.

### Ejemplo de aplicabilidad

```python
#Construir un programa que lea un numero y determine si es un numero positivo

#Datos de numeros
NumDelectura = int(input("Coloca tu numero :3 (TIENE que ser largo)"))

#determina si es un numero positivo 
print("\nEstamos procesando tu numero")

if NumDelectura >= 0:
     print("felicidades su numero es positivo")
else: 
     print("no es un numero positivo")
```
### Operadores y capacidades especiales
###### Comparación: Utilizas símbolos como == (igual), != (distinto), <, >, <=, >=

###### -**Lógicos:** Puedes combinar condiciones usando and (y), or (o) y not (no/negación)
###### -**Encadenamiento:** Python permite escribir condiciones de forma matemática directa, por ejemplo: if 18 <= edad < 35:
###### -**Operador Ternario:** Existe una forma compacta de escribir un if-else en una sola línea: valor = A if condicion else B

```python
Aca van algunos ejercicios aplicables de este concepto
'''Construye un programa que lea un numero entero y determine si
el resultado de sumar sus dos ultimos 
es un numero de 1 digito'''
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

```
