import pygame
from config import config
from envList import env_list

'''
ENVIRONMENT
'''


class Environment():


    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.env_selected = "startup"

        self.load_env()


    def load_env(self):

        self.env = env_list[self.env_selected]()


    def run(self, dt):

        if self.env_selected == self.env.name:
            if self.env_selected == self.env.selected_env:
                self.env.run(dt)
            else:
                self.env_selected = self.env.selected_env
                self.load_env()
        else:
            self.load_env()
