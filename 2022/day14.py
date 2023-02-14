import time


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

def draw(map, sand, min, left, right):
    if min == 166:
        shift = min
    else:
        shift = 8
    str_map = []
    for i in range(min+3):
        tmp = []
        for i in range(right - left + 2*min + 4):
            tmp.append('.')
        str_map.append(tmp)
    for x in map:
        str_map[x[1]][x[0] - left + shift] = '#'

    for x in sand:
        str_map[x[1]][x[0] - left + shift] = 'o'

    str_map[0][500 - left + shift] = 'M'




    for i in range(len(str_map)):
        tmp = ''
        for j in range(len(str_map[i])):
            tmp = tmp + str_map[i][j]
        print(tmp)
    print()

input = open('day14_input.txt', 'r')
# part1(input)

# input = open('day14_input_test.txt', 'r')

line = input.readline().replace('\n', '')
stone = []
map = []

while line != '':
    line = line.split(' -> ')
    for i in range(len(line) - 1):
        tmp = rock_positions(line[i], line[i+1])
        for i in range(len(tmp)):
            if tmp[i] not in map:
                map.append(tmp[i])
                stone.append(tmp[i])
    line = input.readline().replace('\n', '')




min = 0
left = 500
right = 500
for i in range(len(map)):
    if map[i][1] > min:
        min = map[i][1]
    if map[i][0] > right:
        right = map[i][0]
    if map[i][0] < left:
        left = map[i][0]

tmp = rock_positions([left - min - 2, min+2], [right + min + 2, min+2])
for i in range(len(tmp)):
    map.append(tmp[i])


# draw(map, [], min, left, right)



sand = []
sandblock = 0
val = 1
while val != 0:
    x = [500, 0]
    count = 0
    while not isblocked(map, x):
        find = [[x[0], x[1] + 1], [x[0] - 1, x[1] + 1], [x[0] + 1, x[1] + 1]]
        if find[0] not in map:
            x = find[0]
        elif find[1] not in map:
            no_stone = True
            for i in range(min + 3 - x[1]):
                tmp = []
                if [x[i] - i, x[i] + i] in stone:
                    no_stone = False
                    break
                else:
                    tmp.append([x[i] - i, x[i] + i])
            if no_stone:
                for i in range(len(tmp)):
                    sand.append(tmp[i])
                    map.append(tmp[i])
            x = find[1]

        elif find[2] not in map:
            no_stone = True
            for i in range(min + 3 - x[1]):
                tmp = []
                if [x[i] + i, x[i] + 1] in stone:
                    no_stone = False
                    break
                else:
                    tmp.append([x[i] + i, x[i] + 1])
            if no_stone:
                for i in range(len(tmp)):
                    sand.append(tmp[i])
                    map.append(tmp[i])
        if  x == [500, 0]:
            val = 0
            break
        # if x == [501, 1]:
        #     print(isblocked(map, x))
        count = count + 1
        # print('depth of next is %d, interation = %d' %(x[1], count))
        # print(x)
    map.append(x)
    sand.append(x)
    sandblock = sandblock + 1
    draw(map, sand, min, left, right)
    if isblocked(map, [500, 0]):
        break


sand.append([500, 0])
draw(map, sand, min, left, right)

# print(len(sand))
