import json
import os

services = ["api", "worker", "scheduler"]

# GitHub Actions step output
with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    # f.write(f"matrix={json.dumps(services)}\n")
    f.write(f"matrix={services}")
