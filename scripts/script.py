import argparse
import json
import os

from enum import Enum
from typing import Dict, Any, List

class Environment(Enum):
    STAGING = "staging"
    PRODUCTION = "production"

def run(environment: Environment):
    staging_topics = ["deploy.test.topic", "another.test.topic"]
    production_topics = ["production.topic"]

    # GitHub Actions step output
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        # f.write(f"staging_matrix={staging_topics}")
        f.write(f"production_matrix={production_topics}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", default="staging")
    args = parser.parse_args()

    run(args.environment)