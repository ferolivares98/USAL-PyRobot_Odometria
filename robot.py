# -*- coding: utf-8 -*-

import pygame
import math
from constants import *


class Robot:
    def __init__(self):
        self.pos_x = 400
        self.pos_y = 400
        self.theta_giro = 0
        self.rueda_der = 0
        self.rueda_izq = 0

        self.rotada = None
        self.rect_rotada = None
        self.trail_list = []

        self.fuente = pygame.font.SysFont("Arial", 24)
        self.texto = self.fuente.render('default', True, COLOR_NEGRO, COLOR_BLANCO)
        self.textRect = self.texto.get_rect()
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

    def dibujar_fondo(self, screen):
        screen.fill(COLOR_BLANCO)

    def dibujar_pos_info(self, screen):
        texto = f"PosX = {int(self.pos_x)} | PosY = {int(self.pos_y)} | " \
                f"Theta = {int(math.degrees(int(self.theta_giro)))} || " \
                f"Vel_Rueda_Der = {int(self.rueda_der)} | " \
                f"Vel_rueda_Izq = {int(self.rueda_izq)}"
        self.texto = self.fuente.render(texto, True, COLOR_NEGRO, COLOR_BLANCO)
        screen.blit(self.texto, self.textRect)

    def dibujar_trail(self, screen):
        for i in range(0, len(self.trail_list) - 1):
            pygame.draw.line(screen, COLOR_LINEA, (self.trail_list[i][0], self.trail_list[i][1]),
                             (self.trail_list[i + 1][0], self.trail_list[i + 1][1]))
        self.trail_list.append((self.pos_x, self.pos_y))

    def odo_calc(self, vel_encoder_der, vel_encoder_izq, dt):
        conversion_der = (2 * math.pi * (DIAM_RUEDA_DER / 2)) / RESOLUCION_ENCODER
        conversion_izq = (2 * math.pi * (DIAM_RUEDA_IZQ / 2)) / RESOLUCION_ENCODER
        self.rueda_der = conversion_der * vel_encoder_der
        self.rueda_izq = conversion_izq * vel_encoder_izq

        """
        Funcional pero no corresponde con el sprite del robot-vehículo.
        if rueda_der < 0 and rueda_izq > 0:
            distancia_recorrida = rueda_izq / 2
        elif rueda_izq < 0 and rueda_der > 0:
            distancia_recorrida = rueda_der / 2
        else:
            distancia_recorrida = (rueda_der + rueda_izq) / 2
        giro_recorrido = -(rueda_der - rueda_izq) / SEPARACION_RUEDAS  # Revisar

        print(vel_encoder_der, vel_encoder_izq, rueda_der, rueda_izq, distancia_recorrida, giro_recorrido)

        self.theta_giro = self.theta_giro + giro_recorrido
        self.pos_x = self.pos_x + distancia_recorrida * math.cos(self.theta_giro)
        self.pos_y = self.pos_y + distancia_recorrida * math.sin(self.theta_giro)"""
        self.pos_x += ((self.rueda_der + self.rueda_izq) / 2) * math.cos(self.theta_giro) * dt
        self.pos_y -= ((self.rueda_der + self.rueda_izq) / 2) * math.sin(self.theta_giro) * dt
        self.theta_giro += (self.rueda_der - self.rueda_izq) / SEPARACION_RUEDAS*dt
