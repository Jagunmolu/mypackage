from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    install_requires=["numpy", "pandas"],
    url="https://github.com/Jagunmolu/mypackage",
    author="Jagunmolu",
    author_email="kolawolejonathan@gmail.com"
)