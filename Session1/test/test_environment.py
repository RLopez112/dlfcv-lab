from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

# Course-critical packages: the notebooks depend directly on these, so we check
# them explicitly rather than requiring an exact match against the full `pip
# freeze` output. That approach broke for Linux/CUDA students (whose torch
# install pulls in extra `nvidia-*`/`triton` packages macOS never sees), used
# the PATH `pip` instead of the running interpreter, and relied on the
# deprecated `pkg_resources` API.
CRITICAL_PACKAGES = [
    "torch",
    "torchvision",
    "numpy",
    "matplotlib",
    "opencv-python",
    "scikit-image",
    "scikit-learn",
    "pytest",
]

# The repo-root requirements.txt, resolved relative to this file's location:
# Session1/test/test_environment.py -> parents[2] is the repo root.
REQUIREMENTS_PATH = Path(__file__).resolve().parents[2] / "requirements.txt"


def parse_pinned_versions(requirements_path):
    """Parse `name==version` pins from a requirements.txt file into a dict keyed by lowercase name."""
    pins = {}
    with open(requirements_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "==" not in line:
                continue
            name, _, ver = line.partition("==")
            pins[name.strip().lower()] = ver.strip()
    return pins


def test_environment_matches_requirements():
    """
    Check that the course-critical packages (CRITICAL_PACKAGES) are installed
    and match the versions pinned in the repo-root requirements.txt. Extra
    installed packages that are not in the curated list are tolerated.
    """
    pins = parse_pinned_versions(REQUIREMENTS_PATH)
    failures = []

    for package in CRITICAL_PACKAGES:
        expected = pins.get(package)
        if expected is None:
            failures.append(f"  - {package}: no pinned version found in {REQUIREMENTS_PATH}")
            continue
        try:
            installed = version(package)
        except PackageNotFoundError:
            failures.append(f"  - {package}: not installed (requirements.txt pins {expected})")
            continue
        if installed != expected:
            failures.append(f"  - {package}: installed {installed}, but requirements.txt pins {expected}")

    assert not failures, "Environment does not match requirements.txt:\n" + "\n".join(failures)


if __name__ == "__main__":
    try:
        test_environment_matches_requirements()
        print("✅ Environment matches requirements.txt")
    except AssertionError as e:
        print("❌ Environment check failed:")
        print(str(e))
