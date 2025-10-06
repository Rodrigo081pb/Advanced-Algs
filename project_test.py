def test(shortest_path):
    """
    Testa a função shortest_path usando exemplos básicos.
    """
    from my_helpers import load_map
    map_40 = load_map('map-40.pickle')
    result = shortest_path(map_40, 5, 34)
    expected = [5, 12, 34]  # Caminho ótimo correto
    if result == expected:
        print("Teste passou! Caminho correto.")
    else:
        print(f"Teste falhou! Esperado: {expected}, obtido: {result}")
        # Vamos verificar se o resultado é válido mesmo que diferente
        import math
        def calcular_distancia_caminho(map_obj, caminho):
            distancia_total = 0
            for i in range(len(caminho) - 1):
                x1, y1 = map_obj.intersections[caminho[i]]
                x2, y2 = map_obj.intersections[caminho[i+1]]
                distancia_total += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            return distancia_total
        
        if result and len(result) >= 2 and result[0] == 5 and result[-1] == 34:
            dist_esperada = calcular_distancia_caminho(map_40, expected)
            dist_obtida = calcular_distancia_caminho(map_40, result)
            print(f"Distância esperada: {dist_esperada:.6f}")
            print(f"Distância obtida: {dist_obtida:.6f}")
            if abs(dist_obtida - dist_esperada) < 0.001:
                print("Mas a distância é equivalente - algoritmo correto!")
