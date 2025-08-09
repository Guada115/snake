import pygame
import sys
import csv

def guardar_puntaje_csv(nombre, score):
    with open('high_scores.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["nombre", "score"])
        writer.writerow([nombre, score])

def mostrar_game_over(pantalla, ancho, alto, score, high_score, mostrar_menu, main):
    fuente = pygame.font.SysFont(None, 48)
    fuente_pequeña = pygame.font.SysFont(None, 24)

    ingresar_nombre = score > high_score
    nombre = ""
    nombre_guardado = False

    seleccionando = True
    while seleccionando:
        pantalla.fill((30, 30, 30))

        texto = fuente.render("Game Over", True, (255, 0, 0))
        pantalla.blit(texto, (ancho // 2 - texto.get_width() // 2, 80))

        texto_score = fuente_pequeña.render(f"Score: {score}", True, (255, 255, 255))
        pantalla.blit(texto_score, (ancho // 2 - texto_score.get_width() // 2, 140))

        texto_high = fuente_pequeña.render(f"High Score: {high_score}", True, (255, 255, 0))
        pantalla.blit(texto_high, (ancho // 2 - texto_high.get_width() // 2, 170))

        if ingresar_nombre and not nombre_guardado:
            mensaje = fuente_pequeña.render("¡Nuevo récord! Escribe tu nombre:", True, (0, 255, 0))
            pantalla.blit(mensaje, (ancho // 2 - mensaje.get_width() // 2, 210))

            nombre_render = fuente_pequeña.render(nombre + "|", True, (255, 255, 255))
            pantalla.blit(nombre_render, (ancho // 2 - nombre_render.get_width() // 2, 240))
        else:
            botones = {
                "Reiniciar Juego": (ancho // 2, 290),
                "Menú Principal": (ancho // 2, 340)
            }

            for texto, (x, y) in botones.items():
                rect = pygame.Rect(x - 100, y - 20, 200, 40)
                pygame.draw.rect(pantalla, (50, 50, 50), rect)
                pygame.draw.rect(pantalla, (200, 200, 200), rect, 2)

                texto_render = fuente_pequeña.render(texto, True, (255, 255, 255))
                pantalla.blit(texto_render, (x - texto_render.get_width() // 2, y - 10))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ingresar_nombre and not nombre_guardado:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN and nombre.strip() != "":
                        guardar_puntaje_csv(nombre, score)
                        nombre_guardado = True
                        ingresar_nombre = False
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        if len(nombre) < 20 and evento.unicode.isprintable():
                            nombre += evento.unicode

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 290 - 20 < my < 290 + 20:
                    main()
                    return
                elif 340 - 20 < my < 340 + 20:
                    mostrar_menu()
                    main()
