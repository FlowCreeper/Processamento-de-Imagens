from PIL import Image
import time

def converter_para_escala_de_cinza(caminho, modo="average"):
    imagem = Image.open(caminho).convert("RGB")
    
    largura, altura = imagem.size
    imagem_cinza = Image.new("RGB", (largura, altura))
    
    pixels = imagem.load()
    pixels_cinza = imagem_cinza.load()
    
    comeco = time.time()
    
    for x in range(largura):
        for y in range(altura):
            r, g, b = pixels[x, y]
            
            if modo == "average":
                cinza = (r + g + b) // 3
            
            elif modo == "luminosity":
                cinza = int(0.299*r + 0.587*g + 0.114*b)
            
            elif modo == "desaturation":
                cinza = (max(r, g, b) + min(r, g, b)) // 2
            
            else:
                raise ValueError(f"Modo `{modo}` inválido. Use: average, luminosity ou desaturation.")
            
            pixels_cinza[x, y] = (cinza, cinza, cinza)
            
    tempo = time.time() - comeco
    
    imagem_cinza.save("image_alterada.png")
    
    return tempo