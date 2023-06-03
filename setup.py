from setuptools import setup, find_packages

setup(
    name='HunterPass',
    version='0.0.1',
    author='Rafael Macedo',
    description='teste',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hp=HunterPass.main:main',
            # Defina o nome do comando e qual função será executada ao chamá-lo
        ]
    }
)
