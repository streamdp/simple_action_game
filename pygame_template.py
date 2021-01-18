# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# Art from Kenney.nl
# With https://pythonru.com/uroki
# Pygame шаблон - скелет для нового проекта Pygame
import random

from enemies import Mob
from explosion import Explosion
from player import Player
from utils import *


def gen_mobs(count, sprite):
    for i in range(count):
        mob = Mob(sprite)
        all_sprites.add(mob)
        mobs.add(mob)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка всей игровой графики и звуков
background = load_image("starfield.png")
background_rect = background.get_rect()
player_img = load_image("playerShip1_orange.png")

explosion_anim = {'lg': [], 'sm': []}
for i in range(9):
    filename = f'regularExplosion0{i}.png'
    img = load_image(filename)
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)


meteors_img = []
for file in METEORS_FILES:
    meteors_img.append(load_image(file))

expl_sounds = []
for snd in SND_FILES:
    sound = load_snd(snd)
    sound.set_volume(0.4)
    expl_sounds.append(sound)


pygame.mixer.music.load(os.path.join(SND_FOLDER, "tgfcoder-FrozenJam-SeamlessLoop.ogg"))
pygame.mixer.music.set_volume(0.4)

pygame.display.set_caption("Game")
pygame.display
clock = pygame.time.Clock()

# sprites groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()

player = Player(player_img)
all_sprites.add(player)

gen_mobs(10, meteors_img)
score = 0
pygame.mixer.music.play(loops=-1)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    player.bullets.update()
    all_sprites.update()

    mobs_bullets_hits = pygame.sprite.groupcollide(mobs, player.bullets, True, True)
    for hit in mobs_bullets_hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg', explosion_anim)
        all_sprites.add(expl)
        gen_mobs(1, meteors_img)
    # Проверка, не ударил ли моб игрока

    player_mobs_hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in player_mobs_hits:
        random.choice(expl_sounds).play()
        gen_mobs(1, meteors_img)
        player.display_damage_on_the_life_bar += hit.radius / 2
        expl = Explosion(player_mobs_hits.pop().rect.center, 'sm', explosion_anim)
        all_sprites.add(expl)

    if player.life_counter <= 0:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    player.bullets.draw(screen)
    draw_shield_bar(screen, 0, HEIGHT - BAR_HEIGHT, player.life_counter)
    draw_text(screen, 'Score: ' + str(score), 18, WIDTH / 2, 10)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
