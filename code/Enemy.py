#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from abc import ABC, abstractmethod

from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_SHOT_DELAY
from code.Entity import Entity


class Enemy(Entity):  # Removed ABC as it's redundant
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None
