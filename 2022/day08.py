def is_smaller (list, x, y):
    # if x == 0 or y == 0 or x == len(list)-1 or y == len(list[y])-1:
    #     return True
    can_be_seen = True
    for i in range(len(list)):
        if i == x:
            if can_be_seen:
                # print("seen from top")
                return True
            else:
                can_be_seen = True
        else:
            if list[i][y] >= list[x][y]:
                can_be_seen = False
    if can_be_seen:
        # print("seen from below")
        return True
    can_be_seen = True
    for j in range(len(list[x])):
            if j == y:
                if can_be_seen:
                    # print("seen from left")
                    return True
                else:
                    can_be_seen = True
            else:
                if list[x][j] >= list[x][y]:
                    can_be_seen = False
    if can_be_seen:
        # print('seen from right')
        return True
    else:
        return False



def best_view(list, x, y):

    view_up, view_down, view_left, view_right = 1, 1, 1, 1
    for i in range(x - 1):
        if list[x - 1 - i][y] < list[x][y]:
            view_up = view_up + 1
        else:
            break
    for i in range(x+1, len(list) - 1):
        if list[i][y] < list[x][y]:
            view_down = view_down + 1
        else:
            break
    for i in range(y -1):
        if list[x][y - 1 - i] < list[x][y]:
            view_left = view_left + 1
        else:
            break
    for i in range(y+1, len(list) - 1):
        if list[x][i] < list[x][y]:
            view_right = view_right + 1
        else:
            break
    tmp = view_up * view_down * view_left * view_right
    if x == 0 or y == 0 or x + 1 == len(list) or y + 1 == len(list[x]):
        tmp = 0
    print("x, y = (%d, %d), tmp = %d" % (x, y, tmp))
    return tmp



input = open('day08_imput.txt', 'r')
visible = 0
data = [[]]
line = input.readlines()
for i in range(len(line)):
    data.append([])
    line[i] = line[i].replace('\n', '')
    for j in range(len(line[i])):
        data[i].append(int(line[i][j]))

data.pop()
# print(data)
for i in range(len(data)):
    for j in range(len(data[i])):
        if is_smaller(data, i, j):
            visible = visible + 1

tree_score = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        tmp = best_view(data, i, j)
        if tree_score < tmp:
            tree_score = tmp

print(tree_score)
