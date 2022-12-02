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
        'B' : 0,
        'C' : 6,
        }
        score = score + 1 + switch.get(play[0])
    elif play[1] == 'Y':
        switch = {
        'A' : 6,
        'B' : 3,
        'C' : 0,
        }
        score = score + 2 + switch.get(play[0])
    else:
        switch = {
        'A' : 0,
        'B' : 6,
        'C' : 3,
        }
        score = score + 3 + switch.get(play[0])

print(score)
