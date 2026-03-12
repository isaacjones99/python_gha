import argparse
import os
import itertools # Added for handling mismatched list lengths
from enum import Enum
import json

class Environment(Enum):
    STAGING = "staging"
    PRODUCTION = "production"

new_topics = ["topic1", "topic2"]
updated_topics = ["Updated1", "Updated2", "Updated3"]
deleted_topics = ["Deleted1", "Deleted2", "Deleted3", "Deleted4"]

def create_report(environment: Environment):
    with open(f"report_{environment.value}.md", "w") as f:
        f.write(f"### {environment.value.capitalize()}\n\n")
        f.write("| New Topics | Updated Topics | Deleted Topics |\n")
        f.write("| :--- | :--- | :--- |\n")

        for n, u, d in itertools.zip_longest(new_topics, updated_topics, deleted_topics, fillvalue=""):
            f.write(f"| {n} | {u} | {d} |\n")

def run(environment: Environment):
    staging_topics = ["deploy.test.topic", "another.test.topic"]
    production_topics = ["production.topic", "another.production.topic"]

    instance_connector = {
        "mongodb": [
            "connector1",
            "connector2",
        ],
    }

    matrix = [
        {"instance": instance, "connector": connector}
        for instance, connectors in instance_connector.items()
        for connector in connectors
    ]

    # GitHub Actions step output
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            # f.write(f"staging_matrix={staging_topics}\n")
            # f.write(f"production_matrix={production_topics}\n")
            f.write(f"object_matrix={json.dumps(matrix)}")

    # Create report file
    create_report(Environment.STAGING)
    create_report(Environment.PRODUCTION)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", default="staging") # Added -- for proper flag parsing
    args = parser.parse_args()

    run(args.environment)