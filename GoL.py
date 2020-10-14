#Game of Life by Jaap Saers
#The Game of Life is a popular two-dimensional Cellular Automaton which is a fancy way of saying things living on a grid obeying certain rules
#Rules for the game of life are simple. The grid is populated randomly by a number of living and dead cells
#during each generation we check two rules: 
#	1) if a living cell is surrounded by fewer than 2 other living cells, it dies of loneliness
#	2) if a living cell is surrounded my more than 3 other living cells, it dies of overcrowding
#	3) if an empty cell is surrounded by exactly 3 living cells it comes alive (presumably the three living cells like eachother alot)
#These simple rules lead to surprisingly complex and chaotic results

#This programme asks a user to define the length and width of the grid, 
#the probability of a cell being alive during the first iteration, and how many iterations the game should run
#
#Enjoy

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

####TODO: write a thing that checks if the grid is stable. while stable continue to loop, else stop loop
##########stable = no change in number of 1's over eg 30 turns
########## so while sum(pixratio[-30:length(pixratio)]/30? != 1 :  continue to loop

#prompt user for dimensions of the board and the number of ones
userwidth = int(input("How wide should the grid be?"))
userheight = int(input("How high should the grid be?"))
prob_ones = float(input("Probability of a cell being on at the start (input between 0 and 1)?"))
num_ones = int(round(userwidth*userheight*prob_ones))
iters = int(input("How many iteratrions should the game run?"))

#define a board where you can choose the numbers of ones randomly put inside
def make_board(shape, ones): #shape should be a 2d array [height,width] and ones is the number of 1's on the board
    size = np.product(shape)
    board = np.zeros(size, dtype=np.int)
    i = np.random.choice(np.arange(size), ones)
    board[i] = 1
    return board.reshape(shape)

a = make_board([userheight, userwidth], num_ones)


#function that takes in a grid of zeroes and ones like a from above as gridstate and applies game of life rules which is returned as a grid b
def GoL(gridstate):
	b = np.zeros_like(gridstate)
	rows, cols = a.shape
	for i in range(1, rows-1):
	    for j in range(1, cols-1):
	        state = a[i, j]
	        neighbors = a[i-1:i+2, j-1:j+2]
	        k = np.sum(neighbors) - state
	        if state:
	            if k==2 or k==3:
	                b[i, j] = 1
	        else:
	            if k == 3:
	                b[i, j] = 1

	return b

ims = [] #empty list to store images
fig = plt.figure(0)
pixratio = [] #empty list to store the number of 1's in each generation relative to total pixels

for x in range(iters):
	
	print("Run number " + str(x))
	fig.suptitle('Game of Life', fontsize=14, fontweight='bold')
	txt = plt.text(0,0,"Generation: " + str(x))   #add a counter for each 
	im = plt.imshow(a, cmap='Blues', interpolation='none', animated=True)
	ims.append([im, txt])

	pixsum = np.sum(a)/(userwidth*userheight)
	pixratio.append([pixsum])

	#have initial grid "a" and apply game of life rules and store in b
	b = GoL(a)
	a = b 	
	x = x + 1

#animate images from ims
ani = animation.ArtistAnimation(fig, ims, interval=50, repeat=True, repeat_delay = 1000)
#plt.show() ##turn this on to plot in console

f = r"C:\Users\JP\Documents\Programming\python\Game of Life\ " + str(userheight) + "x" + str(userheight) + " grid " + str(prob_ones) +  " prob_one " + str(iters) + " iters" +   ".gif"
writergif = animation.PillowWriter(fps=7) 
ani.save(f, writer=writergif)

f2 = r"C:\Users\JP\Documents\Programming\python\Game of Life\ " + str(userheight) + "x" + str(userheight) + " grid " + str(prob_ones) +  " prob_one " + str(iters) + " iters plot" +   ".png"

plt.figure(1)
plt.plot(pixratio)
plt.ylabel('#ones / total pixels')
plt.savefig(f2)
#plt.show()


