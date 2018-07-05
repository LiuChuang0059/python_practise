#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 23:28:05 2018

@author: liuchuang
"""


from PIL import Image
## pyhton  pillow bag


def fillImage(image):
    """
    if picture is not square
    filled  with white (or some other color)
    """
    width, height = image.size
    length = max(width,height)
    
    new_image = Image.new(image.mode,(length,length),color='white')
    
    
    if width > height :
        new_image.paste(image,(0,int((length-height)/2)))
        
    else:
        new_image.paste(image,(int((length-width)/2),0))
    return new_image

  
def cutImage(image):
    """
    cut into 9 parts  3X3
    """
    width, height = image.size
    
    part_width = int(width/3)
    part_height = int(height/3)
    
    box_list = []  ### to store  9 parts 
    
    for i in range(3):
        for j in range(3):
            
            box = (j * part_width, i * part_width, (j + 1) * part_width, (i + 1) * part_width)
            box_list.append(box)
        
    image_list = [image.crop(box) for box in box_list]  ## save 9 parts of images  
    
    return image_list



def saveImage(image_list,out_dir):
    for (index, image) in enumerate(image_list, start=1):
        # enumerate
        image.save("{out_dir}_{index}.png".format(out_dir=out_dir, index=index), "PNG")



def changeToNineParts(file_path,out_dir='./'):
    image = Image.open(file_path)
    image1 = fillImage(image)
    image_list = cutImage(image1)
    pic_name = file_path.split('.')[0]
    out_dir = out_dir+ r'/'+pic_name
    saveImage(image_list, out_dir)


if __name__ == '__main__':
    changeToNineParts('ttt.png')











