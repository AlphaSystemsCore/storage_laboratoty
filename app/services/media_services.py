from fastapi import UploadFile
from magic import Magic

async def validate_file(file: UploadFile):

    #start with validating mime type and assignig the extension
    ALLOWED_MIME_TYPE = {
        "text/plain": ".txt",
        "application/pdf":".pdf",
        "image/png":".png",
        "video/x-matroska":".x-matroska"

    }

    # mime type extraction and checking
    head_bytes = await file.read(2048)
    await file.seek(0)
    mime_type = Magic(mime=True).from_buffer(head_bytes)
    extension = ALLOWED_MIME_TYPE.get(mime_type)

    if not ALLOWED_MIME_TYPE.get(mime_type):
        # to add custom exception later
        raise ValueError("MIMI type not allowed")
    
    #size validation phase and writing the file to disk
    


    


   


