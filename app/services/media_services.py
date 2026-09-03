from fastapi import UploadFile
import hashlib
from pathlib import Path
import magic
from uuid import uuid4


from app.exceptions.media_exceptions import FileSizeTooLargeError, MimeTypeNotAllowedError

async def validate_file(file: UploadFile):
    """ 
    Reads files in chunk and save it locally
    Only files in the ALLOWED_MIME_TYPES will be valide
        """
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
    if not extension:
        raise MimeTypeNotAllowedError(f"MIME type not allow; Presented MIME type {mime_type}; [{", ".join(ALLOWED_MIME_TYPES.keys())}]")
    
    #generating checksum, validation file size, storing file and handling cleanings
    STORAGE_DIR = Path("uploads")
    STORAGE_DIR.mkdir(exist_ok=True)
    old_filename = file.filename
    unique_filename = f"{uuid4()}{extension}"
    filename = STORAGE_DIR / unique_filename
    ALLOW_FILE_SIZE = 1024 * 1024 * 60
    CHUNK_SIZE = 1024 * 10
    total_byte_read = 0

    sha512 = hashlib.sha512()
    try:
        with open(filename, "wb") as f:
            while chunk := await file.read(CHUNK_SIZE):
                total_byte_read += len(chunk)
                if total_byte_read > ALLOW_FILE_SIZE:
                    raise FileSizeTooLargeError(f"File size too large; Presented:{file.size / (1024 * 1024):.1f} MBs.; Allowed filesize: {ALLOW_FILE_SIZE/ (1024 *1024):.1f} MBs.")
                sha512.update(chunk)
    except Exception as e:
        if filename.exists():
            filename.unlink()
            print(f"{filename} cleaned up!")
            print(old_filename)
            print("Error: ", e)
        raise e
    finally:
        await file.close()

    return {
           "owner_id": uuid4(),
            "generated_filename": unique_filename,
            "original_filename": old_filename,
            "Path": str(filename),
            "checksum": sha512.hexdigest(),
            "mime_type": mime_type,
            "size": total_byte_read,
            "status": "uploaded",
        
                }



   


