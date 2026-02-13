import os
import json

data = {
    "services": ["api", "worker", "scheduler"],
    "version": "1.2.3"
}
json_value = json.dumps(data["services"])

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"result={json_value}\n")
