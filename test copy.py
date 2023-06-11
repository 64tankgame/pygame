import pygame

# 初始化 Pygame
pygame.init()

# 設定視窗大小和標題
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("爆爆王")

# 設定遊戲循環的變數
running = True

# 遊戲循環
while running:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 如果收到退出事件，則停止遊戲循環
            running = False

    # 在這裡更新遊戲畫面和處理遊戲邏輯

    # 在這裡顯示遊戲畫面
    pygame.display.flip()

# 退出 Pygame
pygame.quit()