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

        self.load_env(self.env_selected)


    def load_env(self, env_selected: str):

        self.env = env_list[env_selected]()


    def run(self, dt):

        self.env.run(dt)
