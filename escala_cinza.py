from PIL import Image

def converter_para_escala_de_cinza(caminho):
    imagem = Image.open(caminho).convert("RGB")
    
    largura, altura = imagem.size
    
    imagem_cinza = Image.new("L", (largura, altura))
    
    for x in range(largura):
        for y in range(altura):
            r, g, b = imagem.getpixel((x, y))
            cinza = (r + g + b) // 3
            imagem_cinza.putpixel((x, y), cinza)
    
    imagem_cinza.save('image_preto_branco.png')
    
converter_para_escala_de_cinza('image.png')