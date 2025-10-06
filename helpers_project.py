import pickle
import os

class Map:
    def __init__(self, intersections, roads):
        self.intersections = intersections
        self.roads = roads

def load_map(filename):
    """
    Carrega um mapa a partir de um arquivo pickle.
    Se não encontrar, retorna um mapa de exemplo.
    """
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return Map(data['intersections'], data['roads'])
    else:
        # Exemplo mínimo para testes
        intersections = {
            0: (0, 0),
            1: (1, 1),
            2: (2, 2)
        }
        roads = [ [1], [0,2], [1] ]
        return Map(intersections, roads)

def show_map(map_obj, start=None, goal=None, path=None):
    """
    Função mock para visualização. Apenas imprime informações básicas.
    """
    print("Intersections:", map_obj.intersections)
    print("Roads:", map_obj.roads)
    if start is not None:
        print(f"Start: {start}")
    if goal is not None:
        print(f"Goal: {goal}")
    if path is not None:
        print(f"Path: {path}")
