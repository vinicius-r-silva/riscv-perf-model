import argparse
from abc import ABC, abstractmethod
from storages.storage_explorer import StorageExplorer


class CommandHandler(ABC):
    @abstractmethod
    def run(self, args: argparse.Namespace, database_explorer: StorageExplorer) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")
