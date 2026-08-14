from fastapi import UploadFile
import hashlib
from pathlib import Path
import magic
from uuid import uuid4



from app.exceptions.media_exceptions import FileSizeTooLargeError, MimeTypeNotAllowedError
async def validate_file(file: UploadFile):
    ALLOWED_MIME_TYPES ={
        "text/plain":".txt",
        "application/pdf":".pdf",
        "image/png":".png",
        "video/x-matroska":".mkv"

    }

    # MIME type extraction, validation and extension assignment
    

    magic_numbers = await file.read(2048)
    await file.seek(0)
    mime_type_descriptor= magic.Magic(mime=True)
    mime_type = mime_type_descriptor.from_buffer(magic_numbers)
    extension = ALLOWED_MIME_TYPES.get(mime_type)
    print(mime_type)
    if not extension:
        raise MimeTypeNotAllowedError(f"MIME type not allow; Presented MIME type {mime_type}; [{", ".join(ALLOWED_MIME_TYPES.keys())}]")
    
    #generating checksum, validation file size, storing file and handling cleanings
    STORAGE_DIR = Path("uploads")
    STORAGE_DIR.mkdir(exist_ok=True)
    old_filename = file.filename
    unique_filename = f"{uuid4()}{extension}"
    new_filename = STORAGE_DIR / unique_filename
    ALLOW_FILE_SIZE = 1024 * 1024 * 60
    CHUNK_SIZE = 1024 * 10
    file_size_count = 0

    sha512 = hashlib.sha512()

    with open(new_filename, "wb") as f:
        while chunk := await file.read(CHUNK_SIZE):
            file_size_count += len(chunk)
            if file_size_count > ALLOW_FILE_SIZE:
                raise FileSizeTooLargeError(f"File size too large; Presented:{file.size / (1024 * 1024):.1f} MBs.; Allowed filesize: {ALLOW_FILE_SIZE/ (1024 *1024):.1f} MBs.")

            sha512.update(chunk)
    sha512.hexdigest()

    


   


