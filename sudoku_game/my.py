# # def read():
# #     grid=[]
# #     file=open('out.txt', 'r')
# #     for line in file:
# #         if '-' in line:break
# #     lst=[-1]*9
# #     for l in file: 
# #         line=l.replace('||','|').replace(' ','').strip()[1:-1].split('|')
    
# #         if '-' in line[0]:
# #             if -1 in lst:
# #                 return "unfound value "
# #             grid.append(lst);lst=[-1]*9
# #             if len(grid)%3==0:file.readline()
# #             continue
        
# #         for idx, unti in enumerate(line):
# #             u=unti.strip()
# #             if  u=='' :    continue
# #             if not u.isdigit():
# #                 return "value not a number"
# #             lst[idx]=int(u)
# #     return grid 


# # Python program for Sudoku Generator



# # **********************************************************
# import random

# # function to print grid
# def print_grid(grid):
#     for i in range(9):
#         for j in range(9):
#             print(grid[i][j], end=" ")
#         print()

# # A utility function to check whether num is already
# # present in current row or current column or current 3x3 box
# def is_safe(grid, row, col, num):

#     # Check if num is already present in current row
#     for x in range(9):
#         if grid[row][x] == num:
#             return False

#     # Check if num is already present in current column
#     for x in range(9):
#         if grid[x][col] == num:
#             return False

#     # Check if num is already present in current 3x3 box
#     start_row = row - row % 3
#     start_col = col - col % 3
#     for i in range(3):
#         for j in range(3):
#             if grid[i + start_row][j + start_col] == num:
#                 return False

#     return True


# # A recursive function to fill remaining grid
# def fill_grid(grid):

#     # Find an unassigned cell
#     l = [0, 0]
#     if not find_empty_location(grid, l):
#         return True

#     # Assigning list values to row and col that we got from above Function
#     row = l[0]
#     col = l[1]

#     # Consider digits 1 to 9
#     nums = list(range(1, 10))
    
#      # Shuffle them randomly so that we get different boards every time 
#     random.shuffle(nums)

#      # Try every possible number 
#     for num in nums: 

#          # If it looks promising 
#          if (is_safe(grid,row,col,num)): 

#              # Make tentative assignment 
#              grid[row][col]=num 

#              # Return true ,if success , ya ! 
#              if(fill_grid(grid)): 
#                  return True 

#              # Failure , unmake & try again 
#              grid[row][col] = 0

#     return False


# # Function to find an entry in grid that is still unassigned  
# def find_empty_location(arr,l): 

#      for row in range(9): 
#          for col in range(9): 
#              if(arr[row][col]==0): 
#                  l[0]=row 
#                  l[1]=col 
#                  return True
#      return False


# # Function to remove K digits from sudoku board  
# def remove_k_digits(grid,k): 

#       count=k 
    
#       while (count!=0): 
        
#            i=random.randint(0,8) 
            
#            j=random.randint(0,8) 
            
#            while (grid[i][j]==0):  
                
#                i=random.randint(0,8)  
                
#                j=random.randint(0,8)  
            
#            grid[i][j]=0
            
#            count-=1


# # Driver Code
  
# grid=[[0 for x in range(9)]for y in range(9)] 
  
# fill_grid(grid)

# print("Full Sudoku Board")
# print_grid(grid)

# difficulty=input("Enter difficulty level (easy/medium/hard): ")

# if difficulty=="easy":
#    k=20
   
# elif difficulty=="medium":
#    k=40
   
# else:
#    k=60
   
# remove_k_digits(grid,k)

# print("Sudoku Board with",difficulty,"level")
# print_grid(grid)









# # def check_solution(grid):
# #     rang=list(range(1,10))
# #     for lst in grid:
# #         if sorted(lst)!=rang:return "wrong solution" 
# #     for lst in zip(grid):
# #         if sorted(lst)!=rang:return "wrong solution"
           
# # def solve(grid):
# #     pass
    
# # print(read())
# # def generate_solution(self, grid):
# #     """generates a full solution with backtracking"""
# #     number_list = [1,2,3,4,5,6,7,8,9]
# #     for i in range(0,81):
# #         row=i//9
# #         col=i%9
# #         #find next empty cell
# #         if grid[row][col]==0:
# #             shuffle(number_list)      
# #             for number in number_list:
# #                 if self.valid_location(grid,row,col,number):
# #                     self.path.append((number,row,col))
# #                     grid[row][col]=number
# #                     if not self.find_empty_square(grid):
# #                         return True
# #                     else:
# #                         if self.generate_solution(grid):
# #                             #if the grid is full
# #                             return True
# #             break
# #     grid[row][col]=0  
# #     return False









