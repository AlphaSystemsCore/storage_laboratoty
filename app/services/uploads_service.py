from pathlib import Path
from fastapi import UploadFile
from uuid import uuid4

database ={}
def generate_filename(file:UploadFile):
    file_name = f"{uuid4()}"
    return file_name

async def store_file(file:UploadFile):
    # represents the filesystem path app/uploads
    STORAGE_DIR = Path("uploads")
    # ensure the dir exists
    STORAGE_DIR.mkdir(exist_ok=True)
    #constructs a path pointing to the file destination
    unique_filename = generate_filename(file)
    filename = STORAGE_DIR / unique_filename
    database[file.filename] = unique_filename

    # opens/ creates a destination as a binary file for writing and ensures it closes
    with open(filename, "wb") as f:
        while chunk := await file.read(1024 * 1024):
            # pass the byte to the dest file objects write mechanism
            f.write(chunk)
        await file.close()

    return 


    