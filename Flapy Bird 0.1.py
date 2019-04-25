import pygame
import os, sys, random

logo = pygame.image.load("assets/sprites/yellowbird-midflap.png")
back = pygame.image.load("assets/sprites/background-day.png")
pipe = pygame.image.load("assets/sprites/pipe-green.png")
game_over = pygame.image.load("assets/sprites/gameover.png")

score = 0


class Bird(pygame.sprite.Sprite) :
    def __init__(self, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        flapyBird = pygame.image.load("assets/sprites/yellowbird-midflap.png")
        self.image = flapyBird
        self.rect = flapyBird.get_rect()
        self.rect.center = 50,256
        self.speed = speed
        self.state = []

    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.state == "flying":
            self.speed = 1
            self.state = []

    def going_up(self):
        if self.state != "flying" :
            self.state = "flying"
            self.speed = -25

class Pipes(pygame.sprite.Sprite) :

    def __init__(self, x_pos=250, speed = 4):
        self.speed = speed
        height = random.randrange(192, 400)
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.image = pipe
        self.rect = pipe.get_rect()
        self.rect.midtop = x_pos, height
        self.passed = False
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)

def main():

    #Initialize pygame
    pygame.init()
    font = pygame.font.Font(None, 36)
    global score
    
    #load logo and name
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Flapy Bird")

    #Define and load game screen
    screen = pygame.display.set_mode((288,512))
    screen.blit(back, (0,0))

    pipe = Pipes()
    bird = Bird()
    pipes = pygame.sprite.Group((pipe))
    bird_group = pygame.sprite.Group((bird))
    text_score = font.render(str(score), 1 ,(255,255,255))


    #True if playing
    playing = True

    #Main loop
    while playing:
        pygame.time.Clock().tick(60)
        screen.blit(back, (0,0))
        screen.blit(text_score, (0,0))
        pipes.update()
        bird_group.update()
        pipes.draw(screen)
        bird_group.draw(screen)
        pygame.display.flip()

        #Creation of new pipes
        if pipe.rect.topright[0] < -50 :
            pipe = Pipes()
            pipes = pygame.sprite.Group((pipe))

        if (pipe.passed == False and bird.rect.centerx > pipe.rect.centerx):
            pipe.passed = True
            score +=1
            text_score = font.render(str(score), 1 ,(255,255,255))


        #Check collisions
        if pygame.sprite.spritecollide(bird, pipes, False):
            playing = False
            print(score)
            gameOver()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               bird.going_up()

def gameOver():
    global score
    score = 0
    font = pygame.font.Font(None, 36)

    screen = pygame.display.set_mode((288,512))
    background_black = pygame.Surface(screen.get_size())
    background = background_black.convert()
    background_black.fill((0,0,0))

    text = font.render("Game Over", 1 ,(255,255,255))

    screen.blit(background_black, (0,0))
    screen.blit(text, (144,256))
    
    
    pygame.display.flip()

    g_over = True

    while g_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                g_over = False
                main()

if __name__ =="__main__":
    main()