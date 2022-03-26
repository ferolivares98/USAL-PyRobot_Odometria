# -*- coding: utf-8 -*-

import pygame

from constants import *
from robot import *


# https://gm0.org/en/latest/docs/software/odometry.html


def main():
    pygame.init()
    screen = pygame.display.set_mode((FULL_MAP_WIDTH + CON_WIDTH,
                                      FULL_MAP_HEIGHT))
    pygame.display.set_caption(' Robot  |  Odometría ')
    font = pygame.font.SysFont("Ubuntu", 18, False, False)

    robot = Robot()
    robot.dibujar_robot(screen)

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                # Movimiento continuo hacia delante. Tecla W.
                if event.key == pygame.K_w:
                    robot.movimiento_W()
                # Movimiento continuo hacia atrás. Tecla S.
                if event.key == pygame.K_s:
                    robot.movimiento_S()
                # Movimiento de giro sobre si mismo a la izquierda. Tecla A.
                if event.key == pygame.K_a:
                    robot.movimiento_A()
                # Movimiento de giro sobre si mismo a la derecha. Tecla D.
                if event.key == pygame.K_d:
                    robot.movimiento_D()
                # Movimiento continuo con desviación izquierda. Tecla Q.
                if event.key == pygame.K_q:
                    robot.movimiento_Q()
                # Movimiento continuo con desviación derecha. Tecla E.
                if event.key == pygame.K_e:
                    robot.movimiento_E()

        robot.dibujar_robot(screen)
        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
