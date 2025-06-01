from setuptools import find_packages, setup

setup(
    name="clio_sdk",
    version="0.1.0",
    description="Unified models and adapters for Clio integrations",
    author="Your Name or Org",
    packages=find_packages(include=["clio_sdk", "clio_sdk.*"]),
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0",
        # add other dependencies if needed
    ],
)
