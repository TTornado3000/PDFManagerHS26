import os
import pdfplumber
from Watcher import Watcher


def classify():
    #looks through all the files in directory
    for file_name in os.listdir(Watcher.DIRECTORY_TO_WATCH):
        if not file_name.endswith(".pdf"):
            continue
        try:
            #loops each category
            for category, target_words in keywords.items():
                #compares them with the current file
                if category in file_name:
                    if check_Category_PDF(file_name, target_words):
                        print(f"matching file: ", file_name)
                        break

        except KeyboardInterrupt:
            print("failed")


def check_Category_PDF(file_name, target_words):
    full_path = os.path.join(Watcher.DIRECTORY_TO_WATCH, file_name)
    try:
        with pdfplumber.open(full_path) as pdf:
            if not pdf.pages:
                return False

            first_page = pdf.pages[0]
            text = first_page.extract_text()

            #when text is not empty
            if text:
                for word in target_words:
                    if word in text:
                        return True

    except Exception as e:
        print(f"Error processing {file_name}: {e}")
    return False


keywords = {"dist": ["Discrete Structures", "Helmert"],
            "sheet": ["Discrete Structures", "Helmert"],
            "cs256": ["Databases", "cs256", "Schuldt"],
            "Woche": ["Software Engineering", "Schnider"],
            "00_": ["Linear Systems", "Equation"],
            "01_": ["Linear Systems", "Equation"],
            "02_": ["Linear Systems"],
            "Serie": ["Einführung in die Statistik"],
            "PR": ["Pattern Recognition", "Neurons"]}
classify()
