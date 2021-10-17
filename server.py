import mcpi.minecraft as minecraft
import math
import time
import asyncio
from random import randrange





mc = minecraft.Minecraft.create()
mc.setBlocks(-333, -64, -333, 333, 128, 333, 0)


select = 0
async def iron(ironx,ironz):
    ironx = randrange(-10,10)
    ironz = randrange(-10,10)

    ironcount = 0
    while True:
        time.sleep(.1)
        mc.setBlock(ironx,20,ironz,35)
        block = mc.getBlock(ironx,21,ironz)
        if block == 4:
            if ironcount == 10:
                ironcount = 0
                mc.setBlock(ironx,21,ironz,42)
            else:
                mc.setBlock(ironx,21,ironz,0)
                ironcount +=1

async def gold(goldx,goldz):
    goldx = randrange(-5,5)
    goldz = randrange(-5,5)

    goldcount = 0
    while True:
        time.sleep(.1)
        mc.setBlock(goldx,20,goldz,14)
        block = mc.getBlock(goldx,21,goldz)
        if block == 4:
            if goldcount == 10:
                goldcount = 0
                mc.setBlock(goldx,21,goldz,42,4)
            else:
                mc.setBlock(goldx,21,goldz,0)
                goldcount +=1   
    

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
                
            
    
    #print(str(x)+' '+
offset = 0
ironx = randrange(-10,10)
ironz = randrange(-10,10)
goldx = randrange(-5,5)
goldz = randrange(-5,5)
ironcount = 0
print(str(ironx) + ' '+ str(ironz))
repeat = 0
Run = True
while Run:
    island(offset)
    offset += randrange(5,30)
    time.sleep(1)
    repeat += 1
    if repeat == 10:
        repeat = 0
        Run = False
        

asyncio.run(iron()) 
asyncio.run(gold()) 
