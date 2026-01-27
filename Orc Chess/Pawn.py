from Bomber import Bomber
from Cavalry import Cavalry
from King import SuperKing
from Knight import Knight
from SpriteSheet import SpriteSheet
from piece import Piece


class Pawn(Piece):
    def __init__(self,WIN):
        super().__init__(WIN)
        self.firstMove = True
        self.killCount = 0

    def setImages(self):
        if self.player == 1:
            super().setImages(SpriteSheet('Orc.png'))
        else: 
            super().setImages(SpriteSheet('Armored Axeman.png'))
    
    def checkPromote(self):
        if self.player == 1 and self.gridX == 9:
            return True
        if self.player == 2 and self.gridX == 0:
            return True
        return False
    def ascend(self, x, y, grid, allies, enemies):
        promoted = SuperKing(self.WIN)
        promoted.x = x * self.squareWidth
        promoted.y = y * self.squareHeight
        promoted.gridX = x
        promoted.gridY = y
        promoted.player = self.player
        promoted.setImages()
        grid[x][y] = promoted
        if self.player == 1:
            allies.remove(self)
            allies.append(promoted)
        else: 
            enemies.remove(self)
            enemies.append(promoted) 
    def promote(self, x, y, grid, allies, enemies):
        if grid[x][y] == 'bomb':
                
            promoted = Bomber(self.WIN)
        elif grid[x][y] == 'Cavalry':
            promoted = Cavalry(self.WIN)
        

        else: promoted = Knight(self.WIN)


        promoted.x = x*80
        promoted.y = y*80
        promoted.gridX = x
        promoted.gridY = y
        promoted.player = self.player
        promoted.setImages()
        grid[x][y] = promoted
        if self.player == 1:
            allies.remove(self)
            allies.append(promoted)
        else: 
            enemies.remove(self)
            enemies.append(promoted) 

        


    def move(self, x, y, grid, allies, enemies):
        bombCheck = False
        horseCheck = False
        if isinstance(grid[x][y], Piece) and grid[x][y].player != self.player and (x,y) in self.getValidMoves(grid) and isinstance(grid[x][y], Bomber) == False:
            self.killCount += 1
            if isinstance(grid[x][y], Cavalry):
                self.killCount += 1
                horseCheck = True

        if grid[x][y] == 'bomb':
            bombCheck = True

        returnList = super().move(x, y, grid, allies, enemies)
        if returnList[0]:
            self.firstMove = False
            if self.checkPromote():
                self.ascend(x, y, grid, allies, enemies)
            if bombCheck:
                grid[x][y] = 'bomb'
            if horseCheck:
                grid[x][y] = 'Cavalry'
            if (self.killCount >= 2 or bombCheck):
                self.promote(x, y, grid, allies, enemies)
        
        return returnList   
        
    
    def getValidMoves(self, grid):
        movelist = []
        x = self.gridX
        y = self.gridY
        if self.player == 1:
            
            if (x + 1 < len(grid) and y - 1 >= 0) and (isinstance(grid[x + 1][y - 1 ] , Piece) and grid[x+1][y-1].player != self.player) or self.firstMove:
                movelist.append((x + 1, y - 1))
            if (x + 1 < len(grid) and y + 1 < len(grid)) and (isinstance(grid[x + 1][y +1] , Piece) and grid[x +1 ][y + 1].player != self.player) or self.firstMove:
                movelist.append((x + 1, y +1))   
            if x + 1 < len(grid) and (isinstance(grid[x + 1][y] , Piece) == False):
                movelist.append((x + 1, y))
                if  self.firstMove == True:
                    if isinstance(grid[x + 2][y] , Piece) == False :
                        movelist.append((x + 2,y))
        if self.player == 2:
            
            if (x - 1 >= 0 and y-1 >=0) and (isinstance(grid[x-1][y-1] , Piece) and grid[x-1][y-1].player != self.player) or self.firstMove:
                movelist.append((x-1, y-1))
            if (x - 1 >= 0 and y + 1 < len(grid)) and (isinstance(grid[x-1][y+1] , Piece) and grid[x-1][y+1].player != self.player) or self.firstMove:
                movelist.append((x-1, y+1))  
            if x - 1 >= 0 and (isinstance(grid[x - 1][y] , Piece) == False):
                movelist.append((x - 1, y))  
                if  self.firstMove == True:
                    if isinstance(grid[x-2][y ] , Piece) == False:
                        movelist.append((x-2, y))              
        return movelist