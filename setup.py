from setuptools import setup, find_packages

setup(
    name="tasky",            
    version="1.0.7",                     
    author="Werichu",                    
    author_email="........",           
    description="Gestor de tareas CLI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Werichu/tasky",
    packages=find_packages(),       
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'tasky = tasky.main:main',
        ],
    },
)