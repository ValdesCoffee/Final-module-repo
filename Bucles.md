## 𐙚 ‧₊˚ ⋅ Sentencias repetitivas

૮ ˶ᵔ ᵕ ᵔ˶ ა  
#### Una sentencia repetiva es una instrucción que permite que un conjunto de isntrucciones que se repita una cantidad de veces determinadas. En Python las dos sentencias repetitivas o iterativas más usadas son la instrucción *for* y la instrucción *while*.
---
### Uso del For
##### La sentencia **for** itera sobre secuencias como listas o tuplas. Su lógica es "**para cada elemento** en la colección". Es más segura que `while` pues el número de iteraciones suele conocerse de antemano y **termina automáticamente** al final de la secuencia, evitando bucles infinitos. Es muy legible porque gestiona automáticamente el acceso a los datos.

### Uso del While
##### La sentencia **while** repite un bloque de código **mientras una condición sea verdadera**. Se utiliza cuando **no puedes predecir** cuántas veces se repetirá la acción. Es fundamental que el código interno modifique la variable evaluada para que la condición sea falsa en algún momento y así **evitar un bucle infinito** que bloquee tu programa.
#### **Uso practico del FOR**
```python
#Por ejemplo esta sentencia utilizando un for
from time import sleep
for i in range (0, 10, 1):
    print(i+1)
    sleep(0.5)
```
#### **Uso practico del While**
```python
#contar de 1 al 10.
from time import sleep
i=1
while i < 10:
    print(i)
    i=i+1
    sleep(0.5)
```