import pygame
import sys

def mostrar_game_over(pantalla, ancho, alto, score, high_score, mostrar_menu, main):
    fuente = pygame.font.SysFont(None, 48)
    fuente_pequeña = pygame.font.SysFont(None, 24)

    seleccionando = True
    while seleccionando:
        pantalla.fill((30, 30, 30))

        texto = fuente.render("Game Over", True, (255, 0, 0))
        pantalla.blit(texto, (ancho // 2 - texto.get_width() // 2, 80))

        texto_score_render = fuente_pequeña.render(f"Score: {score}", True, (255, 255, 0))
        pantalla.blit(texto_score_render, (ancho // 2 - texto_score_render.get_width() // 2, 140))

        texto_hig_score_render = fuente_pequeña.render(f"High Score: {high_score}", True, (255, 255, 0))
        pantalla.blit(texto_hig_score_render, (ancho // 2 - texto_hig_score_render.get_width() // 2, 170))

        # Botones
        botones = {

            "Menú Principal": (ancho // 2, 310)
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
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 240 - 20 < my < 240 + 20:
                    main()
                    return
                elif 310 - 20 < my < 310 + 20:
                    mostrar_menu()
                    main()
                    return
