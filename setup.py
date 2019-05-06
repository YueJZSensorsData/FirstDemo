import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yuejzDemo",
    version="0.0.1",
    author="YueJZ",
    author_email="yuejianzhong@sensorsdata.cn",
    description="This is my demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=['SADemo'],
)