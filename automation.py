import os 
import shutil
#folder to be organized
downloads_folder = os.path.expanduser("~/Downloads")
# list of file types
folder_types = {
     ".pdf": "PDFs",
    ".exe": "Executables",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".txt": "Text Files",
    ".doc": "Documents",
    ".docx": "Documents",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".zip": "Archives",
    ".rar": "Archives",
    ".mp3": "Music",
    ".mp4": "Videos",

}
# organization function
def organizeFiles(folderPath):
    # list of files in folder
    files = os.listdir(folderPath)
    for file_name in files:
            file_path = os.path.join(folderPath, file_name)
            if os.path.isdir(file_path):
                continue
            # get file extension
            file_extension = os.path.splitext(file_name)[1].lower()
            # Determine the destination folder based on the file extension 
            destination_folder_name = folder_types.get(file_extension, "Others") # if extension is not found put it in 'others'
            destination_folder_path = os.path.join(folderPath,destination_folder_name)
            # if folder doesn't exist create it
            if not os.path.exists(destination_folder_path):
                 os.makedirs(destination_folder_path)
            # move file to folder
            shutil.move(file_path, os.path.join(destination_folder_path, file_name))


organizeFiles(downloads_folder)