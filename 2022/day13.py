import json
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))



def inOrder(left, right,):
    for i in range(len(left)):
        if i == len(right):
            return False
        elif type(left[i]) == type(right[i]) == list:
            if len(left[i]) == len(right[i]) == 0:
                continue
            elif len(left[i]) == len(right[i]):
                if left[i] == right[i]:
                    return None
                else:
                    return inOrder(left[i], right[i])
            else:
                return inOrder(left[i], right[i])
        if type(left[i]) == type(right[i]) == int:
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False
            else:
                continue
        elif type(left[i]) == int:
            if [left[i]] == right[i]:
                continue
            else:
                return inOrder([left[i]], right[i])
        elif type(right[i]) == int:
            if [right[i]] == left[i]:
                continue
            else:
                return inOrder(left[i], [right[i]])
    if len(right) > len(left):
        return True


def part1(input):
    all_lines = []
    line3 = '\n'
    while line3 == '\n':
        line1 = json.loads(input.readline().replace('\n', ''))
        line2 = json.loads(input.readline().replace('\n', ''))
        line3 = input.readline()
        all_lines.append(line1)
        all_lines.append(line2)
    total = 0
    contradiction = 0
    for i in range(len(all_lines)//2):
        line1 = all_lines[2*i]
        line2 = all_lines[2*i+1]
        if inOrder(line1, line2):
            total = total + i + 1
    return total

def part2(input):
    all_lines = []
    line3 = '\n'
    while line3 == '\n':
        line1 = json.loads(input.readline().replace('\n', ''))
        line2 = json.loads(input.readline().replace('\n', ''))
        line3 = input.readline()
        all_lines.append(line1)
        all_lines.append(line2)
    all_lines.append([[2]])
    all_lines.append([[6]])

    for i in range(len(all_lines)):
        for j in range(i+1, len(all_lines)):
            if not inOrder(all_lines[i], all_lines[j]):
                tmp = all_lines[i]
                all_lines[i] = all_lines[j]
                all_lines[j] = tmp

    divider_packets = []

    for i in range(len(all_lines)):
        if all_lines[i] == [[2]]:
            divider_packets.append(i+1)
        if  all_lines[i] == [[6]]:
            divider_packets.append(i+1)

    return divider_packets[0] * divider_packets[1]


input = open('day13_imput.txt', 'r')
print(part1(input))
input = open('day13_imput.txt', 'r')
print(part2(input))
