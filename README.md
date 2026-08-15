                                            FILE STORAGE ENGINE
Description(shrinked):
        File storage engine, upload and save files.

Full Description:
        User uploads file, after the app has finished streaming the file. It is presented in the backend as file-like object. I check the mime-type by generating the file's mime-type. Checking the file's by using the mime-type to get the extension. Extensions are stored as values in a key-value (mime-type - extension) where, the key is the mime-type while the value is the latter. So I try to retrieve the extension, from the k-v pair. If I get the extension that means the, mime-type is valid. Else the opposite. If valid, I go ahead to size validation, checksum and writing to the disk. File is read in chunks, while I keep read of total read bytes.If the total bytes are greater than the maximum allowed file size, an error is raise and the partially broken written bytes are erased automatically. Else the program continues, checksum is generated simulteneously. As the chunk are validated, and written onto the disk. The rest are now collection of metadata. This is the first part of the system. File storage and metadata storage.
        The last part of this document contain flowchart-like structure to explain the workflow.



Purpose:
        Upload, store, locate, read, write, delete, update, rename and manage file as a whole remotely.
   
File: 
        Is a persistent data identified by a name in a filesystem.(My own thought!)

Filesystem:
        Rules and datastructure that organizes persistent storage into directory or files, allowing the OS to locate, read, write, rename, delete and manage filesystem objects.(My own thought!)

File size Restriction:
        Allowed file size: 50MBs.

Allowed content types or MIME types(only for building and testing): 
        text/plain
        application/pdf
        image/png
        video/x-matroska

How I generated the MIME types:
        Used lib magic, by passing in file-like object and getting its MIME type.

The compressed workflow of the system is using:
The arrow represents the dependants.
Which step comes first.

    user uploads file 
            ^
            |
    my_api_read_byte
            ^
            |
    create a file-like object
            ^
            |
    verify content type
            ^
            |
    check the size
            ^
            |
    collect metadata, generate checksums
            ^
            |
    write the file to the disk and save metadata to db
            ^
            |
    if any of the above process fails, everything is reversed
            ^
            |
    send the client confirmation

Each process depends on the other one, the second depends on the first, and ellipsis

File size validation, checksum and writing to disk:
        Size validation:
                Maximum size have been set to, 50mbs.
                File is read in chunks, as size is measured alongside.
                When the total chunks size surpasses the allowed file, the file is rejected
                
        







                            ©️ALPHASYSTEMSCORE