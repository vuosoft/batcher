import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="batcher", 
    version="0.0.2",
    author="Tero Vaalavuo",
    author_email="tero.vaalavuo@gmail.com",
    description="A utility tool to pack arrays of records to batches",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vuosoft/batcher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)