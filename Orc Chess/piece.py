import os
import pygame





class Piece:

    """Represents a chess piece."""

    def __init__(self, WIN):
        """Initialize attributes to represent a chess piece."""
        self.name = 'pointless'
        self.images = []
        self.image = None
        self.WIN = WIN
        self.frame = 0
        self.clicked = False
        self.rect = None
        self.gridX = 0
        self.gridY = 0
        self.player = 1
        self.squareHeight = 80
        self.squareHeight = 80
        self.validMoves = []
        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

        
    def blitme(self, Width, Height):
        """Draw the piece at its current location."""
        self.x = self.gridX * Width
        self.y = self.gridY * Height
        self.squareHeight = Height
        self.squareWidth = Width
        
        self.rect = pygame.Rect(self.x, self.y, Width, Height, fill = (176,224,230))
        
        self.image = pygame.transform.scale(self.image, (Width, Height))
        if self.clicked == False:
            self.image.set_colorkey((0, 0, 0))
        self.WIN.blit(self.image, self.rect)
        
    def advance(self):
        self.frame += 1
        if (self.frame == len(self.images)):
            self.frame = 0
        self.image = self.images[self.frame]

    def setImages(self, spriteSheet):
        if self.player == 2:
            self.image = pygame.transform.flip(spriteSheet.image_at((30, 30, 40, 40)), True, False)
            self.images.append(self.image)
            self.images.append(pygame.transform.flip(spriteSheet.image_at((130, 30, 40, 40)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((230, 30, 40, 40)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((330, 30, 40, 40)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((430, 30, 40, 40)), True, False))
            self.images.append(pygame.transform.flip(spriteSheet.image_at((530, 30, 40, 40)), True, False))
        else:
            self.image = spriteSheet.image_at((30, 30, 40, 40))
            self.images.append(self.image)
            self.images.append(spriteSheet.image_at((130, 30, 40, 40)))
            self.images.append(spriteSheet.image_at((230, 30, 40, 40)))
            self.images.append(spriteSheet.image_at((330, 30, 40, 40)))
            self.images.append(spriteSheet.image_at((430, 30, 40, 40)))
            self.images.append(spriteSheet.image_at((530, 30, 40, 40)))

    def move(self, x, y, grid, allies, enemies):
        returnList = []
        bomberCheck = False
        if (x,y) in self.getValidMoves(grid):
            returnList.append(True)
            if isinstance(grid[x][y], Piece):
                if grid[x][y].name == 'bomber': # need name to avoid circular imports
                    bomberCheck = True
                    if self.player == 1:
                        allies.remove(self)
                    else: 
                        enemies.remove(self)
                if grid[x][y] in allies:
                    allies.remove(grid[x][y])
                else:                   
                    enemies.remove(grid[x][y])
            grid[self.gridX][self.gridY] = 'empty'
            self.gridX = x
            self.gridY = y
            self.x = x * self.squareWidth
            self.y = y * self.squareHeight
            grid[self.gridX][self.gridY] = self
            if bomberCheck:
                grid[self.gridX][self.gridY] = 'empty'
            self.clicked = False
            return returnList
            
            
        self.clicked = False
        returnList.append(False)
        return returnList




    def getValidMoves(self):
        pass






    




