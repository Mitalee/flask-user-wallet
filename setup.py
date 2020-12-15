import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = "0.0.1"
homepage = "https://github.com/python-amazon-mws/python-amazon-mws"

setuptools.setup(
    name="flask-user-wallet", # Replace with your own username
    version="0.0.1",
    author="Mitalee Mulpuru",
    author_email="mitalee@khaata.in",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)