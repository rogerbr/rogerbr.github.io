from setuptools import setup, find_packages

setup(
    name='mkdocs_custom_lexer',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'custom_lexer = mkdocs_custom_lexer.plugin:CustomLexerPlugin',
        ],
    },
    install_requires=['mkdocs', 'pygments'],
)