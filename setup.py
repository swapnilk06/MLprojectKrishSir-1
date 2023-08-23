## Writing the Setup Script
''' 
    The setup script is the centre of all activity in building, 
    distributing, and installing modules using the Distutils. 
    The main purpose of the setup script is to describe your module distribution to the Distutils, 
    so that the various commands that operate on your modules do the right thing.
'''
# application basic all info in setup.py



from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' # ignore -e . from requirements.txt
# automatically trigger setup.py - but this is not a package then ignore it write code in setup.py

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]  # replace '\n' as black "" - from requirements.txt
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='swapnil',
    author_email='swapnilkathale111@gmail.com',
    packages=find_packages(),
    #install_requires=['numpy','pandas'] 
    install_requires=get_requirements('requirements.txt') # automatics all requirements move in setup.py
)