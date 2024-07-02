import pygame
import time        
def resultado_sonido_ok():
        # pygame.mixer.music.stop()  # Detener cualquier sonido que esté en reproducción
            pygame.mixer.music.load("D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\efectos\\ok.mp3")
            pygame.mixer.music.set_volume(0.1) 
            pygame.mixer.music.play()
            
def  resultado_sonido_falla():
            pygame.mixer.music.load("D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\efectos\\falla.mp3")
            pygame.mixer.music.set_volume(0.1) 
            pygame.mixer.music.play()     
            
def musica_fondo():
    pygame.mixer.music.load("D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\musica\\Ronin.mp3")
    pygame.mixer.music.play(-1)     

def toggle_mute():
    global muted
    if muted:
        pygame.mixer.music.set_volume(1.0)  # Restaurar volumen anterior
    else:
        pygame.mixer.music.set_volume(0.0)  # Silenciar música
    muted = not muted
    
# Función para bajar el volumen
def bajar_volumen():
    volumen_actual = pygame.mixer.music.get_volume()
    if volumen_actual > 0.0:
        nuevo_volumen = max(0.0, volumen_actual - 0.1)  # Reducir en 0.1, mínimo 0.0
        pygame.mixer.music.set_volume(nuevo_volumen)

def subir_volumen():
    volumen_actual = pygame.mixer.music.get_volume()
    if volumen_actual < 1.0:
        nuevo_volumen = min(1.0, volumen_actual + 0.1)  # Aumentar en 0.1, máximo 1.0
        pygame.mixer.music.set_volume(nuevo_volumen)    
        
# Lista de pistas de música
playlist = [
    "D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\musica\\Ronin.mp3",
    "D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\musica\\batalla.mp3",
    "D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\musica\\Magia.mp3",
    "D:\\Desktop\\Curso_de_ingreso_PYTHON\\proramacion_1\\preparacion\\juego_2\\musica\\medieval.mp3",
]

current_track_index = 0  # Índice de la pista actual
music_playing = False     # Bandera para verificar si la música de fondo está reproduciéndose


def load_and_play_track(index):
    global current_track_index
    current_track_index = index
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    
def play_background_music():
    global music_playing
    if not music_playing:
        load_and_play_track(current_track_index)
        pygame.mixer.music.set_volume(0.1) 

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track_index])

    pygame.mixer.music.play()

def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track_index])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()
def espera(tiempo):
    time.sleep(tiempo)
    