from setting import *

class Health_bar(pygame.sprite.Sprite):
    def __init__(self,max_health,x,y):
        super().__init__()
        self.lentgh = 200
        self.y = 20
        self.image_o = pygame.Surface((self.lentgh,self.y))
        self.image_o.fill((255,0,0))
        self.image = self.image_o
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.max_health = max_health
    def update(self,current_health):
        self.image = pygame.Surface((self.lentgh * current_health / self.max_health,self.y))
        self.image.fill((255,0,0))
