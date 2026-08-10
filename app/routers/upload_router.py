from fastapi import APIRouter, UploadFile

from app.schema.uploads_schema import UploadsInUser
from app.services.uploads_service import store_file
uploads_router = APIRouter(tags=["Uploads"])

@uploads_router.post("/uploads/")
async def upload_file(file: UploadFile):
