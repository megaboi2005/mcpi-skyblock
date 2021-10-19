import mcpi.minecraft as minecraft
import math
import time
import asyncio
from random import randrange
import threading

# delete blocks and connect to the world
mc = minecraft.Minecraft.create()
mc.setBlocks(-333, -64, -333, 333, 128, 333, 0)


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
def island(offset):
    ranbiome = randrange(1,3)
    print(ranbiome)
    ranlen = randrange(3,20)
    ranz = (randrange(-127,127))
    for x in range(ranlen):
        
        for z in range((ranlen)):
            
            y = 2*math.sin(x-randrange(0,100000))*math.cos(z-randrange(0,100000))
            
            
            rantree = randrange(1,20)
            if ranbiome == 1:
                #print('forest biome')
                mc.setBlock(x+offset,y+1,z+ranz,2)
                                        
                if rantree == 5:
                    #print('planting trees')
                    mc.setBlocks(x-2+offset,y+6,z-2+ranz,x+2+offset,y+7,z+2+ranz,18)
                    mc.setBlocks(x-1+offset,y+8,z-1+ranz,x+1+offset,y+9,z+1+ranz,18)
                    mc.setBlocks(x+offset,y,z+ranz,x+offset,y+8,z+ranz,17)
                    mc.setBlock(x+offset,y+8,z+ranz,6)
                mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-5,z+ranz,1)
            if ranbiome == 2:
                #print('desert biome')
                y = 0 
                mc.setBlocks(x+offset,y,z+ranz,x+offset,y-y-5,z+ranz,1)
                mc.setBlocks(x+offset,y+1,z+ranz,x+offset,y+3,z+ranz,12)
                if rantree ==5:
                    time.sleep(.5)
                    print('planting cacti')
                    
                    mc.setBlock(x+offset-1,y+4,z+ranz,0)
                    mc.setBlock(x+offset+1,y+4,z+ranz,0)
                    mc.setBlock(x+offset,y+4,z-1+ranz,0)
                    mc.setBlock(x+offset,y+4,z+1+ranz,0)
                    mc.setBlock(x+offset,y+4,z+ranz,81)
                
            
    
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
while Run:
    island(offset)
    offset += randrange(5,30)
    time.sleep(1)
    repeat += 1
    if repeat == 10:
        repeat = 0
        Run = False




#gen(x,y,z,genblock,idwool,amount)
        #iron
# threads
iron = threading.Thread(target=gen, args=(randrange(-10,10),20,randrange(-10,10),42,0,10,'iron'))
iron.start()

        #gold

gold = threading.Thread(target=gen, args=(randrange(-5,5),10,randrange(-5,5),41,4,5,'gold'))
gold.start()

        #diamond

diamond = threading.Thread(target=gen, args=(randrange(-20,20),40,randrange(-20,20),57,9,5,'diamonds'))
diamond.start()