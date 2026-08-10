from fastapi import APIRouter, UploadFile

from app.services.uploads_service import store_file
uploads_router = APIRouter(tags=["Uploads"])

@uploads_router.post("/uploads/")
async def upload_file(file:UploadFile):
    metadata ={
        "file_size": file.size,
        "filename": file.filename,
        "content_type": file.content_type,
    }
    if await store_file(file):
        return metadata


