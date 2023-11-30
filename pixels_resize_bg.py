import cv2
import numpy as np
import sys

# Cargar la imagen
imagen = cv2.imread("fondo432.png")

# Obtener dos pirmeras dimensiones de la imagen, omitir la tercera usando _
alto, ancho, _ = imagen.shape

# Número de columnas y filas en el grid
num_columnas = 36
num_filas = 36


nuevo_ancho = 640
nuevo_alto = 480


# Redimensionar la imagen
imagen_redimensionada_bg = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))
imagen_rgb = cv2.cvtColor(imagen_redimensionada_bg, cv2.COLOR_BGR2RGB)

# Guardar la imagen redimensionada
cv2.imwrite("imagen_redimensionada_bg.jpg", imagen_redimensionada_bg)


# podemos reducir columnas en base a la proporcion de 4:3
nuevo_num_columnas = 36 + (36*((640-432)/432))
nuevo_num_columnas = 40 #int(nuevo_num_columnas) if int(nuevo_num_columnas) % 2 == 0 else int(nuevo_num_columnas)+1

nuevo_num_filas = 36 + (36*((480-432)/432))
nuevo_num_filas = 30 #int(nuevo_num_filas) if int(nuevo_num_filas) % 2 == 0 else int(nuevo_num_filas)+1

print("nuevo_num_columnas", nuevo_num_columnas)
print("nuevo_num_filas", nuevo_num_filas)

# Tamaño del grid
tamano_columna = 640 // nuevo_num_columnas
tamano_fila = 480 // nuevo_num_filas

print("tamano_columna", tamano_columna)
print("tamano_fila", tamano_fila)


# Guardar la salida en un archivo de texto
with open("background.txt", "w") as f:
        
    # Redirigir la salida en la terminal al archivo
    sys.stdout = f

    for i in range(nuevo_num_filas):
        print(f"// fila {i}")
        for j in range(nuevo_num_columnas):
            # Coordenadas del cuadrado
            x1 = j * tamano_columna
            y1 = i * tamano_fila
            x2 = (j + 1) * tamano_columna
            y2 = (i + 1) * tamano_fila
         
            # Extraer el color del cuadrado
            color_cuadrado = imagen_rgb[y1:y2, x1:x2]
            
            # Calcular el promedio de los valores de los píxeles
            color_promedio = np.mean(color_cuadrado, axis=(0, 1)).astype(int)
            color_promedio_formateado = tuple(color_promedio)

            # Imprimir el color del pixel y sus coordenadas
            print(f"color_rgb{color_promedio_formateado};")
            print(f"rectangulo_lleno{x1, y1, x2, y2};")
            
            
        
        
# Restaurar la salida estándar a la consola
sys.stdout = sys.__stdout__

# Dibujar el grid en la imagen
for i in range(1, nuevo_num_columnas):
    x = i * tamano_columna
    cv2.line(imagen_redimensionada_bg, (x, 0), (x, nuevo_alto), (0, 0, 0), 1)

for i in range(1, nuevo_num_filas):
    y = i * tamano_fila
    cv2.line(imagen_redimensionada_bg, (0, y), (nuevo_ancho, y), (0, 0, 0), 1)

# Mostrar la imagen con el grid
cv2.imshow("Imagen con Grid", imagen_redimensionada_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()