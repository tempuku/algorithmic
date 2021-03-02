import sys
from collections import defaultdict
import fileinput
from graphs.bfs.bfs_dict import bfs


def graph_create(cities_nodes, distance_max):
    graph = defaultdict(list)
    for i in range(len(cities_nodes)):
        for j in range(len(cities_nodes)):
            if i == j:
                continue
            distance = abs(cities_nodes[i][0] - cities_nodes[j][0]) + abs(cities_nodes[i][1] - cities_nodes[j][1])
            if distance <= distance_max:
                graph[i].append(j)
    return graph


def interesting_travel(cities_nodes, cities_start_end, distance_max):
    graph = graph_create(cities_nodes, distance_max)
    result = bfs(graph, cities_start_end[0], cities_start_end[1])
    return len(result) - 1 if result else -1


if __name__ == '__main__':
    stdin_fileno = sys.stdin.readlines()
    cities_nodes = []
    cities_number = int(stdin_fileno.pop(0))
    for line in range(cities_number):
        cities_nodes.append([int(x) for x in stdin_fileno[line].split()])
    distance_max = int(stdin_fileno[cities_number])
    cities_start_end = [int(x) for x in stdin_fileno[cities_number + 1].split()]
    result = interesting_travel(cities_nodes, cities_start_end, distance_max)
    sys.stdout.write(str(result))
