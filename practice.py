from collections import deque

def printLevelByLevel(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

           # Print the node at the current level

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  
                    visited.add(neighbor)# Enqueue neighboring nodes

        print("Level Separator")  # Print a separator between levels


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

startNode = 'A'

print("Printing level by level:")
printLevelByLevel(graph, startNode)
