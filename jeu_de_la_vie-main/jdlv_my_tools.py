# -*- coding: utf-8 -*-
"""

"""

from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid):
    for i in range(41):
        if i<22:
            pass
        else:
            for j in range (53):
                grid.cases [i][j]['s'] = death_status
                grid.cases [i][j]['c'] = death_color
            i=i+1
    return grid

def clean_grid1(grid,w,x,y,z,a):
    if a==1:
        clean_grid0(grid,w,x,y,z)
    else:
        for i in range(w):
            if x<i<y:
                pass
            else:
                for j in range (z):
                    grid.cases [i][j]['s'] = death_status
                    grid.cases [i][j]['c'] = death_color
                i=i+1
        return grid

def clean_grid0(grid,w,x,y,z):

    for i in range(w):
        if x<i<y:
            for j in range (z):
                if j > (52):
                    grid.cases [i][j]['s'] = death_status
                    grid.cases [i][j]['c'] = death_color
            else:
                pass
                
            i=i+1
        else:
            pass
    return grid

def make_tete (grid, i, j, color):

    try:
        #pattes
        cases = grid.cases
        cases [i+17] [j+0] ['c'] = life_color
        cases [i+16] [j+0] ['c'] = life_color
        cases [i+15] [j+0] ['c'] = life_color
        cases [i+17] [j+1] ['c'] = life_color
        cases [i+17] [j+2] ['c'] = life_color
        cases [i+17] [j+3] ['c'] = life_color
        cases [i+16] [j+3] ['c'] = life_color
        cases [i+16] [j+4] ['c'] = life_color
        cases [i+15] [j+4] ['c'] = life_color
        cases [i+14] [j+3] ['c'] = life_color
        cases [i+14] [j+2] ['c'] = life_color
        cases [i+14] [j+1] ['c'] = life_color
        cases [i+17] [j+6] ['c'] = life_color
        cases [i+17] [j+7] ['c'] = life_color
        cases [i+17] [j+8] ['c'] = life_color
        cases [i+16] [j+6] ['c'] = life_color
        cases [i+16] [j+9] ['c'] = life_color
        cases [i+16] [j+17] ['c'] = life_color
        cases [i+17] [j+18] ['c'] = life_color
        cases [i+17] [j+19] ['c'] = life_color
        cases [i+17] [j+20] ['c'] = life_color
        cases [i+16] [j+20] ['c'] = life_color
        cases [i+16] [j+22] ['c'] = life_color
        cases [i+17] [j+23] ['c'] = life_color
        cases [i+17] [j+24] ['c'] = life_color
        cases [i+16] [j+25] ['c'] = life_color
        #tete
        cases [i+15] [j+25] ['c'] = life_color
        cases [i+15] [j+26] ['c'] = life_color
        cases [i+15] [j+24] ['c'] = life_color
        cases [i+15] [j+23] ['c'] = life_color
        cases [i+15] [j+22] ['c'] = life_color
        cases [i+15] [j+21] ['c'] = life_color
        cases [i+15] [j+20] ['c'] = life_color
        cases [i+15] [j+19] ['c'] = life_color
        cases [i+15] [j+18] ['c'] = life_color
        cases [i+15] [j+17] ['c'] = life_color
        cases [i+14] [j+16] ['c'] = life_color
        cases [i+13] [j+15] ['c'] = life_color
        cases [i+12] [j+14] ['c'] = life_color
        cases [i+11] [j+14] ['c'] = life_color
        cases [i+10] [j+14] ['c'] = life_color
        cases [i+9] [j+14] ['c'] = life_color
        cases [i+8] [j+15] ['c'] = life_color
        cases [i+7] [j+15] ['c'] = life_color
        cases [i+6] [j+15] ['c'] = life_color
        cases [i+5] [j+15] ['c'] = life_color
        cases [i+4] [j+16] ['c'] = life_color
        cases [i+4] [j+17] ['c'] = life_color
        cases [i+5] [j+18] ['c'] = life_color
        cases [i+6] [j+19] ['c'] = life_color
        cases [i+7] [j+20] ['c'] = life_color
        cases [i+7] [j+21] ['c'] = life_color
        cases [i+7] [j+22] ['c'] = life_color
        cases [i+7] [j+23] ['c'] = life_color
        cases [i+6] [j+24] ['c'] = life_color
        cases [i+5] [j+25] ['c'] = life_color
        cases [i+4] [j+26] ['c'] = life_color
        cases [i+4] [j+27] ['c'] = life_color
        cases [i+5] [j+28] ['c'] = life_color
        cases [i+6] [j+28] ['c'] = life_color
        cases [i+7] [j+28] ['c'] = life_color
        cases [i+8] [j+28] ['c'] = life_color
        cases [i+9] [j+29] ['c'] = life_color
        cases [i+10] [j+29] ['c'] = life_color
        cases [i+11] [j+29] ['c'] = life_color
        cases [i+12] [j+29] ['c'] = life_color
        cases [i+13] [j+28] ['c'] = life_color
        cases [i+14] [j+27] ['c'] = life_color
        #visage
        cases [i+13] [j+25] ['c'] = life_color
        cases [i+13] [j+24] ['c'] = life_color
        cases [i+13] [j+23] ['c'] = life_color
        cases [i+13] [j+22] ['c'] = life_color
        cases [i+13] [j+21] ['c'] = life_color
        cases [i+13] [j+20] ['c'] = life_color
        cases [i+13] [j+19] ['c'] = life_color
        cases [i+12] [j+19] ['c'] = life_color
        cases [i+12] [j+22] ['c'] = life_color
        cases [i+12] [j+25] ['c'] = life_color
        cases [i+10] [j+25] ['c'] = life_color
        cases [i+10] [j+26] ['c'] = life_color
        cases [i+9] [j+26] ['c'] = life_color
        cases [i+10] [j+23] ['c'] = life_color
        cases [i+10] [j+19] ['c'] = life_color
        cases [i+10] [j+18] ['c'] = life_color
        cases [i+9] [j+19] ['c'] = life_color


    except:
        pass
    return grid

