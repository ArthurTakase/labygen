from move import *
from printlaby import *
from newway import *
from goto import *
from end import *
import sys
import time

def secur(command):
    if len(command) != 3 : # Verification du nombre d'argument.
        print("""Vous n'avez pas rentré le bon nombre d'argument.
Pour utiliser ce programme, il faut faire 'python3.8 main.py height width'""")
        exit()
    else :
        return 0

def gen() : # genere le tableau de base
    command = sys.argv # ["laby.py", "10", "20"]
    secur(command)
    xmax = int(command[1])
    ymax = int(command[2])
    tab = []
    for y in range(ymax):
        line = []
        for x in range(xmax):
            if y == 0 and x == 0 :
                line.append("1")
            elif y == ymax - 1 and x == xmax - 1 :
                line.append("0")
            else :
                if y % 2 == 0 :
                    if x % 2 != 0 :
                        line.append("X")
                    else :
                        line.append("0")
                else :
                     line.append("X")
        tab.append(line)

    #print_laby(tab)

    y = 0
    x = 0
    while not end(tab, ymax, xmax) :
        y, x = move(tab, y, x, ymax, xmax)
        if goto_up(tab, x, y) == "no" and goto_down(tab, x, y, ymax) == "no" and goto_left(tab, x, y) == "no" and goto_right(tab, x, y, xmax) == "no" and not end(tab, ymax, xmax):
                x, y = newway(tab, ymax, xmax)
    print_laby(tab)
        #time.sleep(0.000001)

gen()
