import re

def part1(input):
    line = input.readline()
    line = line.replace('\n', '')
    count = 0
    while line != '':
        line = re.split(r',|-', line)
        set1 = []
        set2 = []
        for i in range(int(line[0]), int(line[1]) + 1):
            set1.append(i)
        for i in range(int(line[2]), int(line[3]) + 1):
            set2.append(i)
        set1, set2 = set(set1), set(set2)
        if set1.issubset(set2) or set2.issubset(set1):
            count = count + 1
        line = input.readline()
        line = line.replace('\n', '')
    return count


def part2(input):
    count = 0
    line = input.readline()
    line = line.replace('\n', '')
    while line != '':
        line = re.split(r',|-', line)
        set1 = []
        set2 = []
        for i in range(int(line[0]), int(line[1]) + 1):
            set1.append(i)
        for i in range(int(line[2]), int(line[3]) + 1):
            set2.append(i)
        set1 = set(set1)
        set2 = set(set2)
        if not set1.isdisjoint(set2):
            count = count + 1
        line = input.readline()
        line = line.replace('\n', '')
    return count

input = open('day04_imput.txt', 'r')
print(part1(input))

input = open('day04_imput.txt', 'r')
print(part2(input))
