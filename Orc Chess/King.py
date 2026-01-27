from SpriteSheet import SpriteSheet
from piece import Piece


class King(Piece):
    
    def move(self, x, y, grid, allies, enemies):
        returnList = super().move(x, y, grid, allies, enemies)
        if self.checkPromote():
            self.promote(x, y, grid, allies, enemies)
        return returnList
    def setImages(self):
 
        if self.player == 1: 
            if isinstance(self, SuperKing):
                super().setImages(SpriteSheet('Orc King.png')) # change later
            else:
                super().setImages(SpriteSheet('Orc King.png'))
        else: 
            if isinstance(self, SuperKing):
                super().setImages(SpriteSheet('Super King.png'))
            else:
                super().setImages(SpriteSheet('King.png')) 
    def checkPromote(self):
        if self.player == 1 and self.gridX == 9:
            return True
        if self.player == 2 and self.gridX == 0:
            return True
        return False
    def promote(self, x, y, grid, allies, enemies):
        promoted = SuperKing(self.WIN)
        promoted.x = x* self.squareWidth
        promoted.y = y* self.squareHeight
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
    def getValidMoves(self, grid):
        movelist = []
        x =self.x // self.squareWidth
        y = self.y // self.squareHeight
        i=1
        stop = False
        
        while x + i < len(grid) and i <= 2 and stop == False:
            if isinstance(grid[x + i][y] , Piece):
                stop = True
                if grid[x + i][y].player != self.player:
                    movelist.append((x + i,y))
            else:
                movelist.append((x + i,y))
            i += 1
        i = 1
        stop = False
        while y + i < len(grid) and i <= 2 and stop == False:
            if isinstance(grid[x][y +i] , Piece):
                stop = True
                if grid[x][y + i].player != self.player:
                    movelist.append((x,y + i))
            else:
                movelist.append((x,y + i))
            i += 1
        i = 1
        stop = False
        while x - i >= 0 and i <= 2 and stop == False:
            if isinstance(grid[x - i][y] , Piece):
                stop = True
                if grid[x - i][y].player != self.player:
                    movelist.append((x - i,y))
            else:
                movelist.append((x - i,y))
            i += 1
        i = 1
        stop = False
        while y - i >= 0 and i <= 2 and stop == False:
            if isinstance(grid[x][y - i] , Piece):
                stop = True
                if grid[x][y - i].player != self.player:
                    movelist.append((x ,y - i))
            else:
                movelist.append((x,y - i))
            i += 1
        if (x - 1 >= 0 and y-1 >=0) and (isinstance(grid[x-1][y-1] , Piece) == False or grid[x-1][y-1].player != self.player):
                movelist.append((x-1, y-1))
        if (x - 1 >= 0 and y+1 < len(grid)) and (isinstance(grid[x-1][y+1] , Piece) == False or grid[x-1][y+1].player != self.player):
                movelist.append((x-1, y+1))
        if (x + 1 < len(grid) and y+1 < len(grid)) and (isinstance(grid[x+1][y+1] , Piece) == False or grid[x+1][y+1].player != self.player):
                movelist.append((x+1, y+1))
        if (x + 1 < len(grid) and y-1 >=0) and (isinstance(grid[x+1][y-1] , Piece) == False or grid[x+1][y-1].player != self.player):
                movelist.append((x+1, y-1))
        i
        return movelist

class SuperKing(King):
    

    def getValidMoves(self, grid):
        movelist = []
        x = self.gridX
        y = self.gridY
        i = 1
        stop = False
        while x + i < len(grid) and stop == False:
            if isinstance(grid[x + i][y] , Piece):
                stop = True
                if grid[x + i][y].player != self.player:
                    movelist.append((x + i,y))
            else:
                movelist.append((x + i,y))
            i += 1
        i = 1
        stop = False
        while y + i < len(grid) and stop == False:
            if isinstance(grid[x][y +i] , Piece):
                stop = True
                if grid[x][y + i].player != self.player:
                    movelist.append((x,y + i))
            else:
                movelist.append((x,y + i))
            i += 1
        i = 1
        stop = False
        while x - i >= 0 and stop == False:
            if isinstance(grid[x - i][y] , Piece):
                stop = True
                if grid[x - i][y].player != self.player:
                    movelist.append((x - i,y))
            else:
                movelist.append((x - i,y))
            i += 1
        i = 1
        stop = False
        while y - i >= 0 and stop == False:
            if isinstance(grid[x][y - i] , Piece):
                stop = True
                if grid[x][y - i].player != self.player:
                    movelist.append((x ,y - i))
            else:
                movelist.append((x,y - i))
            i += 1
        i = 1
        stop = False
        while x + i < len(grid) and y + i < len(grid) and stop == False:
            if isinstance(grid[x + i][y +i] , Piece):
                stop = True
                if grid[x + i][y + i].player != self.player:
                    movelist.append((x + i,y + i))
            else:
                movelist.append((x + i,y + i))
            i += 1
        i = 1
        stop = False
        while x + i < len(grid) and y - i >= 0 and stop == False:
            if isinstance(grid[x + i][y - i] , Piece):
                stop = True
                if grid[x + i][y - i].player != self.player:
                    movelist.append((x + i,y - i))
            else:
                movelist.append((x + i,y - i))
            i += 1
        i = 1
        stop = False
        while x - i >= 0 and y + i < len(grid) and stop == False:
            if isinstance(grid[x - i][y + i] , Piece):
                stop = True
                if grid[x - i][y + i].player != self.player:
                    movelist.append((x - i,y + i))
            else:
                movelist.append((x - i,y + i))
            i += 1
        i = 1
        stop = False
        while x - i >= 0 and y - i >= 0 and stop == False:
            if isinstance(grid[x - i][y - i] , Piece):
                stop = True
                if grid[x - i][y - i].player != self.player:
                    movelist.append((x - i ,y - i))
            else:
                movelist.append((x - i, y - i))
            i += 1
        return movelist