from fastapi import FastAPI
from fastapi.responses import FileResponse
from brilho_contraste import ajustar_brilho_contraste
import os

app = FastAPI()

image_path = 'image_alterada.png'

@app.get("/api/brightness-contrast")
async def brightness_contrast(brightness: int = 0, contrast: float = 1.0):
    ajustar_brilho_contraste('image.png', brightness, contrast)
    
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    return {"error": "File not found!"}