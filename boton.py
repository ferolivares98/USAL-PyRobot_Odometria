# -*- coding: utf-8 -*-
import pygame

from constants import COLOR_BOTON


class Boton():
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.color = COLOR_BOTON
        self.width = width
        self.height = height
        self.text = text

    def dibujar(self, window):
        pygame.draw.rect(window, color, (self.x, self.y, self.width, self.height), 0)

    def on_click(self):
        pass