def make_colortete (grid, i, j, color):
    life_color6='white'
    try:
        #tete
        cases = grid.cases
        cases [i+0] [j+1] ['c'] = life_color1
        cases [i+0] [j+2] ['c'] = life_color1
        cases [i+0] [j+11] ['c'] = life_color1
        cases [i+0] [j+12] ['c'] = life_color1
        cases [i+1] [j+1] ['c'] = life_color1
        cases [i+1] [j+2] ['c'] = life_color1
        cases [i+1] [j+3] ['c'] = life_color1
        cases [i+1] [j+10] ['c'] = life_color1
        cases [i+1] [j+11] ['c'] = life_color1
        cases [i+1] [j+12] ['c'] = life_color1
        cases [i+2] [j+1] ['c'] = life_color1
        cases [i+2] [j+2] ['c'] = life_color1
        cases [i+2] [j+3] ['c'] = life_color1
        cases [i+2] [j+4] ['c'] = life_color1
        cases [i+2] [j+9] ['c'] = life_color1
        cases [i+2] [j+10] ['c'] = life_color1
        cases [i+2] [j+11] ['c'] = life_color1
        cases [i+2] [j+12] ['c'] = life_color1
        cases [i+3] [j+1] ['c'] = life_color1
        cases [i+3] [j+2] ['c'] = life_color1
        cases [i+3] [j+3] ['c'] = life_color1
        cases [i+3] [j+4] ['c'] = life_color1
        cases [i+3] [j+5] ['c'] = life_color1
        cases [i+3] [j+6] ['c'] = life_color1
        cases [i+3] [j+7] ['c'] = life_color1
        cases [i+3] [j+8] ['c'] = life_color1
        cases [i+3] [j+9] ['c'] = life_color1
        cases [i+3] [j+10] ['c'] = life_color1
        cases [i+3] [j+11] ['c'] = life_color1
        cases [i+3] [j+12] ['c'] = life_color1
        cases [i+4] [j+0] ['c'] = life_color1
        cases [i+4] [j+1] ['c'] = life_color1
        cases [i+4] [j+2] ['c'] = life_color1
        cases [i+4] [j+4] ['c'] = life_color
        cases [i+4] [j+3] ['c'] = life_color6
        cases [i+4] [j+5] ['c'] = life_color1
        cases [i+4] [j+6] ['c'] = life_color1
        cases [i+4] [j+7] ['c'] = life_color1
        cases [i+4] [j+8] ['c'] = life_color1
        cases [i+4] [j+9] ['c'] = life_color1
        cases [i+4] [j+11] ['c'] = life_color
        cases [i+4] [j+10] ['c'] = life_color6
        cases [i+4] [j+12] ['c'] = life_color1
        cases [i+4] [j+13] ['c'] = life_color1
        cases [i+5] [j+0] ['c'] = life_color1
        cases [i+5] [j+1] ['c'] = life_color1
        cases [i+5] [j+2] ['c'] = life_color1
        cases [i+5] [j+5] ['c'] = life_color1
        cases [i+5] [j+6] ['c'] = life_color1
        cases [i+5] [j+7] ['c'] = life_color1
        cases [i+5] [j+9] ['c'] = life_color1
        cases [i+5] [j+12] ['c'] = life_color1
        cases [i+5] [j+13] ['c'] = life_color1
        cases [i+6] [j+0] ['c'] = life_color1
        cases [i+6] [j+1] ['c'] = life_color2
        cases [i+6] [j+2] ['c'] = life_color2
        cases [i+6] [j+3] ['c'] = life_color1
        cases [i+6] [j+4] ['c'] = life_color1
        cases [i+6] [j+5] ['c'] = life_color1
        cases [i+6] [j+6] ['c'] = life_color1
        cases [i+6] [j+7] ['c'] = life_color1
        cases [i+6] [j+8] ['c'] = life_color1
        cases [i+6] [j+9] ['c'] = life_color1
        cases [i+6] [j+10] ['c'] = life_color1
        cases [i+6] [j+11] ['c'] = life_color1
        cases [i+6] [j+12] ['c'] = life_color2
        cases [i+6] [j+13] ['c'] = life_color2
        cases [i+7] [j+0] ['c'] = life_color1
        cases [i+7] [j+1] ['c'] = life_color2
        cases [i+7] [j+2] ['c'] = life_color2
        cases [i+7] [j+3] ['c'] = life_color1
        cases [i+7] [j+5] ['c'] = life_color1
        cases [i+7] [j+6] ['c'] = life_color1
        cases [i+7] [j+8] ['c'] = life_color1
        cases [i+7] [j+9] ['c'] = life_color1
        cases [i+7] [j+11] ['c'] = life_color1
        cases [i+7] [j+12] ['c'] = life_color2
        cases [i+7] [j+13] ['c'] = life_color2
        cases [i+8] [j+1] ['c'] = life_color1
        cases [i+8] [j+2] ['c'] = life_color1
        cases [i+8] [j+3] ['c'] = life_color1
        cases [i+8] [j+11] ['c'] = life_color1
        cases [i+8] [j+12] ['c'] = life_color1
        cases [i+9] [j+2] ['c'] = life_color1
        cases [i+9] [j+3] ['c'] = life_color1
        cases [i+9] [j+4] ['c'] = life_color1
        cases [i+9] [j+5] ['c'] = life_color1
        cases [i+9] [j+6] ['c'] = life_color1
        cases [i+9] [j+7] ['c'] = life_color1
        cases [i+9] [j+8] ['c'] = life_color1
        cases [i+9] [j+9] ['c'] = life_color1
        cases [i+9] [j+10] ['c'] = life_color1
        cases [i+9] [j+11] ['c'] = life_color1

    except:
        pass
    return grid

