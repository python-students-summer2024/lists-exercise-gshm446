# setup.py
from setuptools import setup, find_packages

setup(
    name='mood_assessor',
    version='0.1',
    packages=find_packages(),
    install_requires=["datetime"],  # 这里列出任何依赖项
)