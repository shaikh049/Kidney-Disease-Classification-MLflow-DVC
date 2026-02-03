# OS related operations ke liye module
# jaise folder banana, file check karna, etc.
import os

# Path ko OS-independent way me handle karne ke liye
from pathlib import Path

# Logging messages print karne ke liye (instead of print)
import logging


# logging ka basic configuration
# INFO level ke messages show honge
# format me time + message print hoga
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)


# Project ka main naam
# isi naam se src ke andar folder banega
project_name = 'cnnClassifier'


# Ye list un sab files aur folders ko define karti hai
# jo project structure me automatically create honge
list_of_files = [

    # GitHub workflows ke liye empty file
    ".github/workflows/.gitkeep",

    # src/cnnClassifier package
    f"src/{project_name}/__init__.py",

    # components module
    f"src/{project_name}/components/__init__.py",

    # utils module
    f"src/{project_name}/utils/__init__.py",

    # config module
    f"src/{project_name}/config/__init__.py",

    # configuration file
    f"src/{project_name}/config/configuration.py",

    # pipeline module
    f"src/{project_name}/pipeline/__init__.py",

    # entity module
    f"src/{project_name}/entity/__init__.py",

    # constants module
    f"src/{project_name}/constants/__init__.py",

    # project level config file
    "config/config.yaml",

    # DVC pipeline file
    "dvc.yaml",

    # model parameters file
    "params.yaml",

    # Python dependencies list
    "requirements.txt",

    # setup.py for packaging
    "setup.py",

    # research notebook
    "research/trials.ipynb",

    # HTML template
    "templates/index.html"
]


# Har file path ke liye loop chalega
for filepath in list_of_files:

    # filepath ko Path object me convert kar rahe hain
    filepath = Path(filepath)

    # path ko directory aur filename me split kar rahe hain
    filedir, filename = os.path.split(filepath)


    # Agar directory empty nahi hai
    # matlab folder create karna padega
    if filedir != "":
        # directory create karo
        # exist_ok=True => agar already hai to error nahi aayega
        os.makedirs(filedir, exist_ok=True)

        # logging message
        logging.info(
            f"Creating directory; {filedir} for the file: {filename}"
        )


    # Agar file exist nahi karti
    # ya exist karti hai but size 0 hai (empty file)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        # file ko write mode me open karo
        # empty file create ho jayegi
        with open(filepath, "w") as f:
            pass  # kuch likh nahi rahe, sirf empty file

            # logging message
            logging.info(f"Creating empty file: {filepath}")


    # Agar file already exist karti hai aur empty nahi hai
    else:
        logging.info(f"{filename} is already exists")
