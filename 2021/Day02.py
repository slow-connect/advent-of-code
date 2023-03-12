input = open('Day02-imput.txt', 'r')

def p1(input):
    forward, depth = 0, 0
    line = input.readline()
    line = line.split()
    while line != []:
        line[1] = int(line[1]) 
        if line[0] == 'forward':
            forward += line[1]
        elif line[0] == 'down':
            depth += line[1]
        else:
            depth -= line[1]
        line = input.readline()
        line = line.split()
    print(forward*depth)
    
def p2(input):
    forward, depth, aim = 0, 0, 0
    line = input.readline()
    line = line.split()
    while line != []:
        line[1] = int(line[1]) 
        if line[0] == 'forward':
            forward += line[1]
            depth += line[1]*aim
        elif line[0] == 'down':
            aim += line[1]
        else:
            aim -= line[1]
        line = input.readline()
        line = line.split()
    print(forward*depth)

# p1(input)
p2(input)
input.close()