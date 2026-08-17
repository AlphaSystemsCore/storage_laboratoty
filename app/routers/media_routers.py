from fastapi import APIRouter, UploadFile, HTTPException, status, File
from starlette.responses import StreamingResponse
from pathlib import Path

from app.services.media_services import validate_file
from app.exceptions.media_exceptions import MediaExceptions
media_router = APIRouter(tags=["Uploads"])

@media_router.post("/medias")
async def upload_file(file: UploadFile = File()):
    try:
        return await validate_file(file)
    except MediaExceptions as e:
        raise HTTPException(
            status_code =status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
  
import asyncio 
from fastapi.responses import StreamingResponse
async def text_generatot():
    for i in range(1000):
        yield f"Chunk {i} \r"
        await asyncio.sleep(0.5)
    


@media_router.get("/medias/v1")
async def stream_data():
    return StreamingResponse(
        content=text_generatot(),
        media_type="text/plain"
    )

import json

async def json_generator():
    for i in range(10000):
        data = {"event_id": i, "status": "processing"}
        yield json.dumps(data) + "\r"
        await asyncio.sleep(1)

@media_router.get("/stream-json")
async def stream_json():
    return StreamingResponse(json_generator(), media_type="application/x-ndjson")


def file_chunk_generator(file_path: str):
    with open(file_path, "rb") as file_chunk:
        while chunk := file_chunk.read(8192):
            yield chunk

@media_router.get("/download")
def download_large_file():
    file_path = "huge_dataset.zip"
    headers =  {"Content-Disposition": 'attachment; filename = "huge_dataset.zip"'}
    return StreamingResponse(file_chunk_generator(file_path), headers=headers, media_type="application/zip")

 
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
