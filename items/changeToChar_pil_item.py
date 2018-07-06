#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 00:19:21 2018

@author: liuchuang


目前 只能转换背景为白色的图片

"""

from PIL import Image 

def get_char(r,g,b,alpha=256):
    """
    change rgb to char 
    gray / 256  = x / len(ascii_char)
    """
    if alpha == 0:
        return " "
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
                      
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
    x= int((gray/(256.0+1))*len(ascii_char))
    
    return ascii_char[x]


def write_file(out_filename,cont):
    """
    write as a txt
    """
    
    with open(out_filename,'w') as fil:
        fil.write(cont)
        
        
def change_to_char(filename,width=150,height=150,out_filename="out_file"):
    """
    change
    print
    write
    """
    text = ""
    
    im = Image.open(filename)
    im = im.resize((width,height),Image.NEAREST)
    
    for i in range(height):
        for j in range(width):
            text += get_char(*im.getpixel((j,i)))  ## get pixel every place 
            
        text +='\n'  ## change line
    print(text)
    write_file(out_filename,text)
    
if __name__ == '__main__' :
    change_to_char('lll.JPG')