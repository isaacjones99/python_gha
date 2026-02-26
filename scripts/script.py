import argparse
import json
import os

from enum import Enum
from typing import Dict, Any, List

class Environment(Enum):
    STAGING = "staging"
    PRODUCTION = "production"

def run(environment: Environment):
    topics = ["deploy.test.topic", "another.test.topic"]

    # GitHub Actions step output
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"matrix={topics}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", default="staging")
    args = parser.parse_args()

    print("::error::Topic deployment failed")
    print("::warning::Topic already exists")
    print("::notice::Deploying new topic")

    run(args.environment)