import argparse
import itertools

from enum import Enum
from typing import Set

class Environment(Enum):
    STAGING = "staging"


class Deployer:
    def __init__(self, environment: Environment, report: bool = False) -> None:
        self.environment = environment
        self.report = report
        print(f"{report=}")

    def find_new_resources(self) -> Set:
        return {
            "topic1",
            "topic2",
            "topic3",
        }

    def run(self):
        self.new_resources = self.find_new_resources()

        if self.report:
            self.create_report()

    def create_report(self):
        print(f"report_{environment.value}.md")
        with open(f"report_{environment.value}.md", "w") as f:
            f.write(f"### {environment.value.capitalize()}\n\n")
            f.write("| New Topics |\n")
            f.write("| :--- |\n")

            for n in itertools.zip_longest(self.new_resources, fillvalue=""):
                f.write(f"| {n} |\n")
        

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Discover and deploy Kafka Connect connectors"
    )

    parser.add_argument(
        "--environment",
        choices=[e.value for e in Environment],
        required=True,
        help="Target environment (staging|production)",
    )

    parser.add_argument(
        "--report",
        help="Create an asset report",
        action="store_true",
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    environment = Environment(args.environment)