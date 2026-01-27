from SpriteSheet import SpriteSheet
from piece import Piece


class Archer(Piece):
    def __init__(self,WIN):
        super().__init__(WIN)
        self.attacking = False
        self.prevX = self.gridX
        self.prevY = self.gridY

    def setImages(self):
        if self.player == 1:
            super().setImages(SpriteSheet('Skeleton Archer.png'))
        else: 
            super().setImages(SpriteSheet('Archer.png'))

    def move(self, x, y, grid, allies, enemies):
        returnList = []
        validMoves = self.getValidMoves(grid)
        if len(validMoves) > 0 and (x,y) in validMoves:
            if self.attacking == False:
                grid[self.gridX][self.gridY] = 'empty'
                self.prevX = self.gridX
                self.prevY = self.gridY
                self.gridX = x
                self.gridY = y
                self.rect.x = x * self.squareWidth
                self.rect.y = y * self.squareHeight
                self.x = x * self.squareWidth
                self.y = y * self.squareHeight
                grid[self.gridX][self.gridY] = self

                self.attacking = True

                if len(self.getValidMoves(grid)) == 0:
                    self.attacking = False
                    self.clicked = False
                    returnList.append(True)
                else:
                    returnList.append(False)
                return returnList


            else:
                self.clicked = False
                self.attacking = False
                returnList.append(True)
                if grid[x][y] in allies:
                    allies.remove(grid[x][y])
                else:
                    enemies.remove(grid[x][y])
                grid[x][y] = 'empty'
                returnList.append(self.prevX)
                returnList.append(self.prevY)
                returnList.append(x)
                returnList.append(y)
        elif self.attacking:
            self.clicked = False
            self.attacking = False
            returnList.append(True)
            returnList.append(self.prevX)
            returnList.append(self.prevY)
            returnList.append(x)
            returnList.append(y)
            return returnList

        self.clicked = False
        returnList.append(False)
        return returnList
    
    def getValidMoves(self, grid):
        movelist = []
        x = self.gridX
        y = self.gridY
        if self.attacking == False:
            if x + 1 < len(grid) and (isinstance(grid[x + 1][y] , Piece) == False):
                movelist.append((x + 1, y))
            if x - 1 < len(grid) and (isinstance(grid[x - 1][y] , Piece) == False):
                movelist.append((x - 1, y))
            if y + 1 < len(grid) and (isinstance(grid[x][y + 1] , Piece) == False):
                movelist.append((x, y +1))
            if y - 1 < len(grid) and (isinstance(grid[x][y - 1] , Piece) == False):
                movelist.append((x, y -1))


        else:
            if x + 2 < len(grid) and ((isinstance(grid[x + 2][y] , Piece) and grid[x+2][y].player != self.player)):
                movelist.append((x + 2, y))
            if x - 2 > 0 and ((isinstance(grid[x - 2][y] , Piece) and grid[x-2][y].player != self.player)):
                movelist.append((x - 2, y))
            if y + 2 < len(grid) and ((isinstance(grid[x][y + 2] , Piece) and grid[x][y+2].player != self.player)):
                movelist.append((x, y +2))
            if y - 2 > 0 and ((isinstance(grid[x][y - 2] , Piece) and grid[x][y-2].player != self.player)):
                movelist.append((x, y -2))

        return movelist