from random import choice
from random import randint
from random import sample

cellnum = list(range(8))

cellname = ['+1','-1','+2','-2','×2','÷2','×3','÷3']

cellfunc = [lambda x: x+1,lambda x: x-1,lambda x: x+2,lambda x: x-2, \
            lambda x: x*2,lambda x: x//2,lambda x: x*3,lambda x: x//3]
            
initx = randint(0,100)
inity = randint(0,100)

t = 0

def pool_start():
	
	alivenum = sample(cellnum,4)
	alivename = list(map(lambda x: cellname[x],alivenum))
  
	print('Goal',inity)
	print('Current',initx)
	print('Time',t)
	print(alivenum)
	print(alivename)

def pool(x):
	
	global initx
	global t
	
	t = t+1
	
	func = cellfunc[x]
	initx = func(initx)
	
	alivenum = sample(cellnum,4)
	alivename = list(map(lambda x: cellname[x],alivenum))
	  
	print('Goal',inity)
	print('Current',initx)
	print('Time',t)
	print(alivenum)
	print(alivename)
  
pool_start()
