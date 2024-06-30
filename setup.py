from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    
    valid_requirements = []
    for requirement in requirements:
        requirement = requirement.strip()
        if not requirement.startswith('-e'):
            valid_requirements.append(requirement)
    
    return valid_requirements

setup(
    name='introProject',
    version='0.0.1',
    author="Ankit",
    author_email='ankitbarik03@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    # Add additional dependencies if needed
)