def make_colorcorps (grid, i, j):
    try:
        #tete
        cases = grid.cases
        cases [i+1] [j+2] ['c'] = beige
        cases [i+1] [j+3] ['c'] = beige
        cases [i+1] [j+4] ['c'] = beige
        cases [i+1] [j+5] ['c'] = beige
        cases [i+1] [j+6] ['c'] = beige
        cases [i+1] [j+7] ['c'] = beige
        cases [i+1] [j+8] ['c'] = beige
        cases [i+1] [j+9] ['c'] = beige
        cases [i+1] [j+10] ['c'] = beige
        cases [i+1] [j+11] ['c'] = beige
        cases [i+1] [j+12] ['c'] = beige
        cases [i+1] [j+13] ['c'] = beige
        cases [i+1] [j+14] ['c'] = beige
        cases [i+1] [j+15] ['c'] = beige
        cases [i+1] [j+16] ['c'] = beige
        cases [i+1] [j+17] ['c'] = beige
        cases [i+1] [j+18] ['c'] = beige
        cases [i+1] [j+19] ['c'] = beige
        #2
        cases [i+2] [j+1] ['c'] = beige
        cases [i+2] [j+2] ['c'] = beige
        cases [i+2] [j+3] ['c'] = rose
        cases [i+2] [j+4] ['c'] = rose
        cases [i+2] [j+5] ['c'] = rose
        cases [i+2] [j+6] ['c'] = rose
        cases [i+2] [j+7] ['c'] = rose
        cases [i+2] [j+8] ['c'] = rose
        cases [i+2] [j+9] ['c'] = rose
        cases [i+2] [j+10] ['c'] = rose
        cases [i+2] [j+11] ['c'] = rose
        cases [i+2] [j+12] ['c'] = rose
        cases [i+2] [j+13] ['c'] = rose
        cases [i+2] [j+14] ['c'] = rose
        cases [i+2] [j+15] ['c'] = rose
        cases [i+2] [j+16] ['c'] = rose
        cases [i+2] [j+17] ['c'] = rose
        cases [i+2] [j+18] ['c'] = rose
        cases [i+2] [j+19] ['c'] = beige
        cases [i+2] [j+20] ['c'] = beige
        a=1
        while a<11:
            cases [i+2+a] [j+1] ['c'] = beige
            cases [i+2+a] [j+2] ['c'] = rose
            cases [i+2+a] [j+3] ['c'] = rose
            cases [i+2+a] [j+4] ['c'] = rose
            cases [i+2+a] [j+5] ['c'] = rose
            cases [i+2+a] [j+6] ['c'] = rose
            cases [i+2+a] [j+7] ['c'] = rose
            cases [i+2+a] [j+8] ['c'] = rose
            cases [i+2+a] [j+9] ['c'] = rose
            cases [i+2+a] [j+10] ['c'] = rose
            cases [i+2+a] [j+11] ['c'] = rose
            cases [i+2+a] [j+12] ['c'] = rose
            cases [i+2+a] [j+13] ['c'] = rose
            cases [i+2+a] [j+14] ['c'] = rose
            cases [i+2+a] [j+15] ['c'] = rose
            cases [i+2+a] [j+16] ['c'] = rose
            cases [i+2+a] [j+17] ['c'] = rose
            cases [i+2+a] [j+18] ['c'] = rose
            cases [i+2+a] [j+19] ['c'] = rose
            cases [i+2+a] [j+20] ['c'] = beige
            a=a+1
        a=11
        cases [i+2+a] [j+1] ['c'] = beige
        cases [i+2+a] [j+2] ['c'] = beige
        cases [i+2+a] [j+3] ['c'] = rose
        cases [i+2+a] [j+4] ['c'] = rose
        cases [i+2+a] [j+5] ['c'] = rose
        cases [i+2+a] [j+6] ['c'] = rose
        cases [i+2+a] [j+7] ['c'] = rose
        cases [i+2+a] [j+8] ['c'] = rose
        cases [i+2+a] [j+9] ['c'] = rose
        cases [i+2+a] [j+10] ['c'] = rose
        cases [i+2+a] [j+11] ['c'] = rose
        cases [i+2+a] [j+12] ['c'] = rose
        cases [i+2+a] [j+13] ['c'] = rose
        cases [i+2+a] [j+14] ['c'] = rose
        cases [i+2+a] [j+15] ['c'] = rose
        cases [i+2+a] [j+16] ['c'] = rose
        cases [i+2+a] [j+17] ['c'] = rose
        cases [i+2+a] [j+18] ['c'] = rose
        cases [i+2+a] [j+19] ['c'] = beige
        cases [i+2+a] [j+20] ['c'] = beige
        a=a+1
        cases [i+2+a] [j+2] ['c'] = beige
        cases [i+2+a] [j+3] ['c'] = beige
        cases [i+2+a] [j+4] ['c'] = beige
        cases [i+2+a] [j+5] ['c'] = beige
        cases [i+2+a] [j+6] ['c'] = beige
        cases [i+2+a] [j+7] ['c'] = beige
        cases [i+2+a] [j+8] ['c'] = beige
        cases [i+2+a] [j+9] ['c'] = beige
        cases [i+2+a] [j+10] ['c'] = beige
        cases [i+2+a] [j+11] ['c'] = beige
        cases [i+2+a] [j+12] ['c'] = beige
        cases [i+2+a] [j+13] ['c'] = beige
        cases [i+2+a] [j+14] ['c'] = beige
        cases [i+2+a] [j+15] ['c'] = beige
        cases [i+2+a] [j+16] ['c'] = beige
        cases [i+2+a] [j+17] ['c'] = beige
        cases [i+2+a] [j+18] ['c'] = beige
        cases [i+2+a] [j+19] ['c'] = beige


    except:
        pass
    return grid

