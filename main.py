import pygame
import sys
from config import config
from environment import Environment as Env

'''
TorchAgent
'''


class Program:


    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((config['screen_w'], config['screen_h']))
        pygame.display.set_caption("TorchAgent")
        self.clock = pygame.time.Clock()
        self.env = Env()


    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000
            pygame.display.update()
            self.env.run(dt)


if __name__ == "__main__":

    TorchAgent = Program()

    TorchAgent.run()