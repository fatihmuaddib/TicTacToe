import os
from pynput import keyboard
from pynput.keyboard import Key
from time import sleep
class TicTacToe:
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.position = [1,1]
        self.player1 = "X"
        self.round = 0
        self.player2 = "O"
        self.computer=False
        self.winner = None
        self.game_state={'row0':0,'row1':0,'row2':0,'column0':0,'column1':0,'column2':0,'diagonal0':0,'diagonal1':0}
        self.pressed = True
    def move_cursor(self, direction):
        self.pressed = False
        if direction == 'r':
            self.position[0] = (self.position[0] + 1) % 3
        elif direction == 'l':
            self.position[0] = (self.position[0] - 1) % 3
        elif direction == 'u':
            self.position[1] = (self.position[1] - 1) % 3
        elif direction == 'd':
            self.position[1] = (self.position[1] + 1) % 3
    def on_key_release(self,key):
        if key == Key.right:
                self.move_cursor('r')
        elif key == Key.left:
                self.move_cursor('l')
        elif key == Key.up:
                self.move_cursor('u')
        elif key == Key.down:
                self.move_cursor('d')
        elif key == Key.enter:
                if self.round%2==0:
                    self.make_move(self.player1,self.position[1],self.position[0])
                elif self.round%2==1 and not self.computer:
                    self.make_move(self.player2,self.position[1],self.position[0])
        elif key == Key.esc:
            exit()
        self.pressed = True  
        if(self.round%2==1 and self.computer):
            self.computer_move()
    def print_board(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.board:
            for element in row:
                if element == None:
                    print(u'\u25A2 ', end="")
                elif element == 5:
                    print("X ", end="")
                else:
                    print("O ", end="")
            print()
    def blinky_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in range(3):
            for element in range(3):
                if row == self.position[1] and element == self.position[0]:
                    print(u'\u25A0 ', end="")
                elif self.board[row][element] == None:
                    print(u'\u25A2 ', end="")
                elif self.board[row][element] == 5:
                    print("X ", end="")
                else:
                    print("O ", end="")
            print()
    def check_win_state(self):
        for winnable in self.game_state:
            if self.game_state[winnable] == 15:
                self.winner = self.player1
                return True
            elif self.game_state[winnable] == 21:
                self.winner = self.player2
                return True
        return False
    def check_draw_state(self):
        for row in self.board:
            for element in row:
                if element == None:
                    return False
        return True
    def make_move(self,player,row,column):
        self.round += 1
        if self.board[row][column] != None:
            print("Invalid move")
            self.round -= 1
            sleep(1)
        else:
            if player== self.player1:
                self.board[row][column]=5
                self.game_state['row'+str(row)]+=5
                self.game_state['column'+str(column)]+=5
                if row==column:
                    self.game_state['diagonal0']+=5
                if row+column==2:
                    self.game_state['diagonal1']+=5
            else:
                self.board[row][column]=7
                self.game_state['row'+str(row)]+=7
                self.game_state['column'+str(column)]+=7
                if row==column:
                    self.game_state['diagonal0']+=7
                if row+column==2:
                    self.game_state['diagonal1']+=7
            if self.check_win_state():
                self.pressed = False
                self.print_board()
                print(self.winner+" wins!")
                sleep(1)
                exit()
            elif self.check_draw_state():
                self.pressed = False
                self.print_board()
                print("Draw!")
                sleep(1)
                exit()
    def computer_move(self):
        if self.board[1][1] == None:
            return self.make_move(self.player2,1,1)
        for prevent in self.game_state:
            if self.game_state[prevent] == 10:
                if prevent == 'diagonal0':
                    for i in range(3):
                        if self.board[i][i] == None:
                            return self.make_move(self.player2,i,i)
                elif prevent == 'diagonal1':
                    for i in range(3):
                        if self.board[i][2-i] == None:
                            return self.make_move(self.player2,i,2-i)
                elif prevent[:3]=='row':
                    for i in range(3):
                        if self.board[int(prevent[3])][i] == None:
                            return self.make_move(self.player2,int(prevent[3]),i)	
                else:
                    for i in range(3):
                        if self.board[i][int(prevent[6])] == None:
                            return self.make_move(self.player2,i,int(prevent[6]))
            if self.game_state[prevent]==14:
                if prevent == 'diagonal0':
                    for i in range(3):
                        if self.board[i][i] == None:
                            return self.make_move(self.player2,i,i)
                elif prevent == 'diagonal1':
                    for i in range(3):
                        if self.board[i][2-i] == None:
                            return self.make_move(self.player2,i,2-i)
                elif prevent[:3]=='row':
                    for i in range(3):
                        if self.board[int(prevent[3])][i] == None:
                            return self.make_move(self.player2,int(prevent[3]),i)	
                else:
                    for i in range(3):
                        if self.board[i][int(prevent[6])] == None:
                            return self.make_move(self.player2,i,int(prevent[6]))
        for row in self.board:
            for element in row:
                if element == None:
                    return self.make_move(self.player2,row.index(element),self.board.index(row))                
    def make_it_blinky(self):
        toggle = True
        while self.pressed:
            if toggle:
                self.print_board()
            else:   
                self.blinky_board()
            toggle = not toggle
            sleep(0.3)
    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        print("Press ESC to exit")
        print("Press ENTER to make a move")
        print("Press UP, DOWN, LEFT, RIGHT to move the cursor")
        print("Play against the computer? (Y/n)")
        if input().lower() == 'n':
            self.computer = False
        else:
            self.computer = True
        print("You are X")
        sleep(1)
        listener = keyboard.Listener(on_release=self.on_key_release)
        listener.start()
        self.make_it_blinky()  
if __name__ == "__main__":
    game=TicTacToe()
    
    game.play_game()