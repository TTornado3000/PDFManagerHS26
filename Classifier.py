import pdfplumber
from pathlib import Path


class Classifier:

    def __init__(self, keywords):
        self.keywords = keywords

    def classify(self, file_path):
        file_name = Path(file_path).name

        for filename_beginning, data in self.keywords.items():
            if file_name.startswith(filename_beginning):
                if self.check_category_PDF(file_path, data["keywords"]):
                    print(f"matching file: ", file_name, filename_beginning)
                    return data["category"]
        return None

    def check_category_PDF(self, file_path, target_words):

        try:

            with pdfplumber.open(file_path) as pdf:
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
            print(f"Error processing {file_path}: {e}")

        return False
