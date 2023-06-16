from setting import *
from bullet2 import *

class player2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.image.load('tank/tank_u.png')
        self.image_p= pygame.image.load('tank/tank_u.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rotate_direction = 0
    

    def update(self):
        global time_tank_2_attack

        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= speed
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rotate_direction != 3:
                self.rotate_direction = 3
                self.image = pygame.transform.rotate(self.image_p, 90)

        if keys[pygame.K_d]:
            self.rect.x += speed
            if self.rect.right>=width:
                self.rect.right=width
            if self.rotate_direction != 1:
                self.rotate_direction = 1
                self.image = pygame.transform.rotate(self.image_p, -90)

        if keys[pygame.K_w]:
            self.rect.y -= speed
            if self.rect.top<=0:
                self.rect.top=0
            if self.rotate_direction != 0:
                self.rotate_direction = 0
                self.image = pygame.transform.rotate(self.image_p, 0)
        
        if keys[pygame.K_s]:
            self.rect.y += speed
            if self.rect.bottom>=height:
                self.rect.bottom=height
            if self.rotate_direction != 2:
                self.rotate_direction = 2
                self.image = pygame.transform.rotate(self.image_p, 180)
        
        if keys[pygame.K_RETURN]:
            if time_tank_2_attack <= 0: 
                bullet = Bullet2(self.rect.centerx,self.rect.centery,self.rotate_direction,0)
                all_bullet_sprite.add(bullet)
                time_tank_2_attack = 160

        if time_tank_2_attack >= 0 :
            time_tank_2_attack -= 1        