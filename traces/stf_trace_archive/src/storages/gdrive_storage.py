import pandas as pd
from storages.base import StorageHandler
from data.config import GDriveStorageConfig
from data.metadata import Metadata

class GDriveStorage(StorageHandler):
    def __init__(self, config: GDriveStorageConfig):
        if not config.path:
            raise ValueError("Storage path cannot be empty.")
        
        raise NotImplementedError();

    @property
    def traces_table(self):
        if self._traces_table is None:
            return self.update_traces_table()

        return self._traces_table

    @property
    def workloads_table(self):
        if self._workloads_table is None:
            return self.update_workloads_table()

        return self._workloads_table

    def update_traces_table(self) -> pd.DataFrame:
        raise NotImplementedError()

    def update_workloads_table(self) -> pd.DataFrame:
        raise NotImplementedError()

    def insert_workload(self, workload_path: str, workload_id: int) -> None:
        raise NotImplementedError()

    def insert_trace(self, trace_path: str, metadata: Metadata) -> None:
        raise NotImplementedError()

    def get_metadata(self, trace_id: str) -> Metadata:
        raise NotImplementedError()

    def save_metadata(self, trace_id: str, path: str) -> None:
        raise NotImplementedError()

    def save_trace(self, trace_id: str, path: str) -> None:
        raise NotImplementedError()

    def save_workload(self, workload_id: int, path: str) -> None:
        raise NotImplementedError()

    @staticmethod
    def setup() -> GDriveStorageConfig:
        raise NotImplementedError()