def color_pates (grid, i, j, color):

    try:
        cases = grid.cases
        cases [i+0] [j+0] ['c'] = life_color1
        cases [i+0] [j+1] ['c'] = life_color1
        cases [i+0] [j+2] ['c'] = life_color1
        cases [i+1] [j+0] ['c'] = life_color1
        cases [i+1] [j+1] ['c'] = life_color1
        cases [i+1] [j+6] ['c'] = life_color1
        cases [i+1] [j+7] ['c'] = life_color1
        cases [i+1] [j+17] ['c'] = life_color1
        cases [i+1] [j+18] ['c'] = life_color1
        cases [i+1] [j+22] ['c'] = life_color1
        cases [i+1] [j+23] ['c'] = life_color1

    except:
        pass
    return grid

def make_lanceur_glisseur_coulisseur_compresseur_aspirateur_aligatueur (grid):
    i= random.randint(10, 65)
    if 18<i<26 or 39<i<47:
        pass
    else:
        j=90
        try:
            cases = grid.cases
            cases [i+0] [j+0] ['c'] = white
            cases [i+0] [j+0] ['s'] = 1
            cases [i-1] [j+0] ['c'] = white
            cases [i-1] [j+0] ['s'] = 1
            cases [i-1] [j+0] ['c'] = white
            cases [i-1] [j+0] ['s'] = 1
            cases [i-2] [j+0] ['c'] = white
            cases [i-2] [j+0] ['s'] = 1
            cases [i-3] [j+1] ['c'] = white
            cases [i-3] [j+1] ['s'] = 1
            cases [i-4] [j+3] ['c'] = white
            cases [i-4] [j+3] ['s'] = 1
            cases [i-3] [j+5] ['c'] = white
            cases [i-3] [j+5] ['s'] = 1
            cases [i-1] [j+5] ['c'] = white
            cases [i-1] [j+5] ['s'] = 1
            cases [i-0] [j+4] ['c'] = white
            cases [i-0] [j+4] ['s'] = 1
            cases [i-0] [j+3] ['c'] = white
            cases [i-0] [j+3] ['s'] = 1
            cases [i-0] [j+2] ['c'] = white
            cases [i-0] [j+2] ['s'] = 1
            cases [i-0] [j+1] ['c'] = white
            cases [i-0] [j+1] ['s'] = 1
        except:
            pass
    return grid

