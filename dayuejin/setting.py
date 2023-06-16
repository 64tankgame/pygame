import pygame
import math


pygame.init()

WIDTH,HEIGHT = 1000,500
FPS = 60

game_screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TANKP2")
player_sprite = pygame.sprite.Group()
turrent_sprite = pygame.sprite.Group()
shell_sprite = pygame.sprite.Group()
bar_sprite = pygame.sprite.Group()


t1_b_img_path = 'dayuejin\\assets\\tankp1\\body.png'
t1_t_img_path = 'dayuejin\\assets\\tankp1\\turrent.png'

t1_b_img = pygame.transform.scale(pygame.image.load(t1_b_img_path),(50,149/2))
t1_b_img = pygame.transform.rotate(t1_b_img,-90)
t1_t_img = pygame.transform.scale(pygame.image.load(t1_t_img_path),(30,50))
t1_t_img = pygame.transform.rotate(t1_t_img,-90)

t2_b_img = pygame.transform.scale(pygame.image.load(t1_b_img_path),(50,149/2))
# 50 74.5
t2_b_img = pygame.transform.rotate(t2_b_img,90)
t2_t_img = pygame.transform.scale(pygame.image.load(t1_t_img_path),(30,50))
t2_t_img = pygame.transform.rotate(t2_t_img,-90)






shell_img_path = 'dayuejin\\assets\\shell\\Light_Shell.png'
shell_img = pygame.transform.scale(pygame.image.load(shell_img_path),(10,24))
shell_img = pygame.transform.rotate(shell_img,-90)



game_font = pygame.font.Font('dayuejin\\assets\\font\\Cubic_11_1.013_R.ttf',20)