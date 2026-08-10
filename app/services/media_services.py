from fastapi import UploadFile

from app.exceptions.media_exceptions import FileSizeTooLarge

def validate_file_size(file: UploadFile):
    """
    check the file size if it is below the MAX_FILE_SIZE
    """
    MAX_FILE_SIZE = 50 * 1024 *1024

    total_size = 0

    while chunk := await file.read(1024 *1024):
        total_size += chunk
        if total_size > MAX_FILE_SIZE:
            raise FileSizeTooLarge("The file size is too LARGE.")

    

def validate_MIME_type():
    """
    checks if the MIME type is allowed by the application
    """
    pass

def validate_file_naive():
    """checks the sent file type and extension"""
    pass

def file_service_assembler(file: UploadFile):
    """assembles all the functions at once """
    validate_file_size(file)
