 # setup.py
from setuptools import setup, find_packages

setup(
    name='lexer_gdscript',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        "pygments.lexers": [
            "gdscp = lexer_gdscript.gdscript:GDScriptLexer",
        ],
    },
    install_requires=[
        'Pygments',
    ],
)