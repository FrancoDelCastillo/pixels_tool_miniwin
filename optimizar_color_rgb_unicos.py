import re

# Nombre del archivo de entrada
archivo_entrada = "salida_peru.txt"

# Leer el contenido del archivo de entrada
with open(archivo_entrada, "r") as archivo:
    texto = archivo.read()

# Buscar todas las llamadas a color_rgb() en el texto
matches_color = re.finditer(r'color_rgb\((\d+), (\d+), (\d+)\);([\s\S]*?)(?=(?:color_rgb|$))', texto)

# Crear un diccionario para realizar un seguimiento de las repeticiones de color_rgb() y sus rectangulo_lleno() asociados
repeticiones_color_rectangulo = {}

# Recorrer las coincidencias y contar las repeticiones
for match_color in matches_color:
    argumentos_color = tuple(map(int, match_color.groups()[:3]))
    repeticiones_color_rectangulo[argumentos_color] = repeticiones_color_rectangulo.get(argumentos_color, [])
    
    # Buscar las llamadas a rectangulo_lleno() debajo de esta llamada a color_rgb()
    matches_rectangulo = re.finditer(r'rectangulo_lleno\(([^)]+)\);', match_color.group(4))

    # Recorrer las coincidencias y guardar los argumentos de rectangulo_lleno()
    for match_rectangulo in matches_rectangulo:
        argumentos_rectangulo = tuple(map(int, match_rectangulo.group(1).split(',')))
        repeticiones_color_rectangulo[argumentos_color].append(argumentos_rectangulo)

# Filtrar los argumentos de color_rgb() que se repiten solo una vez
argumentos_color_una_vez = [arg for arg, rep in repeticiones_color_rectangulo.items() if len(rep) == 1]

# Crear variables en C++ para los argumentos de color_rgb() y rectangulo_lleno() que se repiten solo una vez
codigo_cpp = ""
for argumentos_color in argumentos_color_una_vez:
    codigo_cpp += f"color_rgb({argumentos_color[0]}, {argumentos_color[1]}, {argumentos_color[2]});\n"

    # Crear variables en C++ para los argumentos de rectangulo_lleno() asociados
    for argumentos_rectangulo in repeticiones_color_rectangulo[argumentos_color]:
        codigo_cpp += f"rectangulo_lleno({', '.join(map(str, argumentos_rectangulo))});\n"

# Guardar el resultado en un nuevo archivo
nombre_archivo_salida = "resultado_cpp_unicos.txt"
with open(nombre_archivo_salida, "w") as f:
    f.write(codigo_cpp)

print(f"Resultado guardado en '{nombre_archivo_salida}'")
