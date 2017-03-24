# Import libraries

import glob
import time
import random
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import argparse

# create class for tiles

class tile:
    def __init__(self,n, m, im):
        self.imshape = im.shape
        self.im = im
        self.num = n*10+m
        self.row = n
        self.clm = m
        self.xpos = self.imshape[0]*m
        self.ypos = self.imshape[1]*n
        self.width = self.imshape[0]
        self.heigth = self.imshape[1]

# define funtion to split the image in tiles

def makePuzzle(img, n=4, m=4):
    imshape = img.shape
    # Define empty array to append tiles
    imArray =[]
    tiles ={}
    crop = np.copy(img)
    # Define size of tiles
    length = imshape[0]/m
    width = imshape[1]/n
    # crop the image in tiles and append them
    for nn in range(0,n):
        for mm in range(0,m):
            xstart = nn* length
            xstop = xstart + length
            ystart = mm*width
            ystop = ystart + width
            piece = crop[xstart:xstop, ystart:ystop]
            imArray.append(piece)
            name = ''.join([str(nn+1),str(mm+1)])
            tiles[name] = tile(nn+1, mm+1, piece)
    bTile = np.zeros_like(tiles["11"].im)
    tiles["11"].im = bTile
    tiles["black"] = tiles.pop("11")
    return tiles
    
# Funtion to grad and drop tile into empty space (black tile) 
refPt = []
dragging = False
def drag(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for n in ans:
            if x<=ans[n].xpos & x>ans[n].xpos-ans[n].width & y<=ans[n].ypos & y>ans[n].ypos-ans[n].heigth:
                xOld = ans[n].xpos
                yOld = ans[n].ypos
                marker = n
                dragging = True
    elif event == cv2.EVENT_LBUTTONUP:
        if x<=ans["black"].xpos & x>ans["black"].xpos-ans["black"].width & y<=ans["black"].ypos & y>ans["black"].ypos-ans["black"].heigth:
            xNew = ans["black"].xpos
            yNew = ans["black"].ypos
            ans[marker].xpos = xNew
            ans[marker].ypos = yNew
            ans['black'].xpos = xOld
            ans['black'].ypos = yOld
            dragging = False
            

# load the image, clone it, and setup the mouse callback function

image = cv2.imread("globe.jpg")
ans = makePuzzle(image)
board = np.zeros_like(image)
for ti in ans:
    board[ans[ti].xpos-ans[ti].width:ans[ti].xpos,ans[ti].ypos-ans[ti].heigth:ans[ti].ypos]= ans[ti].im
clone = board.copy()

cv2.namedWindow("board")
cv2.setMouseCallback("board", drag)

# keep looping until the 'q' key is pressed

while True:
    # display the image and wait for a keypress
    cv2.imshow("board", board)
    key = cv2.waitKey(1) & 0xFF
    for ti in ans:
        board[ans[ti].xpos-ans[ti].width:ans[ti].xpos,ans[ti].ypos-ans[ti].heigth:ans[ti].ypos]= ans[ti].im

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        board = clone.copy()
 
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break