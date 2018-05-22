ta# -*- coding: utf-8 -*-
"""
Created on Fri May 18 23:36:31 2018

@author:刘闯

利用数据结构 建立模型

井字棋
"""


###建立棋盘空格位置---棋子 现所有位置都是空格
the_board={'1-1':' ','1-2':' ','1-3':' ',
           '2-1':' ','2-2':' ','2-3': '',
           '3-1':' ','3-2':' ','3-3':' ',
           }

###打印棋盘
def print_board(board):
    ###参数为字典
    print(board['1-1']+'|'+board['1-2']+'|'+board['1-3'])
    print('-+-+-')
    print(board['2-1']+'|'+board['2-2']+'|'+board['2-3'])
    print('-+-+-')
    print(board['3-1']+'|'+board['3-2']+'|'+board['3-3'])


### 允许玩家修改棋子
turn='X'
for i in range(9):
    print_board(the_board)
    print('Turn for '+turn)
    move=input(" Move on which space?: ")
    the_board[move]=turn
    if turn == "X":
        turn='O'
    else:
        turn='X'

print_board(the_board)
    
    
    
    
    
    
    
    
    