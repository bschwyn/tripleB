

class Board():

    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        #'0' is '-'


    def add_token(self,row, column, X=True):
        if X:
            self.board[row][column] = 1
            #1 is 'X'
        else:
            #2 is 'O'
            self.board[row][column] = 2

        #X is true adds x, false adds O

    def print_board(self):
        for row in self.board:
            i= 0
            while i < 3:
                elem = row[i]
                if elem == 0:
                    print('-', end='')
                elif elem== 1:
                    print('X', end='')
                else:
                    print('O', end='')
                i+=1
                if i < 3:
                    print('|', end='')
            print()
        print()

    def board_full(self):
        board_full = True
        for row in self.board:
            if 0 in row:
                board_full = False
        return board_full

    def AI_play(self):

        if self.board_full():
            raise ValueError('error')
        for row in range(3):
            for col in range(3):
                if self.board[row][col] !=0:
                    self.add_token(row,col,1)
                    break
            break


class Ai():
    def __init(self):
        board = Board()


b = Board()
#b.add_token(0,1,1)
b.print_board()
b.AI_play()
b.print_board()
print()
b.AI_play()
b.print_board()
print(b.board_full())

