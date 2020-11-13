import random

winning_lines = [
	[
		[0,0],[0,1],[0,2]
	],
	[
		[1,0],[1,1],[1,2]
	],
	[
		[2,0],[2,1],[2,2]
	],
	[
		[0,0],[1,0],[2,0]
	],
	[
		[0,1],[1,1],[2,1]
	],
	[
		[0,2],[1,2],[2,2]
	],
	[
		[0,0],[1,1],[2,2]
	],
	[
		[0,2],[1,1],[2,0]
	]		
]

#print winning_lines

# Complete the function below to print 2 integers separated by a single space which will be your next move 
def nextMove(player,board):
	the_move = ['X' if player is 'X' else 'O']
	
	#	1. Read / Analyze the board
	#	2. Check for possible winning lines remaining
	#	3. First Priority - 
	#		Fill the winning line of the opponent
	#	   Second Priority - 
	#		Fill the winning line for yourself
	#


	count = 0
	empty_spaces = []
	for i in range(3):
		for j in range(3):
			if (board[i][j] == chr(95)): # If empty spaces are encountered
				count += 1
				empty_spaces.append([i,j])
	rand_coord = random.randrange(0,count)
	#print "Random number:",rand_coord
	#print "My move:",empty_spaces[rand_coord]
	print empty_spaces[rand_coord][0],empty_spaces[rand_coord][1]

#If player is X, I'm the first player.
#If player is O, I'm the second player.
player = raw_input()

#Read the board now. The board is a 3x3 array filled with X, O or _.
board = []
for i in xrange(0, 3):
    board.append(raw_input())

nextMove(player,board); 
