import cv2
import numpy as np
import sys

# Cargar la imagen
imagen = cv2.imread("fondo432.png")

imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Obtener dos pirmeras dimensiones de la imagen, omitir la tercera usando _
alto, ancho, _ = imagen.shape

print("alto:",alto)
print("ancho:", ancho)

# Número de columnas y filas en el grid
num_columnas = 36
num_filas = 36

# Tamaño del grid
tamano_columna = ancho // num_columnas
tamano_fila = alto // num_filas


# Guardar la salida en un archivo de texto
with open("salida.txt", "w") as f:
        
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

            # Imprimir el color del pixel y sus coordenadas
            print(f"color_rgb{color_promedio_formateado};")
            print(f"rectangulo_lleno{x1, y1, x2, y2};")
            
            
        
        
# Restaurar la salida estándar a la consola
sys.stdout = sys.__stdout__

# Dibujar el grid en la imagen
for i in range(1, num_columnas):
    x = i * tamano_columna
    cv2.line(imagen, (x, 0), (x, alto), (0, 0, 0), 1)

for i in range(1, num_filas):
    y = i * tamano_fila
    cv2.line(imagen, (0, y), (ancho, y), (0, 0, 0), 1)

# Mostrar la imagen con el grid
cv2.imshow("Imagen con Grid", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()