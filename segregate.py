import os
from os.path import splitext, join
from shutil import move
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
document_extensions = {".doc": "Word Documents", ".docx": "Word Documents", ".odt": "Word Documents", ".pdf": "PDFs", ".xls": "Excel Files", ".xlsx": "Excel Files", ".ppt": "Presentations", ".pptx": "Presentations", ".txt": "Text Files"}
application_extensions = {".exe": "Executable Files"}
setup_extensions = {".msi": "Installer Files"}
programming_files_extensions = {".c": "C Source Files", ".cpp": "C++ Source Files", ".java": "Java Source Files", ".py": "Python Scripts", ".cs": "C# Source Files", ".html": "HTML Files", ".css": "CSS Files", ".js": "JavaScript Files", ".php": "PHP Files", ".rb": "Ruby Scripts", ".pl": "Perl Scripts", ".swift": "Swift Scripts", ".go": "Go Source Files", ".lua": "Lua Scripts", ".ts": "TypeScript Files", ".sh": "Shell Scripts", ".vb": "Visual Basic Files", ".sql": "SQL Files", ".json": "JSON Files", ".xml": "XML Files", ".yaml": "YAML Files", ".ini": "INI Files", ".cfg": "Configuration Files", ".yml": "YAML Files", ".properties": "Properties Files"}

check_type = [1, 1, 1, 1, 1, 1, 1, 1]
custom_directories = {}

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def segregate_files_by_extension(directory):
    files_found = False

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            extension = splitext(file)[1].lower()
            files_found = True

            if file in custom_directories:
                create_directory(join(directory, custom_directories[file]))
                move(file_path, join(directory, custom_directories[file], file))
            elif extension in image_extensions and check_type[0] == 1:
                create_directory(join(directory, "Images"))
                move(file_path, join(directory, "Images", file))
            elif extension in video_extensions and check_type[1] == 1:
                create_directory(join(directory, "Videos"))
                move(file_path, join(directory, "Videos", file))
            elif extension in audio_extensions and check_type[2] == 1:
                create_directory(join(directory, "Audios"))
                move(file_path, join(directory, "Audios", file))
            elif extension in document_extensions and check_type[3] == 1:
                document_subdir = document_extensions[extension]
                create_directory(join(directory, "Documents", document_subdir))
                move(file_path, join(directory, "Documents", document_subdir, file))
            elif extension in programming_files_extensions and check_type[4] == 1:
                document_subdir = programming_files_extensions[extension]
                create_directory(join(directory, "Documents", document_subdir))
                move(file_path, join(directory, "Documents", document_subdir, file))
            elif extension in application_extensions and check_type[5] == 1:
                create_directory(join(directory, "Applications"))
                move(file_path, join(directory, "Applications", file))
            elif extension in setup_extensions and check_type[6] == 1:
                create_directory(join(directory, "Setups"))
                move(file_path, join(directory, "Setups", file))
            else:
                if check_type[7] == 1 and extension not in image_extensions \
                        and extension not in video_extensions \
                        and extension not in audio_extensions \
                        and extension not in document_extensions \
                        and extension not in programming_files_extensions \
                        and extension not in application_extensions \
                        and extension not in setup_extensions:
                    create_directory(join(directory, "Others"))
                    move(file_path, join(directory, "Others", file))

    if not files_found:
        print("No files found in the directory.")

def sort_files():
    directory = input("Enter directory path: ")
    if os.path.exists(directory):
        segregate_files_by_extension(directory)
        print("Files segregated and moved successfully.")
    else:
        print("The given directory does not exist.")

class MoverHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def on_modified(self, event):
        if event.is_directory:
            return
        segregate_files_by_extension(self.directory)

def sort_files_continuous(directory):
    observer = Observer()
    observer.schedule(MoverHandler(directory), path=directory, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def collapse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            move(file_path, directory)

            
# we can either run this file by uncommenting this or use the interface file to make it simple

# if __name__ == "__main__":
#     choice = input("Enter 'once' to sort files once or 'continuous' for continuous sorting: ")
#     if choice.lower() == 'once':
#         sort_files()
#     elif choice.lower() == 'continuous':
#         directory = input("Enter directory path to continuously monitor and sort: ")
#         if os.path.exists(directory):
#             sort_files_continuous(directory)
#         else:
#             print("The given directory does not exist.")
#     else:
#         print("Invalid choice.")
