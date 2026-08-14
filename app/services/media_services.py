from fastapi import UploadFile
from app.exceptions.media_exceptions import FileSizeTooLargeError, MimeTypeNotAllowedError
async def validate_file(file: UploadFile):
    ALLOWED_MIME_TYPES ={
        "text/plain":".txt",
        "application/pdf":".pdf",
        "image/png":".png",
        "video/x-matroska":".mkv"

    }

    # MIME type extraction, validation and extension assignment
    import magic

    magic_numbers = await file.read(2048)
    await file.close()
    mime_type_descriptor= magic.Magic(mime=True)
    mime_type = mime_type_descriptor.from_buffer(magic_numbers)
    extension = ALLOWED_MIME_TYPES.get(mime_type)
    print(mime_type)
    if not extension:
        raise MimeTypeNotAllowedError(f"MIME type not allow; Presented MIME type {mime_type}; [{", ".join(ALLOWED_MIME_TYPES.keys())}]")
    


    


   


