line = ''
max, elve_max = 0, 0
sum, elve = 0, 0
input = open('day01_imput.txt', 'r')
while True:
    line = input.readline()
    if line == '#\n':
        break
    if line == '\n':
        if sum > max:
            elve_max = elve
            max = sum

        elve = elve + 1
        sum = 0
        continue
    sum = sum + int(line)

print(max)
