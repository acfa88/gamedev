import pygame
from math import *

# Inicialização do pygame e configuração da janela
pygame.init()
WINDOW_SIZE = 800
ROTATE_SPEED = 0.02
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Cubo 3D - Pressione WASD para mover o cubo")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Matriz de projeção (transformação 3D para 2D)
projection_matrix = [[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]]

# Definindo os pontos do cubo
cube_points = [
    [[-1], [-1], [1]],
    [[1], [-1], [1]],
    [[1], [1], [1]],
    [[-1], [1], [1]],
    [[-1], [-1], [-1]],
    [[1], [-1], [-1]],
    [[1], [1], [-1]],
    [[-1], [1], [-1]]
]

# Função para multiplicação de matrizes
def multiply_m(a, b):
    a_rows = len(a)
    a_cols = len(a[0])
    b_rows = len(b)
    b_cols = len(b[0])
    product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]
    if a_cols == b_rows:
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]
    else:
        print("INCOMPATIBLE MATRIX SIZES")
    return product

# Função para conectar os pontos
def connect_points(i, j, points):
    pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))

# Função para aplicar rotação e projeção
def rotate_and_project(cube_points, angle_x, angle_y, angle_z):
    rotation_x = [
        [1, 0, 0],
        [0, cos(angle_x), -sin(angle_x)],
        [0, sin(angle_x), cos(angle_x)]
    ]

    rotation_y = [
        [cos(angle_y), 0, sin(angle_y)],
        [0, 1, 0],
        [-sin(angle_y), 0, cos(angle_y)]
    ]

    rotation_z = [
        [cos(angle_z), -sin(angle_z), 0],
        [sin(angle_z), cos(angle_z), 0],
        [0, 0, 1]
    ]

    points = []
    for point in cube_points:
        rotate_x = multiply_m(rotation_x, point)
        rotate_y = multiply_m(rotation_y, rotate_x)
        rotate_z = multiply_m(rotation_z, rotate_y)
        point_2d = multiply_m(projection_matrix, rotate_z)
        x = (point_2d[0][0] * 100) + WINDOW_SIZE / 2
        y = (point_2d[1][0] * 100) + WINDOW_SIZE / 2
        points.append((x, y))
    return points

# Função para exibir texto na tela
def draw_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    window.blit(text_surface, (x, y))

# Loop principal
angle_x = angle_y = angle_z = 0
while True:
    clock.tick(60)
    window.fill((0, 0, 0))
    draw_text("Pressione WASD para mover o cubo", 20, 20)

    points = rotate_and_project(cube_points, angle_x, angle_y, angle_z)

    for point in points:
        pygame.draw.circle(window, (255, 0, 0), (int(point[0]), int(point[1])), 5)

    connect_points(0, 1, points)
    connect_points(0, 3, points)
    connect_points(0, 4, points)
    connect_points(1, 2, points)
    connect_points(1, 5, points)
    connect_points(2, 6, points)
    connect_points(2, 3, points)
    connect_points(3, 7, points)
    connect_points(4, 5, points)
    connect_points(4, 7, points)
    connect_points(6, 5, points)
    connect_points(6, 7, points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Controle de rotação com teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        angle_y += ROTATE_SPEED
    if keys[pygame.K_d]:
        angle_y -= ROTATE_SPEED
    if keys[pygame.K_w]:
        angle_x += ROTATE_SPEED
    if keys[pygame.K_s]:
        angle_x -= ROTATE_SPEED
    if keys[pygame.K_q]:
        angle_z -= ROTATE_SPEED
    if keys[pygame.K_e]:
        angle_z += ROTATE_SPEED

    pygame.display.update()
