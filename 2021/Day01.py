import numpy as np

input = open('Day01-imput.txt', 'r')

def p1(input):
    line = input.readline()
    line = line.replace(',\n', '')
    prev_line = int(line)
    count = 0
    while line != '':
        line = input.readline()
        line = line.replace(',\n', '')
        if line == '':
            break
        # print(line)
        line = int(line)
        if line > prev_line:
            count += 1
        prev_line = int(line)
    print(count)

def p2(input):
    lines = input.readlines()
    threesums = np.zeros(len(lines)-2)
    for k in range(len(lines)):
        lines[k] = int(lines[k].replace(',\n', ''))
    for i in range(len(lines)-2):
        threesums[i] = lines[i] + lines[i+1] + lines[i+2]
    count = 0
    for k in range(1, len(threesums)):
        if threesums[k] > threesums[k-1]:
            count += 1
    print(count)
    

p2(input)
