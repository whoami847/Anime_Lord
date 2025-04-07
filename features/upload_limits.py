from config.constants import MAX_UPLOAD_SIZE

def check_upload_size(file_size):
    if file_size > MAX_UPLOAD_SIZE:
        return False, f"File exceeds {MAX_UPLOAD_SIZE//1024//1024}MB limit"
    return True, ""
