from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    readme = f.read()

setup(
    name='beets_mosaic',
    version='0.9.0',
    description='Plugin for the music library manager Beets. The mosaic plugin generates a montage of a mosiac from cover art.',
    long_description=readme,
    url='https://github.com/susannamaria/beets-mosaic',
    download_url='https://github.com/SusannaMaria/beets-mosaic.git',
    author='Susanna Maria Hepp',
    author_email='susanna@olsoni.de',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='beets mosaic',
    packages=['beetsplug'],
    install_requires=['beets>=1.4.3','Pillow','Parse','TTFQuery>=2.0.0b1', 'fontTools', 'requests'],
)

