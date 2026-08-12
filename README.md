                                            FILE STORAGE ENGINE
Description:
    This is a file storage engine, the purpose of this project is to store files. Allow easy retrieve, deletion, modification and travesal later.


Allowed file size: 50MBs.

Allowed content types or MIME types: text/plain
                                     application/pdf
                                     image/png":".png
                                     video/x-matroska

How I Created the MIME type list:
I used lib-magic which help me to identify the file types by, passing a file and printing its mime type. Then isolation the mime type in the dictionary ALLOWED_MIME_TYPES
 


File - is a persistent data identified by a name in a filesystem

The workflow of the system is using:

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
    collect metadata
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


                            ©️ALPHASYSTEMSCORE