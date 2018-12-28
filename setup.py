import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = "timelibWAM",
    version = "0.0.1",
    author = "Woody Allen Montilus",
    author_email = "thewamcoding@gmail.com",
    description = "A library made to inform about run time",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/theWAM/timelib.git",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
