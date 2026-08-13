from fastapi import UploadFile
from magic import Magic
import hashlib
from pathlib import Path
from uuid import uuid4

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
    sha512 = hashlib.sha512()

    if not ALLOWED_MIME_TYPE.get(mime_type):
        # to add custom exception later
        raise ValueError(f"MIMI type not allowed; Presented MIMI type: {mime_type}; Allowed MIME types are {", ".join(ALLOWED_MIME_TYPE.keys())}")
    
    #size validation phase, checksum generation and writing the file to disk
    MAX_SIZE = 1024 * 1024 * 50
    STORAGE_DIR  = Path("uploads")
    STORAGE_DIR.mkdir(exist_ok=True)
    filename = f"{uuid4()}{extension}"
    print(filename)
    
    
    while chunk := await file.read():
        #length check
        if MAX_SIZE <= len(chunk):
            # to add custom exception later
            raise ValueError(F"File size is too big; Your presented file {file.size/(1024 * 1024):.2f} MBs. ;[Expected file size is {MAX_SIZE/(1024 *1024)} MBs.]")

        sha512.update(chunk)

    
    checksum = sha512.hexdigest()

    

    


    


   


