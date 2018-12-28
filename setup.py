import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "timelib",
    version = "0.0.1",
    author = "Woody Allen Montilus",
    author_email = "thewamcoding@gmail.com",
    description = "A library made to inform about run time",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/pypa/sampleproject",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)