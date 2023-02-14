score = 0
input = open('day03_imput.txt', 'r')
lines = ['', '', '']
for i in range(3):
    lines[i] = input.readline()
    lines[i] = lines[i].replace('\n', '')

while lines[0] != '':
    common = list(set(lines[0])&set(lines[1])&set(lines[2]))
    char = common[0][0]
    if char.isupper():
        val = ord(char) - 38
    if char.islower():
        val = ord(char) - 96
    score = score + val
    for i in range(3):
        lines[i] = input.readline()
        lines[i] = lines[i].replace('\n', '')

print(score)
