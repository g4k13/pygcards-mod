import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygcards-pygdev",
    version="0.0.5",
    scripts=['pyg-blackjack'],
    author="pygdev",
    author_email="g4k13@github.com",
    description="A cards framework for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/g4k13/pygcards",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
