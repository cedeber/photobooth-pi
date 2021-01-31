import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="photobooth-pi",
    version="0.0.1",
    author="Cédric Eberhardt",
    author_email="hello+code@cedeber.fr",
    description=("Photobooth Pi"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    # license="MIT",
    # keywords = "some keywords",
    # url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "gpiozero",
        "numpy",
        "Pillow",
        "RPi.GPIO",
        "spidev",
        "picamera",
        "opencv-python"
    ],
)
