from setuptools import setup

setup(
    name='tracker',
    version='0.1',
    py_modules=['main'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'tracker=main:main',
        ],
    },
)