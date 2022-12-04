score = 0
input = open('day03_imput.txt', 'r')
line = input.readline()
while line != '':
    line = line.replace('\n', '')
    line1 = line[0:len(line)//2]
    line2 = line[len(line)//2:]
    common = list(set(line1)&set(line2))
    char = common[0][0]
    if char.isupper():
        val = ord(char) - 38
    if char.islower():
        val = ord(char) - 96
    score = score + val
    line = input.readline()

print(score)
