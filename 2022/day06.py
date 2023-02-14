def different(string):
    for i in range(len(string)):
        for j in range(len(string)):
            if i != j:
                if string[i] == string[j]:
                    return False
    return True

def part1(input):
    for i in range(len(input) - 4):
        if different(input[i:i+4]):
            return i+4

def part2(input):
    for i in range(len(input) - 14):
        if different(input[i:i+14]):
            return i+14


input = open('day06_imput.txt', 'r')
input_line = input.readline()
input_line = input_line.replace('\n', '')
while input_line != '':
    print(part1(input_line))
    input_line = input.readline()
    input_line = input_line.replace('\n', '')


input = open('day06_imput.txt', 'r')
input_line = input.readline()
input_line = input_line.replace('\n', '')
while input_line != '':
    print(part2(input_line))
    input_line = input.readline()
    input_line = input_line.replace('\n', '')
