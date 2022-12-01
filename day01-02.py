import numpy as np

line = ''
max = np.array([0, 0, 0])
sum, elve = 0, 0
input = open('day01_imput.txt', 'r')
while True:
    line = input.readline()
    if line == '#\n':
        break
    if line == '\n':
        if sum > max.min():
            max[np.argmin(max)] = sum
        sum = 0
        continue
    sum = sum + int(line)
total = 0
for i in range(3):
    total = max[i] + total
print(max)
print(total)
