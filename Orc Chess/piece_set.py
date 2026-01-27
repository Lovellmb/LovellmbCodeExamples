import os
import pygame
from Archer import Archer
from Cavalry import Cavalry
from Ninja import Ninja
from SpriteSheet import SpriteSheet
from Swordsman import Swordsman
from piece import *
from King import *
from Pawn import Pawn
from Queen import Queen

class PieceSet:


    def __init__(self, WIN, grid):
        """Initialize attributes to represent the overall set of pieces."""
        self.grid = grid
        self.WIN = WIN
        self.enemies = []
        self.allies = []
        self._load_pieces()

    def loadCavalry(self):


        p1rider1 = Cavalry(self.WIN)
              
        p1rider1.x = 0 * 80
        p1rider1.y = 0 * 80
        p1rider1.gridX = 0
        p1rider1.gridY = 0 
        p1rider1.player = 1
        p1rider1.setImages()
        self.allies.append(p1rider1)
        
        p1rider2 = Cavalry(self.WIN)
         
        p1rider2.x = 0 * 80
        p1rider2.y = 9 * 80
        p1rider2.gridX = 0
        p1rider2.gridY = 9 
        p1rider2.player = 1
        p1rider2.setImages() 
        self.allies.append(p1rider2)
        
        p2rider1 = Cavalry(self.WIN)
        
        p2rider1.x = 9 * 80
        p2rider1.y = 0 * 80
        p2rider1.gridX = 9
        p2rider1.gridY = 0 
        p2rider1.player = 2
        p2rider1.setImages()
        self.enemies.append(p2rider1)
        
        p2rider2 = Cavalry(self.WIN)
        
        p2rider2.x = 9 * 80
        p2rider2.y = 9 * 80
        p2rider2.gridX = 9
        p2rider2.gridY = 9 
        p2rider2.player = 2
        p2rider2.setImages()
        self.enemies.append(p2rider2)


    def loadArcher(self):

        p1Archer1 = Archer(self.WIN)
              
        p1Archer1.x = 0 * 80
        p1Archer1.y = 2 * 80
        p1Archer1.gridX = 0
        p1Archer1.gridY = 2 
        p1Archer1.player = 1
        p1Archer1.setImages()
        self.allies.append(p1Archer1)


        p1Archer2 = Archer(self.WIN)
         
        p1Archer2.x = 0 * 80
        p1Archer2.y = 7 * 80
        p1Archer2.gridX = 0
        p1Archer2.gridY = 7 
        p1Archer2.player = 1
        p1Archer2.setImages() 
        self.allies.append(p1Archer2)


        p2Archer1 = Archer(self.WIN)
        
        p2Archer1.x = 9 * 80
        p2Archer1.y = 2 * 80
        p2Archer1.gridX = 9
        p2Archer1.gridY = 2 
        p2Archer1.player = 2
        p2Archer1.setImages()
        self.enemies.append(p2Archer1)
 

        p2Archer2 = Archer(self.WIN)
        
        p2Archer2.x = 9 * 80
        p2Archer2.y = 7 * 80
        p2Archer2.gridX = 9
        p2Archer2.gridY = 7 
        p2Archer2.player = 2
        p2Archer2.setImages()
        self.enemies.append(p2Archer2)

    def loadSwordsman(self):

        p1sword1 = Swordsman(self.WIN)
              
        p1sword1.x = 0 * 80
        p1sword1.y = 3 * 80
        p1sword1.gridX = 0
        p1sword1.gridY = 3 
        p1sword1.player = 1
        p1sword1.setImages()
        self.allies.append(p1sword1)


        p1sword2 = Swordsman(self.WIN)
         
        p1sword2.x = 0 * 80
        p1sword2.y = 6 * 80
        p1sword2.gridX = 0
        p1sword2.gridY = 6 
        p1sword2.player = 1
        p1sword2.setImages() 
        self.allies.append(p1sword2)


        p2sword1 = Swordsman(self.WIN)
        
        p2sword1.x = 9 * 80
        p2sword1.y = 3 * 80
        p2sword1.gridX = 9
        p2sword1.gridY = 3 
        p2sword1.player = 2
        p2sword1.setImages()
        self.enemies.append(p2sword1)
 

        p2sword2 = Swordsman(self.WIN)
        
        p2sword2.x = 9 * 80
        p2sword2.y = 6 * 80
        p2sword2.gridX = 9
        p2sword2.gridY = 6 
        p2sword2.player = 2
        p2sword2.setImages()
        self.enemies.append(p2sword2)

    def loadQueens(self):
        

        p1queen = Queen(self.WIN)
              
        p1queen.x = 0 * 80
        p1queen.y = 4 * 80
        p1queen.gridX = 0
        p1queen.gridY = 4 
        p1queen.player = 1
        p1queen.setImages()
        self.allies.append(p1queen)


        p2queen = Queen(self.WIN)
        
        p2queen.x = 9 * 80
        p2queen.y = 5 * 80
        p2queen.gridX = 9
        p2queen.gridY = 5 
        p2queen.player = 2
        p2queen.setImages()
        self.enemies.append(p2queen)

    def loadNinjas(self):
        

        p1ninja1 = Ninja(self.WIN)
              
        p1ninja1.x = 0 * 80
        p1ninja1.y = 1 * 80
        p1ninja1.gridX = 0
        p1ninja1.gridY = 1 
        p1ninja1.player = 1
        p1ninja1.setImages()
        self.allies.append(p1ninja1)


        p1ninja2 = Ninja(self.WIN)
         
        p1ninja2.x = 0 * 80
        p1ninja2.y = 8 * 80
        p1ninja2.gridX = 0
        p1ninja2.gridY = 8 
        p1ninja2.player = 1
        p1ninja2.setImages() 
        self.allies.append(p1ninja2)


        p2ninja1 = Ninja(self.WIN)
        
        p2ninja1.x = 9 * 80
        p2ninja1.y = 1 * 80
        p2ninja1.gridX = 9
        p2ninja1.gridY = 1 
        p2ninja1.player = 2
        p2ninja1.setImages()
        self.enemies.append(p2ninja1)

        p2ninja2 = Ninja(self.WIN)
        
        p2ninja2.x = 9 * 80
        p2ninja2.y = 8 * 80
        p2ninja2.gridX = 9
        p2ninja2.gridY = 8 
        p2ninja2.player = 2
        p2ninja2.setImages()
        self.enemies.append(p2ninja2)

    def loadKings(self):
       

        p1king = King(self.WIN)

        p1king.x = 0 * 80
        p1king.y = 5 * 80
        p1king.gridX = 0
        p1king.gridY = 5 
        p1king.player = 1
        p1king.setImages()
        self.allies.append(p1king)

        p2king = King(self.WIN)

        p2king.x = 9 * 80
        p2king.y = 4 * 80
        p2king.gridX = 9
        p2king.gridY = 4 
        p2king.player = 2
        p2king.setImages()
        self.enemies.append(p2king)



    def _load_pieces(self):
        """Builds the overall set:
        - Loads images from the sprite sheet.
        - Creates a Piece object, and sets appropriate attributes
          for that piece.
        - Adds each piece to the list self.pieces.
        """
             
        

        for i in range(10):
            orc = Pawn(self.WIN)            
            orc.y = i * 80
            orc.gridY = i
            orc.x = 80
            orc.gridX = 1
            orc.player = 1
            orc.setImages()
            self.allies.append(orc)
            i += 1
        for i in range(10):
            orc = Pawn(self.WIN)           
            orc.x = 80 * 8
            orc.y = i * 80
            orc.gridX =  8
            orc.gridY = i 
            orc.player = 2
            orc.setImages()
            self.enemies.append(orc)
            i += 1
        self.loadCavalry()
        self.loadArcher()
        self.loadKings()
        self.loadSwordsman()
        self.loadNinjas()
        self.loadQueens()


        for enemy in self.enemies:
            self.grid[enemy.gridX][enemy.gridY] = enemy
        for ally in self.allies:
            self.grid[ally.gridX][ally.gridY] = ally

        
        
       
        for enemy in self.enemies:
            for image in enemy.images:
                image = pygame.transform.scale(image, (240, 240))
                

        for enemy in self.allies:
            for image in enemy.images:
                image = pygame.transform.scale(image, (240, 240))
        
        

