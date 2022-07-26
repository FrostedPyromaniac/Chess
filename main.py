from processing import *

#Defining colors
RED = "#FF2200"
BLACK = "#0F0F0F" 
GOLD = "#FFCC00"
SILVER = "#CCCCCC"
GREEN = "#00CC77"
BLUE = "#0066FF"
thing = ""
first_click = (-10,-10)
check_coord_x = 0
check_coord_y = 0

def straights(x1,y1,x2,y2):
  if arr[x2][y2] != None and arr[x2][y2].getColor() == arr[x1][y1].getColor():
    return False
  if abs(x1-x2) == abs(y1-y2):
    return False
  elif x2 != x1 and y2 != y1:
    return False
  elif x2 == x1:
    for i in range(y1,y2):
      if arr[x1][i] != None and arr[x1][i].getColor() == arr[x1][y1]:
        return False
      elif i != y2 and arr[x1][i] != None and i != y1:
        return False
  elif y2 == y1:
    if x2 > x1:
      for i in range(x1,x2):
        if arr[i][y1] != None and arr[i][y1].getColor() == arr[x1][y1]:
          return False
        elif i != x2 and arr[i][y1] != None and i != x1:
          return False
    elif x2 < x1:
      for i in range(x2,x1):
        if arr[i][y1] != None and arr[i][y1].getColor() == arr[x1][y1]:
          return False
        elif i != x1 and arr[i][y1] != None and i != x2:
          return False
        
def diag_check(x1,y1,x2,y2):
  if arr[x2][y2] != None and arr[x2][y2].getColor() == arr[x1][y1].getColor():
    return False
  if abs(x2-x1) != abs(y2-y1):
    return False
  if x2-x1 == 0 or y2-y1 == 0:
    return False
      
  if x2-x1 > 0:
    if y2-y1 > 0:
      for i in range(1,x2-x1):
        if arr[x1+i][y1+i] != None and arr[x1+i][y1+i].getColor() == arr[x1][y1].getColor():
          return False
        elif i != x2-x1 and arr[x1+i][y1+i] != None and arr[x1+i][y1+i].getColor() != arr[x1][y1].getColor():
          return False
    elif y2-y1 < 0:
      for i in range(1,x2-x1):
        if arr[x1+i][y1-i] != None and arr[x1+i][y1-i].getColor() == arr[x1][y1].getColor():
          return False
        elif i != x2-x1 and arr[x1+i][y1-i] != None and arr[x1+i][y1-i].getColor() != arr[x1][y1].getColor():
          return False
    elif x2-x1 < 0:
      if y2-y1 > 0:
        for i in range(1,y2-y1):
          if arr[x1-i][y1+i] != None and arr[x1-i][y1+i].getColor() == arr[x1][y1].getColor():
            return False
          elif i != y2-y1 and arr[x1-i][y1+i] != None and arr[x1-i][y1+i].getColor() != arr[x1][y1].getColor():
            return False
      elif y2 - y1 < 0:
        for i in range(1,-1(x1-x2)):
          if arr[x1-i][y1-i] != None and arr[x1-i][y1-i].getColor() == arr[x1][y1].getColor():
            return False
          elif i != y2-y1 and arr[x1-i][y1-i] != None and arr[x1-i][y1-i].getColor() != arr[x1][y1].getColor():
            return False
#Creating board (stored in array)
arr = []
for i in range(8):
    arr.append([])
    for j in range(8):
      arr[i].append(None)
      
#Global variables called in select square method    
x_value = 0
y_value = 0
count = 0

#Kills piece when called 
def kill(xcoord,ycoord):
  arr[int(xcoord)][int(ycoord)] = None
    
#piece class
############################################Piece############################################
#Piece stores its color and whether it is a king or not
class Piece:
  def __init__(self,color):
    self.color=color
  
  #General is_check function given coords of any piece, func checks if that piece is checking the opposite color's king
  def is_check(self,x1,y1):
    x = 0
    y = 0
    if arr[x1][y1].getColor() == RED:
      for i in range(0,len(arr)):
        for j in range(0,len(arr)):
          if arr[i][j] != None and isinstance(arr[i][j],King) and arr[i][j].getColor() == BLACK:
            x = i
            y = j
            
    if arr[x1][y1].getColor() == BLACK:
      for i in range(0,len(arr)):
        for j in range(0,len(arr)):
          if arr[i][j] != None and isinstance(arr[i][j],King) and arr[i][j].getColor() == RED:
            x = i
            y = j
    
    if arr[x1][y1].valid_check(x1,y1,x,y):
      return True
    else:
      return False
  #Piece stores its own color  
  def getColor(self):
    return self.color
