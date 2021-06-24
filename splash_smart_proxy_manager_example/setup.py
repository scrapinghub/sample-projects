# Automatically created by: shub deploy
from setuptools import setup, find_packages

setup(
    name = 'project',
    version = '1.0',
    packages = find_packages(),
    package_data = {'splash_crawlera_example': ['scripts/*.lua',]},
    entry_points = {'scrapy': ['settings = splash_crawlera_example.settings']},
)
