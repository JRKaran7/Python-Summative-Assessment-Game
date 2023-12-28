import pygame.sprite

import assets
import configs
from layer import Layer


class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.FLOOR
        self.image = assets.sprites_get("ground")
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index, configs.SCREEN_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 3

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
