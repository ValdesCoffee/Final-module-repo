import json
import random
import csv
from rankingthemain import ranking
from otrawea import participantes
from datetime import datetime

# Cargar preguntas
with open('Preguntas.json', encoding='utf-8') as f:
    read = json.load(f)

# Nombre del jugador principal (para el saludo)
def ask():
    ask = input("Holiii, ¡Coloca tu nombre por favor! ⋆˚꩜｡ ")
    # Pregunta el nombre hasta que lo ponga
    while not ask:
        ask = input("You must enter your name: ")

    return ask

def jugar_ronda():
    score = 0
    correct = 0
    nombre_player = ask()
    print(f"\n¡Bienvenido/a {nombre_player}!\n")
    
    # Seleccionar 5 preguntas aleatorias
    preguntas_seleccionadas = random.sample(read, 5)
    
    for pregunta in preguntas_seleccionadas:
        print(f"\n{pregunta['pregunta']}")
        print(pregunta['opciones'])
        
        respuesta = input("\nTienes que elegir entre A B C D\n¿Cuál es tu respuesta?: ").strip().upper()
        
        if respuesta == pregunta.get("respuesta_correcta"):
            print("¡Correcto! Has ganado 20 puntos ❁\n")
            score += 20
            correct += 1 # Cantidades de respuestas correctas
        else:
            print(f"Incorrecto ┗( T﹏T )┛ \nLa respuesta correcta era: {pregunta['respuesta_correcta']}\n")
    
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    participantes.append({"nombre": nombre_player, "puntuacion": score, "fecha": fecha_hora})

    print(f"¡Fin del quiz! Tu puntuación total es: {score} puntos")
    print(f" y la cantidad de respuestas correctas fueron {correct}\n")

# Bucle principal
if __name__ == "__main__":
    while True:
        jugar_ronda()
        
        seguir = input("¿Quieres jugar otra ronda? (sí/no): ").strip().lower()
        if seguir not in ["sí", "si", "s", "yes", "y"]:
            ultimo_nombre = participantes[-1]["nombre"]
            print(f"¡Gracias por jugar, {ultimo_nombre}")
            break

    # Guardar participantes en archivo CSV
    # Esto añade datos al final en lugar de borrar todo
    with open("participantes.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "puntuacion", "fecha"])
        # Solo escribe la cabecera si el archivo está vacío
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(participantes[-1])

    rank = input("¿Desea consultar el ranking actual? (sí/no): ")
    if rank not in ["sí", "si", "s", "yes", "y"]:
        print("¡Hasta la próxima! ¡Nos vemos!")
    else:
        ranking()