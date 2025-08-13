#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH


class Enemy(Entity, ABC):
    def __int__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH