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
        self.diametro_der = DIAM_RUEDA_DER
        self.diametro_izq = DIAM_RUEDA_IZQ
        self.encoder = RESOLUCION_ENCODER
        self.resbalon = 0

        self.rotada = None
        self.rect_rotada = None
        self.trail_list = []

        self.fuente = pygame.font.SysFont("Arial", 24)
        self.fuenteInstrucciones = pygame.font.SysFont("Arial", 18)
        self.texto = self.fuente.render('default', True, COLOR_NEGRO, COLOR_BLANCO)
        self.textRect = self.texto.get_rect()
        self.textRect.center = (FULL_MAP_WIDTH / 10, FULL_MAP_HEIGHT / 10)
        self.texto_ruedas = self.fuente.render('default', True, COLOR_NEGRO, COLOR_BLANCO)
        self.textRect_ruedas = self.texto_ruedas.get_rect()
        self.textRect_ruedas.center = (FULL_MAP_WIDTH / 10, FULL_MAP_HEIGHT / 10 + self.texto_ruedas.get_height())
        self.instrucciones = self.fuenteInstrucciones.render('default', True, COLOR_BLANCO, COLOR_NEGRO)
        self.instruccionesRect = self.instrucciones.get_rect()

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

    def encoder_aumenta(self):
        self.encoder += 10

    def encoder_disminuye(self):
        if self.encoder > 10:
            self.encoder -= 10

    def diametro_derecha_aumenta(self):
        self.diametro_der += 1

    def diametro_izquierda_aumenta(self):
        self.diametro_izq += 1

    def diametro_derecha_disminuye(self):
        if self.diametro_der > 10:
            self.diametro_der -= 1

    def diametro_izquierda_disminuye(self):
        if self.diametro_izq > 10:
            self.diametro_izq -= 1

    def resbalon_derecha(self):
        self.resbalon = -40

    def resbalon_izquierda(self):
        self.resbalon = 40

    def reinicio(self):
        self.pos_x = 400
        self.pos_y = 400
        self.theta_giro = 0
        self.rueda_der = 0
        self.rueda_izq = 0
        self.diametro_der = DIAM_RUEDA_DER
        self.diametro_izq = DIAM_RUEDA_IZQ
        self.encoder = RESOLUCION_ENCODER
        self.resbalon = 0
        self.rotada = None
        self.rect_rotada = None
        self.trail_list = []

    def dibujar_robot(self, screen, imagen_robot):
        """ screen.blit(imagen_robot, pygame.Rect(FULL_MAP_WIDTH, FULL_MAP_HEIGHT,
                                              FULL_MAP_WIDTH / 10,
                                              FULL_MAP_HEIGHT / 10)) """
        self.rotada = pygame.transform.rotozoom(imagen_robot, math.degrees(self.theta_giro), 1)
        self.rect_rotada = self.rotada.get_rect(center=(self.pos_x, self.pos_y))
        screen.blit(self.rotada, self.rect_rotada)

    def dibujar_fondo(self, screen):
        screen.fill(COLOR_BLANCO)
        pygame.draw.rect(screen, COLOR_NEGRO, (FULL_MAP_WIDTH, 0, EXTRA_WIDTH, EXTRA_HEIGHT))
        inst = ("Controles:\n- Avance -> W\n- Retroceso -> S\n"
                "- 90ºIzquierda -> A\n- 90ºDerecha -> D\n"
                "- LigeroGiroIzq -> Q\n- LigeroGiroDer -> E\n- Parar -> \"Resto no en uso\"\n\n"
                "- AumentarEncoder (+10) \n     I + \u2191\n- DisminuirEncoder (-10)\n     I + \u2193\n"
                "- AumentarRuedaDer (+1)\n     O + \u2191\n- DisminuirRuedaDer (-1)\n    O + \u2193\n"
                "- AumentarRuedaIzq (+1)\n     P + \u2191\n- DisminuirRuedaIzq (-1)\n    P + \u2193\n\n"
                "- ResbalónRuedaDer -> V\n- ResbalónRuedaIzq -> B\n- ReiniciarValores -> R")
        inst_list = inst.splitlines()
        tam_height = self.instrucciones.get_size()
        pos_inst_height = FULL_MAP_HEIGHT / 60
        for i, l in enumerate(inst_list):
            self.instrucciones = self.fuenteInstrucciones.render(l, True, COLOR_BLANCO, COLOR_NEGRO)
            screen.blit(self.instrucciones,
                        ((FULL_MAP_WIDTH + EXTRA_WIDTH - (EXTRA_WIDTH / 1.05)), pos_inst_height))
            pos_inst_height += tam_height[1] + (tam_height[1] / 2)

    def dibujar_pos_info(self, screen):
        text = f"PosX = {int(self.pos_x)} | PosY = {int(self.pos_y)} | " \
               f"Theta = {int(math.degrees(int(self.theta_giro)))} || " \
               f"Vel_Rueda_Der = {int(self.rueda_der)} | " \
               f"Vel_rueda_Izq = {int(self.rueda_izq)}"
        self.texto = self.fuente.render(text, True, COLOR_NEGRO, COLOR_BLANCO)
        screen.blit(self.texto, self.textRect)
        text2 = f"Tam_Rueda_Der = {int(self.diametro_der)} | Tam_Rueda_Izq = {int(self.diametro_izq)} | " \
               f"Encoder = {int(self.encoder)}"
        self.texto_ruedas = self.fuente.render(text2, True, COLOR_NEGRO, COLOR_BLANCO)
        screen.blit(self.texto_ruedas, self.textRect_ruedas)

    def dibujar_trail(self, screen):
        for i in range(0, len(self.trail_list) - 1):
            pygame.draw.line(screen, COLOR_LINEA, (self.trail_list[i][0], self.trail_list[i][1]),
                             (self.trail_list[i + 1][0], self.trail_list[i + 1][1]))
        self.trail_list.append((self.pos_x, self.pos_y))

    def odo_calc(self, vel_encoder_der, vel_encoder_izq, ticks_vel):
        '''
        Este if evita que se realicen resbalones en el supuesto de que se pare el vehículo, se pulse la tecla
        de resbalar y rápidamente se arranque el vehículo. Se puede cambiar si ese es el comportamiento deseado.
        '''
        if vel_encoder_der == 0 & vel_encoder_izq == 0:
            self.resbalon = 0
            return
        conversion_der = (2 * math.pi * (self.diametro_der / 2)) / self.encoder
        conversion_izq = (2 * math.pi * (self.diametro_izq / 2)) / self.encoder
        '''
        Dependiendo del valor de resbalón, no sucede nada o se resbala durante 200 llamadas
        la rueda correspondiente al valor de la variable. Si es negativa la derecha, si es positiva
        la izquierda.
        '''
        if self.resbalon == 0:
            self.rueda_der = conversion_der * vel_encoder_der
            self.rueda_izq = conversion_izq * vel_encoder_izq
        elif self.resbalon < 0:  # Resbalon de la rueda derecha.
            self.rueda_der = (conversion_der * vel_encoder_der) - 30
            self.rueda_izq = conversion_izq * vel_encoder_izq
            self.resbalon += 1
        else:  # Resbalón de la rueda izquierda.
            self.rueda_der = conversion_der * vel_encoder_der
            self.rueda_izq = (conversion_izq * vel_encoder_izq) - 30
            self.resbalon -= 1

        self.pos_x += ((self.rueda_der + self.rueda_izq) / 2) * math.cos(self.theta_giro) * ticks_vel
        self.pos_y -= ((self.rueda_der + self.rueda_izq) / 2) * math.sin(self.theta_giro) * ticks_vel
        self.theta_giro += (self.rueda_der - self.rueda_izq) / SEPARACION_RUEDAS * ticks_vel
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
        self.pos_y = self.pos_y + distancia_recorrida * math.sin(self.theta_giro)
        """
