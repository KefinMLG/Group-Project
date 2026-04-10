import pygame

# 1. Initialize pygame
pygame.init()

# 2. Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame")

# 3. Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 4. Game clock (controls FPS)
clock = pygame.time.Clock()

# 5. Game variables
x, y = 100, 100
speed = 5

# 6. Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    # --- Events (keyboard, quit, etc.) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Movement ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed

    # --- Drawing ---
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, 50, 50))  # player square

    # --- Update screen ---
    pygame.display.flip()

# 7. Quit safely
pygame.quit()