import pygame

pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Definir sonidos
sonido_do = pygame.mixer.Sound("tono1.wav")
sonido_re = pygame.mixer.Sound("tono2.wav")
sonido_mi = pygame.mixer.Sound("tono3.wav")
sonido_fa = pygame.mixer.Sound("tono4.wav")

# Cargar imágenes  
imagen1 = pygame.image.load("imagen1.png")
imagen2 = pygame.image.load("imagen2.png")
imagen3 = pygame.image.load("imagen3.png")
imagen4 = pygame.image.load("imagen4.png")
imagen5 = pygame.image.load("imagen5.png")
imagen6 = pygame.image.load("imagen6.png")
imagen7 = pygame.image.load("imagen7.png")
imagen8 = pygame.image.load("imagen8.png")

# Definir pantalla
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 800
tamanio_pantalla = (ANCHO_PANTALLA, ALTO_PANTALLA)
pantalla = pygame.display.set_mode(tamanio_pantalla)
pygame.display.set_caption("Proyecto de Redes")

# Crear lista de imágenes
imagenes = [imagen1, imagen2, imagen3, imagen4, imagen5, imagen6, imagen7, imagen8]

# Definir variables para la posición de las imágenes
posicion_x = 0
posicion_y = 0

# Definiendo variables auxiliares
aux_list = [None] * 8

# Definiendo un contador de filas
cont = 1

# Definir variables para controlar el número de imágenes mostradas
num_imagenes = 0
max_num_imagenes = 8

# Definiendo variables auxiliares
aux = 0
aux2 = 0
aux3 = 0

# Pintamos el Fondo
pantalla.fill(BLANCO)

imagen = pygame.draw.rect(pantalla, BLANCO, pygame.Rect(0, 0, 100, 100))

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        # Comprobar si se presionó una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False


            # Comprobar si se presionó la tecla Enter
            if evento.key == pygame.K_RETURN and cont < 9:


                sonidos = [sonido_fa, sonido_fa, sonido_fa, sonido_do]

                # Reproducir sonidos en secuencia
                for sonido in sonidos:
                    sonido.play()
                    pygame.time.wait(100)  # Esperar 100 milisegundos antes de reproducir el siguiente sonido

                # Guardamos la última posición en X de cada fila

                if cont <= 8:
                    aux_list[cont - 1] = posicion_x

                # Cambiar la posición de las imágenes a la siguiente línea
                posicion_x = 0
                posicion_y += 100

                # Reiniciar el contador de imágenes
                num_imagenes = 0

                # Incrementar el contador
                cont += 1

            # Comprobar si se presionó la tecla de retroceso
            elif evento.key == pygame.K_BACKSPACE:

                # Comprobar si hay imágenes para borrar
                if num_imagenes > 0:
                    # Retroceder a la posición de la imagen anterior
                    posicion_x -= 100

                    # Borrar la imagen anterior dibujando un rectángulo negro en su lugar
                    pygame.draw.rect(pantalla, BLANCO, pygame.Rect(posicion_x, posicion_y, 100, 100))

                    # Decrementar el contador de imágenes
                    num_imagenes -= 1
                elif num_imagenes == 0 and posicion_y > 0:
                    # Retroceder a la fila inmediatamente anterior

                    if aux_list[cont-2] != 0:
                        posicion_x = aux_list[cont-2] - 100
                    elif aux_list[cont-2] == 0:
                        posicion_x = 0


                    posicion_y -= 100

                    # Borrar la imagen anterior dibujando un rectángulo negro en su lugar
                    pygame.draw.rect(pantalla, BLANCO, pygame.Rect(posicion_x, posicion_y, 100, 100))

                    # Incremententando el contador de imágenes
                    num_imagenes = posicion_x/100

                    cont -= 1

            # ERROR
            if evento.key == pygame.K_x:
                sonidos = [sonido_do, sonido_mi, sonido_do, sonido_mi]

                # Reproducir sonidos en secuencia
                for sonido in sonidos:
                    sonido.play()
                    pygame.time.wait(100)  # Esperar 100 milisegundos antes de reproducir el siguiente sonido

            # ENLACE / FINAL
            elif evento.key == pygame.K_z:
                sonidos = [sonido_fa, sonido_re, sonido_fa, sonido_re]

                # Reproducir sonidos en secuencia
                for sonido in sonidos:
                    sonido.play()
                    pygame.time.wait(100)  # Esperar 100 milisegundos antes de reproducir el siguiente sonido

            # Comprobar si se presionó una de las teclas de los tonos
            elif evento.key in [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_a, pygame.K_s, pygame.K_d,
                                pygame.K_f, pygame.K_i, pygame.K_o]:

                # Comprobar si se han mostrado todas las imágenes
                if num_imagenes < max_num_imagenes and evento.key != pygame.K_i and evento.key != pygame.K_o and evento.key != pygame.K_p:

                    # Tocar sonidos si se presionó una tecla específica

                    # TX
                    # BA
                    if evento.key == pygame.K_q:
                        sonido_do.play()
                        imagen = imagenes[0]
                        aux = 0
                        aux2 = 0

                    # BS
                    elif evento.key == pygame.K_w:
                        sonido_re.play()
                        imagen = imagenes[1]
                        aux = 0
                        aux2 = 0

                    # T
                    elif evento.key == pygame.K_e:
                        sonido_mi.play()
                        imagen = imagenes[2]
                        aux = 0
                        aux2 = 0

                    # AI
                    elif evento.key == pygame.K_r:
                        sonido_fa.play()
                        imagen = imagenes[3]
                        aux = 0
                        aux2 = 0

                    # AD
                    elif evento.key == pygame.K_a:
                        sonidos = [sonido_do, sonido_do]
                        imagen = imagenes[4]
                        aux = 1
                        aux2 = 1

                    # SI
                    elif evento.key == pygame.K_s:
                        sonidos = [sonido_re, sonido_re]
                        imagen = imagenes[5]
                        aux = 1
                        aux2 = 0

                    # SD
                    elif evento.key == pygame.K_d:
                        sonidos = [sonido_mi, sonido_mi]
                        imagen = imagenes[6]
                        aux = 1
                        aux2 = 0

                    # V
                    elif evento.key == pygame.K_f:
                        sonidos = [sonido_fa, sonido_fa]
                        imagen = imagenes[7]
                        aux = 1
                        aux2 = 0

                    # Dibujar la imagen en la pantalla
                    pantalla.blit(imagen, (posicion_x, posicion_y))

                    # Actualizar la posición de la siguiente imagen
                    posicion_x += 100

                    # Incrementar el contador de imágenes
                    num_imagenes += 1

                # RX
                # CONFIRMAR
                if evento.key == pygame.K_i:
                    sonido_mi.play()
                    aux = 0
                    aux2 = 0

                # REPETIR
                elif evento.key == pygame.K_o:
                    sonido_do.play()
                    aux = 0
                    aux2 = 0

                # PARAR/SEGUIR
                elif evento.key == pygame.K_p:
                    sonido_fa.play()
                    aux = 0
                    aux2 = 0

                # Reproducir sonidos en secuencia
                if aux == 1:
                    for sonido in sonidos:
                        sonido.play()
                        if aux2 == 0:
                            pygame.time.wait(100)  # Esperar 100 milisegundos antes de reproducir el siguiente sonido
                        elif aux2 == 1:
                            pygame.time.wait(200)  # Esperar 200 milisegundos antes de reproducir el siguiente sonido

                if num_imagenes == 8:
                    aux = 0



    # Dibujar en pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
