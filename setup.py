from setuptools import setup
from setuptools import find_namespace_packages

setup(
    

    # Define the library name, this is what is used along with `pip install`.
    name='text-to-speech',

    # Define the author of the repository.
    author='Khouw Devin N',

    # Define the Author's email, so people know who to reach out to.
    author_email='khouwdevin@gmail.com',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version='0.1.0',

    # I have a long description but that will just be my README
    # file, note the variable up above where I read the file.
    long_description=long_description,

    # This will specify that the long description is MARKDOWN.
    long_description_content_type="text/markdown",

    # Here is the URL where you can find the code, in this case on GitHub.
    url='https://github.com/khouwdevin/speech-to-text-python',

    # These are the dependencies the library needs in order to run.
    install_requires=[
        'speech_recognition',
        'moviepy.editor',
        'pyautogui',
        'keyboard'
    ],

    # Here are the keywords of my library.
    keywords='sigma coding, governments, finance, APIs',

    # here are the packages I want "build."
    # packages=find_namespace_packages(
    #    where=['sigma', 'sigma.*']
    # ),

    # # here we specify any package data.
    # package_data={

    #     # And include any files found subdirectory of the "td" package.
    #     "td": ["app/*", "templates/*"],

    # },

    # I also have some package data, like photos and JSON files, so
    # I want to include those as well.
    include_package_data=True,

    # Here I can specify the python version necessary to run this library.
    python_requires='>=3.7',
)