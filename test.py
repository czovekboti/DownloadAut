import automation
import os
# check if file exists
def contains_file(directory, filename):
    # Construct the full file path
    file_path = os.path.join(directory, filename)
    # Check if the file exists
    return os.path.isfile(file_path)

test = os.path.expanduser("~/Test")
if not os.path.exists(test):
    os.makedirs(test)
file_names = [ 'test2.exe','test1.txt','test3.pdf']
with open(os.path.join(test,file_names[1]), 'w') as file:
    pass
with open(os.path.join(test, file_names[0]) ,'wb') as file:
    pass
with open(os.path.join(test, file_names[2] ),'wb') as file:
    pass

automation.organizeFiles(test)
#list of folders in Test
folders = os.listdir(test)
asserted_names = ["Executables", "Text Files", "PDFs" ]
# Get list of created folders
folders = os.listdir(test)

# Check if folders were created
for asserted_name in asserted_names:
    assert asserted_name in folders, f"Folder '{asserted_name}' was not created"
# Loop through folders to check for correct files
for folder_name in asserted_names:
    folder_path = os.path.join(test, folder_name)
    # List files in the current folder
    folder_files = os.listdir(folder_path)
    # Check if the right file is in the right folder
    if folder_name == "Executables":
        assert any(file.endswith('.exe') for file in folder_files), f"No .exe file found in '{folder_path}'"
    elif folder_name == "Text Files":
        assert any(file.endswith('.txt') for file in folder_files), f"No .txt file found in '{folder_path}'"
    elif folder_name == "PDFs":
        assert any(file.endswith('.pdf') for file in folder_files), f"No .pdf file found in '{folder_path}'"

print("All assertions passed.")