from tkinter import *
import random

# Variables globales
ANCHO_CANVAS = 400
ALTO_CANVAS = 300
RADIO_PELOTA = 50
VELOCIDAD_PELOTA = 2 

# Función para mover la pelota
def mover_pelota():
    global direccion_x, direccion_y  # Declarar las variables como globales
    
    # Obtener las coordenadas actuales de la pelota
    x0, y0, _ , _ = c.coords(pelota_id)
    
    # Calcular las nuevas coordenadas de la pelota
    nuevo_x = x0 + direccion_x * VELOCIDAD_PELOTA
    nuevo_y = y0 + direccion_y * VELOCIDAD_PELOTA

    # Verificar los límites del Canvas
    if nuevo_x + RADIO_PELOTA < 0 or nuevo_x + RADIO_PELOTA > ANCHO_CANVAS:
        direccion_x = -direccion_x  # Cambiar la dirección en el eje x invirtiendo el signo
        color = "#" + ''.join(random.choices("0123456789ABCDEF", k=6))  # Generar un color aleatorio
        c.itemconfig(texto_id, fill=color)  # Cambiar el color del texto

    if nuevo_y + RADIO_PELOTA < 0 or nuevo_y + RADIO_PELOTA > ALTO_CANVAS:
        direccion_y = -direccion_y  # Cambiar la dirección en el eje y invirtiendo el signo
        color = "#" + ''.join(random.choices("0123456789ABCDEF", k=6))  # Generar un color aleatorio
        c.itemconfig(texto_id, fill=color)  # Cambiar el color del texto

    # Mover la pelota a la nueva posición
    c.move(pelota_id, direccion_x * VELOCIDAD_PELOTA, direccion_y * VELOCIDAD_PELOTA)
    c.move(texto_id, direccion_x * VELOCIDAD_PELOTA, direccion_y * VELOCIDAD_PELOTA)

    # Programar el siguiente movimiento de la pelota
    ventana.after(10, mover_pelota)

# Función para iniciar el movimiento de la pelota
def iniciar_movimiento():
    mover_pelota()

# Crear la ventana principal
ventana = Tk()
ventana.title("Pantalla de Carga DVD")
ventana.geometry(f"{(ANCHO_CANVAS+10)}x{(ALTO_CANVAS+60)}")
ventana.resizable(0, 0)

# Crear el Canvas
c = Canvas(ventana, width=ANCHO_CANVAS, height=ALTO_CANVAS, bg="gray15")
c.pack()

# Crear el círculo como fondo de la pelota
x_inicial = ANCHO_CANVAS // 2
y_inicial = ALTO_CANVAS // 2
pelota_id = c.create_oval(x_inicial - RADIO_PELOTA, y_inicial - RADIO_PELOTA, x_inicial + RADIO_PELOTA, y_inicial + RADIO_PELOTA, fill="gray15", outline="gray15")

# Crear el texto "DVD" en el centro del círculo
texto_id = c.create_text(x_inicial, y_inicial, text="DVD", font=("Helvetica", 26), fill="black")

# Crear el botón para iniciar el movimiento
boton_inicio = Button(ventana, text="Iniciar", command=iniciar_movimiento)
boton_inicio.pack()

# Definir la dirección inicial de la pelota
direccion_x = 1  # Movimiento hacia la derecha
direccion_y = 1  # Movimiento hacia abajo

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
