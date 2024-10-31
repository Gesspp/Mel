class ProgramNotFoundError(Exception):
    def __init__(self, program_name: str):
        super().__init__(f"Программа {program_name} не найдена")


class DocumentNotOpenError(Exception):
    def __init__(self):
        super().__init__(f"Документ для работы не открыт")