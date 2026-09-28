import os
import pdfplumber

import Organizer
from Watcher import Watcher


def classify():
    #looks through all the files in directory
    for file_name in os.listdir(Watcher.DIRECTORY_TO_WATCH):
        if not file_name.endswith(".pdf"):
            continue
        try:
            #loops each category
            for filename_beginning, data in keywords.items():
                #compares them with the current file
                if filename_beginning in file_name:
                    if check_Category_PDF(file_name, data["keywords"]):
                        print(f"matching file: ", file_name, filename_beginning)
                        return data["category"]

        except KeyboardInterrupt:
            print("Program closed")


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


keywords = {

    "dist": {
        "category": "Discrete Structures",
        "keywords": ["Discrete Structures", "Helmert"]
    },

    "sheet": {
        "category": "Discrete Structures",
        "keywords": ["Discrete Structures", "Helmert"]
    },

    "cs256": {
        "category": "Databases",
        "keywords": ["Databases", "cs256", "Schuldt"]
    },

    "Woche": {
        "category": "Software Engineering",
        "keywords": ["Software Engineering", "Schnider"]
    },

    "00_": {
        "category": "Scientific Computing",
        "keywords": ["Scientific Computing", "Linear Systems"]
    },

    "01_": {
        "category": "Scientific Computing",
        "keywords": ["Scientific Computing", "Linear Systems"]
    },
    "02_": {
        "category": "Scientific Computing",
        "keywords": ["Scientific Computing"]
    },
    "Serie": {
        "category": "Einführung in die Statistik",
        "keywords": ["Einführung in die Statistik"]
    },
    "PR": {
        "category": "Pattern Recognition",
        "keywords": ["Pattern Recognition", "Neurons"]
    }

}

classify()
