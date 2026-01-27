from SpriteSheet import SpriteSheet
from piece import Piece


class Queen(Piece):
    def setImages(self):
        if self.player == 1:
            super().setImages(SpriteSheet('Wizard.png'))
        else: 
            super().setImages(SpriteSheet('Queen.png'))
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