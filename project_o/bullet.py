from mimetypes import init
import pygame

width=1300
height=750
bullet_image = pygame.transform.scale(pygame.image.load('project_o\\yellow_bullet.png'),(30,30))
#暫時用這個圖片而已，有找到適合的就換

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,rotate_or_not):
        super().__init__()
        self.image = pygame.transform.scale(bullet_image,(50,50))
        self.image_p = pygame.transform.scale(bullet_image,(50,50))
        self.rect = self.image.get_rect()
        self.d = direction
        self.move_speed = 10
        self.rotate_or_not = rotate_or_not
        if self.d==1 or self.d==3:
            self.rect.center = (x,y-15)
        else:
            self.rect.center = (x,y)

    def update(self):
        if self.rotate_or_not == 0:
            if self.d == 0:
                self.image = pygame.transform.rotate(self.image_p,0)
                self.rotate_or_not = 1
            elif self.d == 1:
                self.image = pygame.transform.rotate(self.image_p,-90)
                self.rotate_or_not = 1
            elif self.d ==2 :
                self.image = pygame.transform.rotate(self.image_p,180)
                self.rotate_or_not = 1    
            elif self.d==3:
                self.image = pygame.transform.rotate(self.image_p,90)
                self.rotate_or_not = 1

        
        
        if self.rect.centerx>width or self.rect.centerx < 0 or self.rect.centery > height or self.rect.centery < 0:
            self.kill()
        if self.d == 0:
            vx = 0
            vy = -1 * self.move_speed
        elif self.d == 1:
            vx = 1 * self.move_speed
            vy = 0
        elif self.d == 2:
            vx = 0
            vy = 1 * self.move_speed
        elif self.d == 3:
            vx = -1 * self.move_speed
            vy = 0
        self.rect.centerx += vx
        self.rect.centery += vy

        

