import os
from setuptools import setup, find_packages

# PACKAGE NAME
PKGNAME = "heic_image_converter"

# ======================================================
# VERSION - CHANGE BEFORE RUNNING, PYPI WILL NOT UPLOAD
release = 1
feature = 0
update = 0
# ======================================================

V = f"{release}.{feature}.{update}"
print(f"[LOG] - Executing into version {V}")

AUTH = "John Gutierrez"
KEYWORDS = ['image', 'image-processing', 'heic', 'heic-to-png']
SHORT_DESCR = "Convert .HEIC Images!"


# Get CURRENT DIRECTORY
CURR_DIR = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
print("[LOG] - DIR FILES FOUND:")
for f in os.listdir(CURR_DIR):
    print(f"  [LOG] - {f}")


# Get contents of README file
README_FILENAME = "README.md"
README_PATH = os.path.join(CURR_DIR, README_FILENAME)
print(f"[LOG] - Searching for '{README_FILENAME}' in '{CURR_DIR}'")
with open(README_PATH, "r", encoding="utf-8") as readme:
    LONG_DESCR = readme.read()
    print(f"[LOG] - Found '{README_FILENAME}'")


# Get contents of REQUIREMENTS file
REQUIREMENTS = []
REQUIREMENTS_FILENAME = "requirements.txt"
REQUIREMENTS_PATH = os.path.join(CURR_DIR, REQUIREMENTS_FILENAME)
print(f"[LOG] - Searching for '{REQUIREMENTS_FILENAME}' in '{CURR_DIR}'")
with open(REQUIREMENTS_PATH, "r", encoding="utf-8") as req:
    lines = req.readlines()
    for line in lines:
        if line[0] != "#" and line.strip() != "":
            REQUIREMENTS.append(line.strip())
    print(f"[LOG] - Found '{REQUIREMENTS_FILENAME}'")


# SETUP
print("[LOG] - executing setup...")
setup(
    name=PKGNAME,
    version=V,
    author=AUTH,
    description=SHORT_DESCR,
    long_description=LONG_DESCR,
    long_description_content_type="text/markdown",
    url="https://github.com/XDwightsBeetsX/heic-image-converter",
    license="MIT",
    keywords=KEYWORDS,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=REQUIREMENTS,
    packages=find_packages(PKGNAME, "tests"),
    python_requires='>=3.8',
)
print("[LOG] - done.")
