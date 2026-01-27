from SpriteSheet import SpriteSheet
from piece import Piece



class Ninja(Piece):
    def setImages(self):
        if self.player == 1:
            super().setImages(SpriteSheet('purple orc.png'))
        else: 
            super().setImages(SpriteSheet('Ninja.png'))


    def getValidMoves(self, grid):
        movelist = []
        x = self.gridX
        y = self.gridY
        i = 1
        while x + i < len(grid) and i <= 3 :
            if isinstance(grid[x + i][y] , Piece):              
                if grid[x + i][y].player != self.player:
                    movelist.append((x + i,y))
            else:
                movelist.append((x + i,y))
            i += 1
        i = 1
        while y + i < len(grid) and i <= 3 :
            if isinstance(grid[x][y +i] , Piece):

                if grid[x][y + i].player != self.player:
                    movelist.append((x,y + i))
            else:
                movelist.append((x,y + i))
            i += 1
        i = 1

        while x - i >= 0 and i <= 3 :
            if isinstance(grid[x - i][y] , Piece):
                if grid[x - i][y].player != self.player:
                    movelist.append((x - i,y))
            else:
                movelist.append((x - i,y))
            i += 1
        i = 1

        while y - i >= 0  and i <= 3 :
            if isinstance(grid[x][y - i] , Piece):
                if grid[x][y - i].player != self.player:
                    movelist.append((x ,y - i))
            else:
                movelist.append((x,y - i))
            i += 1
        i = 1

        while x + i < len(grid) and y + i < len(grid) and i <= 3 :
            if isinstance(grid[x + i][y +i] , Piece):
                if grid[x + i][y + i].player != self.player:
                    movelist.append((x + i,y + i))
            else:
                movelist.append((x + i,y + i))
            i += 1
        i = 1

        while x + i < len(grid) and y - i >= 0 and i <= 3 :
            if isinstance(grid[x + i][y - i] , Piece):
                stop = True
                if grid[x + i][y - i].player != self.player:
                    movelist.append((x + i,y - i))
            else:
                movelist.append((x + i,y - i))
            i += 1
        i = 1

        while x - i >= 0 and y + i < len(grid) and i <= 3 :
            if isinstance(grid[x - i][y + i] , Piece):
                if grid[x - i][y + i].player != self.player:
                    movelist.append((x - i,y + i))
            else:
                movelist.append((x - i,y + i))
            i += 1
        i = 1

        while x - i >= 0 and y - i >= 0 and i <= 3 :
            if isinstance(grid[x - i][y - i] , Piece):
                if grid[x - i][y - i].player != self.player:
                    movelist.append((x - i ,y - i))
            else:
                movelist.append((x - i, y - i))
            i += 1
        return movelist