import os
import pdfplumber
from Watcher import Watcher


def classify():
    for file_name in os.listdir(Watcher.DIRECTORY_TO_WATCH):

        try:
            if keyboard_filename in file_name and file_name.endswith(".pdf"):
                lookInside(file_name)

        except KeyboardInterrupt:
            print("failed")


def lookInside(file_name):
    full_path = os.path.join(Watcher.DIRECTORY_TO_WATCH, file_name)
    try:
        with pdfplumber.open(full_path) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()

            if text:
                if keyboard_content in text:
                    print("success")

    except KeyboardInterrupt:
        print("Interrupted by Keyboard")


keyboard_filename = "dist"
keyboard_content = "Discrete Structures"
classify()
