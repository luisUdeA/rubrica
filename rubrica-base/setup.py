import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'rubrica'
AUTHOR = 'Luis Felipe Bustamante Narváez'
AUTHOR_EMAIL = 'ingenierolfbn@gmail.com'
URL = 'https://github.com/luisUdeA/rubrica.git'

LICENSE = 'MIT'
DESCRIPTION = 'Librería para calificar proyectos de Python'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'pandas',
      'numpy'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)