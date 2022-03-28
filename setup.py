import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="lazop-sdk",
    packages=["lazop_sdk"],
    version="1.0.2",
    description="Lazada Official SDK",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PsKs/lazop-sdk",
    author="Pongsakorn",
    author_email="pongsakorn.psks@gmail.com",
    license="README.md",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["requests"],
)
