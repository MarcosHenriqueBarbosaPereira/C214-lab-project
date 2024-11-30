from typing import Dict

from c214_lab_project.domain.entities.file import File


class FileMapper:
    @staticmethod
    def to_dict(file: File) -> Dict:
        return {
            "id": file.id,
            "name": file.name,
            "filesize": file.size,
            "filepath": str(file.filepath),
            "owner": file.owner,
        }