# # N=9
# # def isvaild(grid, row, col, num):

# #     for row in grid:
# #         if num in  row: return False
# #     for col in zip(grid):
# #         if num in  col: return False

# #     st = row - row % 3
# #     end = col - col % 3
# #     for i in range(3):
# #         for j in range(3):
# #             if grid[i + st][j + end] == num:
# #                 return False
# #     return True


# # def solveSudoku(grid, row, col):

# #     if (row == N - 1 and col == N):
# #         return True

# #     if col == N:
# #         row += 1
# #         col = 0
 

# #     if grid[row][col] > 0:
# #         return solveSudoku(grid, row, col + 1)
# #     for num in range(1, N + 1, 1):
       
  
# #         if isvaild(grid, row, col, num):
           

# #             grid[row][col] = num

# #             if solveSudoku(grid, row, col + 1):
# #                 return True

# #         grid[row][col] = 0
# #     return False



# # def read():
# #     grid=[]
# #     file=open('out.txt', 'r')
# #     for line in file:
# #         if '-' in line:break
# #     lst=[-1]*9
# #     for l in file: 
# #         line=l.replace('||','|').replace(' ','').strip()[1:-1].split('|')
    
# #         if '-' in line[0]:
# #             if -1 in lst:
# #                 return "unfound value "
# #             grid.append(lst);lst=[-1]*9
# #             if len(grid)%3==0:file.readline()
# #             continue
        
# #         for idx, unti in enumerate(line):
# #             u=unti.strip()
# #             if  u=='' :    continue
# #             if not u.isdigit():
# #                 return "value not a number"
# #             lst[idx]=int(u)
# #     return grid 





# # def check_solution(grid):
# #     rang=list(range(1,10))
# #     for lst in grid:
# #         if sorted(lst)!=rang:return "wrong solution" 
# #     for lst in zip(grid):
# #         if sorted(lst)!=rang:return "wrong solution"
           
# # def solve(grid):
# #     pass
    
# # print(read())
# # def generate_solution(self, grid):
# #     """generates a full solution with backtracking"""
# #     number_list = [1,2,3,4,5,6,7,8,9]
# #     for i in range(0,81):
# #         row=i//9
# #         col=i%9
# #         #find next empty cell
# #         if grid[row][col]==0:
# #             shuffle(number_list)      
# #             for number in number_list:
# #                 if self.valid_location(grid,row,col,number):
# #                     self.path.append((number,row,col))
# #                     grid[row][col]=number
# #                     if not self.find_empty_square(grid):
# #                         return True
# #                     else:
# #                         if self.generate_solution(grid):
# #                             #if the grid is full
# #                             return True
# #             break
# #     grid[row][col]=0  
# #     return False









# # N=9
# # def isvaild(grid, row, col, num):

# #     for row in grid:
# #         if num in  row: return False
# #     for col in zip(grid):
# #         if num in  col: return False

# #     st = row - row % 3
# #     end = col - col % 3
# #     for i in range(3):
# #         for j in range(3):
# #             if grid[i + st][j + end] == num:
# #                 return False
# #     return True


# # def solveSudoku(grid, row, col):

# #     if (row == N - 1 and col == N):
# #         return True

# #     if col == N:
# #         row += 1
# #         col = 0
 

# #     if grid[row][col] > 0:
# #         return solveSudoku(grid, row, col + 1)
# #     for num in range(1, N + 1, 1):
       
  
# #         if isvaild(grid, row, col, num):
           

# #             grid[row][col] = num

# #             if solveSudoku(grid, row, col + 1):
# #                 return True

# #         grid[row][col] = 0
# #     return False
# Define the size of the board and the square
# N = 9
# SQ = 3

# # Initialize an empty board
# board = [[0 for i in range(N)] for j in range(N)]

# # Check if a number is valid in a given row
# def valid_row(board, row, num):
#     for i in range(N):
#         if board[row][i] == num:
#             return False
#     return True

# # Check if a number is valid in a given column
# def valid_col(board, col, num):
#     for i in range(N):
#         if board[i][col] == num:
#             return False
#     return True

# # Check if a number is valid in a given square
# def valid_sq(board, row, col, num):
#     sr = (row // SQ) * SQ # starting row of the square
#     sc = (col // SQ) * SQ # starting column of the square
#     for i in range(sr, sr + SQ):
#         for j in range(sc, sc + SQ):
#             if board[i][j] == num:
#                 return False
#     return True

# # Check if a number is valid in a given position
# def valid_pos(board, row, col, num):
#     return valid_row(board, row, num) and valid_col(board, col,num) and valid_sq(board,row,col,num)

