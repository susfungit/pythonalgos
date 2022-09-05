"""
In the below solution sudoku is implemented as list 
Each list element is a list that represents values in row
empty space is represented by 0

Assumption that the problem supplied is valid and has one solution
Implementation uses recursive calls
First find the empty cell (cell with 0 value)
Place a value in the cell if it is not already present in row, col, square
repeat. If value cannot be placed means we have to go to prior step 
and replace the value 
"""

def find_empty_cell(sudoku):
# return row and column of the cell that is empty
# if no empty cell is found, return None

	for row in range(9):
		for col in range(9):
			if sudoku[row][col]==0:
				return row, col

	return None,None


def is_valid_value(sudoku, row, col, value):
# check if the value can be applied to the cell[row,col]
	
	#check if the value is already in the given row
	if value in  sudoku[row]:
		return False

	#check if the value is already in the given column
	#first get all the values in the given column

	col_values=[sudoku[i][col] for i in range(0,9)]
	if value in col_values:
		return False

	#now check if value exists in a given square. 
	#first we have to determine the square for which given row, col belongs
	#we determine this by checking starting row and column of the square
	#and check if value exists in the given range

	square_row=(row)//3 * 3
	square_col=(col)//3 * 3

	square_vals=[sudoku[i][j] for i in range(square_row, square_row+3)
					for j in range(square_col,square_col+3)]

	if value in square_vals:
		return False

	#if we have reached here means that value can be applied to the position
	return True



def solve_sudoku(sudoku):
	row,col=find_empty_cell(sudoku)
	if row is None:
		return True
	for i in range(1,10):
		if is_valid_value(sudoku,row, col, i):
			sudoku[row][col]=i
			if solve_sudoku(sudoku):
				return True
		#back track
		sudoku[row][col]=0

	#we have reached here means prior loop did not return during recursion which means we have to back track 
	return False


def print_sudoku(sudoku):
	
	for i in range(9):
		print('-|'*9)
		print('|'.join(str(i) for i in sudoku[i]))

sudoku=[[0,0,0,0,0,0,6,8,0],
	[0,0,0,0,7,3,0,0,9],
	[3,0,9,0,0,0,0,4,5],
	[4,9,0,0,0,0,0,0,0],
	[8,0,3,0,5,0,9,0,2],
	[0,0,0,0,0,0,0,3,6],
	[9,6,0,0,0,0,3,0,8],
	[7,0,0,6,8,0,0,0,0],
	[0,2,8,0,0,0,0,0,0]]


solve_sudoku(sudoku)
print_sudoku(sudoku)
