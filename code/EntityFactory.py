#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        if entity_name == 'Level1Bg':
            list_bg = []
            for i in range(7):
                list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
            return list_bg
        # Adicione outros casos aqui, se necessário
        else:
            return None  # Retorna None se o nome da entidade não for reconhecido