#Subclass for each piece type, super class is piece class
#Pawn class
class Pawn(Piece):
  def valid_check(self,x1,y1,x2,y2):
    if arr[x1][y1].getColor() == RED:
      if y1-1 >= 0 and y1-1 <= 7 and y1+1 >= 0 and y1+1 <= 7 and x1-1 >= 0 and x1-1 <= 7 and x1+1 >= 0 and x1+1 <= 7: 
        if arr[x1][y1+1] != None and isinstance(arr[x1][y1+1],Pawn) and arr[x1][y1+1].getColor() != arr[x1][y1] and y1+1==y2 and x1+1==x2:
          return True
        if arr[x1][y1-1] != None and isinstance(arr[x1][y1-1],Pawn) and arr[x1][y1-1].getColor() != arr[x1][y1] and y1-1==y2 and x1+1==x2:
          return True
    elif arr[x1][y1].getColor() == RED:
      if y1-1 >= 0 and y1-1 <= 7 and y1+1 >= 0 and y1+1 <= 7 and x1-1 >= 0 and x1-1 <= 7 and x1+1 >= 0 and x1+1 <= 7:
        if arr[x1][y1+1] != None and isinstance(arr[x1][y1+1],Pawn) and arr[x1][y1+1].getColor() != arr[x1][y1] and y1+1==y2 and x1-1==x2:
          return True
        if arr[x1][y1-1] != None and isinstance(arr[x1][y1-1],Pawn) and arr[x1][y1-1].getColor() != arr[x1][y1] and y1-1==y2 and x1-1==x2:
          return True
    
    if arr[x2][y2] != None and arr[x2][y2].getColor() == arr[x1][y1].getColor():
      return False
    if abs(x2-x1) == 0 and abs(y2-y1) == 1:
      return False
    elif arr[x1][y1].getColor() == RED and x2 < x1:
      return False
    elif arr[x1][y1].getColor() == BLACK and x2 > x1:
      return False
    if arr[x2][y2] == None:
      if abs(y2-y1) != 0:
        return False
      elif (x1 != 1 and arr[x1][y1].getColor() == RED) or (x1 != 6 and arr[x1][y1].getColor() == BLACK):
        if abs(x2-x1) != 1:
          return False
      else:
        if abs(x2-x1) > 2:
          return False
        elif abs(y2-y1) != 0:
          return False
    else:
      if abs(x2-x1) != 1:
        return False
      elif abs(y2-y1) != 1:
        return False
    return True
        
  
  
#Bishop Class
class Bishop(Piece):
  def valid_check(self,x1,y1,x2,y2):
    if diag_check(x1,y1,x2,y2) != False:
      return True
    else:
      return False
      
 
    
#Rook Class
class Rook(Piece):
  def valid_check(self,x1,y1,x2,y2):
    if straights(x1,y1,x2,y2) != False:
      return True
    else:
      return False
  
      
#Knight class
class Knight(Piece):
  def valid_check(self,x1,y1,x2,y2):
    if arr[x2][y2] != None and arr[x2][y2].getColor() == arr[x1][y1].getColor():
      return False
    if abs(x2-x1) == 1 and abs(y2-y1) == 2:
      return True
    elif abs(x2-x1) == 2 and abs(y2-y1) == 1:
      return True
    if arr[x2][y2] != None and arr[x2][y2].getColor() == arr[x1][y1].getColor():
      return False
    return False
    
  
#Queen class
class Queen(Piece):
  def valid_check(self,x1,y1,x2,y2):
    if abs(x2-x1) == abs(y2-y1):
      if diag_check(x1,y1,x2,y2) != False:
        return True
    elif x2-x1 == 0 and abs(y2-y1) > 0:
      if straights(x1,y1,x2,y2) != False:
        return True
    elif y2-y1 == 0 and abs(x2-x1) > 0:
      if straights(x1,y1,x2,y2) != False:
        return True
    return False
    
  
