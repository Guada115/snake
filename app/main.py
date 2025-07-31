import  pygame
import sys
import random
import os


#Inicializar pygame
pygame.init()

#Definir el tamaño de la pantalla
ancho= 600
alto = 400
tamaño_bloque = 20 #cada cuadrito de la serpiente
fps = 10

#Colores
negro = (0, 0, 0)
verde = (0, 255, 0)
verde_oscuro = (0, 150, 0)

#Score
score = 0


#Cargar archivo high score
def cargar_high_score():
    if os.path.exists("high_score.txt"):
        with open("high_score.txt", "r") as archivo:
            try:
                return int (archivo.read())
            except ValueError:
                return 0
    else:
        return 0
#Guardar el high score
def guardar_high_score(score):
    with open("high_score.txt", "w") as archivo:
        archivo.write(str(score))

high_score = cargar_high_score()
#Crear la pantalla
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake V1 - Python")

#Reloj para controlar los FPS del juego
reloj = pygame.time.Clock()

#pocisión inicial de la serpiente
x_snake = ancho // 2
y_snake = alto // 2

#dirección inicial
vel_x = tamaño_bloque
vel_y = 0

#serpiente representada como lista de segmentos (x, y)
snake = [(ancho //2, alto // 2 )] # cabeza
longitud_snake = 3

def generar_comida():
    while True:
        x = random.randint(0, (ancho - tamaño_bloque) // tamaño_bloque) * tamaño_bloque
        y = random.randint(0, (alto - tamaño_bloque) // tamaño_bloque) * tamaño_bloque
        if (x,y) not in snake: # asegurarse de que la comida no aparezca en la serpiente
            return (x,y)
#comida
comida = generar_comida()

#menú principal
def mostrar_menu():
    fuente = pygame.font.SysFont(None, 36)
    fuente_pequeña = pygame.font.SysFont(None, 24)
    seleccionando = True

    while seleccionando:
        pantalla.fill((30, 30, 30))
        #Titulo del juego
        titulo = fuente.render("Snake game en python By Guada", True, (0,255, 0))
        pantalla.blit(titulo, (ancho // 2 - titulo.get_width() //2, 50))

        #botones
        botones = {
            "Iniciar Juego": (ancho // 2, 150),
            "Escoger nivel": (ancho // 2, 220),
            "Salir": (ancho // 2, 290)
        }
        for texto, (x,y) in botones.items():
            rect = pygame.Rect(x - 100, y - 20, 200, 40)
            pygame.draw.rect(pantalla,(50, 50, 50), rect)
            pygame.draw.rect(pantalla,(200, 200, 200), rect, 2)

            texto_render = fuente_pequeña.render(texto, True, (255, 255, 255))
            pantalla.blit(texto_render, (x - texto_render.get_width() // 2, y -10))
        # Mostrar el score más alto
        fuente = pygame.font.SysFont(None, 30)
        texto_score = fuente.render(f"High Score: {high_score}", True, (255, 255, 0))
        texto_high_score = fuente.render(f"Score: {score}", True, (255, 255, 0))
        pantalla.blit(texto_score, (10, 10))
        pantalla.blit(texto_high_score, (10, 40))
        pygame.display.flip()

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 150 - 20 <my < 150 + 20:
                    return  # Iniciar juego
                elif 220 - 20 < my < 220 + 20:
                    # mplementar la lógica para escoger el nivel
                    seleccionar_nivel()
                elif 290 - 20 < my < 290 + 20:
                    pygame.quit()
                    sys.exit()

def seleccionar_nivel():
    print("Seleccionar nivel")

#Llamar la función del menú
mostrar_menu()

#Bucle del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w and vel_y == 0:
                vel_x = 0
                vel_y = -tamaño_bloque
            elif evento.key == pygame.K_s and vel_y == 0:
                vel_x = 0
                vel_y = tamaño_bloque
            elif evento.key == pygame.K_a and vel_x == 0:
                vel_x = -tamaño_bloque
                vel_y = 0
            elif evento.key == pygame.K_d and vel_x == 0:
                vel_x = tamaño_bloque
                vel_y = 0

    # cabeza basada en la dirección actual
    nueva_cabeza = (snake[0][0] + vel_x, snake[0][1] + vel_y)

    #envolver en los bordes
    x, y = nueva_cabeza
    if x >= ancho:
        x = 0
    elif x < 0:
        x = ancho -tamaño_bloque

    if y >= alto:
        y = 0
    elif y < 0:
        y = alto - tamaño_bloque

    nueva_cabeza = (x, y)
    snake.insert(0, nueva_cabeza)

    #comprobar conlisión consigo misma
    if nueva_cabeza in snake[1:]:
        print("Game Over")
        pygame.quit()
        sys.exit()
        score = 0

    #comprobar si la cabeza de la serpiente toca la comida
    if nueva_cabeza == comida:
        longitud_snake += 1
        score += 1
        if score > high_score:
            high_score = score
            guardar_high_score(high_score)
            

        comida = generar_comida()



    #mantener el tamaño (cortar la cola)
    if len(snake) > longitud_snake:
        snake.pop()

    #Actualizar la posición
    x_snake += vel_x
    y_snake += vel_y



    #Dibujar la pantalla
    pantalla.fill(negro)
    for i, segmento in enumerate(snake):
        color = verde_oscuro if i == 0 else verde
        pygame.draw.rect(pantalla, color, (segmento[0], segmento[1], tamaño_bloque, tamaño_bloque))
        pygame.draw.rect(pantalla, (255, 0, 0), (comida[0], comida[1], tamaño_bloque, tamaño_bloque))
    pygame.display.update()
    #Controlar la velocidad
    reloj.tick(fps) #10 fps

