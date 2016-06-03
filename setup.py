from setuptools import setup, find_packages

setup(
    name='SlackPy',
    version='1.0.1',

    install_requires=[
        'slackclient',
        'requests',
        'flask',
        'oauth2client',
        'PyYaml',
        'gspread'
    ],



    author='Julio Nunez',
    license='MIT',
)
