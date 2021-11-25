import pathlib
from setuptools import setup

ROOT = pathlib.Path(__file__).parent

with open(ROOT / 'README.md', 'r', encoding='utf-8') as f:
    README = f.read()

setup(
    name='disnake-ext-menus',
    author='Rapptz, Kraots',
    url='https://github.com/Kraots/disnake-ext-menus',
    version='0.0.3',
    packages=['disnake.ext.menus'],
    description='An extension module to make reaction based menus with disnake',
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=['disnake'],
    python_requires='>=3.8.0'
)
