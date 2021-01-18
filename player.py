from constants import *
from weapons import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, player_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_sprite
        self.image = pygame.transform.scale(player_sprite, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - BAR_HEIGHT - 10
        self.speedx = 0
        self.life_counter = 100
        self.shoot_delay = 350
        self.last_shot = pygame.time.get_ticks()
        self.bullets = pygame.sprite.Group()
        self.life_bar_update_delay = 100
        self.life_bar_last_change = pygame.time.get_ticks()
        self.display_damage_on_the_life_bar = 0

    def update(self):
        self.update_life_bar()
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullet.shoot_sound.play()
            self.bullets.add(bullet)

    def update_life_bar(self):
        if self.display_damage_on_the_life_bar > 0:
            now = pygame.time.get_ticks()
            if now - self.life_bar_last_change > self.life_bar_update_delay:
                self.life_bar_last_change = now
                self.life_counter -= BAR_UPDATE_TICK * self.display_damage_on_the_life_bar
                self.display_damage_on_the_life_bar -= BAR_UPDATE_TICK * self.display_damage_on_the_life_bar
        if self.display_damage_on_the_life_bar >= self.life_counter:
            self.life_bar_update_delay = 50