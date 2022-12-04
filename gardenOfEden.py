import pygame
from rendering import *
from gardenOfEdenMaps import *
import time
from config import config
from agent import Agent
from UI import UI

'''
GARDEN OF EDEN
'''


class GardenOfEden():


    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.name = 'GE'
        self.selected_env = "GE"

        #render loading splash
        render_img('assets/startupEnv/loading.png', [config['screen_w'] / 2, config['screen_h'] / 2])
        pygame.display.update()

        self.UI = UI()

        #prepare env
        self.font_24 = pygame.font.SysFont(None, 24)
        self.font_36 = pygame.font.SysFont(None, 36)
        self.font_72 = pygame.font.SysFont(None, 72)

        self.action = 'none'

        self.textbox_rect = None

        self.bg_rect = None
        self.bg_img = None

        self.incubators = layer_0
        self.agents = []

        self.direction = pygame.math.Vector2()
        self.position = ([config['screen_w'] / 2, config['screen_h'] / 2])
        self.speed = config['camera_speed']
        self.camera_rect = None

        self.config = {
            'num_agents': '10',
            'begin_incubating': 'True',
        }

        self.generation = 0
        self.timestamp = 0

        self.UI_action_dict = {
            'paused': True,
        }

        self.timer1_start = 0
        self.timer2_start = 0
        self.timer1 = 0
        self.timer2 = 0
        self.paused_total = 0
        self.init_pause = True

        self.config_line_selected = -1

        self.mouse_cooldown = True
        self.cooldown_running = False
        self.cooldown_time = 350
        self.cooldown_start = 0


    def run(self, dt):

        self.display_surface.fill('black')

        self.dt = dt

        if self.mouse_cooldown == True:
            self.mouse_cooldown = False
            self.cooldown_running = True
            self.cooldown_start = pygame.time.get_ticks()

        if self.cooldown_running == True:
            if (self.cooldown_start + self.cooldown_time) < pygame.time.get_ticks():
                self.cooldown_running = False
                self.cooldown_start = 0

        if self.action == 'none':
            self.action_configure_env()
        elif self.action == 'generate':
            self.action_generate_init()
        elif self.action == 'render':
            self.action_render()


    def action_configure_env(self):

        
        bounds_rect = pygame.Rect(0, 0, config['screen_w'] - 200, config['screen_h'] - 300)
        bounds_rect.center = config['screen_w'] / 2, config['screen_h'] / 2

        if self.textbox_rect is None:
            self.textbox_rect = pygame.Rect(0, 0, config['screen_w'] - 200, config['screen_h'] - 300)
            self.textbox_rect.center = config['screen_w'] / 2, config['screen_h'] / 2
            self.textbox_rect.height = (len(list(self.config.values())) * 50) + 25

        for i in range(len(self.config.values())):

            text = f'{list(self.config.keys())[i]}: {list(self.config.values())[i]}'

            text_rect, _ = render_text(text, self.font_24, "WHITE", [self.textbox_rect.topleft[0] + 20, self.textbox_rect.topleft[1] + 25 + (i * 50)], centered=False)    
            if text_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                    self.config_line_selected = i

            if i == self.config_line_selected:
                cursor = pygame.Rect(text_rect.topright, (3, text_rect.height))
                if time.time() % 1 > 0.5:
                    pygame.draw.rect(self.display_surface, 'WHITE', cursor)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(list(self.config.values())[self.config_line_selected]) > 0:
                            self.config[f'{str(list(self.config.keys())[self.config_line_selected])}'] = self.config[f'{str(list(self.config.keys())[self.config_line_selected])}'][:-1]
                    else:
                        self.config[f'{str(list(self.config.keys())[self.config_line_selected])}'] += event.unicode
                elif event.type == pygame.MOUSEWHEEL:
                    if 495 <= self.textbox_rect.bottomleft[1] <= 725:  
                        self.textbox_rect = self.textbox_rect.move(0, event.y * 10)
                        if 495 > self.textbox_rect.bottomleft[1]:
                            self.textbox_rect = self.textbox_rect.move(0, 20)
                        if 725 < self.textbox_rect.bottomleft[1]:
                            self.textbox_rect = self.textbox_rect.move(0, -20)
        
        pygame.draw.rect(self.display_surface, (50, 50, 50), bounds_rect, 5, 10)
              
        bottom_rect = pygame.Rect(bounds_rect.bottomleft[0], bounds_rect.bottomleft[1], config['screen_w'] - 200, config['screen_h'] - 300)
        pygame.draw.rect(self.display_surface, 'BLACK', bottom_rect)

        top_rect = pygame.Rect(bounds_rect.topleft[0], bounds_rect.topleft[1], config['screen_w'] - 200, config['screen_h'] - 300)
        top_rect.bottomleft = bounds_rect.topleft
        pygame.draw.rect(self.display_surface, 'BLACK', top_rect)

        render_text('Configure Garden Of Eden Environment', self.font_72, 'WHITE', [config['screen_w'] / 2, (config['screen_h'] / 4) - 100])

        _, back_rect = render_text('Back', self.font_36, 'WHITE', [config['screen_w'] / 2, config['screen_h'] - 100 ], [25, 25], (50, 50, 50), 4, 10)

        if back_rect.collidepoint(pygame.mouse.get_pos()):
            _, back_rect = render_text('Back', self.font_36, 'WHITE', [config['screen_w'] / 2, config['screen_h'] - 100 ], [25, 25], 'WHITE', 4, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'changeEnv'
                self.selected_env = 'startup'

        _, generate_rect = render_text('Generate', self.font_36, 'WHITE', [(config['screen_w'] / 2) + 400, config['screen_h'] - 100 ], [25, 25], (50, 50, 50), 4, 10)

        if generate_rect.collidepoint(pygame.mouse.get_pos()):
            _, generate_rect = render_text('Generate', self.font_36, 'WHITE', [(config['screen_w'] / 2) + 400, config['screen_h'] - 100 ], [25, 25], 'WHITE', 4, 10)
            if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                self.mouse_cooldown = True
                self.action = 'generate'


    def action_generate_init(self):

        #render loading splash
        render_img('assets/startupEnv/loading.png', [config['screen_w'] / 2, config['screen_h'] / 2])
        pygame.display.update()

        if self.bg_rect is None:
            self.bg_img, self.bg_rect = render_img('assets/GardenOfEden/background.png', [config['screen_w'] / 2, config['screen_h'] / 2])

        self.display_surface.blit(self.bg_img, self.bg_rect)

        for i in range(config['tile_num_h']):
            for j in range(config['tile_num_w']):
                if layer_1[i][j] == 1:
                    asset_img, asset_rect = render_img('assets/GardenOfEden/incubator.png', [self.bg_rect.topleft[0] + (j * config['tile_size']), self.bg_rect.topleft[1] + (i * config['tile_size'])])
                    self.incubators[i][j] = (asset_img, asset_rect)
                else:
                    self.incubators[i][j] = 0

        for a in range(int(self.config['num_agents'])):

            self.agents.append(Agent(index_no=a, constructed=True))

            for i in range(config['tile_num_h']):
                for j in range(config['tile_num_w']):
                    if layer_1[i][j] == 1:
                        self.agents[a].location_x = j
                        self.agents[a].location_y = i

        self.action = 'render'


    def action_render(self):

        if self.bg_rect is None:
            self.bg_img, self.bg_rect = render_img('assets/GardenOfEden/background.png', [config['screen_w'] / 2, config['screen_h'] / 2])

        self.display_surface.blit(self.bg_img, self.bg_rect)

        for i in range(config['tile_num_h']):
            for j in range(config['tile_num_w']):
                if layer_1[i][j] == 1:
                    asset_img, asset_rect = render_img('assets/GardenOfEden/incubator.png', [self.bg_rect.topleft[0] + (j * config['tile_size']), self.bg_rect.topleft[1] + (i * config['tile_size'])])
                    
                    if asset_rect.collidepoint(pygame.mouse.get_pos()):
                        inflated_rect = asset_rect.inflate(15, 15)
                        pygame.draw.rect(self.display_surface, (200, 200, 200), inflated_rect, 3, 10)

                        if pygame.mouse.get_pressed(3)[0] == True and self.cooldown_running == False:
                            self.mouse_cooldown = True
                            self.selected_agent((i, j))

                    self.incubators[i][j] = (asset_img, asset_rect)
                else:
                    self.incubators[i][j] = 0

        self.camera()

        if self.UI_action_dict['paused'] == False:
            self.init_pause = False
            self.paused_total = self.paused_total + self.timer2
            self.timer2_start = 0
            self.timer2 = 0
            if self.timer1_start == 0:
                self.timer1_start = time.time()
            self.timer1 = time.time() - (self.timer1_start + self.paused_total)
            self.timestamp =+ self.timer1

        elif self.UI_action_dict['paused'] == True:
            if self.init_pause == False:
                if self.timer2_start == 0:
                    self.timer2_start = time.time()
                self.timer2 = time.time() - self.timer2_start

        self.UI_action_dict = self.UI.render_UI_shell(self.generation, self.timestamp)

        pygame.display.update()


    def camera(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = 1
        elif keys[pygame.K_s]:
            self.direction.y = -1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = 1
        elif keys[pygame.K_d]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        if self.direction.x != 0:
            self.bg_rect.x += self.direction.x * self.speed * self.dt

        if self.direction.y != 0:
            self.bg_rect.y += self.direction.y * self.speed * self.dt


    def selected_agent(self, index: tuple):

        pass