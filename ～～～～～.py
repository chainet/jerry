import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
plot_poins = []
for x in range(0, 640):
    y = int(math.sin(x / 640.0 * 4 * math.pi) * 200 + 240)
    plot_poins.append([x, y])
pygame.draw.lines(screen, [0, 0, 0], False, plot_poins, 2)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()