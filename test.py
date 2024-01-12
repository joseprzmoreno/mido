from utils import *
import threading
import random 

instr1 = 'dong01.ogg'
instr2 = 'heaven_strings01.ogg'
instr3 = 'orion_string01.ogg'

start = 0
stop = 4
step = 0.25
times = [i * step for i in range(int(start / step), int(stop / step))]
notes = [60, 62, 67, 62] * 3 + [69, 70, 74, 67]
durs = [0.25] * 16
vels = [64] * 16

times2 = [0, 1, 2, 3]
notes2 = [60, 72, 67, 67+12]
durs2 = [2] * 4
vels2 = [24, 12, 20, 8]

def a():
    for i in range(0,5):
        play_seq(instr1, times, notes, durs, vels)

def b():
    for i in range(0,5):
        play_seq(instr2, times2, notes2, durs2, vels2)

def c():
    for i in range(0,5):
        play_seq(instr3, times2, notes2, durs2, vels2)

orchestrate([a, b, c])

print("Finished")