def Depth_First_Search(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

def Breadth_First_Search(graph, start):
    queue = [start]
    visited = set()

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited

graph = {
    1: {3, 5},
    2: {4},
    3: {5, 6},
    4: {2},
    5: {6},
    6: {5}
}

print(Depth_First_Search(graph, 2))
print(Breadth_First_Search(graph, 1))