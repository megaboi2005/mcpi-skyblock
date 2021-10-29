import mcpi.minecraft as minecraft
import math
import time
import asyncio
from random import randrange
import threading
import random
import numpy as np 
seedinput = input('insert seed here (must be an integer): ')
try:
    random.seed(seedinput)
except:
    random.seed()

# delete blocks and connect to the world
mc = minecraft.Minecraft.create()
mc.setBlocks(-128, -64, -128, 128, 128, 128, 0)


# dictionary for generators
gens = {
  "iron": 0,
  "gold": 0,
  "diamond": 0
}
# generators (very buggy )
def gen(x,y,z,genblock,idwool,amount,genname):
    print(f'started gen {genname}')
    gens[genname] = 0
    while True:
        
        
        mc.setBlock(x,y,z,35,idwool)
        block = mc.getBlock(x,y+1,z)
        if block == 4:
            if gens[genname] == amount:
                gens[genname] = 0
                mc.setBlock(x,y+1,z,genblock)
                
            else:
                mc.setBlock(x,y+1,z,0)
                gens[genname] +=1
                time.sleep(.5)



    
# current island generator
def island(offset,ranbiome,ranz):
    snowsel = 0

    print(ranbiome)
    ranlen = random.randint(3,20)

    for x in range(ranlen):
        
        for z in range((ranlen)):
            
            y = 2*math.sin(x-random.randint(1,100000))*math.cos(z-randrange(0,100000))
            

            
            rantree = random.randint(0,20)
            if ranbiome == 1:
                #print('forest biome')
                mc.setBlock(x+offset,y+1,z+ranz,2)
                mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-5,z+ranz,1)   
                
                if rantree == 5:
                    #print('planting trees')
                    mc.setBlocks(x-2+offset,y+6,z-2+ranz,x+2+offset,y+7,z+2+ranz,18)
                    mc.setBlocks(x-1+offset,y+8,z-1+ranz,x+1+offset,y+9,z+1+ranz,18)
                    mc.setBlocks(x+offset,y,z+ranz,x+offset,y+8,z+ranz,17)
                    mc.setBlock(x+offset,y+8,z+ranz,6)
                if rantree == 10:
                    mc.setBlock(x+offset,y+2,z+ranz,37)
                
            if ranbiome == 2:
                #print('desert biome')
                y = 0 
                mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-5,z+ranz,1)
                mc.setBlocks(x+offset,y+1,z+ranz,x+offset,y+3,z+ranz,12)
                if rantree == 5:
                    time.sleep(.5)
                    
                    
                    mc.setBlock(x+offset-1,y+4,z+ranz,0)
                    mc.setBlock(x+offset+1,y+4,z+ranz,0)
                    mc.setBlock(x+offset,y+4,z-1+ranz,0)
                    mc.setBlock(x+offset,y+4,z+1+ranz,0)
                    mc.setBlock(x+offset,y+4,z+ranz,81)
            if ranbiome == 3:
                y = 10*math.sin(x-random.randint(1,100000))*math.cos(z-randrange(0,100000))
                randblock = randrange(1,10)
                if randblock == 5:
                    mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-randrange(10,20),z+ranz,16)

                
                else:
                    mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-randrange(10,20),z+ranz,1)
                    mc.setBlocks(x+offset,y+1,z+ranz,x+offset,y+randrange(1,10),z+ranz,80)
                
            if ranbiome == 4:
                randblock = randrange(1,10)
                mc.setBlock(x+offset,y+1,z+ranz,87)
                mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-5,z+ranz,87)  
                randblock = randrange(1,10)
                if randblock == 5:
                    mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-10,z+ranz,10)
                if randblock == 2:
                    mc.setBlock(x+offset,y+2,z+ranz,40)
            if ranbiome == 5:
                y = y/15
                randblock = randrange(1,10)
                mc.setBlocks(x+offset,y+1,z+ranz,x+offset,y+1+randrange(0,1),z+ranz,80)
                if z == ranlen-1 or x == ranlen-1 or z == ranlen-ranlen or x == ranlen-ranlen: 
                    mc.setBlocks(x+offset,y,z+ranz,x+offset,y-randrange(10,20),z+ranz,80)
                else:
                    
                    mc.setBlocks(x+offset,y,z+ranz,x+offset,y-randrange(10,20),z+ranz,1)
                
                randblock = randrange(1,10)
                
                
    
# useless variables and some important ones lol
offset = 0
ironx = randrange(-10,10)
ironz = randrange(-10,10)
goldx = randrange(-5,5)
goldz = randrange(-5,5)
ironcount = 0
print(str(ironx) + ' '+ str(ironz))
repeat = 0
Run = True
# runs generator 
island(0,1,0)
while Run:
    ranz = random.randint(-127,127)
    ranbiome = randrange(1,6)
    island(offset,ranbiome,ranz)
    offset = randrange(-127,127)
    time.sleep(1)
    repeat += 1
    if repeat == 20:
        repeat = 0
        Run = False




#gen(x,y,z,genblock,idwool,amount)
        #iron
# threads
iron = threading.Thread(target=gen, args=(random.randint(-50,50),20,random.randint(-10,10),42,0,10,'iron'))
iron.start()

        #gold

gold = threading.Thread(target=gen, args=(random.randint(-5,5),10,random.randint(-5,5),41,4,5,'gold'))
gold.start()

        #diamond

diamond = threading.Thread(target=gen, args=(random.randint(-100,100),40,random.randint(-100,100),57,9,5,'diamonds'))
diamond.start()
