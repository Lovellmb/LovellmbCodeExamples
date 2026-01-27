from SpriteSheet import SpriteSheet
from piece import Piece


class Bomber(Piece):
    def __init__(self, WIN):
        super().__init__(WIN)
        self.name = 'bomber'    
    def setImages(self):
        if self.player == 1:
            super().setImages(SpriteSheet('bomb orc.png'))
        else:
            super().setImages(SpriteSheet('bomb orc.png')) # change this later


    def getValidMoves(self, grid):
        movelist = []
        x = self.gridX
        y = self.gridY
        movex = -1
        
        while movex < 2:
            movey = -1
            while movey < 2:
                if x +movex < len(grid) and  x +movex > 0 and y +movey < len(grid) and  y +movey > 0:
                    if (isinstance(grid[x + movex][y + movey], Piece)) == False or grid[x + movex][y + movey].player != self.player:
                        movelist.append((x + movex, y + movey))
                movey += 1
            movex += 1
        
        

        return movelist
