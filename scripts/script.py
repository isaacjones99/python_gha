import argparse
import os

from enum import Enum
from typing import Dict, Any, List

class Environment(Enum):
    STAGING = "staging"
    PRODUCTION = "production"


data = {
    "Status": "✅ Success",
    "Coverage": "85%",
    "Runtime": "12s"
}

def create_report():
    with open("report.md", "w") as f:
        f.write("### Python script results\n")
        f.write("| Metric | Values | \n")
        f.write("| :--- | :--- |\n")
        for key, value in data.items():
            f.write(f"| {key} | {value} |\n")

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