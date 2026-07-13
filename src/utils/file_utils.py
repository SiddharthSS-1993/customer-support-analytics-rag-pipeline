from pathlib import Path

import pandas as pd

def read_csv_file(input_file_path: Path) -> pd.DataFrame:
    """Reads a CSV file and returns a pandas DataFrame"""

    if not input_file_path.exists():
        raise FileNotFoundError(f"Input file notfound: {input_file_path}")
    
    return pd.read_csv(input_file_path)

def write_csv_file(dataset: pd.DataFrame,
                   output_file_path: Path) -> None:
    """Write a dataframe to csv and create its parent directory if required"""
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(output_file_path, index=False)

    
    