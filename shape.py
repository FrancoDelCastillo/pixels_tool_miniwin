
from PIL import Image


# crea un red_shape.png con todo el shape de la imagen
#crea un ufo_cut_green.png es la imagen con fondo blanco

# Cargar la imagen
imagen = Image.open("nave_peru_pixel.png")

verde_fosforescente = (0, 255, 0, 255)

# Crear un fondo del color deseado (rojo en este caso)
fondo_verde = Image.new("RGBA", imagen.size, (verde_fosforescente))  # Rojo: (255, 0, 0), totalmente opaco (alpha: 255)

# Componer la imagen sobre el fondo rojo
imagen_sobre_verde = Image.alpha_composite(fondo_verde, imagen)

imagen_sobre_verde.save("nave_peru_green.png")

ancho, alto = imagen_sobre_verde.size

print(ancho)
print(alto)

# Coordenadas de píxeles no verdes
coordenadas_no_verdes = []

for y in range(alto):
    for x in range(ancho):
        
        color_pixel = imagen_sobre_verde.getpixel((x, y))
        
        # Si el píxel no es completamente transparente, agregar sus coordenadas a la lista
        if color_pixel  != verde_fosforescente:
            coordenadas_no_verdes.append((x, y))


# Crear una nueva imagen con fondo rojo
red_shape = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))  # Rojo: (255, 0, 0), totalmente opaco (alpha: 255)

# Iterar sobre las coordenadas no transparentes y copiar el color rojo en la nueva imagen
for x, y in coordenadas_no_verdes:
    red = (255, 0, 0, 255)  # Rojo: (255, 0, 0), totalmente opaco (alpha: 255)
    red_shape.putpixel((x, y), red)

# Guardar la nueva imagen con fondo rojo
red_shape.save("nave_peru_red_shape.png")