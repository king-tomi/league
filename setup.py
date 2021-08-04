from os import name
from setuptools import setup, find_packages
import pathlib

#home directory
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="league-maker",
    version="1.0.0",
    description="create new league, team, player and fixtures with ease",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/king-tomi/league",
    author="Ayodabo Tomisin",
    authro_email="ayodabooluwatomisin@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Oprerating System :: OS Independent",
    ],
    packages = ["league","team","player","fixture"],
    include_package_data=True,
    install_requires=["pandas"]
)