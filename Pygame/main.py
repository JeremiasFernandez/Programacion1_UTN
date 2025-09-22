import pygame
import const
import character

player = character.Character(250, 115)

pygame.init()

ventana = pygame.display.set_mode((const.anchoVentana,
                                   const.altoVentana))

pygame.display.set_caption("The ultimate experiment")

run = True
while run:

    player.draw(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Izquierda")
            elif event.key == pygame.K_d:
                print("Derecha")
            elif event.key == pygame.K_s:
                print("Abajo")
            elif event.key == pygame.K_w:
                print("Arriba")
        pygame.display.update()








