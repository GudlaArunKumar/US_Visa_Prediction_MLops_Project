from dataclasses import dataclass 


@dataclass
class DataIngestionArtifact:

    # storing the generated artifacts file paths
    train_file_path: str 
    test_file_path: str