def color_queue2 (grid, i, j, color):
    try:
        cases=grid.cases
        cases [i+1] [j+1] ['c'] = life_color1
        cases [i+1] [j+2] ['c'] = life_color1
        cases [i+1] [j+3] ['c'] = life_color1
        cases [i+1] [j+4] ['c'] = life_color1
        cases [i+2] [j+3] ['c'] = life_color1
        cases [i+2] [j+4] ['c'] = life_color1
        cases [i+2] [j+5] ['c'] = life_color1
        cases [i+2] [j+6] ['c'] = life_color1
    except:
        pass
    return grid

def color_queue1 (grid, i, j, color):
    try:
        cases=grid.cases
        cases [i+1] [j+4] ['c'] = life_color1
        cases [i+1] [j+5] ['c'] = life_color1
        cases [i+2] [j+2] ['c'] = life_color1
        cases [i+2] [j+3] ['c'] = life_color1
        cases [i+2] [j+4] ['c'] = life_color1
        cases [i+2] [j+5] ['c'] = life_color1
        cases [i+3] [j+1] ['c'] = life_color1
        cases [i+3] [j+2] ['c'] = life_color1
        cases [i+4] [j+1] ['c'] = life_color1
        cases [i+4] [j+2] ['c'] = life_color1
    except:
        pass
    return grid

