import os
import subprocess
from google.genai import types


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args:
            command.extend(args)            
            
        process = subprocess.run(command, capture_output=True, cwd=working_dir_abs, text=True, timeout=30)
        
        output = ""
        
        if process.returncode != 0:
            output += f"Process exited with code {process.returncode}\n"
        if not process.stdout and not process.stderr:
            output += "No output produced"
        if process.stdout:
            output += f"STDOUT:\n{process.stdout}\n"
        if process.stderr:
            output += f"STDERR:\n{process.stderr}\n"
        
        return output
        
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run specified python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments to pass to the Python script",
                items=types.Schema(type=types.Type.STRING)
            ),
        },
        required=["file_path"]
    ),
)