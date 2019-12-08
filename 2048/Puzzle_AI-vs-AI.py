# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:29:05 2019

@author: pravash
"""
# -*- coding: utf-8 -*-
 

import random
import tkinter  
from tkinter import Frame, Label, CENTER
import datetime
import logic1
import minimax
import AlphaZero_with_pytorch
import constants as c
import numpy as np

class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')


        self.master.bind("<Key>",self.key_down )
        

        # self.gamelogic = gamelogic
        self.commands = {c.KEY_UP: logic1.up, c.KEY_DOWN: logic1.down,
                         c.KEY_LEFT: logic1.left, c.KEY_RIGHT: logic1.right,
                         c.KEY_UP_ALT: logic1.up, c.KEY_DOWN_ALT: logic1.down,
                         c.KEY_LEFT_ALT: logic1.left, c.KEY_RIGHT_ALT: logic1.right,
                         c.KEY_H: logic1.left, c.KEY_L: logic1.right,
                         c.KEY_K: logic1.up, c.KEY_J: logic1.down}

        self.grid_cells = []
        self.current_player=0
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)


    def gen(self):
        return random.randint(0, c.GRID_LEN - 1)

    def init_matrix(self):
        self.matrix = logic1.new_game(c.GRID_LEN)#Change here to change a game size
        self.history_matrixs = list()
        self.matrix = logic1.add_two(self.matrix,0)
        self.matrix = logic1.add_two(self.matrix,0)
        self.matrix = logic1.add_two(self.matrix,1)
        self.matrix = logic1.add_two(self.matrix,1)


    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j][0]
                new_player = self.matrix[i][j][1]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT_P[new_player],
                        fg="black")
        self.update_idletasks()


    def key_down(self, event):
        """Once the key is pressed the key_down function runs till the game state gives winner.
        """
        game_start="not over"
        
        while game_start =="not over":
            # AI - Action

            key = AlphaZero_with_pytorch.alphaZeroSearch(self.matrix,self.current_player,10,0.5,1.,True)
         
            # AI - Action
            print(key)
            if key == c.KEY_BACK and len(self.history_matrixs) > 1:
                self.matrix = self.history_matrixs.pop()
                self.update_grid_cells()
                print('back on step total step:', len(self.history_matrixs))
            elif key in self.commands:
                self.matrix, done = self.commands[key](self.matrix,self.current_player)#self.commands[repr(event.char)](self.matrix,self.current_player)
                print (self.commands[key])
                if self.current_player<1: #replace 1 by number of players -1
                    self.current_player=self.current_player+1
                else:
                    self.current_player=0
                if done:
                    self.matrix = logic1.add_two(self.matrix,self.current_player)
                    # record last move
                    self.history_matrixs.append(self.matrix)
                    self.update_grid_cells()
                    done = False
                    if logic1.game_state(self.matrix) != 'not over':
                        if logic1.game_state(self.matrix) != "draw":
                            root = tkinter.Tk()
                            root.title("Win") 
                            Label(root, text="Player {} Wins!".format(logic1.game_state(self.matrix)),bg=c.BACKGROUND_COLOR_GAME,font = c.FONT).pack()
                            root.mainloop() 
                            """
                            self.grid_cells[1][1].configure(
                                text="P5layer {}".format(logic1.game_state(self.matrix)), bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                            self.grid_cells[1][2].configure(
                                text="Wins!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                            """
                        else:
                            root = tkinter.Tk()
                            root.title("Draw")
                            Label(root, text="Draw",bg=c.BACKGROUND_COLOR_GAME,font = c.FONT).pack()
                            """
                            self.grid_cells[1][1].configure(
                                text="Draw", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                        """
            game_start=str(logic1.game_state(self.matrix))
                
         
        
    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2

gamegrid = GameGrid()

