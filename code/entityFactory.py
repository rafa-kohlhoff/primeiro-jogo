#!/usr/bin/python
# -*- coding: utf-8 -*-

from Player import Player
from Enemy import Enemy
from Background import Background


class EntityFactory(Player, Enemy, Background):
    def __init__(self):
        self.get_entity(entity_type: str): -> Entity = None