# # Find an empty position on the board (-1,-1) if none
# def find_empty(board):
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == 0:
#                 return (i,j)
#     return (-1,-1)

# # Solve the board using backtracking algorithm 
# def solve(board):

#     # Find an empty position on the board 
#     row,col = find_empty(board)

#     # If no empty position found then we are done 
#     if row == -1 and col == -1:
#         return True
    
#     # Try numbers from 1 to N 
#     for num in range(1,N+1):

#         # Check if the number is valid at that position 
#         if valid_pos(board,row,col,num):

#             # Place the number on the board 
#             board[row][col] = num

#             # Recursively try to solve the rest of the board 
#             if solve(board):
#                 return True
            
#             # If not solvable then backtrack and remove the number 
#             board[row][col] = 0
    
#     # If no number works then it is unsolvable 
#     return False

# # Generate a full solved sudoku using backtracking algorithm 
# solve(board)

# # Print out the solved sudoku 
# for i in range(N):
#    print(*board[i])

# import numpy as np
# import math

# N = 3

# rewrite of https://www.tutorialspoint.com/valid-sudoku-in-python
# def isValidSudoku(M): 
#     '''
#     Check a sudoku matrix:
#         A 9x9 sudoku matrix is valid iff every:
#           row contains 1 - 9 and
#           col contains 1 - 9 and
#           3x3 contains 1 - 9
#         0 is used for blank entry
#     '''
#     for i in range(9):
#         row = {}
#         col = {}
#         block = {}
#         row_cube = N * (i//N)
#         col_cube = N * (i%N)
#         for j in range(N*N):
#             if M[i][j] != 0 and M[i][j] in row:
#                 return False
#             row[M[i][j]] = 1
#             if M[j][i] != 0 and M[j][i] in col:
#                 return False
#             col[M[j][i]] = 1
#             rc = row_cube + j//N
#             cc = col_cube + j%N
#             if M[rc][cc] in block and M[rc][cc] != 0:
#                 return False
#             block[M[rc][cc]]=1
#     return True
    
# def generate_sudoku_puzzles(run_size, seed):  
    
#     order = int(math.sqrt(run_size))
#     count = 0
#     valid = 0
#     empty = []
#     np.random.seed(seed) # for reproducible results
    
#     for k in range(order):
#         for l in range(order):

#             A = np.fromfunction(lambda i, j: ((k*i + l+j) % (N*N)) + 1, (N*N, N*N), dtype=int)
#             B = np.random.randint(2, size=(N*N, N*N))
#             empty.append(np.count_nonzero(B))
#             C = A*B
#             count += 1

#             if isValidSudoku(C):
#                 valid += 1
#                 last = C
# #               print('C(',k,l,') is valid sudoku:')
# #               print(C) # Uncomment for puzzle

#     print('Tried', count, 'valid', valid, 'yield', round(valid/count, 3)*100, '%', 'Average Clues', round(sum(empty)/len(empty)))
#     return(last)

# posTest = np.array([(0, 7, 0, 0, 4, 0, 0, 6, 0), \
#                     (3, 0, 0, 5, 0, 7, 0, 0, 2), \
#                     (0, 0, 5, 0, 0, 0, 3, 0, 0), \
#                     (0, 4, 0, 3, 0, 6, 0, 5, 0), \
#                     (6, 0, 0, 0, 0, 0, 0, 0, 8), \
#                     (0, 1, 0, 2, 0, 8, 0, 3, 0), \
#                     (0, 0, 7, 0, 0, 0, 4, 0, 0), \
#                     (1, 0, 0, 8, 0, 2, 0, 0, 9), \
#                     (0, 6, 0, 0, 9, 0, 0, 1, 0), \
#                     ])

# negTest = np.array([(0, 7, 0, 0, 4, 0, 0, 6, 2), \
#                     (3, 0, 0, 5, 0, 7, 0, 0, 2), \
#                     (0, 0, 5, 0, 0, 0, 3, 0, 0), \
#                     (0, 4, 0, 3, 0, 6, 0, 5, 0), \
#                     (6, 0, 0, 0, 0, 0, 0, 0, 8), \
#                     (0, 1, 0, 2, 0, 8, 0, 3, 0), \
#                     (0, 0, 7, 0, 0, 0, 4, 0, 0), \
#                     (1, 0, 0, 8, 0, 2, 0, 0, 9), \
#                     (0, 6, 0, 0, 9, 0, 0, 1, 0), \
#                     ])

# print('Positive Quality Control Test:', isValidSudoku(posTest))
# print('Negative Quality Control Test:', isValidSudoku(negTest))

# print(generate_sudoku_puzzles(10000, 0))