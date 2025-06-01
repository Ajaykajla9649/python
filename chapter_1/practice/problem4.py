import os

# Specify the directory path
directory_path = "."  # Current directory

try:
    # Get the list of all files and directories
    entries = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except NotADirectoryError:
    print(f"The path '{directory_path}' is not a directory.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")