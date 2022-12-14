
def rock_positions(a, b):
    if type(a) == str:
        a = a.split(',')
    if type(b) == str:
        b = b.split(',')
    for i in range(len(a)):
        a[i] = int(a[i])
        b[i] = int(b[i])
    tmp = []
    if a[0] == b[0]:
        if a[1] < b[1]:
            for i in range(b[1] - a[1] + 1):
                tmp.append([a[0], a[1] + i])
        elif a[1] > b[1]:
            for i in range(a[1] - b[1] + 1):
                tmp.append([a[0], a[1] - i])
    elif a[1] == b[1]:
        if a[0] < b[0]:
            for i in range(b[0] - a[0] + 1):
                tmp.append([a[0] + i, a[1]])
        if a[0] > b[0]:
            for i in range(a[0] - b[0] + 1):
                tmp.append([a[0] - i, a[1]])
    return tmp

def isblocked(map, pos):
    find = [[pos[0], pos[1] + 1], [pos[0] - 1, pos[1] + 1], [pos[0] + 1, pos[1] + 1]]
    found = 0
    for i in range(len(find)):
        if find[i] in map:
            found = found + 1
    if found == 3:
        return True
    if found > 3:
        return False


def part1(input):
    line = input.readline().replace('\n', '')
    map = []

    while line != '':
        line = line.split(' -> ')
        for i in range(len(line) - 1):
            tmp = rock_positions(line[i], line[i+1])
            for i in range(len(tmp)):
                if tmp[i] not in map:
                    map.append(tmp[i])
        line = input.readline().replace('\n', '')
    sandblock = 0
    val = 1
    while val != 0:
        x = [500, 0]
        val = 1
        while not isblocked(map, x):
            find = [[x[0], x[1] + 1], [x[0] - 1, x[1] + 1], [x[0] + 1, x[1] + 1]]
            if find[0] not in map:
                x = find[0]
            elif find[1] not in map:
                x = find[1]
            elif find[2] not in map:
                x = find[2]
            if x[1] > 200:
                val = 0
                break
            it_count = it_count + 1
        map.append(x)
        sandblock = sandblock + 1
    return sandblock - 1


input = open('day14_input.txt', 'r')
part1(input)
