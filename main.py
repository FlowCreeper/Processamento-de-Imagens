from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse, Response
from brilho_contraste import ajustar_brilho_contraste
from escala_cinza import converter_para_escala_de_cinza
from fastapi.middleware.cors import CORSMiddleware
import shutil
from enum import Enum
import json

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

app = FastAPI()

router = APIRouter(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

image_path = 'image.png'
modified_image_path = 'image_alterada.png'

class GrayConversionMode(Enum):
    AVERAGE = 'average'
    LUMINOSITY = 'luminosity'
    DESATURATION = 'desaturation'

@router.get("/brightness-contrast")
async def brightness_contrast(brightness: int = 0, contrast: float = 1.0):
    try:
        ajustar_brilho_contraste(modified_image_path, brightness, contrast)
    
        return Response()
    except BaseException as e:
        print(e)
        return Response(content="An unexpected error occurred", status_code=500)
        
@router.get("/b-and-w")
async def black_and_white(mode: GrayConversionMode):
    try:
        tempo = converter_para_escala_de_cinza(modified_image_path, mode.value)
        
        return Response(content=json.dumps({'time': tempo}))
    except BaseException as e:
        print(e)
        return Response(content="An unexpected error occurred", status_code=500)
    
@router.get("/image")
async def image():
    try:
        return FileResponse(modified_image_path)
    except BaseException as e:
        print(e)
        return Response(content="An unexpected error occurred", status_code=500)
    
@router.get("/reset")
async def reset():
    try:
        shutil.copy2(image_path, modified_image_path)
    except BaseException as e:
        print(e)
        return Response(content="An unexpected error occurred", status_code=500)
    
app.include_router(router)