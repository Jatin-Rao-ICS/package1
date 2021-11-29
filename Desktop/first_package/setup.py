from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Package for our Project'
LONG_DESCRIPTION = 'ML Powered test case generation'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ML Powered test case generation", 
        version=VERSION,
        author="Vaibhav Kulkarni",
        #author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Software Engineers",
            "Programming Language :: Python :: 3",
            # "Operating System :: MacOS :: MacOS X",
            # "Operating System :: Microsoft :: Windows",
        ]
)