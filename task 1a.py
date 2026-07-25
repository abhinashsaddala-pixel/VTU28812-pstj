from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}
def bfs(start, goal=None):
    if start not in graph:
        print(f"Start node '{start}' does not exist in the graph.")
        return
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        if goal is not None and node == goal:
            print("\nGoal node found!")
            return
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    if goal is not None:
        print("\nGoal node not found!")
    else:
        print()
if __name__ == "__main__":
    start = input("Enter starting node: ").strip().upper()
    goal_input = input("Enter goal node (or press Enter to skip): ").strip()
    goal = goal_input.upper() if goal_input else None
    print("\nBFS Traversal:")
    bfs(start, goal)
