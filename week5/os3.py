import os
from pathlib import Path

projectName = "MEOW"
listOfFiles = [
    ".github/workflows/.gitkeep",
    f"{projectName}/__init__.py",
    f"{projectName}/input/__init__.py",
    f"{projectName}/input/data.csv",
    f"{projectName}/src/__init__.py",
    f"{projectName}/src/train.py",
    f"{projectName}/src/predict.py",
    f"{projectName}/src/model_selection.py",
    f"{projectName}/src/tune_model.py",
    f"{projectName}/src/utils.py",
    f"{projectName}/models/model1.py",
    f"{projectName}/models/model2.py",
    f"{projectName}/notebooks/exploration.ipynb",
    f"{projectName}/README.md",
]

for filepath in listOfFiles:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if(not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            