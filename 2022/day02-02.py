line = ''
score = 0
input = open('day02_imput.txt', 'r')
while True:
    line = input.readline()
    line = line.replace('\n', '')
    if line == '':
        break
    play = line.split(' ')
    if play[1] == 'X':
        switch = {
        'A' : 3,
        'B' : 1,
        'C' : 2,
        }
        score = score + switch.get(play[0])
    elif play[1] == 'Y':
        switch = {
        'A' : 4,
        'B' : 5,
        'C' : 6,
        }
        score = score + switch.get(play[0])
    else:
        switch = {
        'A' : 8,
        'B' : 9,
        'C' : 7,
        }
        score = score + switch.get(play[0])

print(score)
