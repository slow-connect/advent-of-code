from collections import deque

def monkey_0(old):
    new = old * 13
    new = new // 3
    if new % 3 == 0:
        return new, 2
    else:
        return new, 1

def monkey_1(old):
    new = old + 2
    new = new // 3
    if new % 13 == 0:
        return new, 7
    else:
        return new, 2

def monkey_2(old):
    new = old + 8
    new = new // 3
    if new % 19 == 0:
        return new, 4
    else:
        return new, 7

def monkey_3(old):
    new = old + 1
    new = new // 3
    if new % 17 == 0:
        return new, 6
    else:
        return new, 5

def monkey_4(old):
    new = old * 17
    new = new // 3
    if new % 5 == 0:
        return new, 6
    else:
        return new, 3

def monkey_5(old):
    new = old + 3
    new = new // 3
    if new % 7 == 0:
        return new, 1
    else:
        return new, 0

def monkey_6(old):
    new = old * old
    new = new // 3
    if new % 11 == 0:
        return new, 5
    else:
        return new, 0

def monkey_7(old):
    new = old + 6
    new = new // 3
    if new % 2 == 0:
        return new, 4
    else:
        return new, 3



items = [deque([54, 98, 50, 94, 69, 62, 53, 85]), deque([71, 55, 82]), deque([77, 73, 86, 72, 87]), deque([97, 91]), deque([78, 97, 51, 85, 66, 63, 62]), deque([88]), deque([87, 57, 63, 86, 87, 53]), deque([73, 59, 82, 65])]

item_handled = [0, 0, 0, 0, 0, 0, 0, 0]
monkey = 'monkey_'

for rounds in range(1000):
    for j in range(len(item_handled)):
        while len(items[j]) != 0:
            item = items[j].popleft()
            tmp = monkey + str(j)
            new_weight, target = locals()[tmp](item)
            item_handled[j] = item_handled[j] + 1
            items[target].append(new_weight)

print(item_handled)

max_item = max(item_handled)
for i in range(len(item_handled)):
    if max_item == item_handled[i]:
        item_handled[i] = 0
second_max = max(item_handled)

print(max_item * second_max)
