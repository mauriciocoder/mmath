
from setuptools import setup

config = {
        'description': 'Math functions for statistics',
        'author': 'Mauricio Bonetti',
        'url': 'URL',
        'download_url': 'WHERE TO DOWNLOAD IT',
        'author_email': 'nfoti@uw.edu',
        'version': '0.0.1',
        'install_requires': [],
        'packages': ['mmath'],
        'scripts': [],
        'name': 'mmath'
}

# Add in any extra build steps for cython, etc.

setup(**config)
