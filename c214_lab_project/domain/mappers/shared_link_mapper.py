from typing import Dict

from c214_lab_project.domain.entities.shared_link import SharedLink


class SharedLinkMapper:
    @staticmethod
    def to_dict(shared_link: SharedLink) -> Dict:
        return {
            "id": shared_link.id,
            "permissions": shared_link._props["permissions"],
            "file": shared_link.file,
            "shared_by": shared_link.shared_by,
        }
