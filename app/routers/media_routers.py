from fastapi import APIRouter, UploadFile, HTTPException, status, File
from starlette.responses import StreamingResponse
from pathlib import Path

from app.services.media_services import validate_file
from app.exceptions.media_exceptions import MediaExceptions
media_router = APIRouter(tags=["Uploads"])

@media_router.post("/media")
async def upload_file(file: UploadFile = File()):
    try:
        return await validate_file(file)
    except MediaExceptions as e:
        raise HTTPException(
            status_code =status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
  
