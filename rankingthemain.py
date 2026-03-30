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