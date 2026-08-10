from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from fastapi import UploadFile

class UploadsInUser(BaseModel):
    file:UploadFile
    description: str | None = None

class UploadsIn(UploadsInUser):
    file_id: UUID
    file_name: str
    description: str
    path: str
    file_type: str
    status: str
    content_type: str
    extension: str
    time_created: datetime
    