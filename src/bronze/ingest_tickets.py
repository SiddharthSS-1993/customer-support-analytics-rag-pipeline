from pathlib import Path
import pandas as pd

support_tickets_raw_input = Path("data/raw/support_tickets.csv")
support_tickets_bronze_output = Path("data/processed/bronze_support_tickets.csv")


def ingest_tickets():
    if not support_tickets_raw_input.exists():
        raise FileNotFoundError(f"Raw file not found: {support_tickets_raw_input}")
    support_tickets = pd.read_csv(support_tickets_raw_input)

    support_tickets_bronze_output.parent.mkdir(parents=True, exist_ok=True)
    support_tickets.to_csv(support_tickets_bronze_output, index=False)

    print("Bronze ingestion completed.")
    print(f"Rows ingested: {len(support_tickets)}")
    print(f"Output written to {support_tickets_bronze_output}")




if __name__ == "__main__":
    ingest_tickets()