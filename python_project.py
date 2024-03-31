def display_board():
  board = ['1','2','3','4','x','6','7','8','9']
  print ("+----+----+----+")
  for i in range(0,9,3):
      print("|    |    |    |") 
      print("| {}  | {}  | {}  |".format(board[i],board[i+1],board[i+2]))
      print("|    |    |    |")
      print("+----+----+----+")  
display_board()

