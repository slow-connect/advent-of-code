n = 9
stacks_config = []
for i in range(n):
    stacks_config.append(['#'])
# print(stacks_config)
input = open('day05_input_stacks.txt', 'r')
lines = input.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


for i in range(1,len(lines) + 1):
    for y in range(len(lines[-i])):
        if y%4 == 1:
            if lines[-i][y].isupper():
                stacks_config[y//4].append(lines[-i][y])


movement = open('day05_moving_stacks.txt', 'r')
line = movement.readline()
line = line.replace('\n', '')
while line != '':
    line = line.split(' ')
    n = int(line[1])
    start = int(line[3]) - 1
    dest = int(line[5]) - 1
    for i in range(n):
        if stacks_config[start][-1] != '#':
            stacks_config[dest].append(stacks_config[start].pop())
    line = movement.readline()
    line = line.replace('\n', '')

top_of_stacks = ''
for i in range(len(stacks_config)):
    print(stacks_config[i])
    top_of_stacks = top_of_stacks + stacks_config[i].pop()

print(top_of_stacks)
