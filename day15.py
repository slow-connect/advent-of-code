import intervals as I
from tqdm import tqdm



def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part1(input):
    line = input.readline()
    line = line.replace('\n', '').replace(':', '').replace(',', '')
    sensor = []
    beacon = []
    while line != '':
        line = line.split(' ')
        line[2] = line[2].split('=')
        line[3] = line[3].split('=')
        line[-2] = line[-2].split('=')
        line[-1] = line[-1].split('=')
        sensor.append([int(line[2][-1]), int(line[3][-1])])
        beacon.append([int(line[-2][-1]), int(line[-1][-1])])
        line = input.readline()
        line = line.replace('\n', '').replace(':', '').replace(',', '')


    intervall = I.empty()

    y = 2000000
    for k in range(len(sensor)):
        diff = manhattan_distance(sensor[k], beacon[k]) - abs(sensor[k][1] - y)
        tmp = I.closed(sensor[k][0] - diff, sensor[k][0] + diff)
        intervall = intervall.union(tmp)


    for pos in beacon:
        if pos[1] == y:
            intervall = intervall.difference(I.open(pos[0]-1, pos[0]+1))


    print(intervall)
    print(intervall.upper-intervall.lower)

def part2(input):
    line = input.readline()
    line = line.replace('\n', '').replace(':', '').replace(',', '')
    sensor = []
    beacon = []
    while line != '':
        line = line.split(' ')
        line[2] = line[2].split('=')
        line[3] = line[3].split('=')
        line[-2] = line[-2].split('=')
        line[-1] = line[-1].split('=')
        sensor.append([int(line[2][-1]), int(line[3][-1])])
        beacon.append([int(line[-2][-1]), int(line[-1][-1])])
        line = input.readline()
        line = line.replace('\n', '').replace(':', '').replace(',', '')


    all_region = I.closed(0, 4000000)
    all = ~I.empty()


    for y in tqdm(range(4000000, -1, -1)):
        intervall = I.empty()
        for k in range(len(sensor)):
            diff = manhattan_distance(sensor[k], beacon[k]) - abs(sensor[k][1] - y)
            tmp = I.closed(sensor[k][0] - diff, sensor[k][0] + diff)
            intervall = intervall.union(tmp)
        intervall = all_region.difference(intervall)
        if not intervall.is_empty():
            if intervall.upper - intervall.lower > 1:
                print(y)
                print(intervall)


input = open('day15_input.txt', 'r')
part1(input)

input = open('day15_input.txt', 'r')
part2(input)
