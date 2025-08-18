import pygame


# C
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'player1': 3,
    'player1Shot': 1,
    'player2': 3,
    'player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'player1': 300,
    'player1Shot': 1,
    'player2': 300,
    'player2Shot': 1,
    'Enemy1': 40,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'player1': 9,
    'player2': 15,
    'Enemy1': 15,
    'Enemy2': 15,

}
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXITE')
# P
PLAYER_KEY_UP = {'player1': pygame.K_UP,
                 'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN,
                 'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,
                 'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,
                 'player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'player1': pygame.K_RCTRL,
                 'player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
