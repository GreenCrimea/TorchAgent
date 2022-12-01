import pygame
from config import config
from time import sleep
from rendering import *
import sys

'''
STARTUP ENV
'''


class StartupEnv():


    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.name = 'startup'
        self.selected_env = "startup"

        #render loading splash
        render_img('assets/startupEnv/loading.png', [config['screen_w'] / 2, config['screen_h'] / 2])
        pygame.display.update()

        #prepare env
        self.font_24 = pygame.font.SysFont(None, 24)
        self.font_36 = pygame.font.SysFont(None, 36)
        self.font_72 = pygame.font.SysFont(None, 72)

        self.action = "none"

        self.mouse_cooldown = True
        self.cooldown_running = False
        self.cooldown_time = 350
        self.cooldown_start = 0


    def run(self, dt):

        self.display_surface.fill('black')

        #TITLE
        render_text('TorchAgent', self.font_72, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) - 100])
        render_text(config['version'], self.font_24, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) - 60])

        if self.mouse_cooldown == True:
            self.mouse_cooldown = False
            self.cooldown_running = True
            self.cooldown_start = pygame.time.get_ticks()

        if self.cooldown_running == True:
            if (self.cooldown_start + self.cooldown_time) < pygame.time.get_ticks():
                self.cooldown_running = False
                self.cooldown_start = 0 

        if self.action == 'none':
            self.action_none()
        elif self.action == 'exit':
            self.action_exit()
        #elif self.action == 'load':
        #    self.action_load()
        elif self.action == 'new':
            self.action_new()
        #elif self.action == 'edit':
        #    self.action_edit()
        

    def action_none(self):

        _, new_rect = render_text('New Environment', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 60], [25, 25], (50, 50, 50), 4, 10)
        _, load_rect = render_text('Load Environment', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 120], [25, 25], (50, 50, 50), 4, 10)
        _, edit_rect = render_text('Edit Instance Config', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 180], [25, 25], (50, 50, 50), 4, 10)
        _, exit_rect = render_text('Exit', self.font_36, 'WHITE', [config['screen_w'] / 2, config['screen_h'] - 100 ], [25, 25], (50, 50, 50), 4, 10)

        if new_rect.collidepoint(pygame.mouse.get_pos()):

            _, new_rect = render_text('New Environment', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 60], [25, 25], 'WHITE', 4, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'new'

        if load_rect.collidepoint(pygame.mouse.get_pos()):

            _, load_rect = render_text('Load Environment', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 120], [25, 25], 'WHITE', 4, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'load'

        if edit_rect.collidepoint(pygame.mouse.get_pos()):

            _, edit_rect = render_text('Edit Instance Config', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 180], [25, 25], 'WHITE', 4, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'edit'

        if exit_rect.collidepoint(pygame.mouse.get_pos()):

            _, exit_rect = render_text('Exit', self.font_36, 'WHITE', [config['screen_w'] / 2, config['screen_h'] - 100 ], [25, 25], 'WHITE', 4, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'exit'


    def action_exit(self):

        pygame.quit()
        sys.exit()


    def action_load(self):

        pass


    def action_new(self):

        _, select_rect = render_text('Select New Environment', self.font_36, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 80])
        _, GE_rect = render_text('Garden of Eden', self.font_24, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 180], [15, 15], (50, 50, 50), 2, 10)
        _, back_rect = render_text('Back', self.font_36, 'WHITE', [config['screen_w'] / 2, config['screen_h'] - 100 ], [25, 25], (50, 50, 50), 4, 10)

        if GE_rect.collidepoint(pygame.mouse.get_pos()):
            _, GE_rect = render_text('Garden of Eden', self.font_24, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) + 180], [15, 15], 'WHITE', 2, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'changeEnv'
                self.selected_env = 'GE'

        if back_rect.collidepoint(pygame.mouse.get_pos()):
            _, back_rect = render_text('Back', self.font_36, 'WHITE', [config['screen_w'] / 2, config['screen_h'] - 100 ], [25, 25], 'WHITE', 4, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'none'


    def action_edit(self):

        pass
