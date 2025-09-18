from typing import Type, Dict
from storages.local_storage import LocalStorage
from storages.gdrive_storage import GDriveStorage

STORAGE_TYPE_MAP: Dict[str, Type] = {
    "local-storage": LocalStorage,
    "gdrive-storage": GDriveStorage,
}
