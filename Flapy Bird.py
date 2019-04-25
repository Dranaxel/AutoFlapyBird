import pygame
import os, sys, random

logo = pygame.image.load("assets/sprites/yellowbird-midflap.png")
back = pygame.image.load("assets/sprites/background-day.png")
pipe = pygame.image.load("assets/sprites/pipe-green.png")


class Bird(pygame.sprite.Sprite) :
    def __init__(self, speed = -1):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        flapyBird = pygame.image.load("assets/sprites/yellowbird-midflap.png")
        self.image = flapyBird
        self.rect = (50, 256)
        self.speed = speed
        self.state = []
        screen.blit(self.image, self.rect)

    def update(self):
        X, Y = self.rect
        self.rect = (X, Y - self.speed)
        if self.state == "flying":
            self.speed = -1
            self.state = []

    def going_up(self):
        if self.state != "flying" :
            self.state = "flying"
            self.speed = 15

class Pipes(pygame.sprite.Sprite) :

    def __init__(self, x_pos=287.0, speed = 1):
        height = random.randrange(192, 400)
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.image = pipe
        self.speed = 10
        self.rect = (x_pos,height)
        screen.blit(self.image, self.rect)
        
    def update(self):
        X, Y = self.rect
        self.rect = (X-self.speed, Y)
        print(self.rect)

def main():

    #Initialize pygame
    pygame.init()
    
    #load logo and name
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Flapy Bird")

    #Define and load game screen
    screen = pygame.display.set_mode((288,512))
    screen.blit(back, (0,0))

    pipe = Pipes()
    bird = Bird()
    allsprites = pygame.sprite.Group((pipe, bird))


    #True if playing
    playing = True

    #Main loop
    while playing:
        pygame.time.Clock().tick(60)
        screen.blit(back, (0,0))
        allsprites.update()
        allsprites.draw(screen)
        pygame.display.flip()

        if pipe.rect[0] < -50 :
            pipe = Pipes()
            allsprites = pygame.sprite.Group((pipe, bird))

        #collisions = pygame.sprite.spritecollide(bird, allsprites, False)
        #print(collisions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               bird.going_up()

def gameOver():
    pass

if __name__ =="__main__":
    main()