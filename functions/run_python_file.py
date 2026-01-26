import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Arguments to pass to the Python file",
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(abs_file_path):
            raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
        
        if not abs_file_path.endswith(".py"):
            raise Exception(f'Error: "{file_path}" is not a Python file')
        
        command = ["python", abs_file_path]

        if args:
            command.extend(args)

        # Set the working directory properly.
        # Capture output (i.e., stdout and stderr).
        # Decode the output to strings, rather than bytes; this is done by setting text=True.
        # Set a timeout of 30 seconds to prevent infinite execution.
        process = subprocess.run(command, cwd=abs_working_dir, text=True, timeout=30, capture_output=True)
        # Build an output string based on the CompletedProcess object:
        # If the process exited with a non-zero returncode, include "Process exited with code X".
        # If no output was produced in stdout or stderr (both of which are attributes of CompletedProcess), add "No output produced".
        # Otherwise, include any text in stdout prefixed with STDOUT:, and any text in stderr prefixed with STDERR:.
        output = ""
        if process.returncode != 0:
            output += f"Process exited with code {process.returncode}"
            return output
        
        if not process.stdout and not process.stderr:
            output += "No output produced"
            return output
        
        if process.stdout:
            output += f"STDOUT:\n{process.stdout}"
        if process.stderr:
            output += f"STDERR:\n{process.stderr}"

        return output
    except Exception as e:
        return e