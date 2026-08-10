from fastapi import APIRouter, UploadFile, HTTPException, status

from app.schema.uploads_schema import UploadsInUser
from app.services.uploads_service import file_service_assembler
from app.exceptions.media_exceptions import MediaExceptions
media_router = APIRouter(tags=["Uploads"])

@media_router.post("/medias")
def upload_file(file: UploadFile):
    try:
        file_service_assembler(file)
    except MediaExceptions:
        raise HTTPException(
            status_code =status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

        