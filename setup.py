import os
import codecs

from setuptools import setup


current_dir = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(current_dir, "README.md"), encoding="utf-8") as readme:
    long_description = "\n" + readme.read()

with codecs.open(os.path.join(current_dir, "kitacrypto", "version.py")) as version:
    exec(version.read())

setup(
    name="kitacrypto",
    version=__version__,  # noqa: F821
    author="Alexandr Rutkovskij",
    author_email="kitanoyoru@protonmail.com",
    packages=["kitacrypto"],
    url="https://github.com/kitanoyoru/kitaCryptoCLI",
    licens="MIT",
    description="CLI app to see current cryptocurrencies' price.",
    long_description=long_description,
    zip_safe=True,
    python_requires=">=3.6",
)
