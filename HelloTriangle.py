# A placa de vídeo transforma eletricidade em gráficos através de um processo complexo que envolve vários componentes eletrônicos especializados.
# Ela é um componente essencial em um computador, responsável por converter dados digitais em sinais visuais exibidos no monitor.

# A GPU (Graphics Processing Unit) é o componente central da placa de vídeo.
# Ela contém milhares de núcleos otimizados para cálculos gráficos, permitindo processamento paralelo massivo.

# Memória de Vídeo (VRAM):
# A VRAM armazena dados gráficos, como texturas e modelos 3D, necessários para a renderização.

# Vertices e Triângulos:
# O processo começa com a definição de objetos tridimensionais em termos de vértices (pontos no espaço 3D) e triângulos formados por esses vértices.

# Vertex Shader:
# Um pequeno programa que roda na GPU e processa cada vértice individualmente.
# Ele aplica transformações, como rotações, escalas e translações, para posicionar os objetos na cena.

# Rasterização:
# Após o processamento dos vértices, a GPU preenche as áreas entre os triângulos com pixels, um processo conhecido como rasterização.

# Fragment Shader:
# Outro programa que roda na GPU, responsável por calcular a cor final de cada pixel gerado na etapa de rasterização.
# Ele leva em conta texturas, iluminação e sombreamento.

# Texturização e Mapeamento de Texturas:
# As texturas são imagens aplicadas sobre superfícies dos objetos.
# A GPU mapeia essas texturas nos triângulos para adicionar detalhes visuais.

# Iluminação e Sombreamento:
# A iluminação simula a interação da luz com os objetos.
# Modelos como o Phong calculam a cor de cada pixel com base na luz ambiente, difusa e especular.
# O sombreamento define quais áreas estão iluminadas ou na sombra.

# Blend e Z-Buffering:
# Após o cálculo da cor de cada pixel, a GPU combina os pixels sobrepostos e resolve problemas de oclusão usando técnicas como Z-Buffering.

# Saída para o Monitor:
# Por fim, os dados processados são enviados para o monitor através de interfaces como HDMI ou DisplayPort.

# Exemplo simples para ilustrar o processo:

import numpy as np

def simulate_gpu_processing(vertex_data):
    # Simula o processamento de vértices
    processed_vertices = vertex_data * np.array([1.0, 1.0, 1.0])
    print("Vértices processados:", processed_vertices)
    
    # Simula a rasterização
    pixels = processed_vertices[:, :2]
    print("Pixels gerados na rasterização:", pixels)

    # Simula o Fragment Shader aplicando cor aos pixels
    colors = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])  # RGB
    print("Cores aplicadas aos pixels:", colors)

    return pixels, colors

# Dados de exemplo (vértices em um espaço 3D)
vertex_data = np.array([
    [0.5, 0.5, 0.0],
    [-0.5, 0.5, 0.0],
    [0.0, -0.5, 0.0]
])

# Executa a simulação
simulate_gpu_processing(vertex_data)


#Hello Triangle: Exemplo de Programação dentro da placa de video.

import glfw
from OpenGL.GL import *
import numpy as np
import ctypes

vertex_shader_code = """
#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;

out vec3 vertexColor;

void main()
{
    gl_Position = vec4(position, 1.0);
    vertexColor = color;
}
"""

fragment_shader_code = """
#version 330 core
in vec3 vertexColor;
out vec4 fragColor;

void main()
{
    fragColor = vec4(vertexColor, 1.0);
}
"""

vertices = np.array([
    -0.5, -0.5, 0.0,  1.0, 0.0, 0.0,  # Red
     0.5, -0.5, 0.0,  0.0, 1.0, 0.0,  # Green
     0.0,  0.5, 0.0,  0.0, 0.0, 1.0   # Blue
], dtype=np.float32)

def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
        error = glGetShaderInfoLog(shader)
        raise RuntimeError(f'Shader compile error: {error.decode()}')
    return shader

def create_shader_program(vertex_code, fragment_code):
    vertex_shader = compile_shader(vertex_code, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_code, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    if glGetProgramiv(program, GL_LINK_STATUS) != GL_TRUE:
        error = glGetProgramInfoLog(program)
        raise RuntimeError(f'Program link error: {error.decode()}')

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program


def main():
    if not glfw.init():
        raise Exception("GLFW can't be initialized")

    window = glfw.create_window(800, 600, "OpenGL Triangle", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window can't be created")

    glfw.make_context_current(window)

    program = create_shader_program(vertex_shader_code, fragment_shader_code)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(3 * vertices.itemsize))
    glEnableVertexAttribArray(1)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(program)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glBindVertexArray(0)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glDeleteVertexArrays(1, [VAO])
    glDeleteBuffers(1, [VBO])
    glfw.terminate()

if __name__ == "__main__":
    main()
