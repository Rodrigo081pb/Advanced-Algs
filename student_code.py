def shortest_path(graph, start, goal, heuristic):
    """
    Implementa o algoritmo de busca A* para encontrar o caminho mais curto entre start e goal.
    graph: dict, onde as chaves são nós e os valores são listas de tuplas (vizinho, custo)
    start: nó inicial
    goal: nó objetivo
    heuristic: função que estima o custo do nó atual até o objetivo
    """
    from heapq import heappop, heappush

    open_set = set([start])
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
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
        for neighbor, cost in graph.get(current, []):
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    open_set.add(neighbor)
                    heappush(heap, (f_score[neighbor], neighbor))
    return None  # Caminho não encontrado
