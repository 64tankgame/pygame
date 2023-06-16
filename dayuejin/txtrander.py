from setting import *
import pygame.freetype


txt = game_font.render("測試字體",True,(0,0,0))
txtrext = txt.get_rect()
txtrext.center = (WIDTH/2,HEIGHT/2)