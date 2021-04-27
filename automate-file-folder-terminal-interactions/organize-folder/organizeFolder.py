import os
from pathlib import Path

# OUTPUT FORMAT OF THE DIRECTORY
SUB_FOLDERS = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def identifyFile(value):
    for cat, exts in SUB_FOLDERS.items():
        for ext in exts:
            if ext == value:
                return cat
    return 'MISC'

def organizeFolder():
    # SCANNING ALL THE FILES IN THE DIRECTORY
    for item in os.scandir():
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        folder = identifyFile(fileType)
        folderPath = Path(folder)
        if folderPath.is_dir() != True:
            folderPath.mkdir()
        # ORGANIZING FILES INTO SUB FOLDERS
        filePath.rename(folderPath.joinpath(filePath))

# MAIN FUNCTION
organizeFolder()
