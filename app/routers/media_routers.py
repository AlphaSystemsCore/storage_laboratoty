from fastapi import APIRouter, UploadFile, HTTPException, status


from app.services.media_services import file_service_assembler
from app.exceptions.media_exceptions import MediaExceptions
media_router = APIRouter(tags=["Uploads"])

@media_router.post("/medias")
async def upload_file(file: UploadFile):
    try:
        await file_service_assembler(file)
    except MediaExceptions as e:
        raise HTTPException(
            status_code =status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return {"size":"valid"}

