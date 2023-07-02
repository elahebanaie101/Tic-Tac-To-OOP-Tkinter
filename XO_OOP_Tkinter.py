import tkinter as tk
import random


class Board: #it's the Board structure
    def __init__(self, root):
        self.buttons = []
        self.root = root
        self.status = [0,0,0] # win,lose,equal
        self.players = ['human','computer']
        self.current_player= random.choice(self.players)
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x500")
        self.root.configure(bg='yellow')
        for i in range(3):
            for j in range(3):
                self.buttons.append(tk.Button(self.root, text="",bg='white', width=8, height=5,
                                   command=lambda i=i, j=j: gamer.human_move(self.buttons[3*i+j])))
                self.buttons[3*i+j].grid(row=i+1, column=j+1)
        self.equal = tk.Label(root, text=f"equal={self.status[2]}") 
        self.win = tk.Label(root, text=f"win={self.status[0]}")
        self.lose = tk.Label(root, text=f"lose={self.status[1]}")
        self.win.grid(row=5, column=1, columnspan=4)
        self.lose.grid(row=6, column=1,columnspan=4)
        self.equal.grid(row=7, column=1,columnspan=4)
        self.quit = tk.Button(root,command=root.destroy, width=4,height=2,text="Quit")
        self.quit.grid(row=8,column=0)
        self.reset = tk.Button(root, width=4,height=2,text="Reset")
        self.reset.grid(row=8,column=1)
        self.Continue = tk.Button(root, width=8,height=2,text="Continue")
        self.Continue.grid(row=8,column=2)
        self.end_label = tk.Label(root,bg='red')
        self.end_label.grid(row=9,column=1,columnspan=3, pady=10)
        
        self.reset.bind('<Button-1>', self.reset_func)
        self.Continue.bind('<Button-1>', self.game_process)
        
        
        
    def start_game(self):
        gamer.Get_Table(self.buttons)
        if self.current_player == 'computer':
           gamer.computer_move()
            
    def Occupy_Button(self,choosen_button,button_occupied):
        choosen_button.configure(text=button_occupied)
        choosen_button["state"] = tk.DISABLED
    def check_end(self):
        self.win_positions = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7],[2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]
        for i in range(8):
            if "O" == self.buttons[self.win_positions[i][0]]["text"] == self.buttons[self.win_positions[i][1]]["text"] == self.buttons[self.win_positions[i][2]]["text"]:
               return 'computer', [self.win_positions[i][0], self.win_positions[i][1], self.win_positions[i][2]]
            elif "X" == self.buttons[self.win_positions[i][0]]["text"] == self.buttons[self.win_positions[i][1]]["text"] == self.buttons[self.win_positions[i][2]]["text"]:
               return 'human', [self.win_positions[i][0], self.win_positions[i][1], self.win_positions[i][2]]
        end = 0
        for i in range(0,9):
            if not self.buttons[i]["text"] == "":
                end +=1
        if end == 9:
           return 'equal', []
        return 3, []
    def end_labels(self):
        Finiish = False
        winner, end_positions = self.check_end()
        if winner == 'computer':
            self.status[1] +=1
            self.lose.configure(text=f"lose={self.status[1]}")
            self.end_label.configure(text="You Lose")
            for i in end_positions[0], end_positions[1], end_positions[2]:
                self.buttons[i].configure(bg='red')
            Finiish = True

        elif winner == 'human':
            self.status[0] +=1
            self.win.configure(text=f"win={self.status[0]}")
            self.end_label.configure(text="You Won")
            for i in end_positions[0], end_positions[1], end_positions[2]:
                self.buttons[i].configure(bg='red')
            Finiish = True

        elif winner == 'equal':
            self.status[2] +=1
            self.equal.configure(text=f"equal={self.status[2]}")
            self.end_label.configure(text="Equal")
            for i in range(9):
                self.buttons[i].configure(bg='white')
            Finiish = True
            
        if Finiish:
            for i in range(9):
                self.buttons[i]['state'] = tk.DISABLED
            self.Continue['state'] = tk.NORMAL
        return Finiish
            
    def game_process(self,event,end=0):
        self.end_label.configure(text="",bg='red')
        for i in range(9):
            self.buttons[i].configure(text="",bg='white',state='normal')
        if end==0:
            self.current_player=random.choice(self.players)
            if self.current_player == 'computer':
                gamer.computer_move()
        self.Continue.configure(state="disabled")
                
    def reset_func(self,event):
        self.game_process(event,1)
        self.status = [0,0,0]
        self.win.configure(text=f"win:{self.status[0]}")
        self.lose.configure(text=f"lose:{self.status[1]}")
        self.equal.configure(text=f"equal:{self.status[2]}")
            
        
            
class Player:
    
    def Get_Table(self,check_buttons):
        self.buttons = check_buttons
    
    
    
    
    def human_move(self,choosen_button):
        Game.Occupy_Button(choosen_button,"X")
        check_game=Game.end_labels()
        if not check_game:
           self.computer_move()
           
           
    def computer_move(self):
        checker = self.win_or_lose()
        if not checker:
            self.playing()
        Game.end_labels()
        

           
    def win_or_lose(self):
        self.win_positions = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7],[2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]
        self.poses = [[0, 1, 2], [0, 2, 1], [1, 2, 0]]
        check = False
        for sym in ["O","X"]:
            for i in self.win_positions:
                for j in self.poses:
                    if self.buttons[i[j[0]]]["text"] == self.buttons[i[j[1]]]["text"] == sym:
                        if self.buttons[i[j[2]]]["text"] == "":
                            Game.Occupy_Button(self.buttons[i[j[2]]], "O")
                            check = True
                            return check
        return check
    
    def playing(self):
        playing =[0,2,6,8,4,1,3,5,7]
        for i in playing:
            if self.buttons[i]["text"] == "":
                Game.Occupy_Button(self.buttons[i], "O")
                break
        
    
root = tk.Tk()
gamer = Player()
Game = Board(root)
Game.start_game()
root.mainloop()
