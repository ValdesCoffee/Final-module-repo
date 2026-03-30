
## 1. Estructura del Proyecto (Modulación)

El código está dividido en **tres módulos** (archivos) para mantener una buena organización y seguir el principio de responsabilidad única:

| Archivo              | Propósito Principal                              | Contenido Principal |
|----------------------|--------------------------------------------------|---------------------|
| `otrawea.py`         | Almacenamiento de datos compartidos              | Lista global `participantes` |
| `rankingmain.py`     | Mostrar el ranking global                        | Función `ranking()` |
| `proceso.py`         | Lógica principal del juego y persistencia        | Flujo del quiz, guardado CSV y llamada al ranking |

**Ventajas de esta modulación:**
- Código más limpio y fácil de mantener.
- Cada archivo tiene una única responsabilidad.
- Permite reutilizar funciones entre módulos mediante `import`.

---

## 2. Análisis Detallado de Cada Archivo y Variables

### 2.1. `otrawea.py`

```python
participantes = []
```

**Explicación:**
- `participantes` es una **lista global** que se importa en los otros archivos.
- Sirve para guardar temporalmente en memoria todos los jugadores que participan durante la ejecución.
- Cada elemento es un **diccionario** con esta estructura:
  ```python
  {
      "nombre": "Nombre del jugador",
      "puntuacion": 80,           # entero
      "fecha": "2026-03-29 22:15:30"
  }
  ```

---

### 2.2. `rankingmain.py`

```python
import csv
from otrawea import participantes

def ranking():
    try:
        with open('participantes.csv', encoding='utf-8') as f:
            read = list(csv.DictReader(f))
            
            ranking_ordenado = sorted(
                read, 
                key=lambda x: int(x['puntuacion']), 
                reverse=True
            )
            
            print("--- 🏆 TOP GLOBALES 🏆 ---")
            for i, p in enumerate(ranking_ordenado[:10], start=1):
                print(f"{i}. {p['nombre']} - {p['puntuacion']} pts")
                
    except FileNotFoundError:
        print("Aún no hay archivo de participantes.")
```

**Explicación paso a paso:**

- `csv.DictReader(f)`: Lee el archivo CSV y convierte cada fila en un diccionario.
- `sorted(..., key=lambda x: int(x['puntuacion']), reverse=True)`: Ordena los participantes de mayor a menor puntuación.
- `enumerate(..., start=1)`: Numera el ranking empezando desde 1.
- Solo muestra los **10 mejores** jugadores.
- Si el archivo `participantes.csv` no existe, muestra un mensaje amigable.

---

### 2.3. `proceso.py` – Archivo Principal

#### a) Carga inicial de preguntas
```python
import json
with open('Preguntas.json', encoding='utf-8') as f:
    read = json.load(f)
```
- `read`: Variable que contiene **todas** las preguntas cargadas del archivo JSON.

#### b) Función `ask()` – Pedir nombre
```python
def ask():
    ask = input("Holiii, ¡Coloca tu nombre por favor! ⋆˚꩜｡ ")
    while not ask:                       # Repite mientras esté vacío
        ask = input("You must enter your name: ")
    return ask
```
- Valida que el usuario ingrese un nombre.
- Retorna el nombre introducido.

#### c) Función `jugar_ronda()` – Lógica del juego

**Variables importantes:**

| Variable              | Tipo     | Función |
|-----------------------|----------|-------|
| `score`               | int      | Acumula la puntuación (20 puntos por respuesta correcta) |
| `correct`             | int      | Cuenta cuántas respuestas fueron correctas |
| `nombre_player`       | str      | Nombre del jugador actual |
| `preguntas_seleccionadas` | list | 5 preguntas elegidas aleatoriamente con `random.sample()` |
| `fecha_hora`          | str      | Fecha y hora actual en formato `YYYY-MM-DD HH:MM:SS` |

**Proceso dentro de la ronda:**
1. Se selecciona 5 preguntas aleatorias.
2. Para cada pregunta:
   - Se muestra la pregunta y las opciones.
   - Se recibe la respuesta del usuario (A, B, C o D).
   - Se compara con `pregunta.get("respuesta_correcta")`.
   - Si es correcta → `score += 20` y `correct += 1`.
3. Al terminar las 5 preguntas:
   - Se crea un diccionario con los datos del jugador.
   - Se agrega a la lista global `participantes.append({...})`.

---

#### d) Bucle Principal y Guardado en CSV

```python
if __name__ == "__main__":
    while True:
        jugar_ronda()
        
        seguir = input("¿Quieres jugar otra ronda? (sí/no): ").strip().lower()
        if seguir not in ["sí", "si", "s", "yes", "y"]:
            break

    # === PROCESO DE EXPORTACIÓN A CSV ===
    with open("participantes.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "puntuacion", "fecha"])
        
        # Escribe la cabecera solo si el archivo está vacío
        if f.tell() == 0:
            writer.writeheader()
        
        # Guarda SOLO el último participante
        writer.writerow(participantes[-1])
    
    # Pregunta si quiere ver el ranking
    rank = input("¿Desea consultar el ranking actual? (sí/no): ")
    if rank in ["sí", "si", "s", "yes", "y"]:
        ranking()
```

**Explicación detallada del guardado en CSV:**

- `"a"` → Modo **append** (añadir al final, sin borrar datos anteriores).
- `csv.DictWriter` → Objeto que facilita escribir diccionarios como filas CSV.
- `fieldnames` → Define el orden de las columnas: `nombre`, `puntuacion`, `fecha`.
- `if f.tell() == 0:` → Detecta si el archivo es nuevo y escribe la fila de encabezados.
- `writer.writerow(participantes[-1])` → Escribe únicamente el último jugador registrado.

**Nota:** Actualmente solo se guarda el último jugador de cada ejecución completa. Si se juegan varias rondas, solo se guarda la última.

---

## 3. Flujo Completo del Sistema

1. Se ejecuta `proceso.py`
2. Se cargan las preguntas desde `Preguntas.json`
3. Bucle de juego:
   - Pedir nombre
   - Jugar 5 preguntas aleatorias
   - Guardar resultado en memoria (`participantes`)
   - Guardar resultado en disco (`participantes.csv`)
   - Preguntar si quiere jugar otra ronda
4. Al finalizar → Opción de ver el ranking (lee y ordena el CSV)

---

## 4. Resumen de Funciones y Variables Clave

- **`participantes`** (lista global): Almacena todos los jugadores en memoria.
- **`score`**: Puntuación acumulada en la ronda actual.
- **`correct`**: Cantidad de respuestas correctas.
- **`ranking_ordenado`**: Lista ordenada por puntuación descendente.
- **`csv.DictWriter`**: Herramienta para escribir datos en formato CSV.
- **`csv.DictReader`**: Herramienta para leer datos del CSV como diccionarios.

---

