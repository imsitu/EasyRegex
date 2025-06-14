from pathlib import Path
from setuptools import setup, find_packages

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text()

setup(
    name="easyregex",
    version="0.1.0",
    description="Convert simple English phrases into regular expressions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["regex"],
)
