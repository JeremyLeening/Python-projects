import pygame
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

BAR_WIDTH = 10
BAR_HEIGHT_MULTIPLIER = 2
BAR_COLOR = (0, 255, 0)  # Green
SWAP_COLOR = (255, 0, 0)  # Red
SORTED_COLOR = (0, 0, 255)  # Blue

# Delay (in milliseconds) for visualization
DELAY = 1

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")


def draw_bar(heights, color_map):
    window.fill((255, 255, 255))

    for i, height in enumerate(heights):
        x = i * (BAR_WIDTH + 1)
        y = WINDOW_HEIGHT - height
        color = color_map.get(i, BAR_COLOR)
        pygame.draw.rect(window, color, (x, y, BAR_WIDTH, height))

    pygame.display.update()


def bubble_sort(heights):
    n = len(heights)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            color_map = {j: SWAP_COLOR, j + 1: SWAP_COLOR}
            draw_bar(heights, color_map)
            pygame.time.wait(DELAY)

            if heights[j] > heights[j + 1]:
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
                swapped = True
        if not swapped:
            break


def main():
    heights = [random.randint(50, WINDOW_HEIGHT) for _ in range(WINDOW_WIDTH // (BAR_WIDTH + 1))]

    running = True
    while running:


        bubble_sort(heights)

        draw_bar(heights, {i: SORTED_COLOR for i in range(len(heights))})
        time.sleep(5)
        running = False

    pygame.quit()


if __name__ == '__main__':
    main()