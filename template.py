import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s")
package_name="CNNClassifier"


list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/intigration/__init__.py",
    "configs/config.yaml",
    
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py"
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb", 
]

for filepath in list_of_files:
    path(filepath)