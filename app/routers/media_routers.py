from fastapi import APIRouter, UploadFile, HTTPException, status, File
from starlette.responses import Response 

from app.services.media_services import validate_file
from app.exceptions.media_exceptions import MediaExceptions
media_router = APIRouter(tags=["Uploads"])

@media_router.post("/medias")
async def upload_file(file: UploadFile = File()):
    try:
        await validate_file(file)
    except MediaExceptions as e:
        raise HTTPException(
            status_code =status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return {"size":"valid"}

from pathlib import Path
@media_router.get("/medias")
async def read_file():
    STORAGE_DIR = Path("uploads")
    file_path = STORAGE_DIR / "The-Linux-Command-Line-Book-5th-Edition.pdf"
    def file_iterator(chunk_size= 1024 * 1024 * 10):
        with open(file_path,  "rb") as f:
            while chunk := f.read(chunk_size):
                yield chunk

    return Response(
        content=b"".join(file_iterator()),
        media_type="application/octet-stream",
        headers={"Content-Disposition":f'attachment; filename="{"djfk"}"'}
    )
