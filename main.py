import pygame
import sys
from bibliotecaDatos import* 
from bibliotecaSonidos import*
from bibliotecaDiseno import*


# Bucle principal
play_background_music()     # Comienza la reproducción de la música de fondo
running = True              # Establece una bandera para controlar el bucle principal del juego.
while running:              # Inicia un bucle que continuará ejecutándose mientras running sea True.
    for event in pygame.event.get(): # aca se captura todos los eventos que suceden en Pygame
        mouse_pos = pygame.mouse.get_pos() # Se obtiene la posición actual del cursor del mouse.
        if event.type == pygame.QUIT:      # Verifica si el evento es del tipo "QUIT" (cuando el usuario cierra la ventana del juego).
            running = False                # Si se recibe un evento de tipo "QUIT", se detiene el bucle estableciendo running como falso.
        # Gestion para reproducir musica y operar con teclas
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    toggle_mute()
                elif event.key == pygame.K_DOWN:
                    bajar_volumen()
                elif event.key == pygame.K_UP:
                    subir_volumen()
                elif event.key == pygame.K_LEFT:    # va a la siguiente pista
                    next_track()
                elif event.key == pygame.K_RIGHT:   # va a la pista anterior
                    previous_track()
                elif event.key == pygame.K_s:  # Tecla 's' para detener la música
                    stop_music()
                elif event.key == pygame.K_b:  # Tecla 'b' para reproducir música de fondo
                    play_background_music()
                    
        # Manejo de clics del ratón
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse down: {event.pos}") # se imprime la posición del click.
            
            if rect_boton_jugar.collidepoint(event.pos):
                nombre_usuario=None
                boton_reiniciar_activado = True
                if not nombre_usuario:
                    nombre_usuario = obtener_nombre_usuario()
                esta_jugando = True
                contador_jugar +=1
                if contador_jugar > 1:
                        puntaje=0
                        respuesta_seleccionada = None
                        indice_pregunta = 0
                        resultado = None
                        valida_click = 0
                        esta_jugando = True
                        
            if rect_boton_Reiniciar.collidepoint(event.pos) and boton_reiniciar_activado:
                agregar_puntaje(nombre_usuario, puntaje)
                contador_reinicio+=1
                if contador_reinicio >= 1:
                    puntaje=0
                    veces=0
                    respuesta_seleccionada = None
                    indice_pregunta = 0
                    resultado = None
                    valida_click = 0
                    esta_jugando = True
                    apagar_preguntas_despues_reinocio =False
                    boton_reiniciar_activado = False  # Deshabilitar el botón Reiniciar después de presionarlo


                
            if rect_boton_volver.collidepoint(event.pos):
                esta_jugando = False
                agregar_puntaje(nombre_usuario, puntaje)
                pregunta = False
                veces=0
                mostrando_puntajes =False
                
            if rect_boton_puntaje.collidepoint(event.pos):
                esta_jugando = False
                if mostrando_puntajes ==False: 
                    mostrando_puntajes = True
                elif mostrando_puntajes ==True: 
                    mostrando_puntajes = False
            
            if rect_boton_salir.collidepoint(event.pos):
                running = False
                
                
            if rect_boton_preguntar.collidepoint(mouse_pos):
                apagar_preguntas_despues_reinocio =True
                veces+=1
                boton_reiniciar_activado = True # Deshabilitar el botón Reiniciar después de presionarlo
                pregunta = True
                valida_click = 0
                resultado = None  # Reiniciar el resultado al hacer una nueva pregunta
                indice_pregunta = (indice_pregunta + 1) % len(sub_listas)  # Avanzar a la siguiente pregunta
                botones_apagados = []  # Reiniciar el estado de los botones apagados

            # Si se hace clicK en uno de los botones de las respuestas y el botón no está apagado, se establece ok, respuesta_seleccionada y se incrementa valida_click.
            if botones[1].collidepoint(mouse_pos) and 1 not in botones_apagados:
                respuesta_seleccionada = 'a'
                valida_click += 1
            elif botones[2].collidepoint(mouse_pos) and 2 not in botones_apagados:
                respuesta_seleccionada = 'b'
                valida_click += 1
            elif botones[3].collidepoint(mouse_pos) and 3 not in botones_apagados:
                respuesta_seleccionada = 'c'
                valida_click += 1

            # Si respuesta_seleccionada no es None, se verifica si la respuesta es correcta o incorrecta, se actualiza el puntaje
            # y se reproducen sonidos correspondientes. Además, si la respuesta es incorrecta, se apaga el botón correspondiente.
            if respuesta_seleccionada is not None:
                if respuesta_seleccionada == sub_listas[indice_pregunta][4]:
                    resultado = "Correcto"
                    resultado_sonido_ok()
                    puntaje += 10  # Incrementar el puntaje
                    valida_click = 3
                else:
                    resultado = "Incorrecto"
                    resultado_sonido_falla()
                    puntaje -= 5
                    # Dependiendo de cuál opción (a, b, c) fue seleccionada incorrectamente,
                    # se agrega el número correspondiente a botones_apagados.
                    # Esto se usa para desactivar visualmente el botón de respuesta seleccionado incorrectamente.
                    if respuesta_seleccionada == 'a':
                        botones_apagados.append(1)
                    elif respuesta_seleccionada == 'b':
                        botones_apagados.append(2)
                    elif respuesta_seleccionada == 'c':
                        botones_apagados.append(3)
                respuesta_seleccionada = None
            
            
    # Llenar la pantalla con color de fondo
    screen.fill(COLOR_FONDO)

    # Dibujar botones
    if mostrando_puntajes == True and esta_jugando == False :
            screen.fill((134, 235, 134))   # Color de fondo cuando se está jugando
            # Mostrar los tres mejores puntajes
            top_puntajes = obtener_top_puntajes()
            y_eje = 50
            
            for i in range(len(top_puntajes)):
                    registro = top_puntajes[i]
                    
                    texto= (f" | {i + 1}     | {registro['nombre']:<12}     {registro['puntaje']:<3}")
                    texto_surface = fuente.render(texto, True, COLOR_BOTON)
                    screen.blit(texto_surface, (50, y_eje))
                    y_eje += 50
            titulo=(f" | Pos | {'Nombre':<12} | {'Puntaje':<3} |")
            titulo_surface = fuente.render(titulo, True, COLOR_BOTON)
            screen.blit(titulo_surface, (50, 10))
    
    if not esta_jugando:
        dibujar_boton(screen, rect_boton_jugar, COLOR_BOTON, COLOR_BOTON_SOMBRA, "Jugar", fuente)
        dibujar_boton(screen, rect_boton_puntaje, COLOR_BOTON, COLOR_BOTON_SOMBRA, "Puntaje", fuente)
        dibujar_boton(screen, rect_boton_salir, COLOR_BOTON, COLOR_BOTON_SOMBRA, "Salir", fuente)
    else:
        screen.fill((134, 235, 134))  # Color de fondo cuando se está jugando
        if nombre_usuario:
            dibujar_texto("Buena Suerte!: " + nombre_usuario, fuente, COLOR_TEXTO, screen, 20, 10)
            dibujar_boton_cheti(screen, rect_boton_preguntar, COLOR_BOTON_CHETY, COLOR_BOTON_SOMBRA_CHETY, COLOR_BOTON_HOVER_CHETY, "Preguntar", fuente, mouse_pos)
            if boton_reiniciar_activado:
                dibujar_boton_reinicia(screen, rect_boton_Reiniciar, COLOR_BOTON, COLOR_BOTON_SOMBRA, COLOR_BOTON_APAGADO_R, COLOR_BOTON_SOMBRA_APAGADO_R, "Reiniciar", fuente, boton_reiniciar_activado)
            dibujar_boton(screen, rect_boton_volver, COLOR_BOTON, COLOR_BOTON_SOMBRA, "Volver", fuente)
            
            # Mostrar puntaje
            puntaje_surface = fuente.render(f"Puntaje: {puntaje}", True, COLOR_TEXTO)
            puntaje_rect = puntaje_surface.get_rect(center=(400, 50))
            screen.blit(puntaje_surface, puntaje_rect)
            
            # Mostrar Veces/oprtunidades
            veces_surface = fuente.render(f"Partidas: {veces}", True, COLOR_TEXTO)
            veces_rect = veces_surface.get_rect(center=(600, 50))
            screen.blit(veces_surface, veces_rect)
            
        
        if pregunta:
            # Dibujar pregunta y opciones
            # Dibujar pregunta y opciones si valida_click es menor a 2 y apagar_preguntas_despues_reinocio no es False
            if valida_click < 2:
                if apagar_preguntas_despues_reinocio !=False :
                    dibujar_boton_cheti(screen, botones[0], COLOR_BOTON_CHETY, COLOR_BOTON_HOVER_CHETY, COLOR_BOTON_SOMBRA_CHETY, sub_listas[indice_pregunta][0], fuente_pregunta, mouse_pos)  # Pregunta
                    dibujar_boton_cheti(screen, botones[1], COLOR_BOTON_CHETY, COLOR_BOTON_HOVER_CHETY, COLOR_BOTON_SOMBRA_CHETY, "Opción a: " + sub_listas[indice_pregunta][1], fuente, mouse_pos, apagado=(1 in botones_apagados))  # Opción a
                    dibujar_boton_cheti(screen, botones[2], COLOR_BOTON_CHETY, COLOR_BOTON_HOVER_CHETY, COLOR_BOTON_SOMBRA_CHETY, "Opción b: " + sub_listas[indice_pregunta][2], fuente, mouse_pos, apagado=(2 in botones_apagados))  # Opción b
                    dibujar_boton_cheti(screen, botones[3], COLOR_BOTON_CHETY, COLOR_BOTON_HOVER_CHETY, COLOR_BOTON_SOMBRA_CHETY, "Opción c: " + sub_listas[indice_pregunta][3], fuente, mouse_pos, apagado=(3 in botones_apagados))  # Opción c
            else:
                mostrar_resultado_y_imagen(resultado)


    pygame.display.flip()

pygame.quit()
sys.exit()
