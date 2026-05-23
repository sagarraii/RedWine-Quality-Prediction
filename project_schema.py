import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s'
)

project_name = "data_science_project"

list_of_files = [
    ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",

    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]

for file_path in list_of_files:

    file_path = Path(file_path)

    filedir = file_path.parent

    if filedir != Path(""):

        os.makedirs(filedir, exist_ok=True)

        logging.info(f"Creating directory: {filedir}")

    if (not file_path.exists()) or (file_path.stat().st_size == 0):

        with open(file_path, "w"):
            pass

        logging.info(f"Creating empty file: {file_path}")

    else:

        logging.info(f"{file_path} already exists")