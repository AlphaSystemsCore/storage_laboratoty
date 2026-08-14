class MediaExceptions(Exception):
    """
    the root exception for all media errors
    """
    pass

class FileSizeTooLargeError(MediaExceptions):
    """
    raised when the size of the file have become too large
    """
    pass

class MimeTypeNotAllowedError(MediaExceptions):
    """raised when the application recieves a mime type that is not allowed in"""
    pass

