import os
from google.genai import types


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            list_of_contents_of_the_target_directory = []
            for content in os.listdir(target_dir):
                target_dir_of_content = os.path.normpath(os.path.join(target_dir, content))
                list_of_contents_of_the_target_directory.append(f"- {content}: file_size={os.path.getsize(target_dir_of_content)} bytes, is_dir={os.path.isdir(target_dir_of_content)}")
            contents_of_the_target_directory = "\n".join(list_of_contents_of_the_target_directory)
            return contents_of_the_target_directory
            
        
    except Exception as e:
        return f"Error: {e}"
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)