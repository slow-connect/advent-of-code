from collections import deque

def monkey_0(old):
    new = old * 19
    new = new % 9699690
    if new % 23 == 0:
        return new, 2
    else:
        return new, 3

def monkey_1(old):
    new = old + 6
    new = new % 9699690
    if new % 19 == 0:
        return new, 2
    else:
        return new, 0

def monkey_2(old):
    new = old * old
    new = new % 9699690
    if new % 13 == 0:
        return new, 1
    else:
        return new, 3

def monkey_3(old):
    new = old + 3
    new = new % 9699690
    if new % 17 == 0:
        return new, 0
    else:
        return new, 1


items = [deque([79, 98]), deque([54, 65, 75, 74]), deque([79, 60, 97]), deque([74])]

item_handled = [0, 0, 0, 0]

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
