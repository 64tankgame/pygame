from setting import *
from shell import SHELL1,SHELL2
from health_bar import Health_bar

class TANK_P1_T(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = t1_t_img
        self.image_p = t1_t_img
        self.rect = self.image.get_rect()
        self.rect.center = (x+20,y)
        self.angle = 0
    def update(self,x,y,angle):
        # x +=  10*math.cos(angle)
        # y +=  10*math.sin(angle)
        self.rect.center = (x,y)
        self.image = pygame.transform.rotate(self.image_p,math.degrees(angle))
        old_center = self.rect.center   
        self.rect = self.image.get_rect()
        self.rect.center = old_center 

class TANK_P1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = t1_b_img
        self.image_p = t1_b_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.angle = 0
        self.move_speed = 2
        self.max_health = 100
        self.health = self.max_health
        self.turrent = TANK_P1_T(x,y)
        turrent_sprite.add(self.turrent)
        self.fire_cooldown = 30
        self.health_bar = Health_bar(self.max_health,40,HEIGHT-40)
        bar_sprite.add(self.health_bar)
        
    def health_check(self):
        self.health_bar.update(self.health)

    def move_front(self):
        vx = math.cos(self.angle)
        vy = math.sin(self.angle)
        self.rect.centerx += vx*self.move_speed
        self.rect.centery -= vy*self.move_speed
        
    def move_back(self):
        vx = math.cos(self.angle)
        vy = math.sin(self.angle)
        self.rect.centerx -= vx*(self.move_speed/2)
        self.rect.centery += vy*(self.move_speed/2)
    
    def rotate(self,d):
        self.angle += d * math.pi/180
        self.image = pygame.transform.rotate(self.image_p,math.degrees(self.angle))
        old_center = self.rect.center   
        self.rect = self.image.get_rect()
        self.rect.center = old_center  
    
    def shoot(self):
        shell = SHELL1(self.rect.centerx,self.rect.centery,self.angle)
        shell_sprite.add(shell)
    
    def countdown(self):
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1

    def damage(self,damage):
        self.health -= damage
        if self.health<=0:
            self.turrent.kill()
            self.kill()
    
    def shooted_check(self):
        for shell in shell_sprite:
            if self.rect.colliderect(shell.rect):
                if isinstance(shell,SHELL2):
                    self.damage(shell.get_damage())
                    shell.kill()

    def update(self):
        self.health_check()
        self.shooted_check()
        self.countdown()
        self.turrent.update(self.rect.centerx,self.rect.centery,self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_front()
        if keys[pygame.K_s]:
            self.move_back()
        if keys[pygame.K_d]:
            self.rotate(-1)
        if keys[pygame.K_a]:
            self.rotate(1)
        if keys[pygame.K_SPACE] and self.fire_cooldown == 0:
            self.fire_cooldown = 30
            self.shoot()
        
class TANK_P2_T(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = t2_t_img
        self.image_p = t2_t_img
        self.rect = self.image.get_rect()
        self.rect.center = (x+20,y)
        self.angle = math.pi
    def update(self,x,y,angle):
        # vx =  10*math.cos(angle)
        # vy =  10*math.sin(angle)
        self.rect.center = (x,y)
        self.image = pygame.transform.rotate(self.image_p,math.degrees(angle))
        old_center = self.rect.center   
        self.rect = self.image.get_rect()
        self.rect.center = old_center         

class TANK_P2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = t2_b_img
        self.image_p = t2_b_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.angle = math.pi
        self.move_speed = 2
        self.max_health = 100
        self.health = self.max_health
        self.turrent = TANK_P2_T(x,y)
        turrent_sprite.add(self.turrent)
        self.fire_cooldown = 30
        self.health_bar = Health_bar(self.max_health,WIDTH-240,HEIGHT-40)
        bar_sprite.add(self.health_bar)


    def health_check(self):
        self.health_bar.update(self.health)    
        
    # def move_front(self):
    #     if (0 < self.rect.x < WIDTH) and (0 < self.rect.y < HEIGHT):
    #         vx = math.cos(self.angle)
    #         vy = math.sin(self.angle)
    #         self.rect.centerx += vx*self.move_speed
    #         self.rect.centery -= vy*self.move_speed

    
        
    # def move_back(self):
    #     vx = math.cos(self.angle)
    #     vy = math.sin(self.angle)
    #     self.rect.centerx -= vx*(self.move_speed/2)
    #     self.rect.centery += vy*(self.move_speed/2)

    def move_front(self):
        vx = math.cos(self.angle)
        vy = math.sin(self.angle)
        new_x = self.rect.centerx + vx * self.move_speed
        new_y = self.rect.centery - vy * self.move_speed
        if self.rect.width / 2 <= new_x <= WIDTH - self.rect.width / 2 and \
                self.rect.height / 2 <= new_y <= HEIGHT - self.rect.height / 2:
            self.rect.centerx = new_x
            self.rect.centery = new_y

    def move_back(self):
        vx = math.cos(self.angle)
        vy = math.sin(self.angle)
        new_x = self.rect.centerx - vx * (self.move_speed / 2)
        new_y = self.rect.centery + vy * (self.move_speed / 2)
        if self.rect.width / 2 <= new_x <= WIDTH - self.rect.width / 2 and \
                self.rect.height / 2 <= new_y <= HEIGHT - self.rect.height / 2:
            self.rect.centerx = new_x
            self.rect.centery = new_y


    def rotate(self,d):
        self.angle += d * math.pi/180
        self.image = pygame.transform.rotate(self.image_p,math.degrees(self.angle-math.pi))
        old_center = self.rect.center   
        self.rect = self.image.get_rect()
        self.rect.center = old_center  
    
    def shoot(self):
        shell = SHELL2(self.rect.centerx,self.rect.centery,self.angle)
        shell_sprite.add(shell)
    
    def countdown(self):
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1

    def shoot(self):
        shell = SHELL2(self.rect.centerx,self.rect.centery,self.angle)
        shell_sprite.add(shell)
    
    def countdown(self):
        if self.fire_cooldown > 0:
            self.fire_cooldown -= 1

    def damage(self,damage):
        self.health -= damage
        if self.health<=0:
            self.turrent.kill()
            self.kill()
    
    def shooted_check(self):
        for shell in shell_sprite:
            if self.rect.colliderect(shell.rect):
                if isinstance(shell,SHELL1):
                    self.damage(shell.get_damage())
                    shell.kill()

    def update(self):
        self.health_check()
        self.shooted_check()
        self.countdown()
        self.turrent.update(self.rect.centerx,self.rect.centery,self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_8] or keys[pygame.K_UP]:
            self.move_front()
        if keys[pygame.K_KP_5] or keys[pygame.K_DOWN]:
            self.move_back()
        if keys[pygame.K_KP_6] or keys[pygame.K_RIGHT]:
            self.rotate(-1)
        if keys[pygame.K_KP_4] or keys[pygame.K_LEFT]:
            self.rotate(1)
        if keys[pygame.K_KP_0] or keys[pygame.K_RETURN] and self.fire_cooldown == 0:
            self.fire_cooldown = 30
            self.shoot()