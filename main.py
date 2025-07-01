# main.py
import pygame
from constants import *
from algorithms.dijkstra import dijkstra

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    clock = pygame.time.Clock()

    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]  # 0=empty, 1=start, 2=end, 3=wall

    def handle_mouse_click(grid, pos):
        col, row = pos[0] // GRID_SIZE, pos[1] // GRID_SIZE
        if pygame.mouse.get_pressed()[0]:  # Left click
            if grid[row][col] == 0:
                grid[row][col] = 3  # Wall
        elif pygame.mouse.get_pressed()[2]:  # Right click
            if 1 not in sum(grid, []):  # No start node
                grid[row][col] = 1
            elif 2 not in sum(grid, []):  # No end node
                grid[row][col] = 2

    def draw_grid(screen, grid):
        for row in range(ROWS):
            for col in range(COLS):
                color = WHITE
                if grid[row][col] == 1: color = RED
                elif grid[row][col] == 2: color = GREEN
                elif grid[row][col] == 3: color = GRAY
                pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, BLACK, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_pos = [(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 1][0]
                    end_pos = [(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 2][0]
                    for node in dijkstra(grid, start_pos, end_pos):
                        grid[node[0]][node[1]] = 4  # 4=path
                        draw_grid(screen, grid)
                        pygame.display.update()
                        pygame.time.delay(100)  # Slow animation

        # Handle mouse clicks outside event loop
        if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            handle_mouse_click(grid, pos)

        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()# main.py
import pygame
from constants import *
from algorithms.dijkstra import dijkstra

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    clock = pygame.time.Clock()

    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]  # 0=empty, 1=start, 2=end, 3=wall

    def handle_mouse_click(grid, pos):
        col, row = pos[0] // GRID_SIZE, pos[1] // GRID_SIZE
        if pygame.mouse.get_pressed()[0]:  # Left click
            if grid[row][col] == 0:
                grid[row][col] = 3  # Wall
        elif pygame.mouse.get_pressed()[2]:  # Right click
            if 1 not in sum(grid, []):  # No start node
                grid[row][col] = 1
            elif 2 not in sum(grid, []):  # No end node
                grid[row][col] = 2

    def draw_grid(screen, grid):
        for row in range(ROWS):
            for col in range(COLS):
                color = WHITE
                if grid[row][col] == 1: color = RED
                elif grid[row][col] == 2: color = GREEN
                elif grid[row][col] == 3: color = GRAY
                pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, BLACK, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_pos = [(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 1][0]
                    end_pos = [(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 2][0]
                    for node in dijkstra(grid, start_pos, end_pos):
                        grid[node[0]][node[1]] = 4  # 4=path
                        draw_grid(screen, grid)
                        pygame.display.update()
                        pygame.time.delay(100)  # Slow animation

        # Handle mouse clicks outside event loop
        if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            handle_mouse_click(grid, pos)

        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()