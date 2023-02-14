import heapq
from numpy import Inf

# x = end // len(map[0])
# y = end % len(map[0])


def neibourg(x, y, x_max, y_max):
    if x == 0 and y == 0:
        return [[x+1, y], [x, y+1]]
    elif x == 0 and y == y_max:
        return [[x+1, y], [x, y-1]]
    elif x == x_max and y == 0:
        return [[x-1, y], [x, y+1]]
    elif x == x_max and y == y_max:
        return [[x-1, y], [x, y-1]]
    elif x == 0:
        return [[x, y-1], [x+1, y], [x, y+1]]
    elif y == 0:
        return [[x-1, y], [x, y+1], [x+1, y]]
    elif x == x_max:
        return [[x, y-1], [x-1, y], [x, y+1]]
    elif y == y_max:
        return [[x-1, y], [x, y], [x+1, y]]
    else:
        return [[x, y-1], [x-1, y], [x+1, y], [x, y+1]]

def part1(input):
    adjacency_list, start, end = make_adjacency_list_1(input)

    distance = dijkstra(start, end, adjacency_list)

    return distance[end]

def part2(input):
    adjacency_list, start, end = make_adjacency_list_2(input)
    distances = []
    for i in range(len(start)):
        distances.append(dijkstra(start[i], end, adjacency_list)[end])
    return distances


def make_adjacency_list_1(input):
    map = input.readlines()
    for i in range(len(map)):
        map[i] = map[i].replace('\n', '')
        map[i] = list(map[i])
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                start = [i, j]
                map[i][j] = 96
            elif map[i][j] == 'E':
                goal = [i, j]
                map[i][j] = 123
            elif map[i][j] != 'S' or map[i][j] != 'E':
                map[i][j] = ord(map[i][j])
    adjacency_list = [[] for i in range(len(map[0]) * len(map))]

    # init adjacency list:
    node_nr = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            for k in neibourg(i, j, len(map) - 1, len(map[i]) - 1):
                if (map[i][j] + 1 >= map[k[0]][k[1]]) or (map[k[0]][k[1]] == 123 and map[i][j] == 121) or (map[i][j] == 96 and map[k[0]][k[1]] == 98):
                    adjacency_list[node_nr].append(k[0]*len(map[i]) + k[1])
            if map[i][j] == 96:
                start = node_nr
            if map[i][j] == 123:
                end = node_nr
            node_nr = node_nr + 1
    return adjacency_list, start, end

def make_adjacency_list_2(input):
    map = input.readlines()
    for i in range(len(map)):
        map[i] = map[i].replace('\n', '')
        map[i] = list(map[i])
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                map[i][j] = 97
            elif map[i][j] == 'E':
                map[i][j] = 123
            elif map[i][j] != 'S' or map[i][j] != 'E':
                map[i][j] = ord(map[i][j])
    adjacency_list = [[] for i in range(len(map[0]) * len(map))]

    # init adjacency list:
    node_nr = 0
    start_node = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            for k in neibourg(i, j, len(map) - 1, len(map[i]) - 1):
                if (map[i][j] + 1 >= map[k[0]][k[1]]) or (map[k[0]][k[1]] == 123 and map[i][j] == 121) or (map[i][j] == 96 and map[k[0]][k[1]] == 98):
                    adjacency_list[node_nr].append(k[0]*len(map[i]) + k[1])
            if map[i][j] == 97:
                start_node.append(node_nr)
            if map[i][j] == 123:
                end = node_nr
            node_nr = node_nr + 1
    return adjacency_list, start_node, end

def dijkstra(start, end, adjacency_list):
    visited = [False for _ in range(len(adjacency_list))]
    distance = [Inf for _ in range(len(adjacency_list))]
    distance[start] = 0

    pq = [(0, start)]
    while len(pq) > 0:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v in adjacency_list[u]:
            if distance[v] > distance[u] + 1:
                distance[v] = distance[u] + 1
                heapq.heappush(pq, (distance[v], v))
    return distance

input = open('day12_imput.txt', 'r')

print(part1(input))

input = open('day12_imput.txt', 'r')

print(min(part2(input)))
