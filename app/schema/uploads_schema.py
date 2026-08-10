from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class Uploads(BaseModel):
    file_id: UUID
    file_name: str
    description: str
    path: str
    file_type: str
    status: str
    content_type: str
    extension: str
    time_created: datatime
    