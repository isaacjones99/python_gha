import argparse
import json
import os

from enum import Enum
from typing import Dict, Any, List

class Environment(Enum):
    STAGING = "staging"
    PRODUCTION = "production"

def normalize_topics(topics: List[Dict[str, Any]]):
    matrix = []
    for topic in topics:
        matrix[topic["topic_name"]] = topic
    return [matrix]

def run(environment: Environment):
    topics = [
        {
            "topic_name": "deploy.test.topic",
            "partitions_count": "3",
            "replication_factor": "3",
            "configs": [
                {
                    "name": "min.insync.replicas",
                    "value": "2"
                },
                {
                    "name": "message.timestamp.before.max.ms",
                    "value": "9223372036854775807"
                },
                {
                    "name": "message.timestamp.after.max.ms",
                    "value": "9223372036854775807"
                },
                {
                    "name": "cleanup.policy",
                    "value": "compact"
                }
            ]
        },
    ]

    # GitHub Actions step output
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"matrix={json.dumps(normalize_topics(topics))}")

    # print(normalize_topics(topics))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", default="staging")
    args = parser.parse_args()

    run(args.environment)