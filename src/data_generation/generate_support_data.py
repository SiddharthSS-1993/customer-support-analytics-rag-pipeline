from pathlib import Path
import random
from datetime import timedelta

import pandas as pd
from faker import Faker

OUTPUT_DIRECTORY = Path("data/generated/raw/")

CUSTOMER_COUNT = 2000
PRODUCT_COUNT = 100
AGENT_COUNT = 50
TICKET_COUNT = 10000

RANDOM_SEED = 42

fake_data_generator = Faker()
Faker.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

def create_customers(customer_count: int) -> pd.DataFrame:
    """Create synthetic Customer Master Data"""

    customer_records = []

    for customer_number in range(1, customer_count + 1):
        customer_records.append({
                "customer_id": f"C{customer_number:06d}",
                "customer_name": fake_data_generator.name(),
                "email_address": fake_data_generator.unique.email(),
                "country": fake_data_generator.country(),
                "customer_segment": random.choice(
                    ["Consumer", "Small Business", "Enterprise"]
                ),
                "registration_date": fake_data_generator.date_between(
                    start_date="-5y",
                    end_date="today",
                ),
            })
    return pd.DataFrame(customer_records)

def create_products(product_count: int) -> pd.DataFrame:
    """Create synthetic product reference data"""

    product_categories = ["Laptop",
                          "Mobile Application",
                          "Payments",
                          "Cloud Storage",
                          "Gaming"]
    product_records = []

    for product_number in range(1, product_count + 1):
        product_category = random.choice(product_categories)

        product_records.append(
            {
                "product_id": f"P{product_number:04d}",
                "product_name": f"{product_category} Product {product_number}",
                "product_category": product_category,
                "product_status": random.choice(["Active", "Active", "Active", "Retired"]),
            })
        
    return pd.DataFrame(product_records)
    
def create_agents(agent_count: int) -> pd.DataFrame:
    """Create synthetic support-agent reference data."""

    support_teams = [
        "Technical Support",
        "Billing Support",
        "Customer Care",
        "Escalations",
    ]

    agent_records = []

    for agent_number in range(1, agent_count + 1):
        agent_records.append(
            {
                "agent_id": f"A{agent_number:04d}",
                "agent_name": fake_data_generator.name(),
                "support_team": random.choice(support_teams),
                "experience_level": random.choice(
                    ["Junior", "Intermediate", "Senior"]
                ),
                "active_flag": random.choice([True, False]),
            }
        )

    return pd.DataFrame(agent_records)

def create_sla_policies() -> pd.DataFrame:
    """Create SLA targets for each ticket-priority level."""

    sla_policy_records = [
        {
            "priority": "Low",
            "first_response_target_hours": 24,
            "resolution_target_hours": 72,
        },
        {
            "priority": "Medium",
            "first_response_target_hours": 8,
            "resolution_target_hours": 48,
        },
        {
            "priority": "High",
            "first_response_target_hours": 4,
            "resolution_target_hours": 24,
        },
        {
            "priority": "Critical",
            "first_response_target_hours": 1,
            "resolution_target_hours": 8,
        },
    ]

    return pd.DataFrame(sla_policy_records)

def create_support_tickets(
    ticket_count: int,
    customers: pd.DataFrame,
    products: pd.DataFrame,
    agents: pd.DataFrame,
) -> pd.DataFrame:
    """Create synthetic support-ticket transactional data."""

    issue_categories = [
        "Login",
        "Payment",
        "Performance",
        "Application Crash",
        "Refund",
        "Hardware",
        "Account Access",
    ]

    priorities = ["Low", "Medium", "High", "Critical"]
    ticket_statuses = ["Open", "In Progress", "Resolved", "Closed"]

    customer_ids = customers["customer_id"].tolist()
    product_ids = products["product_id"].tolist()
    active_agent_ids = agents.loc[agents["active_flag"], "agent_id"].tolist()

    ticket_records = []

    for ticket_number in range(1, ticket_count + 1):
        created_timestamp = fake_data_generator.date_time_between(
            start_date="-1y",
            end_date="now",
        )

        ticket_status = random.choice(ticket_statuses)

        resolved_timestamp = None
        if ticket_status in {"Resolved", "Closed"}:
            resolved_timestamp = created_timestamp + timedelta(
                hours=random.randint(1, 120)
            )

        ticket_records.append(
            {
                "ticket_id": f"T{ticket_number:08d}",
                "customer_id": random.choice(customer_ids),
                "product_id": random.choice(product_ids),
                "assigned_agent_id": random.choice(active_agent_ids),
                "created_timestamp": created_timestamp,
                "resolved_timestamp": resolved_timestamp,
                "issue_category": random.choice(issue_categories),
                "priority": random.choice(priorities),
                "ticket_status": ticket_status,
                "ticket_text": fake_data_generator.sentence(nb_words=14),
            }
        )

    return pd.DataFrame(ticket_records)

def write_dataset(dataset: pd.DataFrame, file_name: str) -> None:
    """Write One generated dataset to the configured output directory"""

    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok = True)

    dataset.to_csv(OUTPUT_DIRECTORY / file_name, index=False)
    print(f"Created {file_name}: {len(dataset):,} records")

def generate_all_datasets() -> None:
    """Generate and store all customer support source datasets"""
    
    customers = create_customers(CUSTOMER_COUNT)
    products = create_products(PRODUCT_COUNT)
    agents = create_agents(AGENT_COUNT)
    sla_policies = create_sla_policies()
    
    tickets = create_support_tickets(ticket_count=TICKET_COUNT,
                                     customers=customers,
                                     products=products,
                                     agents=agents)
    
    write_dataset(customers, "customers.csv")
    write_dataset(products, "products.csv")
    write_dataset(agents, "agents.csv")
    write_dataset(sla_policies, "sla_policies.csv")
    write_dataset(tickets, "support_tickets.csv")

if __name__ == "__main__":
    generate_all_datasets()