def color_queue3 (grid, i, j, color):
    try:
        cases=grid.cases
        cases [i+1] [j+1] ['c'] = life_color1
        cases [i+1] [j+2] ['c'] = life_color1
        cases [i+2] [j+2] ['c'] = life_color1
        cases [i+2] [j+3] ['c'] = life_color1
        cases [i+3] [j+3] ['c'] = life_color1
        cases [i+3] [j+4] ['c'] = life_color1
        cases [i+4] [j+4] ['c'] = life_color1
        cases [i+4] [j+5] ['c'] = life_color1
    except:
        pass
    return grid

def make_corps (grid, i, j, color):

    try:
        #corps
        cases = grid.cases
        cases [i+15] [j+15] ['c'] = life_color
        cases [i+15] [j+14] ['c'] = life_color
        cases [i+15] [j+13] ['c'] = life_color
        cases [i+15] [j+12] ['c'] = life_color
        cases [i+15] [j+11] ['c'] = life_color
        cases [i+15] [j+10] ['c'] = life_color
        cases [i+15] [j+9] ['c'] = life_color
        cases [i+15] [j+8] ['c'] = life_color
        cases [i+15] [j+7] ['c'] = life_color
        cases [i+15] [j+6] ['c'] = life_color
        cases [i+15] [j+5] ['c'] = life_color
        cases [i+15] [j+4] ['c'] = life_color
        cases [i+15] [j+3] ['c'] = life_color
        cases [i+15] [j+2] ['c'] = life_color
        cases [i+14] [j+1] ['c'] = life_color
        cases [i+13] [j+0] ['c'] = life_color
        cases [i+12] [j+0] ['c'] = life_color
        cases [i+11] [j+0] ['c'] = life_color
        cases [i+10] [j+0] ['c'] = life_color
        cases [i+9] [j+0] ['c'] = life_color
        cases [i+8] [j+0] ['c'] = life_color
        cases [i+7] [j+0] ['c'] = life_color
        cases [i+6] [j+0] ['c'] = life_color
        cases [i+5] [j+0] ['c'] = life_color
        cases [i+4] [j+0] ['c'] = life_color
        cases [i+3] [j+0] ['c'] = life_color
        cases [i+2] [j+0] ['c'] = life_color
        cases [i+1] [j+1] ['c'] = life_color
        cases [i+0] [j+2] ['c'] = life_color
        cases [i+0] [j+3] ['c'] = life_color
        cases [i+0] [j+4] ['c'] = life_color
        cases [i+0] [j+5] ['c'] = life_color
        cases [i+0] [j+6] ['c'] = life_color
        cases [i+0] [j+7] ['c'] = life_color
        cases [i+0] [j+8] ['c'] = life_color
        cases [i+0] [j+9] ['c'] = life_color
        cases [i+0] [j+10] ['c'] = life_color
        cases [i+0] [j+11] ['c'] = life_color
        cases [i+0] [j+12] ['c'] = life_color
        cases [i+0] [j+13] ['c'] = life_color
        cases [i+0] [j+14] ['c'] = life_color
        cases [i+0] [j+15] ['c'] = life_color
        cases [i+0] [j+16] ['c'] = life_color
        cases [i+0] [j+17] ['c'] = life_color
        cases [i+0] [j+18] ['c'] = life_color
        cases [i+0] [j+19] ['c'] = life_color
        cases [i+1] [j+20] ['c'] = life_color
        cases [i+2] [j+21] ['c'] = life_color
        cases [i+3] [j+21] ['c'] = life_color
        cases [i+4] [j+21] ['c'] = life_color
        cases [i+5] [j+21] ['c'] = life_color
        cases [i+6] [j+21] ['c'] = life_color
        #point du chat
        cases [i+3] [j+18] ['c'] = life_color3
        cases [i+2] [j+12] ['c'] = life_color3
        cases [i+3] [j+7] ['c'] = life_color3
        cases [i+4] [j+3] ['c'] = life_color3
        cases [i+6] [j+9] ['c'] = life_color3
        cases [i+7] [j+5] ['c'] = life_color3
        cases [i+9] [j+8] ['c'] = life_color3
        cases [i+12] [j+9] ['c'] = life_color3
        cases [i+11] [j+3] ['c'] = life_color3



    except:
        pass
    return grid

