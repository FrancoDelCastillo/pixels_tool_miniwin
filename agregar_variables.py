# Definir los valores de x e y
x = "x"
y = "y"

# Leer líneas desde el archivo
with open("goku_lineas.txt", "r") as archivo_entrada, open("nuevas_lineas.txt", "w") as archivo_salida:
    for linea in archivo_entrada:
        if "rectangulo_lleno" in linea:
            partes = linea.split("(")
            valores = [int(''.join(filter(str.isdigit, valor))) for valor in partes[1].split(", ")]
            nuevos_valores = [f"{val}+{x if i % 2 == 0 else y}" for i, val in enumerate(valores)]
            linea_modificada = f"{partes[0]}({', '.join(map(str, nuevos_valores))});"
            archivo_salida.write(linea_modificada.strip() + '\n')
        else:
            archivo_salida.write(linea.strip() + '\n')