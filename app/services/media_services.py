from fastapi import UploadFile
import magic
from uuid import uuid4
import hashlib


from app.exceptions.media_exceptions import FileSizeTooLarge, MimeTypeNotAllowedError
async def validate_file_size(file: UploadFile):
    """
    check the file size if it is below the MAX_FILE_SIZE
    """
    MAX_FILE_SIZE = 50 * 1024 *1024
    total_size = 0
    while chunk := await file.read(1024 *1024):
        total_size += len(chunk)
        if total_size > MAX_FILE_SIZE:
            raise FileSizeTooLarge("The file size is too LARGE.")
    
    await file.seek(0)
    return {"size":"valid"}


async def validate_MIME_type(file: UploadFile):
    """
    checks if the MIME type of the file for now, later I will make a list of allowed MIME type to validate from
    """
    ALLOWED_MIME_TYPES ={
        "image/jpeg":".jpg",
        "image/png":".png",
        "image/webp":".webp",
        "application/pdf":".pdf",
    }

    head_bytes = await file.read(2048)

    await file.seek(0)

    # this one will detect the descriptor 
    description_detector = magic.Magic()
    description = description_detector.from_buffer(head_bytes)
    # this where I detect the mime type of a file 
    mime_detector = magic.Magic(mime=True)
    mime_type = mime_detector.from_buffer(head_bytes)
    
    if mime_type not in ALLOWED_MIME_TYPES.keys():
        raise MimeTypeNotAllowedError(f"This mime type not allowed.[You submitted this:{mime_type}]; Allowed MIME types are: {ALLOWED_MIME_TYPES.keys()}")

    extension = ALLOWED_MIME_TYPES.get(mime_type)
    return description, mime_type, extension



def create_file_name():
    """creates and returns a unique and url safe file names, I have resided for uuid for robustness"""
    return uuid4()

async def create_file_checksum(file: UploadFile):
    """
    hashed the file, giving them digital fingerprints, this will help me to, 
    detect duplicates, debug, and audit trails, deduplication, and detect a change in a file...
    """
    sha256 = hashlib.sha256()
    while chunk := await file.read(1024 * 1024):
        sha256.update(chunk)
    await file.seek(0)
    # returning digest in hexadigit format
    return sha256.hexdigest()


async def file_service_assembler(file: UploadFile):
    """assembles all the functions at once """
    """this are my tests during development to see how things run"""
    print(await validate_file_size(file))
    print(await validate_MIME_type(file))
    print(await create_file_checksum(file))
    

async def save_metadata():
    """collects all file metadata, and save it """
    pass
