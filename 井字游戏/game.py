import pygame
from pygame.locals import *
import logic
RED = (255, 0, 0)
WHITE = (255, 255, 255)
def draw_text(text, pos):
    background = pygame.Surface(screen.get_size())
    font=pygame.font.Font('/usr/share/fonts/truetype/arphic/ukai.ttc',16)
    font_text=font.render(text, True, WHITE)
    rect=font_text.get_rect()
    rect.center=pos
    print(rect)
    screen.blit(font_text, rect)
    pygame.display.update()
    

def draw_circle(position):
    pygame.draw.circle(screen, RED, position, 50, 5)
    pygame.display.update()

def draw_falk(position):
    pygame.draw.line(screen, RED, (position[0]-50, position[1]-50), (position[0]+50, position[1]+50), 5)
    pygame.draw.line(screen, RED, (position[0]-50, position[1]+50), (position[0]+50, position[1]-50), 5)
    pygame.display.update()

def init_screen():
    screen.fill((0,80,0))
    color = 100,255,200
    width = 2
    pygame.draw.line(screen, color, (100, 100), (460, 100), width)
    pygame.draw.line(screen, color, (100, 100), (100, 460), width)
    pygame.draw.line(screen, color, (220, 100), (220, 460), width)
    pygame.draw.line(screen, color, (340, 100), (340, 460), width)
    pygame.draw.line(screen, color, (460, 100), (460, 460), width)
    pygame.draw.line(screen, color, (100, 460), (460, 460), width)
    pygame.draw.line(screen, color, (100, 220), (460, 220), width)
    pygame.draw.line(screen, color, (100, 340), (460, 340), width)

    pygame.display.update()

pygame.init() # 初始化
screen = pygame.display.set_mode((600,600)) # Window size
pygame.display.set_caption("Drawing Line 文件格式") # windows caption

who = "O"
init_screen()

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = 0, 0
            mouse_down = event.button
            mouse_down_x,mouse_down_y = event.pos
            print(mouse_down_x,mouse_down_y)
            if 100 <= mouse_down_x < 220:
                x = 0
            elif 220 <= mouse_down_x < 340:
                x = 1
            elif 340 <= mouse_down_x < 460:
                x = 2
            else:
                x = -1
            if 100 <= mouse_down_y < 220:
                y = 0
            elif 220 <= mouse_down_y < 340:
                y = 1
            elif 340 <= mouse_down_y < 460:
                y = 2
            else:
                y = -1
            print(x,y)
            if x == -1 or y == -1:
                print("ERROR")
            elif logic.square[y][x] != 0:
                print("该位置已被占,请重新输入：")
                draw_text("该位置已被占,请重新输入：", (100,16))
            else:
                logic.set_XY(who, x, y)
                if who == "O":
                    draw_circle((x*120+160,y*120+160))
                    who = "X"
                else:
                    draw_falk((x*120+160,y*120+160))
                    who = "O"
            logic.print_square()
            if logic.judge_win(1)==1:
                print("Player O, 你赢了！")
                draw_text("Player O, 你赢了！", (100, 480))
                pygame.quit()
            if logic.judge_win(2)==1:
                print("Player X, 你赢了！")
                draw_text("Player X, 你赢了！", (100, 480))
                pygame.quit()
            elif logic.judge_win(1) ==2:
                print("[平局]！")
                draw_text("平局", (100, 480))
                pygame.quit()
            # draw_text()
                        
    # pygame.font.get_fonts()
