import pygame
import sys

# Inicialización de Pygame
pygame.init()
pygame.mixer.init()
# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Botones Chetos Pygame")

# Colores
COLOR_FONDO = (134, 235, 134) 
COLOR_BOTON = (245, 51, 44)
COLOR_BOTON_SOMBRA = (200, 20, 20)
COLOR_TEXTO = (255, 255, 255)

COLOR_FONDO_CHETY = (255, 255, 255)
COLOR_BOTON_CHETY = (245, 51, 44)
COLOR_BOTON_HOVER_CHETY = (255, 80, 80)
COLOR_BOTON_SOMBRA_CHETY = (200, 20, 20)
COLOR_TEXTO_CHETY = (255, 255, 255)

COLOR_CORRECTO = (100, 100, 0)
COLOR_INCORRECTO = (255, 0, 0)
COLOR_APAGADO = (100, 100, 100)
COLOR_TITULO =(245, 51, 44)


# Coordenadas y dimensiones de los botones
rect_boton_jugar = pygame.Rect(300, 200, 200, 50)
rect_boton_puntaje = pygame.Rect(300, 300, 200, 50)
rect_boton_salir = pygame.Rect(300, 400, 200, 50)
rect_boton_preguntar = pygame.Rect(25, 50, 200, 50)
rect_boton_Reiniciar = pygame.Rect(25, 125, 200, 50)
rect_boton_volver = pygame.Rect(25, 200, 200, 50)

# Estado del juego
esta_jugando = False
pregunta = False
indice_pregunta = 0  # Para rastrear qué pregunta se está mostrando
respuesta_seleccionada = None
resultado = None
valida_click = 0
puntaje = 0
botones_apagados = []
nombre_usuario = None
mostrando_puntajes =False
contador_jugar=0
contador_reinicio=0
boton_reiniciar_activado = True 
apagar_preguntas_despues_reinocio =True
muted = False
veces=0

# Define colores para el botón cuando está desactivado
COLOR_BOTON_APAGADO_R = (150, 150, 150)
COLOR_BOTON_SOMBRA_APAGADO_R = (100, 100, 100)
# Fuente
fuente = pygame.font.SysFont(None, 40)
fuente_pregunta = pygame.font.SysFont(None, 24)

# Función para dibujar un botón con sombra
def dibujar_boton(screen, rect, color_boton, color_sombra, texto, fuente):
    # Dibujar sombra
    sombra_rect = rect.move(5, 5)
    pygame.draw.rect(screen, color_sombra, sombra_rect, border_radius=15)
    
    # Dibujar botón
    pygame.draw.rect(screen, color_boton, rect, border_radius=15)
    
    # Renderizar texto
    texto_surface = fuente.render(texto, True, COLOR_TEXTO)
    texto_rect = texto_surface.get_rect(center=rect.center)
    screen.blit(texto_surface, texto_rect)

# Función para dibujar un botón con sombra y hover
def dibujar_boton_cheti(screen, rect, color_boton, color_hover, color_sombra, texto, fuente, mouse_pos, apagado=False):
    # Determinar el color del botón dependiendo del estado hover
    color_actual = COLOR_APAGADO if apagado else (color_hover if rect.collidepoint(mouse_pos) else color_boton)
    
    # Dibujar sombra
    sombra_rect = rect.move(5, 5)
    pygame.draw.rect(screen, color_sombra, sombra_rect, border_radius=15)
    
    # Dibujar botón
    pygame.draw.rect(screen, color_actual, rect, border_radius=15)
    
    # Renderizar texto
    texto_surface = fuente.render(texto, True, COLOR_TEXTO)
    texto_rect = texto_surface.get_rect(center=rect.center)
    screen.blit(texto_surface, texto_rect)

