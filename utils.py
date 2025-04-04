import sys, os

def get_path(relative_path):
    """Получает корректный путь к файлу, работая и в .exe, и в исходном коде"""
    if hasattr(sys, '_MEIPASS'):  # Проверяем, существует ли атрибут
        base_path = sys._MEIPASS  # PyInstaller распаковывает файлы сюда
    else:
        base_path = os.path.abspath(".")  # Обычный запуск Python

    return os.path.join(base_path, relative_path)