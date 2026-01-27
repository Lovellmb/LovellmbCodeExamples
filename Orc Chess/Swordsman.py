from SpriteSheet import SpriteSheet
from piece import Piece


class Swordsman(Piece):

    def setImages(self):
        if self.player == 1:
            super().setImages(SpriteSheet('Werewolf.png'))
        else:
            super().setImages(SpriteSheet('Swordsman.png')) 

    def getValidMoves(self, grid):
        movelist = []
        x = self.x // self.squareWidth
        y = self.y // self.squareHeight
        
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