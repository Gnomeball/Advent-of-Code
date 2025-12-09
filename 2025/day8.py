from math import prod, dist
from itertools import combinations

# Used for part two
import networkx

with open("data/day8.txt") as file:
    junction_boxes = [ tuple(map(int, line.split(","))) for line in file.read().splitlines() ]


def get_distances(junction_boxes):
    distances = {}
    connections = combinations(junction_boxes, 2)

    for connection in connections:
        distances[connection] = dist(*connection)

    sorted_distances = sorted(distances.items(), key = lambda e: e[1], reverse = True)

    return sorted_distances


def connect_circuits(distances, size):
    circuits = [ set( distances.pop()[0] ) ]

    for _ in range(size - 1):
        left, right = connection = distances.pop()[0]

        index_found = set()
        for i, circuit in enumerate(circuits):
            if left in circuit:
                circuits[i] = circuits[i].union(set(connection))
                index_found.add(i)
            if right in circuit:
                circuits[i] = circuits[i].union(set(connection))
                index_found.add(i)

        if not index_found:
            circuits.append(set(connection))

        if len(index_found) == 2:
            index, connection = sorted(index_found)
            circuits[index].update(circuits[connection])
            circuits.pop(connection)

    return circuits


def build_network(connections):
    graph = networkx.Graph()

    for connection in connections:
        (left, right), distance = connection
        graph.add_edge(left, right, weight = distance)

    return networkx.minimum_spanning_tree(graph)


def find_last_two(graph):
    max_distance = 0
    max_edge = None

    for edge in graph.edges(data = True):
        distance = edge[2]['weight']
        if distance > max_distance:
            max_distance = distance
            max_edge = edge

    return max_edge[0][0] * max_edge[1][0]


distances = get_distances(junction_boxes)
circuits = sorted(connect_circuits(distances.copy(), 1000), key = len, reverse = True)

print("Part one =", prod(len(c) for c in circuits[:3]))
print("Part two =", find_last_two(build_network(distances)))
