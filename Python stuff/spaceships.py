import pygame
import os
import random



pygame.font.init()
pygame.mixer.init()

bullet_sound = pygame.mixer.Sound(os.path.join('Assets','gun.mp3'))
hit_sound = pygame.mixer.Sound(os.path.join('Assets','explode.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 100)



WIDTH, HEIGHT = 800,600
GAME_TITLE = "Space Battle"
SHIP_WIDTH, SHIP_HEIGHT = 40,55


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(GAME_TITLE)

FPS = 60


ship_vel = 5
bullet_vel = 8

max_health = 5


yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2



SPLASH = 1
PLAYING = 2
OVER = 3





YELLOW = (255,255,0)
RED = (255,0,0)
SPACE_IMAGE = pygame.image.load(os.path.join('assets', 'space.jpg'))
SPACE_IMAGE = pygame.transform.scale(SPACE_IMAGE, (WIDTH,HEIGHT))

YELLOW_SHIP = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
YELLOW_SHIP = pygame.transform.rotate(YELLOW_SHIP, 90)
YELLOW_SHIP = pygame.transform.scale(YELLOW_SHIP, (SHIP_WIDTH, SHIP_HEIGHT))

RED_SHIP = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))
RED_SHIP = pygame.transform.rotate(RED_SHIP, -90)
RED_SHIP = pygame.transform.scale(RED_SHIP, (SHIP_WIDTH, SHIP_HEIGHT))





def move_yellow_ship(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= ship_vel
        if yellow.x < 0:
            yellow.x = 0
    if keys_pressed[pygame.K_d]:
        yellow.x += ship_vel
        if yellow.x + SHIP_WIDTH> WIDTH // 2:
            yellow.x = 10
            yellow.y = random.randrange(0,HEIGHT-SHIP_HEIGHT//2)
    if keys_pressed[pygame.K_w]:
        yellow.y -= ship_vel
        if yellow.y < 0:
            yellow.y = 0
    if keys_pressed[pygame.K_s]:
        yellow.y += ship_vel
        if yellow.y > HEIGHT-SHIP_HEIGHT:
            yellow.y = HEIGHT-SHIP_HEIGHT

def move_red_ship(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= ship_vel
        if red.x < WIDTH // 2:
            red.x = WIDTH - SHIP_WIDTH
            red.y = random.randrange(0,HEIGHT-SHIP_HEIGHT//2)
    if keys_pressed[pygame.K_RIGHT]:
        red.x += ship_vel
        if red.x > WIDTH-SHIP_WIDTH:
            red.x = WIDTH-SHIP_WIDTH
    if keys_pressed[pygame.K_UP]:
        red.y -= ship_vel
        if red.y < 0:
            red.y = 0
    if keys_pressed[pygame.K_DOWN]:
        red.y += ship_vel
        if red.y > HEIGHT-SHIP_HEIGHT:
            red.y = HEIGHT-SHIP_HEIGHT



def move_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        elif red.colliderect(bullet):
            yellow_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(red_hit))
            hit_sound.play()
    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if bullet.x < -5:
            red_bullets.remove(bullet)
        elif yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(yellow_hit))
            hit_sound.play()
            

def draw_splash():
    WIN.blit(SPACE_IMAGE, (0,0))
    splash_text = TITLE_FONT.render("SPACE BATTLE",True, RED)
    WIN.blit(splash_text,(WIDTH //2 - splash_text.get_width()//2,HEIGHT //2 - splash_text.get_height()//2))

    pygame.display.update()




def draw_over(message):
    WIN.blit(SPACE_IMAGE, (0,0))
    game_over_text = TITLE_FONT.render(message,True, RED)
    WIN.blit(game_over_text,(WIDTH //2 - game_over_text.get_width()//2,HEIGHT //2 - game_over_text.get_height()//2))

    pygame.display.update()

def draw_game(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health):



    WIN.blit(SPACE_IMAGE, (0,0))

    red_health_text = HEALTH_FONT.render("Health: "+str(red_health),True,RED)
    WIN.blit(red_health_text,(WIDTH * 3 // 4 - red_health_text.get_width()//2,10))

    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health),True,YELLOW)
    WIN.blit(yellow_health_text,(WIDTH // 4 - yellow_health_text.get_width()//2,10))

    WIN.blit(YELLOW_SHIP, (yellow.x,yellow.y))

    WIN.blit(RED_SHIP, (red.x,red.y))

    



    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    yellow = pygame.Rect(10, HEIGHT//2 -SHIP_HEIGHT//2, SHIP_WIDTH, SHIP_HEIGHT)
    red = pygame.Rect(WIDTH-10-SHIP_WIDTH, HEIGHT//2 -SHIP_HEIGHT//2, SHIP_WIDTH, SHIP_HEIGHT)
    run = True

    yellow_bullets = []
    red_bullets = []

    yellow_health = max_health
    red_health = max_health

    stage = SPLASH

    while run: 
        clock.tick(FPS)
        
        my_events  = pygame.event.get()
        

        for event in my_events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == red_hit:
                red_health -=1
                if red_health == 0:
                    stage = OVER
            if event.type == yellow_hit:
                yellow_health -=1
                if yellow_health == 0:
                    stage = OVER
            if event.type == pygame.KEYDOWN:
                if stage == SPLASH:
                    stage = PLAYING
                elif stage == OVER:
                    yellow_bullets = []
                    red_bullets = []
                    yellow_health = max_health
                    red_health = max_health
                    yellow = pygame.Rect(10, HEIGHT//2 -SHIP_HEIGHT//2, SHIP_WIDTH, SHIP_HEIGHT)
                    red = pygame.Rect(WIDTH-10-SHIP_WIDTH, HEIGHT//2 -SHIP_HEIGHT//2, SHIP_WIDTH, SHIP_HEIGHT)
                    stage = PLAYING


                elif event.key == pygame.K_LCTRL and len(yellow_bullets) < 3:
                    bullet = pygame.Rect(yellow.x + SHIP_WIDTH, yellow.y + SHIP_HEIGHT/2, 10, 5)
                    yellow_bullets.append(bullet)
                    bullet_sound.play()
                    
                elif event.key == pygame.K_RCTRL and len(red_bullets) < 3:
                    bullet = pygame.Rect(red.x,red.y + SHIP_HEIGHT/2, 10, 5)
                    red_bullets.append(bullet)
                    bullet_sound.play()

        if stage == SPLASH:
            draw_splash()

        elif stage == PLAYING:
            keys_pressed = pygame.key.get_pressed()
            move_yellow_ship(keys_pressed,yellow)
            move_red_ship(keys_pressed,red)
            draw_game(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health)
            move_bullets(yellow_bullets,red_bullets,yellow,red)
        elif stage == OVER:
            if red_health == 0:
                draw_over("YELLOW WINS!")
            else: 
                draw_over("RED WINS!")


    pygame.quit()

if __name__ == "__main__":
    main()
    
