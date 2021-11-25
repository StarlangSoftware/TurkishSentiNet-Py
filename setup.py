from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-SentiNet',
    version='1.0.16',
    packages=['SentiNet'],
    url='https://github.com/StarlangSoftware/TurkishSentiNet-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish SentiNet',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={'': ['data/*.xml']},
)
