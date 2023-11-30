import cv2
import numpy as np
import sys
import math

# Cargar la imagen con fondo verde
imagen = cv2.imread("nave_peru_green.png")

imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Obtener dos pirmeras dimensiones de la imagen, omitir la tercera usando _
alto, ancho, _ = imagen.shape

print("alto:",alto)
print("ancho:", ancho)

# RED GREEN BLUE
bg_color = (0, 255, 0)


# Número de columnas y filas en el grid
num_columnas = 19 # width
num_filas = 17 # height

# lo minimo que se puede reducir es al 10% o escala 1:1
## nuevo_ancho =  int(ancho * 1) if int(ancho * 1) % 2 == 0 else int(ancho * 1)+1
## nuevo_alto = int(alto * 1) if int(alto * 1) % 2 == 0 else int(alto * 1)+1

nuevo_ancho = ancho # nuevo_ancho if nuevo_ancho > num_columnas else num_columnas
nuevo_alto = alto # nuevo_alto if nuevo_alto > num_filas else num_filas

print("nuevo_ancho:", nuevo_ancho)
print("nuevo_alto:",nuevo_alto)

# Redimensionar la imagen
# imagen_redimensionada = cv2.resize(imagen, (nuevo_ancho, nuevo_alto))
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Guardar la imagen redimensionada
# cv2.imwrite("imagen_redimensionada_peru.png", imagen_redimensionada)

# Tamaño del grid
tamano_columna = nuevo_alto // num_filas
tamano_fila = nuevo_ancho // num_columnas 

print("tamano_fila:",tamano_fila)
print("tamano_columna:", tamano_columna)



# Guardar la salida en un archivo de texto
with open("salida_peru.txt", "w") as f:
        
    # Redirigir la salida en la terminal al archivo
    sys.stdout = f
    
    for i in range(num_filas):
        print(f"// fila {i}")
        for j in range(num_columnas):
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
            if bg_color != color_promedio_formateado:
                # Imprimir el color del pixel y sus coordenadas
                print(f"color_rgb{color_promedio_formateado};")
                
                print(f"rectangulo_lleno({x1}+x, {y1}+y, {x2}+x, {y2}+y);")



                   
# Restaurar la salida estándar a la consola
sys.stdout = sys.__stdout__

# Dibujar el grid en la imagen
for i in range(1, num_columnas):
    x = i * tamano_columna
    cv2.line(imagen, (x, 0), (x, nuevo_alto), (0, 0, 0), 1)

for i in range(1, num_filas):
    y = i * tamano_fila
    cv2.line(imagen, (0, y), (nuevo_ancho, y), (0, 0, 0), 1)

# Mostrar la imagen con el grid
cv2.imshow("Imagen con Grid", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()