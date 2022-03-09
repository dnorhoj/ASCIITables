from setuptools import setup

setup(
    name='cooltables',
    version='0.0.3',
    author='dnorhoj',
    author_email='daniel.norhoj@gmail.com',
    description="A tool for easily making text tables in terminal from python lists.",
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    packages=["cooltables"],
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ]
)
