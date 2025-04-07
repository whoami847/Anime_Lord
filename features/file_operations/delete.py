from database.crud import delete_file_record

def delete_file(file_id):
    # 1. Delete from storage
    # 2. Delete from database
    delete_file_record(file_id)
    # Add error handling
