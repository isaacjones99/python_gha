import argparse
import os

from enum import Enum
from typing import Dict, Any, List

class Environment(Enum):
    STAGING = "staging"
    PRODUCTION = "production"


new_topics = [
    "topic1",
    "topic2"
]

def create_report():
    with open("report.md", "w") as f:
        f.write("### Python script results\n")
        f.write("| New | Updated | Deleted | \n")
        f.write("| :--- | :--- | :--- |\n")
        for new_topic in new_topics:
            f.write(f"| {new_topic} | | |\n")

def run(environment: Environment):
    staging_topics = ["deploy.test.topic", "another.test.topic"]
    production_topics = ["production.topic", "another.production.topic"]

    # GitHub Actions step output
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"staging_matrix={staging_topics}\n")
        f.write(f"production_matrix={production_topics}\n")

    # Create report file
    create_report()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", default="staging")
    args = parser.parse_args()

    run(args.environment)