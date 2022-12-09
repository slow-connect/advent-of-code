def tail_neibough(tail, head):
    if head[0] - 1 <= tail[0] <= head[0] + 1 and head[1] - 1 <= tail[1] <= head[1] + 1:
        return True
    else:
        return False

def assert_direction(str):
    if str == 'L':
        return 0, 1
    elif str == 'R':
        return 0, 0
    elif str == 'U':
        return 1, 0
    elif str == 'D':
        return 1, 1
    # WARNING: input not valid
    else:
        warnings.warn('Direction cannot be asserted')

def nextposition(head, tail):
    # print(type(head))
    if not tail_neibough(tail, head):
        if tail[0] == head[0]:
            if tail[1] < head[1]:
                tail[1] = tail[1] + 1
            else:
                tail[1] = tail[1] - 1
        elif tail[1] == head[1]:
            if tail[0] < head[0]:
                tail[0] = tail[0] + 1
            else:
                tail[0] = tail[0] - 1
        else:
            if tail[0] < head[0] and tail[1] < head[1]:
                tail[0] = tail[0] + 1
                tail[1] = tail[1] + 1
            if tail[0] < head[0] and tail[1] > head[1]:
                tail[0] = tail[0] + 1
                tail[1] = tail[1] - 1
            if tail[0] > head[0] and tail[1] < head[1]:
                tail[0] = tail[0] - 1
                tail[1] = tail[1] + 1
            if tail[0] > head[0] and tail[1] > head[1]:
                tail[0] = tail[0] - 1
                tail[1] = tail[1] - 1
    return tail

input = open('day09_imput.txt', 'r')
line = input.readline()
line = line.replace('\n', '')
tail = [0, 0]
for i in range(8):
    locals()['element_' + str(i)] = [0, 0]
head = [0, 0]
all_positions = [head]
for i in range(8):
    all_positions.append(locals()['element_' + str(i)])
all_positions.append(tail)
tail_visited = [(0, 0)]
head_lst = [(0, 0)]
tail_lst = [(0, 0)]
while line != '':
    line = line.split(' ')
    moving_index, direction = assert_direction(line[0])
    for i in range(int(line[1])):
        all_positions[0][moving_index] = all_positions[0][moving_index] + (-1)**direction
        for j in range(1, len(all_positions)):
            all_positions[j] = nextposition(all_positions[j-1], all_positions[j])
        if tuple(all_positions[-1]) not in tail_visited:
            tail_visited.append(tuple(all_positions[-1]))
    line = input.readline()
    line = line.replace('\n', '')
print(len(tail_visited))
