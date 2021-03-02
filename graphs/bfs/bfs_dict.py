def bfs(graph, start, end):
    visited = [start]
    queue = [start]
    hierarchy = {start: None}

    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            path = [end]
            child = end
            while start not in path:
                path = [hierarchy[child]] + path
                child = hierarchy[child]
            return path

        for node in graph[current]:
            if node not in visited:
                visited += [node]
                queue += [node]
                hierarchy[node] = current
    return


if __name__ == '__main__':
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
    result = bfs(graph, 'a', 'j')
    # print(result)
