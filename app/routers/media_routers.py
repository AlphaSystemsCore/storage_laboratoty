from fastapi import APIRouter, UploadFile, HTTPException, status, File
from starlette.responses import StreamingResponse
from pathlib import Path

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

@media_router.get("/medias/{filename}")
async def stream_file(filename):
    STORAGE_DIR = Path("uploads")
    file_path = STORAGE_DIR / f"{filename}"
    print(file_path)
    # created an iterator that yields chunks of bytes
    def iterator(file_path, chunk_size=1024 ):
        with open(file_path, "rb") as f:
            while chunk:= f.read(chunk_size):
                yield chunk
    headers = {
        "Content-Disposition": f'inline; filename="{file_path}"',
        "Accept-Ranges": "bytes"
    }
    return StreamingResponse(
        content=iterator(file_path),
        media_type="image/jpg",
        headers=headers
    )



 
# @media_router.get("/medias/v1")
# async def read_file():
#     """
#     not generally streaming, records everything into memory before rendering to the clien
#     I think this is the flaw of this design
#     """
#     STORAGE_DIR = Path("uploads")
#     file_path = STORAGE_DIR / "The-Linux-Command-Line-Book-5th-Edition.pdf"
#     def file_iterator(chunk_size= 1024 * 1024 * 10):
#         with open(file_path,  "rb") as f:
#             while chunk := f.read(chunk_size):
#                 yield chunk

#     return Response(
#         content=b"".join(file_iterator()),
#         media_type="application/octet-stream",
#         headers={"Content-Disposition":f'inline'}
#     )
