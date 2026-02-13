import os

value = "hello-from-python"

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write("result={value}\n")
