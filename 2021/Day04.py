import numpy as np
import sys
f = open('Day04_sequence.txt', 'r')
sequence = f.readline().replace('\n', '').split(',')
sequence = np.array(sequence, dtype=int)
f.close()


class Boards:
    def __init__(self, lst):
        self.numbers = np.matrix(lst)
        self.drawn = np.zeros(self.numbers.shape)
    def new_number(self, number):
        if np.in1d(self.numbers, number).any():
            coord = np.where(self.numbers == number)
            # print(coord[0][0])
            # print(coord[1][0])
            self.drawn[coord[0][0]][coord[1][0]] = 1
        else:
            pass
    def complete(self):
        for k in range(len(self.drawn)):
            if np.all(self.drawn[:, k] == 1):
                return True
        for k in range(len(self.drawn[0])):
            if np.all(self.drawn[k, : ] == 1):
                return True
        return False
    def print(self):
        print()
        print(self.numbers)
        print()
        print(self.drawn)
        print()
        print('-----------------------------------')
# somehow this is not working....
    def calculate_score(self, number):
        sum = 0
        numbers = self.numbers
        drawn = self.drawn
        # return calc_score(numbers, drawn, number)
        for i in range(len(numbers)):
            for j in range(len(numbers[i])):
                if drawn[i][j] == 0:
                    sum += numbers[i][j]
        score = sum * number
        return score


def p1(sequence, incomplete_boards, boards):
    for drow in sequence:
        for k in incomplete_boards:
            boards[k].new_number(drow)
            if boards[k].complete():
                incomplete_boards.remove(k)
                boards[k].print()
                print(drow)
                sys.exit()


def p2(sequence, incomplete_boards, boards):
    last_board = True
    for drow in sequence:
        if last_board:
            for k in incomplete_boards:
                boards[k].new_number(drow)
                if boards[k].complete():
                    incomplete_boards.remove(k)

                if len(incomplete_boards) == 1:
                    last_board = False
        else:
            boards[incomplete_boards[0]].new_number(drow)
            if boards[incomplete_boards[0]].complete():
                boards[incomplete_boards[0]].print()
                print(drow)
                sys.exit()



f = open('Day04_boards.txt', 'r')
line = f.readline()
line = line.replace('\n', '')
count = 0
board = 'board_'
incomplete_boards = []
boards = []
while True:
    board_lst = []
    while line != '':
        line = line.replace('  ', ' ')
        line = line.split(" ")
        if len(line) == 1:
            break
        tmp = []
        # print(line)
        for k in range(len(line)):
            tmp.append(int(line[k]))
        board_lst.append(tmp)
        line = f.readline()
        line = line.replace('\n', '')
    boards.append(Boards(board_lst))
    incomplete_boards.append(count)
    count += 1
    if len(line) == 1:
        break
    line = f.readline()
    # if line == '#':
    #     break
    # line = f.readline()
    # if line == '#':
    #     break
    line  = line.replace('\n', '')

# p1(sequence, incomplete_boards.copy(), board)
p2(sequence, incomplete_boards.copy(), boards)
