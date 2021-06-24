# Automatically created by: shub deploy
from setuptools import setup, find_packages

setup(
    name = 'project',
    version = '1.0',
    packages = find_packages(),
    package_data = {'splash_smart_proxy_manager_example': ['scripts/*.lua',]},
    entry_points = {'scrapy': ['settings = splash_smart_proxy_manager_example.settings']},
)
