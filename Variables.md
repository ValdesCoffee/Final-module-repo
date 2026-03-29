## 𐙚 ‧₊˚ ⋅ Operadores de datos y tipos de variables en python 

૮ ˶ᵔ ᵕ ᵔ˶ ა  
#### Un operador es un caracter que representa una operacíon. Un grupo de operadores que usan Python son los operadores aritmeticos. Su significado, representacion y uso se presenta a continuación.
---

## 𐙚 ‧ Tipos de operadores 
```python

| Significado    | Signo         | Uso                                                | 
|--------------  |---------------|----------------------------------------------------|
| Suma           | +             | Obtiene el resultado de sumar dos valores          |
| Resta          | -             | Obtiene la diferencia entre dos valores            |
| Multiplicación | *             | Obtiene el producto entre dos valores              |
| División       | /             | Obtiene el resultado de dividir un valor entre otro|
| Modulo         | %             | Obtiene el residuo de una división                 |
| División entera| //            | Obtiene el producto entre dos valores              |
| Potenciación   | **            | Obtiene el resultado de elevar una base            |
|                |               | a una potencia                                     |
---------------------------------------------------------------------------------------
```
## 𐙚 ‧ Tipos de datos
#### En este lenguahe de programación reconoce que tipo de dato puede almacenar dicha los principales datos son.
```python

| Tipo           | Signo         | Uso                                                | 
|--------------  |---------------|----------------------------------------------------|
|Entero          | int           | Numero sin punto decimal  corto                    |
| corto          |               |  Ejemplo: 45                                       |
|--------------- |---------------|----------------------------------------------------|
|Entero          | int           |Numero sin punto decimal, más grande                |
|largo           |               |   Ejemplo: 45678                                   |
|--------------- |---------------|----------------------------------------------------|
|Reales          | float         |Numerp con un punto decimal                         |
|                |               |   Ejemplo: 36.42                                   |
|--------------- |---------------|----------------------------------------------------|
|Cadenas         | str           |Cojunto de caracteres                               |
|                |               |   Ejemplo: "Hola                                   |
|--------------- |---------------|----------------------------------------------------|

```
#### Esta instrucción va acompañada de un tipo de dato (Como los que se encuentran) en la columna identificador Python de la tabla inmediatamente anterior y de un titulo que es el que aparece para indicarle al usuario que escriba lo que le solicitamos.

### ¿Como se veria aplicado esto en un ejercicio?
###### *Objetivo:* Construir un programa que lea un numero entero y determine si es un numero par.
```python
numero = int(input("Ingresa un número: "))
# Primero defines una variable tipo entero corto
if numero % 2 == 0:
    print("El número es Par")
# Utilizas una condicion con la variable antes definida
# y utilizas la modulo que busca el residuo de esa variable
 
# y si su residuo es = 0 es PAR
else:
    print("El número es Impar")
# y si deja residuo es IMPAR
```