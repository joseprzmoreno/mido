from utils import *
import threading
import random 

instr1 = 'Freeboy'
instr2 = 'heaven_strings01.ogg'
instr3 = 'Freeboy'

times1 = [i * 0.25 for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]
notes1 = [62,62+12,67,69] * 4
durs1 = [0.25] * 16
vels1 = [64] * 16

times2 = [0,1,2,3]
notes2 = [[62,66,69],[66,69,73],[70,73,77],[67,69,73,77]]
durs2 = [1] * 4
vels2 = [50] * 4

times3 = [0, 2]
notes3 = [69, 67]
durs3 = [4] * 2
vels3 = [30] * 2

def a():
    play_seq(instr1, times1, notes1, durs1, vels1)

def b():
    play_seq(instr2, times2, notes2, durs2, vels2)

def c():
    play_seq(instr3, times3, notes3, durs3, vels3)

orchestrate([a, b, c])

print("Finished")