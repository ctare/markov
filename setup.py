from setuptools import setup, find_packages
from markov import __author__, __version__, __license__

setup(
        name="ctare_markov_chain",
        version=__version__,
        description="Markov chain library.",
        license=__license__,
        author=__author__,
        author_email="sankaku9006221@gmail.com",
        url="https://github.com/ctare/markov.git",
        keywords="markov markov_chain python",
        packages=find_packages(),
        install_requires=[],
        )
