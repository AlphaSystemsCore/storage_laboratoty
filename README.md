                                            FILE STORAGE ENGINE
Description:
        File storage engine, upload and save files.

Purpose:
        Upload, store, locate, read, write, delete, update, rename and manage file as a whole.
   
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

How I Created the MIME type list:
I used lib-magic which helps me to identify the mime types by, passing a file and printing its mime type. Then isolating the mime type in the dictionary ALLOWED_MIME_TYPES.

 




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