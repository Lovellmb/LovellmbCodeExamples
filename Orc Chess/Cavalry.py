import pygame
from SpriteSheet import SpriteSheet
from piece import Piece


class Cavalry(Piece):

    def setImages(self):
        if self.player == 2:
            spriteSheet = SpriteSheet('Lancer.png')
            self.image = pygame.transform.flip(spriteSheet.image_at((30, 15, 45, 45)), True, False)
            self.images.append(self.image)
            self.images.append(pygame.transform.flip(spriteSheet.image_at((130, 15, 45, 45)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((230, 15, 45, 45)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((330, 15, 45, 45)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((430, 15, 45, 45)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((530, 15, 45, 45)), True, False))
        else:
            spriteSheet = SpriteSheet('Orc rider-Idle.png')
            self.image = spriteSheet.image_at((30, 20, 40, 40))
            self.images.append(self.image)
            self.images.append(spriteSheet.image_at((130, 20, 40, 40)))
            self.images.append(spriteSheet.image_at((230, 20, 40, 40)))
            self.images.append(spriteSheet.image_at((330, 20, 40, 40)))
            self.images.append(spriteSheet.image_at((430, 20, 40, 40)))
            self.images.append(spriteSheet.image_at((530, 20, 40, 40)))

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
        return movelist