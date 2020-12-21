
grid=["_","_","_",
     "_","_","_",
     "_","_","_"]
game=True
winner=None
p="X"
def suzi():
  for i in range(0,9,3):
    print(grid[i]+" "+grid[i+1]+" "+grid[i+2])
  while game :
    
    game_changer(p)
    
    checking_of_winner()
    check_tie()
  
  
    changing_of_player(p)


def game_changer(current_player):
  ind=int(input("number between 1 to 9: " ))
  ind=ind-1
  grid[ind]=p
  show_grid(grid)

    
   
def show_grid(grid):
    for i in range(0,9,3):
      for j in range(i,i+3):
        print(grid[j],end=" ")
      print()
def check(row):
  global game 
  first_row =[]
  for i in range(3):
    first_row.append(grid[i])
  if first_row[0]==first_row[1]==first_row[2] and first_row[0]!="_":
    s=0
    
  else:
     s=1
  second_row =[]
  for i in range(3,6):
    second_row.append(grid[i])
  if second_row[0]==second_row[1]==second_row[2] and second_row[0]!="_":
     c=0
  else:
     c=1
  third_row =[]
  for i in range(6,9):
    third_row.append(grid[i])
  if third_row[0]==third_row[1]==third_row[2] and third_row[0]!="_":
     m=0
  else:
     m=1
  if s==0 or c==0 or m==0:
    game=False
  if s==0:
    return grid[2]
  elif c==0:
    return grid[5]
  elif m==0:
    return grid[8]
  return


def check1(column):
  global game 
  first_column =[]
  for i in range(0,9,3):
    first_column.append(grid[i])
  if first_column[0]==first_column[1]==first_column[2] and first_column[0]!="_":
     f=0
  else:
     f=1
  second_column =[]
  for i in range(1,9,3):
    second_column.append(grid[i])
  if second_column[0]==second_column[1]==second_column[2] and second_column[0]!="_":
     z=0
  else:
     z=1
  third_column=[]
  for i in range(2,9,3):
    third_column.append(grid[i])
  if third_column[0]==third_column[1]==third_column[2] and third_column[0]!="_":
     q=0
  else:
     q=1
  if f==0 or z==0 or q==0:
    game=False
  if f==0:
    return grid[0]
  elif z==0:
    return grid[1]
  elif q==0:
    return grid[2]
  return
def check2(diagonal):
  global game 
  first_diagonal =[]
  for i in range(0,9,4):
    first_diagonal.append(grid[i])
  if first_diagonal[0]==first_diagonal[1]==first_diagonal[2] and first_diagonal[0]!="_":
     b=0
  else:
     b=1
  second_diagonal =[]
  for i in range(2,7,2):
    second_diagonal.append(grid[i])
  if second_diagonal[0]==second_diagonal[1]==second_diagonal[2] and second_diagonal[0]!="_":
     w=0
  else:
     w=1
  
  if b==0 or w==0:
    game=False
  if b==0:
    return grid[0]
  elif w==0:
    return grid[2]
  
  return
    
def checking_of_winner():
  global winner
  row_win=check(grid)
  column_win=check1(grid)
  diagonal_win=check2(grid)
  if row_win:
    winner=row_win
  elif column_win:
    winner=column_win
  elif diagonal_win:
    winner=diagonal_win
    
  else:
    winner=None


def check_tie():
  global game 
  if "_" not in grid:
    game=False
  return
    
  
    
def changing_of_player(current_player):
  global p
  if p=="X":
    p="O"
  elif p=="O":
     p="X"

    
       
      
    


suzi()
if winner=="X" or winner=="O":
  print(winner+" is winner")
elif winner==None:
  print("tie")














    