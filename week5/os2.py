import os
from pathlib import Path

projectName = "templateProject"
listOfFiles = [
    ".github/workflows/.gitkeep",
    f"{projectName}/__init__.py",
    f"{projectName}/components/__init__.py",
    f"{projectName}/config/__init__.py",
    f"{projectName}/config/configure.py",
    f"{projectName}/pipeline/__init.py",
    f"{projectName}/entity/__init.py",
    f"{projectName}/constants/__init.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
]

for filepath in listOfFiles:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if(not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            