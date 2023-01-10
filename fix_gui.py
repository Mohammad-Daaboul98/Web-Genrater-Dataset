import random
import os
import sys

directory = os.fsencode('C:/Users/basel/Desktop/Senior Project/master/compiler/gui')

for file in os.listdir(directory):
    filename = os.fsdecode(file)

with open('C:/Users/basel/Desktop/Senior Project/master/compiler/gui/'+filename,'r') as inp:
    fixed = inp.read().replace(' ','\n')

with open('C:/Users/basel/Desktop/Senior Project/master/compiler/gui/'+filename, 'w') as out:
    out.write(fixed)