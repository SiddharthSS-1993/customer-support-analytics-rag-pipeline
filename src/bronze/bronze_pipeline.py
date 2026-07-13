from pathlib import Path
from typing import Any

from src.utils.config_utils import load_yaml_configuration
from src.utils.file_utils import read_csv_file, write_csv_file
from src.utils.logger import create_logger

CONFIGURATION_FILE_PATH = Path("config/bronze_config.yaml")

bronze_pipeline_logger = create_logger("BronzePipeline")

def ingest_dataset(dataset_name: str,
                   raw_data_directory: Path,
                   bronze_output_directory: Path) -> int:
    """Ingest One Raw CSV into the Bronze Layer
       Returns number of Records written to the Bronze layer.
    """

    input_file_path = raw_data_directory / f"{dataset_name}.csv"
    output_file_path = bronze_output_directory / f"{dataset_name}.csv"

    bronze_pipeline_logger.info(f"Starting Ingestion for Dataset {dataset_name}")

    raw_dataset = read_csv_file(input_file_path=input_file_path)

    write_csv_file(dataset=raw_dataset,
                   output_file_path=output_file_path)
    
    record_count = len(raw_dataset)

    bronze_pipeline_logger.info(f"Completed ingestion of dataset {dataset_name} | \
                                 Records: {record_count}, | Output: {output_file_path}")


    return record_count

def run_bronze_pipeline() -> None:
    """Load configuration and ingest all configured datasets"""

    
    bronze_pipeline_logger.info("Bronze Pipeline Started")

    configuration_values: dict[str, Any] = load_yaml_configuration(configuration_file_path \
                                                                   =CONFIGURATION_FILE_PATH)
    
    raw_data_directory = Path(configuration_values["RAW_DATA_DIRECTORY"])

    bronze_output_directory = Path(configuration_values["BRONZE_OUTPUT_DIRECTORY"])

    dataset_names = configuration_values["datasets"]

    total_record_count = 0
    successful_dataset_count = 0

    for dataset_name in dataset_names:
        try:
            record_count = ingest_dataset(dataset_name=dataset_name,
                                          raw_data_directory=raw_data_directory,
                                          bronze_output_directory=bronze_output_directory)
            total_record_count += record_count
            successful_dataset_count += 1

        except Exception as e:
            bronze_pipeline_logger.exception(f"Ingestion failed for dataset {dataset_name}") 

    bronze_pipeline_logger.info(f"Bronze Pipeline Completed | Successful datasets: \
                                {str(successful_dataset_count)} out of {str(len(dataset_names))} | \
                                Total records: {str(total_record_count)}")
    
if __name__ == "__main__":
        run_bronze_pipeline()





    