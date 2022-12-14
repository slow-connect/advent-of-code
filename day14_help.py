lines = open('day14_final_pyramid.txt', 'r').readlines()

count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'o' or lines[i][j] == 'M':
            count = count + 1
print(count)
