import pygame

def load_image(image_path, x, y):
    image = pygame.image.load(image_path).convert_alpha()
    sprite = pygame.sprite.Sprite()
    sprite.image = image
    sprite.rect = sprite.image.get_rect()
    sprite.rect.center = (x, y)
    return sprite

pygame.init()

screen = pygame.display.set_mode((800, 600))

sprite = load_image('fluxosheep.png',400,300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))
    screen.blit(sprite.image, sprite.rect)
    pygame.display.flip()