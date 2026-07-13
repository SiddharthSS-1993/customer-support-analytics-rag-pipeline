from pathlib import Path
from typing import Any

import yaml

def load_yaml_configuration(configuration_file_path: Path) -> dict[str: Any]:
    """Load and return configuration values from YAML file topython dictionary"""

    if not configuration_file_path.exists():
        raise FileNotFoundError(f"Configuration File not found: {configuration_file_path}")
    
    with configuration_file_path.open(mode="r",
                                      encoding="utf-8",
                                      ) as configuration_file:
        configuration_values = yaml.safe_load(configuration_file)

        if not configuration_values:
            raise ValueError(f"Configuration File in Empty: {configuration_file_path}")
        
        return configuration_values
    

