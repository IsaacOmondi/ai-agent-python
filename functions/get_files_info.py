import os

def get_files_info(working_directory, directory="."):
    try:
        
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')

        if not os.path.isdir(target_dir):
            raise Exception(f'"{target_dir}" is not a directory')
        
        dir_items = os.listdir(target_dir)
        for item in dir_items:
            # README.md: file_size=1032 bytes, is_dir=False
            print(f'- {item}: file_size={os.path.getsize(os.path.join(target_dir, item))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, item))}')
    
    except Exception as e:
        print(f'Error: {e}')
        return f'Error: {e}'