# -*- coding: utf-8 -*-

import pygame
import math
from constants import *


class Robot:
    def __init__(self):
        self.pos_x = 400
        self.pos_y = 400
        self.theta_giro = 0
        self.rotada = None
        self.rect_rotada = None
        self.font = pygame.font.SysFont("Arial", 24, False, False)
        self.textRect = self.font.get_rect()
        self.textRect.center = (FULL_MAP_WIDTH / 10, FULL_MAP_HEIGHT / 10)

    @staticmethod
    def movimiento_W():
        encoder_der = 10
        encoder_izq = 10
        return encoder_der, encoder_izq

    @staticmethod
    def movimiento_S():
        encoder_der = -10
        encoder_izq = -10
        return encoder_der, encoder_izq

    @staticmethod
    def movimiento_A():
        encoder_der = 10
        encoder_izq = -10
        return encoder_der, encoder_izq

    @staticmethod
    def movimiento_D():
        encoder_der = -10
        encoder_izq = 10
        return encoder_der, encoder_izq

    @staticmethod
    def movimiento_Q():
        encoder_der = 10
        encoder_izq = 3
        return encoder_der, encoder_izq

    @staticmethod
    def movimiento_E():
        encoder_der = 3
        encoder_izq = 10
        return encoder_der, encoder_izq

    def dibujar_robot(self, screen, imagen_robot):
        """ screen.blit(imagen_robot, pygame.Rect(FULL_MAP_WIDTH, FULL_MAP_HEIGHT,
                                              FULL_MAP_WIDTH / 10,
                                              FULL_MAP_HEIGHT / 10)) """
        self.rotada = pygame.transform.rotozoom(imagen_robot, math.degrees(self.theta_giro), 1)
        self.rect_rotada = self.rotada.get_rect(center=(self.pos_x, self.pos_y))
        screen.blit(self.rotada, self.rect_rotada)
        # screen.blit(imagen_robot, (self.pos_x, self.pos_y))
        pygame.display.flip()

    def dibujar_fondo(self, screen):
        screen.fill(COLOR_BLANCO)
        pygame.display.flip()


    def dibujar_pos_info(self, screen):
        texto = f"PosX = {self.pos_x}\nPosY = {self.pos_y}\nTheta = {int(math.degrees(self.theta_giro))}"
        txt_en_pantalla = self.font.render(texto, True, COLOR_BLANCO, COLOR_NEGRO)
        screen.blit(txt_en_pantalla, )


    def odo_calc(self, vel_encoder_der, vel_encoder_izq):
        conversion_der = (2 * math.pi * (DIAM_RUEDA_DER / 2)) / RESOLUCION_ENCODER
        conversion_izq = (2 * math.pi * (DIAM_RUEDA_IZQ / 2)) / RESOLUCION_ENCODER
        rueda_der = conversion_der * vel_encoder_der
        rueda_izq = conversion_izq * vel_encoder_izq

        if rueda_der < 0 and rueda_izq > 0:
            distancia_recorrida = rueda_izq / 2
        elif rueda_izq < 0 and rueda_der > 0:
            distancia_recorrida = rueda_der / 2
        else:
            distancia_recorrida = (rueda_der + rueda_izq) / 2
        giro_recorrido = -((rueda_der - rueda_izq) / SEPARACION_RUEDAS)  # Revisar

        print(vel_encoder_der, vel_encoder_izq, rueda_der, rueda_izq, distancia_recorrida, giro_recorrido)

        self.theta_giro = self.theta_giro + giro_recorrido
        self.pos_x = self.pos_x + distancia_recorrida * math.cos(self.theta_giro)
        self.pos_y = self.pos_y + distancia_recorrida * math.sin(self.theta_giro)
