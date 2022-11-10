import random as rnd 
import numpy as np
#1import matplotlib.pyplot as plt
grid = np.zeros((6, 7), dtype = int)
print(grid)
gameover = False

def checkgameover():
    winvertical = checkwinvertical()
    winhorizontal = checkwinhorizontal()
    windiagupright = checkwindiagupright()
    windiagupleft = checkwindiagupleft()
    draw = gameoverdraw()
    if winvertical or winhorizontal or windiagupright or windiagupleft or draw:
        finalgameboard(grid)
        return True
   

def errorcolumnfull(q):
    p = input("choose a different column in the range 1 to 7 ")
    p = checkfornum(p)
    p = errorchecker3000(p)
    p = p - 1
    q = 5
    return q

def errorcolumnfullcomp(s):
    while s < 0:
        r = rnd.randint(0,6)
        s = 5
    return s

def gameoverdraw():
    if np.sum(grid) == 63:
        print("The game is over, the board is full and the result is a draw")
        return True

def checkwinvertical():
    for x in range(7):
        for y in range(3):
            if grid[y,x] == grid[y+1,x] == grid[y+2,x] == grid[y+3,x] ==1:
                print("you won m8 well done")
                return True
            if grid[y,x] == grid[y+1,x] == grid[y+2,x] == grid[y+3,x] ==2:
                print("the computer won and you lost, seriously m8 u lost to a random bot r u dumb bravv")
                return True

def checkwinhorizontal():
   for x in range(3):
       for y in range(6):
           if grid[y,x] == grid[y,x+1] == grid[y,x+2] == grid[y,x+3] ==1:
               print("you won m8 well done")
               return True
           if grid[y,x] == grid[y,x+1] == grid[y,x+2] == grid[y,x+3] ==2:
               print("the computer won and you lost, seriously m8 u lost to a random bot r u dumb bravv")
               return True

def checkwindiagupright():
   for x in range(4):
       for y in range(3,6):
           if grid[y,x] == grid[y-1,x+1] == grid[y-2,x+2] == grid[y-3,x+3] ==1:
               print("you won m8 well done")
               return True
           if grid[y,x] == grid[y-1,x+1] == grid[y-2,x+2] == grid[y-3,x+3] ==2:
               print("the computer won and you lost, seriously m8 u lost to a random bot r u dumb bravv")
               return True

def checkwindiagupleft():
   for x in range(3,7):
       for y in range(3,6):
           if grid[y,x] == grid[y-1,-1] == grid[y-2,x-2] == grid[y-3,x-3] ==1:
               print("you won m8 well done")
               return True
           if grid[y,x] == grid[y-1,x-1] == grid[y-2,x-2] == grid[y-3,x-3] ==2:
               print("the computer won and you lost, seriously m8 u lost to a random bot r u dumb bravv")
               return True

def errorchecker3000(p):
    while p < 1 or p > 7 or type(p) != int:
        p = (input("You must choose an integer between 1 and 7 inclusive "))
        p = checkfornum(p)
    return p

def checkfornum(p):
    pisobtained = False
    while pisobtained == False:
        try:
            p = eval(p)
            pisobtained = True
        except:
            p = input("You must choose an number ")
    return p

def placetoken(grid):
    tokenisplaced = False
    q = 5
    p = input("choose a column from 1 to 7 ")
    p = checkfornum(p)
    p = errorchecker3000(p)
    p = p - 1
    while tokenisplaced == False:
        if grid[q,p] == 0:
            grid[q,p] = 1
            tokenisplaced = True
        elif q < 1:
            p = input("choose a different column in the range 1 to 7 ")
            p = checkfornum(p)
            p = errorchecker3000(p)
            p = p - 1
            q = 5
        else:
            q = q-1
    return grid

def computer(grid):
    tokenisplacedcomp = False
    s = 5
    r = rnd.randint(0,6)
    while tokenisplacedcomp == False:
        if grid[s,r] == 0:
            grid[s,r] = 2
            tokenisplacedcomp = True
        elif s < 1:
            r = rnd.randint(0,6)
            s = 5
        else:
           s = s-1
    return grid

def finalgameboard(grid):
    return
    
    
check = checkgameover()    
while check != True:
    grid = placetoken(grid)
    grid = computer(grid)
    print(grid)
    check = checkgameover()
    
    #things left to do:
        #fix the issue where it prints it 4 times
        #plot the final graph
        #i think that's it all the error checking is done and the game actually works now.
        #put nicer messages for when u win and stuff
        #maybe change the variables to column and stuff to make it easier to understand
        #write a description for each thingy
        #make the layout clear
        #give a welcome message
        #you could also change the way it works to allow for the computer to go first or to play against another player but that's a lot of work so allow it
