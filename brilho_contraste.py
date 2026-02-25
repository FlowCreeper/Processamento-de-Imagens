from PIL import Image
import numpy as np

def ajustar_brilho_contraste(caminho: str, brilho: int, contraste: int):
    imagem = Image.open(caminho).convert("RGB")
    
    img_array = np.array(imagem, dtype=np.float32)
    
    img_array += brilho
    
    img_array *= contraste
    
    np.clip(img_array, 0, 255, out=img_array)
    
    imagem_ajustada = Image.fromarray(img_array.astype('uint8'))
    imagem_ajustada.save('image_alterada.png')
    
ajustar_brilho_contraste('image.png', 10, 2)