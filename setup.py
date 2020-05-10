from setuptools import find_packages, setup

version = "0.0.2"
required = ["requests>=2.23.0"]

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="python_covid",
    version=version,
    description="Get data from covid cases",
    url="https://github.com/daviwesley/python-covid",
    author="Davi Wesley",
    author_email="wesley.sud7@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
