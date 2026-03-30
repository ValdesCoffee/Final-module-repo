## 𐙚 ‧₊˚ ⋅ Funciones

૮ ˶ᵔ ᵕ ᵔ˶ ა  
#### Es un conjunto breve de instrucciones que permiten alcanzar facilmente un pequeño objetivo. Una **función** es una secuencia de instrucciones con nombre que realiza una tarea específica y solo se ejecuta al ser invocada. Se define usando **def**, seguido de su nombre y paréntesis. Su fin es **organizar el código**, evitar la duplicación y abstraer algoritmos complejos para que el programa sea legible y fácil de mantener. Pueden recibir **parámetros** y devolver resultados mediante **return**; si este falta, retornan **None**.

### Ejemplos de funciones
```python
nombre = input("n\Hola coloca tu nombre: ")

def ponernombre5():
    print(nombre*5)

ponernombre5()
```
#### Este es bastante sencillo pero sigue la regla de DEF + NOMBRE + PARAMETROS.

```python 
#Construir una funcion que reciba una lista de datos numericos y retorna la suma de dichos datos
print("*"*15)
print("Bienvenido :D")
print("="*15)
def funcionreturnsuma():
    colocanum = int(input("Coloca un numero : "))
    colocanum2 = (int(input("Coloca un numero : ")))
    colocanum3 = (int(input("Coloca un numero : ")))
    print(colocanum+colocanum2+colocanum3)
    return colocanum, colocanum2, colocanum3
funcionreturnsuma()

```