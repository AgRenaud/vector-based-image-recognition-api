import subprocess


def test():
    subprocess.run(
        ["python", "-m", "coverage", "run", "-m", "unittest", "discover"]
    )

def report():
    subprocess.run(
        ["python", "-m", "coverage", "report"]
    )

def format():
    subprocess.run(
        ["black", "app"]
    )
