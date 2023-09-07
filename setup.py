from setuptools import find_packages, setup

from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
    requirements = [requirement.replace('\n', '') for requirement in requirements]
    if '-e .' in requirements:
        requirements.remove('-e .')
        
setup(
    name="CCP",
    version="0.0.1",
    author="Samarjeet",
    author_email="chhabrasamarjeetsingh@gmail.com",
    packages=find_packages(),
    install_requires=[],
)