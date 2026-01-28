import os
def manual_data_path(file_name)->str:
    path = os.path.join(
        'data',
        'manual_data',
        file_name
    )
    return path