import warnings

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


input = open('day09_imput.txt', 'r')
line = input.readline()
line = line.replace('\n', '')
tail = [0, 0]
head = [0, 0]
tail_visited = [(0, 0)]
head_lst = [(0, 0)]
tail_lst = [(0, 0)]
count = 1
while line != '':
    line = line.split(' ')
    moving_index, direction = assert_direction(line[0])
    for i in range(int(line[1])):
        head[moving_index] = head[moving_index] + (-1)**direction
        head_lst.append(tuple(head))
        if not tail_neibough(tail, head):
            tail[moving_index] = tail[moving_index] + (-1)**direction
            # assert direction to move in diagonally
            if head[0] != tail[0] and head[1] != tail[1]:
                tail_moving = (moving_index + 1) % 2
                if head[(moving_index + 1) % 2] > tail[tail_moving]:
                    tail_direction = 0
                else:
                    tail_direction = 1
                tail[tail_moving] = tail[tail_moving] + (-1)**tail_direction
        tail_lst.append(tuple(tail))
        if tuple(tail) not in tail_visited:
            tail_visited.append(tuple(tail))
    line = input.readline()
    line = line.replace('\n', '')
    count = count + 1
print(len(tail_visited))
