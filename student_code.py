def shortest_path(map_obj, start, goal, heuristic):
    """
    Implementa o algoritmo de busca A* para encontrar o caminho mais curto entre start e goal.
    map_obj: objeto Map contendo intersections e roads
    start: nó inicial
    goal: nó objetivo
    heuristic: função que estima o custo do nó atual até o objetivo
    """
    from heapq import heappop, heappush
    import math

    def distance(node1, node2):
        """Calcula a distância euclidiana entre dois nós"""
        x1, y1 = map_obj.intersections[node1]
        x2, y2 = map_obj.intersections[node2]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    open_set = set([start])
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(map_obj, start, goal)}
    heap = [(f_score[start], start)]

    while heap:
        _, current = heappop(heap)
        if current == goal:
            # Reconstrói o caminho
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        
        open_set.discard(current)
        
        for neighbor in map_obj.roads[current]:
            # Usa distância euclidiana real entre os nós
            edge_cost = distance(current, neighbor)
            tentative_g_score = g_score[current] + edge_cost
            
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(map_obj, neighbor, goal)
                
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    heappush(heap, (f_score[neighbor], neighbor))
    
    return None  # Caminho não encontrado
