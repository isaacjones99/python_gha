import argparse
import os

from enum import Enum

class Environment(Enum):
    STAGING = "staging"
    PRODUCTION = "production"

def run(environment: Environment):
    print(f"{environment}")
    services = ["api", "worker", "scheduler"]

    # GitHub Actions step output
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"matrix={services}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", default="staging")
    args = parser.parse_args()

    run(args.environment)