# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:46:48 2019

@author: Prava
"""

import random
import tkinter  
from tkinter import Frame, Label, CENTER
import datetime
import logic1
import minimax
import AlphaZero_with_pytorch
import constants as c
import numpy as np





z=0
znew=0
result = 0   

for i in range(5):#Number of games for test 1
    """
    Matrix init
    """
    matrix = logic1.new_game(c.GRID_LEN)#Change here to change a game size
    history_matrixs = list()
    matrix = logic1.add_two(matrix,0)
    matrix = logic1.add_two(matrix,0)
    matrix = logic1.add_two(matrix,1)
    matrix = logic1.add_two(matrix,1)
    
    
    
    
    
    
    
    """
    Dict of commands
    """
    commands = {c.KEY_UP: logic1.up, c.KEY_DOWN: logic1.down,
                     c.KEY_LEFT: logic1.left, c.KEY_RIGHT: logic1.right,
                     c.KEY_UP_ALT: logic1.up, c.KEY_DOWN_ALT: logic1.down,
                     c.KEY_LEFT_ALT: logic1.left, c.KEY_RIGHT_ALT: logic1.right,
                     c.KEY_H: logic1.left, c.KEY_L: logic1.right,
                     c.KEY_K: logic1.up, c.KEY_J: logic1.down}
    
    """
    First player set to zero
    """
    current_player = 0
    
    game_start="not over"
    
    while game_start =="not over":
        # AI - Action
                
        
        key = AlphaZero_with_pytorch.alphaZeroSearch(matrix,current_player,10,0.5,result,False)
     
        # AI - Action
        #print(key)
        #Move_list =[logic1.up,logic1.down,logic1.left,logic1.right]
        
           
        
        matrix, done = commands[key](matrix,current_player)#self.commands[repr(event.char)](self.matrix,self.current_player)
        if current_player<1: #replace 1 by number of players -1
            current_player=current_player+1
        else:
            current_player=0
        if done:
            matrix = logic1.add_two(matrix,current_player)
            # record last move
            history_matrixs.append(matrix)
            done = False
            if logic1.game_state(matrix) != 'not over':
                if logic1.game_state(matrix) != "draw":
                    print(current_player,'win')

                else:
                    print('Draw')

    
        game_start=str(logic1.game_state(matrix))
        
    
    """
    Getting a maximum value from matrix
    """
    
    print(z)
    MatrixList=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            MatrixList.append((matrix[i][j][0]))
    znew = max(MatrixList)
    print(znew)
    if znew > z:
        z= znew
        
        result = 1
    else:
         result= -1
    
    print(result)            
    print(matrix)
    
     

    
