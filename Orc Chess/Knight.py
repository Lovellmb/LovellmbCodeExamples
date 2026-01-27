from Cavalry import Cavalry
from King import King, SuperKing
from SpriteSheet import SpriteSheet
from piece import Piece


class Knight(Piece):
    def __init__(self,WIN):
        super().__init__(WIN)
        self.killCount = 0

    def setImages(self):
        if self.player == 1:
            super().setImages(SpriteSheet('Armored Orc.png'))
        else: 
            super().setImages(SpriteSheet('Knight.png'))


    def move(self, x, y, grid, allies, enemies):
        horseCheck = False
        if isinstance(grid[x][y], Piece) and grid[x][y].player != self.player and (x,y) in self.getValidMoves(grid):
            self.killCount += 1
            if isinstance(grid[x][y], Cavalry):
                self.killCount += 1


        returnList = super().move(x, y, grid, allies, enemies)
        if returnList[0]:           
            if horseCheck:
                grid[x][y] = 'Cavalry'
            if self.killCount >= 2 and (self in allies or self in enemies):
                self.promote(x, y, grid, allies, enemies)
        return returnList
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
        if grid[x][y] == 'Cavalry':
            promoted = Cavalry(self.WIN)
        else:
            promoted = King(self.WIN)

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

    def getValidMoves(self, grid):
        movelist = []
        x = self.gridX
        y = self.gridY
        movex = -1
        
        while movex < 2:
            movey = -1
            while movey < 2:
                if x + movex < len(grid) and  x + movex >= 0 and y +movey < len(grid) and  y + movey >= 0:
                    if (isinstance(grid[x + movex][y + movey], Piece)) == False or grid[x + movex][y + movey].player != self.player:
                        movelist.append((x + movex, y + movey))
                movey += 1
            movex += 1

        return movelist