def make_queue1 (grid, i, j, color):

    try:
        #queue1
        cases = grid.cases
        cases [i+0] [j+0] ['c'] = life_color
        cases [i+0] [j+1] ['c'] = life_color
        cases [i+0] [j+2] ['c'] = life_color
        cases [i+0] [j+3] ['c'] = life_color
        cases [i+1] [j+3] ['c'] = life_color
        cases [i+1] [j+4] ['c'] = life_color
        cases [i+2] [j+4] ['c'] = life_color
        cases [i+2] [j+5] ['c'] = life_color
        cases [i+3] [j+5] ['c'] = life_color
        cases [i+3] [j+6] ['c'] = life_color
        cases [i+1] [j+0] ['c'] = life_color
        cases [i+2] [j+0] ['c'] = life_color
        cases [i+2] [j+1] ['c'] = life_color
        cases [i+3] [j+1] ['c'] = life_color
        cases [i+3] [j+2] ['c'] = life_color
        cases [i+4] [j+2] ['c'] = life_color
        cases [i+4] [j+3] ['c'] = life_color
        cases [i+5] [j+3] ['c'] = life_color
        cases [i+5] [j+4] ['c'] = life_color
        cases [i+5] [j+5] ['c'] = life_color
        cases [i+6] [j+5] ['c'] = life_color

    except:
        pass
    return grid

def make_queue2 (grid, i, j, color):

    try:
        #queue2
        cases = grid.cases
        cases [i+0] [j+1] ['c'] = life_color
        cases [i+0] [j+2] ['c'] = life_color
        cases [i+0] [j+3] ['c'] = life_color
        cases [i+0] [j+4] ['c'] = life_color
        cases [i+0] [j+5] ['c'] = life_color
        cases [i+1] [j+5] ['c'] = life_color
        cases [i+1] [j+6] ['c'] = life_color
        cases [i+1] [j+7] ['c'] = life_color
        cases [i+2] [j+7] ['c'] = life_color
        cases [i+4] [j+7] ['c'] = life_color
        cases [i+4] [j+6] ['c'] = life_color
        cases [i+3] [j+6] ['c'] = life_color
        cases [i+3] [j+5] ['c'] = life_color
        cases [i+3] [j+4] ['c'] = life_color
        cases [i+3] [j+3] ['c'] = life_color
        cases [i+2] [j+2] ['c'] = life_color
        cases [i+2] [j+1] ['c'] = life_color
        cases [i+2] [j+0] ['c'] = life_color
        cases [i+1] [j+0] ['c'] = life_color

    except:
        pass
    return grid

def make_queue3 (grid, i, j, color):

    try:
        #queue3
        cases = grid.cases
        cases [i+0] [j+4] ['c'] = life_color
        cases [i+0] [j+5] ['c'] = life_color
        cases [i+1] [j+3] ['c'] = life_color
        cases [i+1] [j+2] ['c'] = life_color
        cases [i+2] [j+1] ['c'] = life_color
        cases [i+3] [j+0] ['c'] = life_color
        cases [i+4] [j+0] ['c'] = life_color
        cases [i+5] [j+1] ['c'] = life_color
        cases [i+5] [j+2] ['c'] = life_color
        cases [i+4] [j+3] ['c'] = life_color
        cases [i+3] [j+3] ['c'] = life_color
        cases [i+3] [j+4] ['c'] = life_color
        cases [i+3] [j+5] ['c'] = life_color

    except:
        pass
    return grid

def make_rectangle (grid, i, j, color):

    try:
        #arc en ciel
        cases = grid.cases
        cases [i+0] [j-0] ['c'] = color
        cases [i+0] [j-1] ['c'] = color
        cases [i+0] [j-2] ['c'] = color
        cases [i+0] [j-3] ['c'] = color
        cases [i+0] [j-4] ['c'] = color
        cases [i+0] [j-5] ['c'] = color
        cases [i+1] [j-0] ['c'] = color
        cases [i+1] [j-1] ['c'] = color
        cases [i+1] [j-2] ['c'] = color
        cases [i+1] [j-3] ['c'] = color
        cases [i+1] [j-4] ['c'] = color
        cases [i+1] [j-5] ['c'] = color


    except:
        pass
    return grid

def make_rainbow(grid, i, j, color):
    grid = make_rectangle (grid, i+25, j+5, 'red') and make_rectangle(grid, i+27, j+5, 'orange')\
        and make_rectangle(grid, i+29, j+5, 'yellow') and make_rectangle(grid, i+31, j+5, 'lime')\
        and make_rectangle(grid, i+33, j+5, 'deepskyblue') and make_rectangle(grid, i+35, j+5, 'blueviolet')
    return grid

