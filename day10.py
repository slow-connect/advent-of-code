
def part1(input):
    X = 1
    total = 0
    cycle = 0
    line = input.readline()
    line = line.replace('\n', '')
    while line != '':
        if line == 'noop':
            cycle = cycle + 1
        line = line.split(' ')
        if line[0] == 'addx':
            cycle = cycle + 2
        if (20 + cycle) % 40 == 0:
            total = total + cycle * X
        if (20 + cycle) % 40 == 1 and line[0] == 'addx':
            total = total + (cycle - 1) * X
        if line[0] == 'addx':
            X = X + int(line[1])
        line = input.readline()
        line = line.replace('\n', '')
    return total

def part2(input):
    X = 1
    cycle = 0
    line = input.readline()
    line = line.replace('\n', '')
    crt = ''
    while line != '':
        if line == 'noop':
            if X-1 <= (cycle % 40) <= X+1:
                crt = crt + '#'
            else:
                crt = crt + '.'
            if (cycle) % 40 == 39:
                print(crt)
                crt = ''
            cycle = cycle + 1
        line = line.split(' ')
        if line[0] == 'addx':
            if X-1 <= (cycle % 40) <= X+1:
                crt = crt + '#'
            else:
                crt = crt + '.'
            if (cycle) % 40 == 39:
                print(crt)
                crt = ''
            cycle = cycle + 1
            if X-1 <= (cycle % 40) <= X+1:
                crt = crt + '#'
            else:
                crt = crt + '.'
            if (cycle) % 40 == 39:
                print(crt)
                crt = ''
            cycle = cycle + 1
        if line[0] == 'addx':
            X = X + int(line[1])
        line = input.readline()
        line = line.replace('\n', '')



input = open('day10_imput.txt', 'r')
print(part1(input))

input = open('day10_imput.txt', 'r')
part2(input)
