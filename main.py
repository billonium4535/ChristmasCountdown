import pygame
import random
from datetime import datetime, timedelta

pygame.init()
window_size = (250, 150)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Christmas Countdown")
pygame.font.init()
font = pygame.font.SysFont('Copperplate Gothic', 20, bold=True)


class Snowflake:
    def __init__(self):
        self.x = random.randint(0, window_size[0])
        self.y = random.randint(-10, -5)
        self.speed = random.randint(1, 3)
        self.radius = random.randint(1, 3)
        self.drift = random.uniform(-0.5, 0.5)

    def update(self):
        self.y += self.speed
        self.x += self.drift

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)


def get_workdays_until(local_target_date):
    today = datetime.now().date()
    days_left = (local_target_date - today).days + 1
    workdays = 0

    for day in range(days_left):
        current_day = today + timedelta(days=day)
        if current_day.weekday() < 5:
            workdays += 1

    return workdays - 1


running = True
clock = pygame.time.Clock()
snowflakes = []

target_date = datetime(datetime.now().year, 12, 22).date()
workdays_left = get_workdays_until(target_date)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 135, 62))

    if len(snowflakes) < 100:
        snowflakes.append(Snowflake())

    for flake in snowflakes:
        flake.update()
        flake.draw(screen)
        if flake.y > window_size[1]:
            snowflakes.remove(flake)

    daysText = font.render(f"Days Until Finish:", True, (157, 34, 53))
    daysValueText = font.render(f"{workdays_left}", True, (157, 34, 53))
    screen.blit(daysText, (window_size[0] // 11, 10))
    screen.blit(daysValueText, ((window_size[0] + 80) // 3, 32))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
