from fastapi import UploadFile
from magic import Magic

async def validate_file(file: UploadFile):

    #start with validating mime type
    ALLOWED_MIME_TYPE = {
        "text/plain": ".txt",
        "application/pdf":".pdf",
        "image/png":".png",
        "video/x-matroska":".x-matroska"

    }
    
    head_bytes = await file.read(2048)
    await file.seek(0)

    mime_type = Magic(mime=True).from_buffer(head_bytes)
    print(mime_type)


