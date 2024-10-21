from docx import Document
from pathlib import Path


class WordExecutor:
    def __init__(self):
        self._command_map = {
            "new_document" : self._word_new_document
        }

    def execute(self, command: str, *args):
        if command not in self._command_map:
            raise Exception(f"Команда {command} не найдена")
        return self._command_map[command](*args)


    def _word_new_document(self, file_name: str):
        path = (Path.home() / "Desktop" / f"{file_name}.docx")
        self.doc_name = str(path)
        self.doc = Document()
        self.doc.save(self.doc_name)

    def _word_new_paragraph(self, text: str):
        self.doc.add_paragraph(text)
        self.doc.save(self.doc_name)