#King class
class King(Piece):
  def valid_check(self,x1,y1,x2,y2):
    if arr[x2][y2] != None and arr[x2][y2].getColor() == arr[x1][y1].getColor():
      return False
    if x1 == x2 and abs(y2-y1) == 1:
      return True
    elif y1 == y2 and abs(x2-x1) == 1:
      return True
    elif x2 == x1 + 1 and y2 == y1 + 1:
      return True
    elif x2 == x1-1 and y2 == y1 + 1:
      return True
    elif x2 == x1+1 and y2 == y1-1:
      return True
    elif x2 == x1-1 and y2 == y1-1:
      return True
    if arr[x2][y2] != None and arr[x2][y2].getColor() == arr[x1][y1].getColor():
      return False
    return False
    
  
#Each class has a valid move check that checks if a certain x1,y1,x2,y2 is legal for that piece.
##############################################Board############################################

class Board:
  def __init__(self):
    #Starting Positions
    red_pawns = [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
    red_knights = [[0,1],[0,6]]
    red_bish = [[0,2],[0,5]]
    red_rooks = [[0,0],[0,7]]
    red_queen = [0,5]
    red_king = [0,4]
    
    black_pawns = [[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7]]
    black_knights = [[7,1],[7,6]]
    black_bish = [[7,2],[7,5]]
    black_rooks = [[7,0],[7,7]]
    black_queen = [7,5]
    black_king = [7,4]
    
    #Adding Piece objects to array indexes they are needed. (Red)
    for i in range(len(red_pawns)):
      arr[red_pawns[i][0]][red_pawns[i][1]] = Pawn(RED)
    for i in range(len(red_knights)):
      arr[red_knights[i][0]][red_knights[i][1]] = Knight(RED)
    for i in range(len(red_bish)):
      arr[red_bish[i][0]][red_bish[i][1]] = Bishop(RED)
    for i in range(len(red_rooks)):
      arr[red_rooks[i][0]][red_rooks[i][1]] = Rook(RED)
    arr[0][4] = Queen(RED)
    arr[0][3] = King(RED)
    #Adding Piece objects to array indexes they are needed. (Black)
    for i in range(len(black_pawns)):
      arr[black_pawns[i][0]][black_pawns[i][1]] = Pawn(BLACK)
    for i in range(len(black_knights)):
      arr[black_knights[i][0]][black_knights[i][1]] = Knight(BLACK)
    for i in range(len(black_bish)):
      arr[black_bish[i][0]][black_bish[i][1]] = Bishop(BLACK)
    for i in range(len(black_rooks)):
      arr[black_rooks[i][0]][black_rooks[i][1]] = Rook(BLACK)
    arr[7][4] = Queen(BLACK)
    arr[7][3] = King(BLACK)
      
class GameEngine:
  def __init__ (self):
    self.b = Board()
    self.redTurn = True
    self.black_check = False
    self.red_check = False
    
  #Draws Board
  def display (self):
    #Deciding the fill color of the square
    for j in range(0,8):
      for i in range(0,8):
        if j%2 == 0:
          if i%2 == 0:
            fill(128,128,255)
          elif i%2 != 0:
            fill(64,192,255)
        else:
          if i%2 == 0:
            fill(64,192,255)
          elif i%2 != 0:
            fill(128,128,255)
        #Drawing the squares that compose the board
        noStroke()
        rect(i*50,j*50,50,50)
    #Drawing Pieces
    for i in range(len(arr)):
      for j in range(len(arr)):
        if arr[i][j] != None:
          if isinstance(arr[i][j] , Pawn):
            if arr[i][j].getColor() == RED:
              fill(RED)
              image(red_pawn,i*50,j*50)
            elif arr[i][j].getColor() == BLACK:
              fill(BLACK)
              image(black_pawn,i*50,j*50)
          elif isinstance(arr[i][j],Knight):
            if arr[i][j].getColor() == RED:
              fill(RED)
              image(red_knight,i*50,j*50)
            elif arr[i][j].getColor() == BLACK:
              fill(BLACK)
              image(black_knight,i*50,j*50)
          elif isinstance(arr[i][j],Bishop):
            if arr[i][j].getColor() == RED:
              image(red_bishop,i*50,j*50)
            elif arr[i][j].getColor() == BLACK:
              image(black_bishop,i*50,j*50)
          elif isinstance(arr[i][j],Rook):
            if arr[i][j].getColor() == RED:
              image(red_rook,i*50,j*50)
            else:
              image(black_rook,i*50,j*50)
          elif isinstance(arr[i][j],King):
            if arr[i][j].getColor() == RED:
              fill(RED)
              image(red_king,i*50,j*50)
            else:
              fill(BLACK)
              image(black_king,i*50,j*50)
          elif isinstance(arr[i][j],Queen):
            if arr[i][j].getColor() == RED:
              image(red_queen,i*50,j*50)
            else:
              image(black_queen,i*50,j*50)
   #Allows players to select squares and calls other functions to move pieces
  #Flips color after turn
  def flipColor(self):
    if self.redTurn:
      self.redTurn = False
    else:
      self.redTurn = True
    
  #Moves piece by copying piece to new array spot and then deleting old piece  
  def move(self,x1,y1,x2,y2):
    #Moves piece
    arr[x2][y2]=arr[x1][y1]
    kill(x1,y1)

      
      
  #Returns current color turn
  def now_color(self):
    if self.redTurn:
      return RED
    else:
      return BLACK
      
  def select_square(self):
    global count, x_value, y_value, pic1, pic2, first_click, thing
    g.display()
    x_inc = 0
    y_inc = 0
    #Count represents which click a color is on
    if count == 1:
      #If a piece on the first selected square,
      if arr[x_value][y_value] != None:
        #If the pieces color matches the current color turn and piece is not king,
        if arr[x_value][y_value].getColor() == self.now_color():
          if isinstance(arr[x_value][y_value],Pawn):
            if arr[x_value][y_value].getColor() == RED:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(red_pawn,x_value*50,y_value*50)
              first_click = (x_value,y_value)
            elif arr[x_value][y_value].getColor() == BLACK:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(black_pawn,x_value*50,y_value*50)
              first_click = (x_value,y_value)
          elif isinstance(arr[x_value][y_value],Rook):
            if arr[x_value][y_value].getColor() == RED:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(red_rook,x_value*50,y_value*50)
              first_click = (x_value,y_value)
            elif arr[x_value][y_value].getColor() == BLACK:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(black_rook,x_value*50,y_value*50)
              first_click = (x_value,y_value)
          elif isinstance(arr[x_value][y_value],Knight):
            if arr[x_value][y_value].getColor() == RED:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(red_knight,x_value*50,y_value*50)
              first_click = (x_value,y_value)
            elif arr[x_value][y_value].getColor() == BLACK:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(black_knight,x_value*50,y_value*50)
              first_click = (x_value,y_value)
          elif isinstance(arr[x_value][y_value],Bishop):
            if arr[x_value][y_value].getColor() == RED:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(red_bishop,x_value*50,y_value*50)
              first_click = (x_value,y_value)
            elif arr[x_value][y_value].getColor() == BLACK:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(black_bishop,x_value*50,y_value*50)
              first_click = (x_value,y_value)
          elif isinstance(arr[x_value][y_value],Queen):
            if arr[x_value][y_value].getColor() == RED:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(red_queen,x_value*50,y_value*50)
              first_click = (x_value,y_value)
            elif arr[x_value][y_value].getColor() == BLACK:
              fill(255)
              #Selection indicator
              rect(x_value*50,y_value*50,50,50)
              image(black_queen,x_value*50,y_value*50)
              first_click = (x_value,y_value)
          elif isinstance(arr[x_value][y_value],King):
            fill(255)
            #Selection indicator
            rect(x_value*50,y_value*50,50,50)
            if arr[x_value][y_value].getColor() == RED:
              image(red_king,x_value*50,y_value*50)
              
            elif arr[x_value][y_value].getColor() == BLACK:
              image(black_king,x_value*50,y_value*50)
            first_click = (x_value,y_value)
            
        else:
          #If certain color's turn and they are moving opposite colors piece, clicks = 0
          count = 0
      else:
        #If square is empty,
          count = 0
    elif count == 2:
      #If two clicks,
      x1, y1 = first_click
      if x1 == x_value and y1 == y_value:
        count = 0
        first_click = (0,0)
      #Check if legal move,
      
      if arr[x1][y1] != None and arr[x1][y1].getColor() == RED and arr[x1][y1].valid_check(x1,y1,x_value,y_value):
        if arr[x_value][y_value] != None:
          #If in check and other side doesnt see and tries taking a piece, then not the piece and dont let it get killed
          if isinstance(arr[x_value][y_value],Pawn):
            thing = "Pawn"
          if isinstance(arr[x_value][y_value],Knight):
            thing = "Knight"
          if isinstance(arr[x_value][y_value],Rook):
            thing = "Rook"
          if isinstance(arr[x_value][y_value],Bishop):
            thing = "Bishop"
          if isinstance(arr[x_value][y_value],Queen):
            thing = "Queen"
        #Move when valid
        self.move(x1,y1,x_value,y_value)
        in_check = False
        for i in range(0,len(arr)):
          for j in range(0,len(arr)):
            if arr[i][j] != None and arr[i][j].getColor() == BLACK and arr[i][j].is_check(i,j):
              #If in check then undo move until move is valid under check circumstances
              self.move(x_value,y_value,x1,y1)
              if thing != "": 
                if thing == "Pawn":
                  arr[x_value][y_value] = Pawn(BLACK)
                if thing == "Knight":
                  arr[x_value][y_value] = Knight(BLACK)
                if thing == "Rook":
                  arr[x_value][y_value] = Rook(BLACK)
                if thing == "Bishop":
                  arr[x_value][y_value] = Bishop(BLACK)
                if thing == "Queen":
                  arr[x_value][y_value] = Queen(BLACK)
              count = 0
              in_check = True
        if in_check == False:
          self.flipColor()
        thing = ""
      #Same thing as above except for black
      elif arr[x1][y1] != None and arr[x1][y1].getColor() == BLACK and arr[x1][y1].valid_check(x1,y1,x_value,y_value):
        if arr[x_value][y_value] != None:
          if isinstance(arr[x_value][y_value],Pawn):
            thing = "Pawn"
          if isinstance(arr[x_value][y_value],Knight):
            thing = "Knight"
          if isinstance(arr[x_value][y_value],Rook):
            thing = "Rook"
          if isinstance(arr[x_value][y_value],Bishop):
            thing = "Bishop"
          if isinstance(arr[x_value][y_value],Queen):
            thing = "Queen"
        self.move(x1,y1,x_value,y_value)
        in_check = False
        for i in range(0,len(arr)):
          for j in range(0,len(arr)):
            if arr[i][j] != None and arr[i][j].getColor() == RED and arr[i][j].is_check(i,j):
              self.move(x_value,y_value,x1,y1)
              if thing != "":
                if thing == "Pawn":
                  arr[x_value][y_value] = Pawn(RED)
                if thing == "Knight":
                  arr[x_value][y_value] = Knight(RED)
                if thing == "Rook":
                  arr[x_value][y_value] = Rook(RED)
                if thing == "Bishop":
                  arr[x_value][y_value] = Bishop(RED)
                if thing == "Queen":
                  arr[x_value][y_value] = Queen(RED)
              count = 0
              in_check = True
        if in_check == False:
          self.flipColor()
        thing = ""
      
          
          
    
     
    else:
      #if first click is not legal, make them choose again
      count = 0
    b = 0
    c = 0
    #If a color has won, makes large text saying (blank) has won
    for i in range(0,len(arr)):
      for j in range(0,len(arr)):
        if isinstance(arr[i][j],King) and arr[i][j].getColor() == RED:
          b += 1
        elif isinstance(arr[i][j],King) and arr[i][j].getColor() == BLACK:
          c += 1
    if b == 0:
      textSize(40)
      text("Black Wins!!!",75,215)
    elif c == 0:
      textSize(40)
      text("Red Wins!!!",100,215)
      
    for i in range(0,7):
      if isinstance(arr[7][i],Pawn):
        arr[7][i] = Queen(RED)
      elif isinstance(arr[0][i],Pawn):
        arr[0][i] = Queen(BLACK)

g = GameEngine()

def setup():
  size(400,400)
  global red_king,black_king,red_pawn,black_pawn,red_knight,black_knight,red_rook,black_rook,red_queen,black_queen,red_bishop,black_bishop
  red_king = loadImage("crown_red_50.png")
  black_king = loadImage("crown_black_50.png")
  red_pawn = loadImage("red_pawn.png")
  black_pawn = loadImage("black_pawn.png")
  red_knight = loadImage("red_knight.png")
  black_knight = loadImage("black_knight.png")
  red_rook = loadImage("red_rook.png")
  black_rook = loadImage("black_rook.png")
  red_queen = loadImage("red_queen.png")
  black_queen = loadImage("black_queen.png")
  red_bishop = loadImage("red_bishop.png")
  black_bishop = loadImage("black_bishop.png")
  g.display()
   
  
def mouseClicked():
  global count, x_value, y_value
  count += 1
  x_value = mouseX//50
  y_value = mouseY//50
  g.select_square()



run()



