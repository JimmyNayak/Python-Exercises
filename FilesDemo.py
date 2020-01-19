from pathlib import Path

# path = Path("module")
# print(path.exists())

# dir_path = Path(input("Please enter directory name to create: "))
# if dir_path.exists():
#     print(f"{dir_path.name} is already exist")
# else:
#     dir_path.mkdir()
#     print(f"{dir_path.name} is created")


# dir_path = Path(input("Please enter directory name to remove: "))
# if dir_path.exists():
#     dir_path.rmdir()
#     print(f"{dir_path.name} is deleted")
# else:
#     print(f"{dir_path.name} is not exist")

# from click import File
#
# file_name = input("Please enter directory name to search: ")
# is_file_found = False
# file_data = File()
# dir_path = Path()
# for file in dir_path.glob('*.py'):
#     if file.name == file_name + '.py':
#         file_data = file
#         is_file_found = True
#         break
#
# if is_file_found:
#     print(f"{file_data.name} is found at {file_data.absolute()}")
# else:
#     print("File does not found")

path = Path()
for file in path.glob('*'):
    if file.is_dir():
        print(f"{file.name} is a directory.")
    else:
        print(f"{file.name} is a file.")
