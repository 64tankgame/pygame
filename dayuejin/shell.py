from setting import *

class SHELL1(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__()
        self.image = shell_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.move_speed = 20
        self.damage = 10
        self.angle = angle
        self.image = pygame.transform.rotate(self.image,math.degrees(self.angle))
    
    def get_damage(self):
        return self.damage
    
    def update(self):
        if self.rect.centerx > WIDTH or self.rect.centerx < 0 or  self.rect.centery > HEIGHT or self.rect.centery < 0:
            self.kill()
        self.rect.centerx += math.cos(self.angle) * self.move_speed
        self.rect.centery -= math.sin(self.angle) * self.move_speed


class SHELL2(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__()
        self.image = shell_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.move_speed = 20
        self.angle = angle
        self.damage = 10
        self.image = pygame.transform.rotate(self.image,math.degrees(self.angle))
    def get_damage(self):
        return self.damage
    def update(self):
        if self.rect.centerx > WIDTH or self.rect.centerx < 0 or  self.rect.centery > HEIGHT or self.rect.centery < 0:
            self.kill()
        self.rect.centerx += math.cos(self.angle) * self.move_speed
        self.rect.centery -= math.sin(self.angle) * self.move_speed
        