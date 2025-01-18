import pathlib
from setuptools import setup
from setuptools import find_packages

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Prarthana-102383015",
    version="1.0.0",
    description="TOPSIS Implementation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/prarthana127/Topsis-Prarthana-102383015",
    author="Prarthana Samal",
    author_email="psamal_be22@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "topsis=Topsis.__main__:main", 
        ],
    },
)