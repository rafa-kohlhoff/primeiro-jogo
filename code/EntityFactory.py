#!/usr/bin/python
# -*- coding: utf-8 -*-
from code import Background
from code.const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    # Correctly pass the 'position' variable directly
                    list_bg.append(Background(f'Level1Bg{i}', position(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg