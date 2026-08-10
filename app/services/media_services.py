from fastapi import UploadFile
import magic

from app.exceptions.media_exceptions import FileSizeTooLarge

async def validate_file_size(file: UploadFile):
    """
    check the file size if it is below the MAX_FILE_SIZE
    """
    MAX_FILE_SIZE = 50 * 1024 *1024
    
    ALLOWED_FILE_TYPES ={
        "image/jpeg":".jpg",
        "image/png":".png",
        "image/webp":".webp",
        "application/pdf":".pdf",
    }

    total_size = 0
    while chunk := await file.read(1024 *1024):
        total_size += len(chunk)
        if total_size > MAX_FILE_SIZE:
            raise FileSizeTooLarge("The file size is too LARGE.")
    
    await file.seek(0)


async def validate_MIME_type(file: UploadFile):
    """
    checks if the MIME type of the file for now, later I will make a list of allowed MIME type to validate from
    """
    head_bytes = await file.read(2048)

    await file.seek(0)

    description_detector = magic.Magic()
    description = description_detector.from_buffer(head_bytes)
    print(description)

    mime_detector = magic.Magic(mime=True)
    mime_type = mime_detector.from_buffer(head_bytes)
    print(mime_type)
    
    test = magic.Magic()


def validate_file_naive():
    """checks the sent file type and extension"""
    pass

async def file_service_assembler(file: UploadFile):
    """assembles all the functions at once """
    await validate_file_size(file)
    await validate_MIME_type(file)
