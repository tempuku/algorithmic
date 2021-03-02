def bfs(graph, start, goal):
    explored = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                print(queue)
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
    print("So sorry, but a connecting" \
          "path doesn't exist :(")
    return


if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["a", "d", "f"],
        "c": ["a", "d", "e"],
        "d": ["b", "c"],
        "e": ["c", "f", "i"],
        "f": ["b", "e", "g", "i"],
        "g": ["f", "h", "i"],
        "h": ["g", "j"],
        "i": ["e", "f", "g", "j"],
        "j": ["i"]}
    bfs(graph, 'a', 'j')
