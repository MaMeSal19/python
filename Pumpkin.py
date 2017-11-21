from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
#from random import randint
mc = Minecraft.create()

def init(): 
	# change 192.168.1.13 to 127.0.0.1 or your ip
	mc = Minecraft.create("127.0.0.1", 4711)
	x, y, z = mc.player.getPos()  
	return mc
	
def pumpkin(mc,x,y,z):
	mc.setBlocks(x-2, y, z+2, x+2, y+5, z+8, 35, 1)
	mc.setBlocks(x,y,z+5,x,y+7,z+5,35,5) 

def clear(mc,x,y,z):
	h,k,l = 20,20,20
	mc.setBlocks(x-h,y-k,z-l,x+h,y+k,z+l, 0)

def righteye(mc,x,y,z):
	wool = 35,15
	mc.setBlocks(x,y,z,x,y,z, wool)
	
def lefteye(mc,x,y,z):
	wool = 35,15
	mc.setBlocks(x,y,z,x,y,z, wool)
	
def nose(mc,x,y,z):
	wool = 35,15
	mc.setBlocks(x,y,z,x,y,z, wool)
	
def mouth(mc,x,y,z):
	wool = 35,15
	mc.setBlocks(x,y,z,x,y,z+4, wool)
	
def main():
	mc = init()
	x1,y1,z1 = 0,5,0
	mc.player.setPos(x1,y1,z1)
	#mc.player.getPos()
	x,y,z = mc.player.getPos()
	clear(mc,x1,y1,z1)
	pumpkin(mc,x,y,z)
	nose(mc,x1+2,y1+3,z1+5)
	lefteye(mc,x1+2,y1+4,z1+7)
	righteye(mc,x1+2,y1+4,z1+3)
	mouth(mc,x1+2,y1+1,z1+3)
	
def flakes(mc,x,z,k):
	m = 41
    for n in range(0,k):
		if (n > (k -2 )
			m = 30
			mc.setBlock(x,y+k,z,m)
                     
def main():
count = 0
while count < 1000:
	x1 = randint(-100,100)
	z1 = randint(-100,100)
	k = randint(3,15)
	flakes(mc,x,y,z,k)
	count = count + 1
	
main()
