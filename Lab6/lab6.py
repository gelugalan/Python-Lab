import os
import sys

def print_file_contents(directory, extension):
    try:
        files = [file for file in os.listdir(directory) if file.endswith(extension)]

        for file in files:
            file_path = os.path.join(directory, file)
            with open(file_path, 'r') as f:
                print(f.read())

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except OSError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def rename_files_with_prefix(directory):
    try:
        files = os.listdir(directory)

        for i, file in enumerate(files, start=1):
            file_path = os.path.join(directory, file)
            new_name = f"file{i}.{file.split('.')[-1]}"
            os.rename(file_path, os.path.join(directory, new_name))

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except OSError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def calculate_total_size(directory):
    try:
        total_size = 0

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)

        print(f"Total size of files in {directory}: {total_size} bytes")

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def count_files_by_extension(directory):
    try:
        files = os.listdir(directory)
        extension_count = {}

        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                _, file_extension = os.path.splitext(file)
                extension_count[file_extension] = extension_count.get(file_extension, 0) + 1

        for ext, count in extension_count.items():
            print(f"{ext}: {count} files")

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{directory}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <script_number> <directory_path> [file_extension]")
        return

    script_number = int(sys.argv[1])
    directory_path = sys.argv[2]

    if script_number == 1:
        if len(sys.argv) != 4:
            print("Usage for script 1: python script.py 1 <directory_path> <file_extension>")
            return
        file_extension = sys.argv[3]
        print_file_contents(directory_path, file_extension)
    elif script_number == 2:
        rename_files_with_prefix(directory_path)
    elif script_number == 3:
        calculate_total_size(directory_path)
    elif script_number == 4:
        count_files_by_extension(directory_path)
    else:
        print("Invalid script number. Choose a number between 1 and 4.")

if __name__ == "__main__":
    main()




# python lab6.py 1 ./Test/Aici .txt
# python lab6.py 2 ./Test/Aici 
# python lab6.py 2 ./Test/Aici 
# python lab6.py 2 ./Test/Aici 