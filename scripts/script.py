import json
import os

data = {
    "services": ["api", "worker", "scheduler"],
    "version": "1.2.3"
}

# Write to GITHUB_OUTPUT
with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"matrix={json.dumps(data['services'])}\n")