def rien (grid, color):

    try:
        cases = grid.cases
    except:
        pass
    return grid

def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
##            if previous_status ==life_status:
##                print("1")
##                next_cases [i] [j] = revive_case (next_cases [i] [j-1])
            if nbre_alive_voisins == 3:
                 next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                 next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def part1 (grid, compteur):
    clean_grid(grid)
    next_grid = make_rainbow(grid, 0, 24, 'red') and make_colorcorps(grid,23,25) and make_rainbow(grid, 1, 18, 'red') and make_corps(grid, 23, 25, 'red') and make_tete(grid, 23, 23, 'red') \
        and make_queue1(grid, 29, 19, 'red') and make_rainbow(grid, 0, 0, 'red')\
        and make_rainbow(grid, 1, 6, 'red') and make_rainbow(grid, 0, 12, 'red')\
        and make_colortete(grid, 28, 38, 'red') and color_pates(grid, 38, 24, 'red')\
        and color_queue3(grid, 29, 19, 'red') 
    return next_grid

def part2 (grid, compteur):
    clean_grid(grid)
    next_grid = make_rainbow(grid, 1, 24, 'red') and make_colorcorps(grid,23,25) and  make_rainbow(grid, 0, 18, 'red') and make_corps(grid, 23, 25, 'red') and make_tete(grid, 23, 22, 'red') \
        and make_queue2(grid, 31, 18, 'red') and make_rainbow(grid, 1, 0, 'red')\
        and make_rainbow(grid, 0, 6, 'red') and make_rainbow(grid, 1, 12, 'red')\
        and make_colortete(grid, 28, 37, 'red') and color_pates(grid, 38, 23, 'red')\
        and color_queue2(grid, 31, 18, 'red')
    return next_grid

def part3 (grid, compteur):
    clean_grid(grid)
    next_grid =make_rainbow(grid, 0, 24, 'red') and make_colorcorps(grid,22,25) and  make_rainbow(grid, 1, 18, 'red') and make_corps(grid, 22, 25, 'red') and make_tete(grid, 22, 22, 'red') \
        and make_queue3(grid, 30, 19, 'red') and make_rainbow(grid, 0, 0, 'red')\
        and make_rainbow(grid, 1, 6, 'red') and make_rainbow(grid, 0, 12, 'red')\
        and make_colortete(grid, 27, 37, 'red') and color_pates(grid, 37, 23, 'red')\
        and color_queue1(grid, 30, 19, 'red')
    return next_grid

def part4 (grid, compteur):
    clean_grid(grid)
    next_grid = make_rainbow(grid, 1, 24, 'red') and make_colorcorps(grid,22,25) and  make_rainbow(grid, 0, 18, 'red') and make_corps(grid, 22, 25, 'red') and make_tete(grid, 22, 23, 'red') \
        and make_queue2(grid, 30, 18, 'red') and make_rainbow(grid, 1, 0, 'red')\
        and make_rainbow(grid, 0, 6, 'red') and make_rainbow(grid, 1, 12, 'red')\
        and make_colortete(grid, 27, 38, 'red') and color_pates(grid, 37, 24, 'red')\
        and color_queue2(grid, 30, 18, 'red')
    return next_grid

def part5(grid,compteur):
    next_grid =make_lanceur_glisseur_coulisseur_compresseur_aspirateur_aligatueur (grid)
    return next_grid

def apply_rules (grid, compteur):
    next_grid = grid
    next_grid= apply_game_of_life_rules (next_grid)
    if compteur % 4 == 0:
        next_grid = part1(next_grid, compteur)
    elif compteur % 4 == 1:
        next_grid = part2(next_grid, compteur)
    elif compteur % 4 == 2:
        next_grid = part3(next_grid, compteur)
    elif compteur % 4 == 3:
        next_grid = part4(next_grid, compteur)
    if compteur % 20== 1:
        next_grid = part5(next_grid, compteur)
    if compteur % 20==1:
        clean_grid1(next_grid,90,22,41,6,10)
    if compteur % 20==1:
        clean_grid1(next_grid,90,19,41,59,1)
    time.sleep(0.00)
    return next_grid


