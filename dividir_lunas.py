from PIL import Image

img = Image.open("lunas/lunas.jpeg")

# 🔥 AJUSTE MANUAL (IMPORTANTE)
# recorta la zona donde realmente están las lunas
img = img.crop((0, 50, img.width, img.height))  
# ↑ puedes ajustar este "60" si aún salen letras

cols = 6
rows = 5

ancho, alto = img.size

ancho_celda = ancho / cols
alto_celda = alto / rows

contador = 1

for fila in range(rows):
    for col in range(cols):

        izquierda = int(col * ancho_celda)
        arriba = int(fila * alto_celda)
        derecha = int((col + 1) * ancho_celda)
        abajo = int((fila + 1) * alto_celda)

        recorte = img.crop((izquierda, arriba, derecha, abajo))

        recorte.save(f"lunas/luna_{contador}.jpg")
        contador += 1