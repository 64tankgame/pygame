from mimetypes import init
import pygame

width=1100
height=650
path = 'tank/magicball1.png'

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.d = direction
        if self.d==1 or self.d==3:
            self.rect.center = (x,y-15)
        else:
            self.rect.center = (x,y)

    def update(self):
        if self.rect.centerx>width or self.rect.centerx < 0 or self.rect.centery > height or self.rect.centery < 0:
            self.kill()
        if self.d == 0:
            vx = 0
            vy = -1
        elif self.d == 1:
            vx = 1
            vy = 0
        elif self.d == 2:
            vx = 0
            vy = 1
        elif self.d == 3:
            vx = -1
            vy = 0
        self.rect.centerx += vx
        self.rect.centery += vy

        

