from datetime import datetime
from pathlib import Path

def str2date(value: str) -> datetime:
    try:
        return datetime.strptime(value, "%d/%m/%Y")
    except:
        raise Exception(f"{value} não é uma data válida")

def get_pics_from_folder(folder: str | Path):
    pass