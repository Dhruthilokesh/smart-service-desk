import json
from pathlib import Path


class FileRepository:
    def __init__(self, file_path="data/requests.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def load_all(self):
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

                if not data:
                    return []

                return data

        except json.JSONDecodeError:
            print("Warning: JSON file is empty or corrupted. Starting with no requests.")
            return []

    def save_all(self, requests):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(requests, file, indent=4)