import pygame
import os
import time

from piece_set import *
from Network import Network

class Game:
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    Black = (0,0,0)
    WIDTH, HEIGHT = 800,800

    # 2d list to track what sqaures have pieces on them. 
    grid = [
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],
        ['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty']
    ]

    gridWidth = 10
    gridHeight = 10
    FPS = 10

    squareWidth = WIDTH/gridWidth
    squareHeight = HEIGHT/gridHeight


    firstMove = True
    
    grid[4][2] = 'bomb'
    grid[5][7] = 'bomb'
    

    n = Network()
    player = int(n.getPlayer())
    print(str(player))
    playerTurn = 1


    moveList = []


    Bomb_Image = pygame.image.load(os.path.join('assets', 'bomb.png'))
    Bomb_Image = pygame.transform.scale(Bomb_Image, (squareWidth * 1.5,squareHeight * 1.5))

    Background = pygame.image.load(os.path.join('assets', 'chess board.png'))
    Background = pygame.transform.scale(Background, (WIDTH,HEIGHT))
    
    WIN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE, pygame.SRCALPHA)
    WIN.fill([173,216,230])
    orc_set = PieceSet(WIN, grid)
    enemies = orc_set.enemies
    allies = orc_set.allies
    currClicked = None

    
    
    
    def readMove(string):
        print(string)
        list = string.split(",")
        returnlist = []
        print(string)
        for s in list:
            returnlist.append(int(s))
        return returnlist

    
    def createMove(self,movedX,movedY, newX,newY, takenX,takenY):
        
        move = str(movedX) + "," + str(movedY) + "," + str(newX) + "," + str(newY) + "," + str(takenX) + "," + str(takenY)
        return move

    def move(self, input):
        list = self.readMove(input)
        
        self.grid[list[0]][list[1]].move(list[2],list[3],self.grid, self.allies, self.enemies)
        if list[4] >= 0:
            self.grid[list[2]][list[3]].move(list[4],list[5],self.grid, self.allies, self.enemies)


        
    
    def draw_game(self):
        self.WIN.blit(self.Background, (0,0))
        
        
        if (self.grid[4][2] == 'bomb'):
            self.WIN.blit(self.Bomb_Image, (3.75 * self.squareWidth , 1.75 * self.squareHeight))
        if (self.grid[5][7] == 'bomb'):
            self.WIN.blit(self.Bomb_Image, (4.75 * self.squareWidth, 6.75 * self.squareHeight))
   
        for enemy in self.enemies:
            enemy.blitme(self.squareWidth, self.squareHeight)
        for ally in self.allies:
            ally.blitme(self.squareWidth, self.squareHeight)
            
        if self.currClicked != None:
            for pair in self.currClicked.getValidMoves(self.grid):
                center = (pair[0] * self.squareWidth + self.squareWidth // 2, pair[1] * self.squareHeight + self.squareHeight // 2)
                color = (255,255,255)
                pygame.draw.circle(self.WIN, color, center, 10, 0 )
        self.drawGrid(self)
        pygame.display.update()

    def drawGrid(self):
        
        i = 0
        while i < 10:
            pygame.draw.line(self.WIN,self.Black,(i * self.WIDTH/self.gridWidth, 0), (i * self.WIDTH/self.gridWidth, self.HEIGHT) , width = self.WIDTH // 400)
            pygame.draw.line(self.WIN,self.Black,(0, i * self.HEIGHT/self.gridHeight), (self.WIDTH, i * self.HEIGHT/self.gridHeight) , width =  self.HEIGHT // 400)
            i += 1
        pygame.display.update()

    def drawWin(self):
        if self.checkWin(self) == 'ally loss':
            text = 'Player 2 wins'
        elif self.checkWin(self) == None:
            text = 'Opponent Disconnected'
        else:
            text = 'Player 1 wins'
        pygame.draw.rect(self.WIN, (0,0,0), (0, self.HEIGHT //2 - self.HEIGHT //10, self.WIDTH,100))   
        text = pygame.font.SysFont('comicsans', int(self.WIDTH / 20)).render(text,True, (255,0,0))
        self.WIN.blit(text,(self.WIDTH //3 , self.HEIGHT //2 - self.HEIGHT //10))
        pygame.display.update()


    def checkWin(self):
        allyCount = 0
        enemyCount = 0
        for ally in self.allies:
            if isinstance(ally, King):
                allyCount += 1
        for enemy in self.enemies:
            if isinstance(enemy, King):
                enemyCount += 1
        if allyCount == 0:
            return 'ally loss'
        if enemyCount == 0:
            return 'enemy loss'
        return None

    def run_game(self):
        clock = pygame.time.Clock()
        run = True
        GRID = False
        self.draw_game(self)
        gameOver = False
        
        
        while run: 
            
            clock.tick(self.FPS)

            my_events  = pygame.event.get()
            
            if self.playerTurn != self.player and (self.firstMove == False or self.player == 2):
                data = self.n.getData()

                if data == '':
                    gameOver = True
                    self.playerTurn = self.player

                elif data != None:

                    self.move(self, data)
                    if self.checkWin(self) == 'ally loss':                                   
                        gameOver = True

                    if self.checkWin(self) == 'enemy loss':                                   
                        gameOver = True
                    self.playerTurn = self.player
            

            for event in my_events:
                if event.type == pygame.WINDOWRESIZED:
                    self.draw_game(self)
                    self.WIDTH = self.WIN.get_width()
                    
                    self.HEIGHT = self.WIN.get_height()
                    self.squareWidth = self.WIDTH / 10
                    print(self.squareWidth)
                    self.squareHeight = self.HEIGHT / 10
                    self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE, pygame.SRCALPHA)
                    self.Bomb_Image = pygame.transform.scale(self.Bomb_Image, (self.squareWidth * 1.5,self.squareHeight * 1.5))
                    self.Background = pygame.transform.scale(self.Background, (self.WIDTH,self.HEIGHT))

                if event.type == pygame.QUIT:
                    run = False
                if gameOver == False:
                    if event.type == pygame.MOUSEBUTTONUP:                   
                        mousex, mousey = pygame.mouse.get_pos()
                        x = int(mousex // self.squareWidth)
                        y = int(mousey // self.squareHeight)
                        
                        
                        
                        pygame.display.update()
                        if self.playerTurn == self.player:
                            if isinstance(self.currClicked, Piece):
                        
                                clickedX = self.currClicked.gridX
                                clickedY = self.currClicked.gridY
                                check = self.currClicked.move(x, y, self.grid, self.allies, self.enemies) # check is a list TRUE/False, removed piece index]
                                if check[0]:
                                    
                                    self.firstMove = False
                                    if len(check) > 1:
                                        self.n.send(self.createMove(self, check[1],check[2],clickedX , clickedY, check[3], check[4]))
                                    else:                                        
                                        self.n.send(self.createMove(self, clickedX,clickedY, self.currClicked.gridX,self.currClicked.gridY, -1, -1))

                                    if self.player == 1:
                                        self.playerTurn = 2
                                    else:
                                        self.playerTurn = 1

                                    if self.checkWin(self) == 'ally loss':
                                    
                                        gameOver = True

                                    if self.checkWin(self) == 'enemy loss':
                                    
                                        gameOver = True

                                if self.currClicked.clicked == False:
                                    self.currClicked = None
                            elif isinstance(self.grid[x][y], Piece):
                                if self.currClicked == None and self.player == self.grid[x][y].player:
                                    self.grid[x][y].clicked = True
                                    self.currClicked = self.grid[x][y]
                        
            pygame.event.clear()
            if gameOver == False:      
                for enemy in self.enemies:
                    enemy.advance() 
                for ally in self.allies:
                    ally.advance() 
                self.draw_game(self)

            

            if gameOver == True:
                self.draw_game(self)
                self.drawWin(self)
                gameOver = 'stop'


                



        pygame.quit()

if __name__ == '__main__':
    Game.run_game(Game)


