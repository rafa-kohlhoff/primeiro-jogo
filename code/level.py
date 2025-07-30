#!/usr/bin/python
# -*- coding: utf-8 -*-

from Game import Game
from EntityFactory import EntityFactory


class Level(Game, EntityFactory):
    def __init__(self):
        self.window = None
        self.name = None
        self.entity_list = None

    def run(self, ):
        pass