# Función para dibujar texto
def dibujar_texto(texto, fuente, color, superficie, x, y):
    textobj = fuente.render(texto, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    superficie.blit(textobj, textrect)


#imagenes
imagen_usuario = pygame.image.load("D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\imagenes\\usuario.png")
imagen_usuario = pygame.transform.scale(imagen_usuario,(60,80)) 
imagen_rec = imagen_usuario.get_rect()
imagen_rec.x = 170
imagen_rec.y = 250

imagen_correcto = pygame.image.load("D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\imagenes\\correcto.png")
imagen_correcto = pygame.transform.scale(imagen_correcto,(300,300)) 
imagen_rec_correcto = imagen_correcto.get_rect()
imagen_rec_correcto.x = 410
imagen_rec_correcto.y = 100

imagen_incorrecto = pygame.image.load("D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\imagenes\\incorrecto.png")
imagen_incorrecto = pygame.transform.scale(imagen_incorrecto,(200,200)) 
imagen_rec_incorrecto = imagen_incorrecto.get_rect()
imagen_rec_incorrecto.x = 500
imagen_rec_incorrecto.y = 90

# Coordenadas y dimensiones de los botones
rect_boton_jugar = pygame.Rect(300, 200, 200, 50)
rect_boton_puntaje = pygame.Rect(300, 300, 200, 50)
rect_boton_salir = pygame.Rect(300, 400, 200, 50)
rect_boton_preguntar = pygame.Rect(25, 50, 200, 50)
rect_boton_Reiniciar = pygame.Rect(25, 125, 200, 50)
rect_boton_volver = pygame.Rect(25, 200, 200, 50)

# Coordenadas y dimensiones de los botones de las opciones
botones = [
    pygame.Rect(250, 275, 525, 50),  # Pregunta
    pygame.Rect(300, 350, 400, 50),  # Opción a
    pygame.Rect(300, 425, 400, 50),  # Opción b
    pygame.Rect(300, 500, 400, 50)   # Opción c
]

# Función para obtener nombre del usuario
def obtener_nombre_usuario():
    input_box = pygame.Rect(250, 275, 300, 50)
    color_inactivo = pygame.Color(245, 51, 44) #('lightskyblue3')
    color_activo = pygame.Color(100, 20, 100)#('dodgerblue2')
    color = color_inactivo
    activo = False
    nombre = ''
    hecho = False

    while not hecho:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    activo = not activo
                else:
                    activo = False
                color = color_activo if activo else color_inactivo
            if event.type == pygame.KEYDOWN:
                if activo:
                    if event.key == pygame.K_RETURN:
                        hecho = True
                    elif event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        nombre += event.unicode

        screen.fill(COLOR_FONDO)
        txt_surface = fuente.render(nombre, True, color)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        # Configuración de la pantalla
        dibujar_texto("Ingrese su Nombre ;)", fuente, COLOR_TITULO, screen, 260, 240)
        screen.blit(imagen_usuario, imagen_rec)
        
        pygame.display.flip()

    return nombre


def dibujar_boton_reinicia(screen, rect, color_boton, color_sombra, color_boton_apagado, color_sombra_apagado, texto, fuente, activo=True):
    if activo:
        # Dibujar sombra
        sombra_rect = rect.move(5, 5)
        pygame.draw.rect(screen, color_sombra, sombra_rect, border_radius=15)
        
        # Dibujar botón activo
        pygame.draw.rect(screen, color_boton, rect, border_radius=15)
    else:
        # Dibujar sombra apagada
        sombra_rect = rect.move(5, 5)
        pygame.draw.rect(screen, color_sombra_apagado, sombra_rect, border_radius=15)
        
        # Dibujar botón apagado
        pygame.draw.rect(screen, color_boton_apagado, rect, border_radius=15)
    
    # Renderizar texto
    texto_surface = fuente.render(texto, True, COLOR_TEXTO)
    texto_rect = texto_surface.get_rect(center=rect.center)
    screen.blit(texto_surface, texto_rect)

def mostrar_resultado_y_imagen(resultado):
    resultado_color = COLOR_CORRECTO if resultado == "Correcto" else COLOR_INCORRECTO
    resultado_surface = fuente.render(resultado, True, resultado_color)
    resultado_rect = resultado_surface.get_rect(center=(400, 100))
        
    if resultado == "Correcto":
    # mostrar_resultado_sonido(resultado)
        screen.blit(resultado_surface, resultado_rect)
        screen.blit(imagen_correcto, imagen_rec_correcto)
    else:
        screen.blit(resultado_surface, resultado_rect)
        screen.blit(imagen_incorrecto, imagen_rec_incorrecto)
