import pathlib
import re
from pathlib import Path

# This script changes img  HTML tags to ![[]]
# Useful to run after conversion of notes from One Note to markdown with Pandoc

RootFolder: Path = pathlib.Path("C:/Users/janek/Desktop/test")

FileList = list(RootFolder.rglob("*.md"))

for fileItem in FileList:
    print(fileItem)
    try:
        with open(fileItem, "r", encoding='utf-8') as File:
            FileContent = File.read()

            Images = re.findall("<img src=.* />", FileContent)

            for Image in Images:
                ImageSource = Image[10:]
                EndIndex = ImageSource.index('"')
                ImageSource = ImageSource[:EndIndex]
                ReplaceWith = "![[" + ImageSource + "]]"
                FileContent = FileContent.replace(Image, ReplaceWith)

    except Exception as error:
        print(f"error opening {fileItem}: {error}")
    try:
        with open(fileItem, "w", encoding='utf-8') as File:
            File.write(FileContent)
    except Exception as error:
        print(f"error writing {fileItem}: {error}")
