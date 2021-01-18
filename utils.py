from constants import *


def load_image(filename):
    return pygame.image.load(os.path.join(IMG_FOLDER, filename)).convert()


def load_snd(filename):
    return pygame.mixer.Sound(os.path.join(SND_FOLDER, filename))


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if pct >= 50:
        pygame.draw.rect(surf, GREEN, fill_rect)
    elif 30 < pct < 50:
        pygame.draw.rect(surf, YELLOW, fill_rect)
    else:
        pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)