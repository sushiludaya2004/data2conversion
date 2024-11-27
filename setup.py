from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_req(file_path:str)->List[str]:
    '''
    Function : Returns list of requirements
    '''
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

setup(
    name='Data2Conversion End-to-End MLOps Project',
    version='0.0.1',
    author='Sushil Udaya Kumar',
    packages=find_packages(),
    # Function to fetch the requirements from requirement.txt is defined above
    install_requires=get_req("requirements.txt")
)