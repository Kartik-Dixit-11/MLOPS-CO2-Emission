from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Dataingestconfig:
    Source: Path
    Destination: Path

@dataclass(frozen=True)
class Model_Config:
    Test: Path
    Train:Path
    Load: Path
    mlflow_uri: str