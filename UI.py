import pygame
from config import config
from rendering import *
import time
'''
UI
'''


class UI():


    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.font_24 = pygame.font.SysFont(None, 24)
        self.font_36 = pygame.font.SysFont(None, 36)
        self.font_72 = pygame.font.SysFont(None, 72)

        self.generation = 0

        self.timestamp = 0

        self.UI_rect_b = pygame.Rect(0, config['screen_h'] - 80, config['screen_w'] / 2, 80)


        self.UI_rect_t = pygame.Rect(0, 0, config['screen_w'], 50)
        self.UI_play, self.UI_play_rect = render_img('assets/UI/play.png', [40, 25])
        self.UI_playing_rect = self.UI_play_rect.inflate(1, 1)
        self.UI_pause, self.UI_pause_rect = render_img('assets/UI/pause.png', [100, 25])
        self.UI_paused_rect = self.UI_pause_rect.inflate(1, 1)
        self.UI_menu = None

        self.paused = True

        self.frame_count = 0

        self.mouse_cooldown = True
        self.cooldown_running = False
        self.cooldown_time = 350
        self.cooldown_start = 0


    def render_UI_shell(self, generation, timestamp):

        self.generation = generation
        self.timestamp = timestamp

        if self.mouse_cooldown == True:
            self.mouse_cooldown = False
            self.cooldown_running = True
            self.cooldown_start = pygame.time.get_ticks()

        if self.cooldown_running == True:
            if (self.cooldown_start + self.cooldown_time) < pygame.time.get_ticks():
                self.cooldown_running = False
                self.cooldown_start = 0

        pygame.draw.rect(self.display_surface, (150, 150, 150), self.UI_rect_b)
        pygame.draw.rect(self.display_surface, (150, 150, 150), self.UI_rect_t)

        self.display_surface.blit(self.UI_play, self.UI_play_rect)
        self.display_surface.blit(self.UI_pause, self.UI_pause_rect)

        if time.time() % 1 > 0.5:
            if self.paused:
                pygame.draw.rect(self.display_surface, 'RED', self.UI_paused_rect, 3, 3)
            else:
                pygame.draw.rect(self.display_surface, 'GREEN', self.UI_playing_rect, 3, 3)

        if self.UI_play_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.paused = False

        if self.UI_pause_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.paused = True

        render_text(f'Generation: {self.generation}', self.font_24, "BLACK", [200, 5], centered=False)
        render_text(f'Time: {round(self.timestamp)}', self.font_24, "BLACK", [200, 27], centered=False)

        self.frame_count += 1

        UI_action_dict = {
            'paused': self.paused
        }

        return UI_action_dict

