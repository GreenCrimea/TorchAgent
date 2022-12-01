import pygame
from config import config
from time import sleep
from rendering import *

'''
STARTUP ENV
'''


class StartupEnv():


    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        #render loading splash
        render_img('assets/startupEnv/loading.png', [config['screen_w'] / 2, config['screen_h'] / 2])
        pygame.display.update()

        #prepare env
        self.font_24 = pygame.font.SysFont(None, 24)
        self.font_36 = pygame.font.SysFont(None, 36)
        self.font_72 = pygame.font.SysFont(None, 72)

        self.action = "none"


    def run(self, dt):

        self.display_surface.fill('black')

        #TITLE
        render_text('TorchAgent', self.font_72, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) - 100])
        render_text(config['version'], self.font_24, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) - 60])

        if self.action == 'none':
            
            _, new_rect = render_text('New Environment', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 60], [25, 25], (50, 50, 50), 4, 10)
            _, load_rect = render_text('Load Environment', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 120], [25, 25], (50, 50, 50), 4, 10)
            _, edit_rect = render_text('Edit Instance Config', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 180], [25, 25], (50, 50, 50), 4, 10)
            _, exit_rect = render_text('Exit', self.font_36, 'WHITE', [config['screen_w'] / 2, config['screen_h'] - 100 ], [25, 25], (50, 50, 50), 4, 10)


    def overlay(self):

        pass
