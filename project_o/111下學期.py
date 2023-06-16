import pygame
import random

# 初始化pygame
pygame.init()

# 設置視窗大小和標題
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("爆爆王")

# 載入圖像
background_image = pygame.image.load("background.png")
player_image = pygame.image.load("player.png")
bomb_image = pygame.image.load("bomb.png")
explosion_image = pygame.image.load("explosion.png")

# 設定玩家初始位置
player_x = 400
player_y = 500

# 設定炸彈初始位置和速度
bomb_x = random.randint(0, 800)
bomb_y = 0
bomb_speed = 5

# 設定爆炸動畫的計數器
explosion_counter = 0

# 遊戲主循環
running = True
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移動玩家
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < 800:
        player_x += 5

    # 移動炸彈
    bomb_y += bomb_speed
    if bomb_y > 600:
        bomb_x = random.randint(0, 800)
        bomb_y = 0

    # 檢查是否撞上炸彈
    if abs(bomb_x - player_x) < 50 and abs(bomb_y - player_y) < 50:
        explosion_counter = 10
        bomb_x = random.randint(0, 800)
        bomb_y = 0

    # 渲染畫面
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(bomb_image, (bomb_x, bomb_y))
    if explosion_counter > 0:
        screen.blit(explosion_image, (player_x - 50, player_y - 50))
        explosion_counter -= 1
    pygame.display.update()

 # 在這裡更新遊戲畫面和處理遊戲邏輯

    # 在這裡顯示遊戲畫面
    pygame.display.flip()
# 關閉pygame
pygame.quit()