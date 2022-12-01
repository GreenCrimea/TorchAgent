from config import config
import pygame

'''
RENDERING
'''


def render_text(    string: str,
                    font: pygame.font,
                    color: str,
                    location: list = [0, 0],
                    rect_inflate: list = [0, 0], 
                    rect_colour: str = None,
                    rect_border_thickness: float = 0,
                    rect_border_radius: int = 0):

    display_surface = pygame.display.get_surface()

    text = font.render(string, True, color)
    text_rect = text.get_rect()
    text_rect.center = location[0], location[1]
    inflated_rect = text_rect

    if rect_colour is not None:
        inflated_rect = text_rect.inflate(rect_inflate[0], rect_inflate[1])
        pygame.draw.rect(display_surface, rect_colour, inflated_rect, rect_border_thickness, rect_border_radius)

    display_surface.blit(text, text_rect)

    return text_rect, inflated_rect

   
def render_img( path: str,
                location: list = [0, 0]):

    display_surface = pygame.display.get_surface()

    img = pygame.image.load(path).convert_alpha()
    img_rect = img.get_rect()
    img_rect.center = location[0], location[1]
    display_surface.blit(img, img_rect)