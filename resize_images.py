#!/usr/bin/python

from PIL import Image
import os, sys

directory = 'images'

path = os.path.join(os.getcwd(), directory)
dirs = os.listdir( path )
basewidth = 640

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            img = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(f +'.jpg', 'JPEG')

resize()