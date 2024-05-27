"""
Написати програму для обходу графа за алгоритмом пошуку в ширину:
"""

from collections import deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Представлення графа списком суміжності
graph = {
    1: [2, 6, 8],
    2: [1, 3, 5],
    3: [2, 4, 6, 7],
    4: [3, 5, 7],
    5: [2, 4, 6],
    6: [1, 3, 5, 7],
    7: [3, 4, 6, 8],
    8: [1, 7]
}

#Запустіть BFS з вершини яку обирете нижче
bfs(graph, 5)
