from setuptools import setup, find_packages


setup(
    name='sc_scripts_demo',
    version='1.0',
    packages=find_packages(),
    scripts=[
        'bin/check_jobs.py',
    ],
    entry_points={
        'scrapy': ['settings = sc_scripts_demo.settings'],
    },
)
