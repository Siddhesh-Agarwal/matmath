from setuptools import setup, find_packages

setup(
    name="matmath",
    version="v3.0.0",
    author="Siddhesh Agarwal",
    author_email="siddhesh.agarwal@gmail.com",
    description="A simple and efficient module for matrix and vector manipulation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Siddhesh-Agarwal/matmath",
    project_urls={
        "Bug Tracker": "https://github.com/Siddhesh-Agarwal/matmath/issues"
    },
    keywords=["matrix", "matrices", "vector", "vectors"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    packages=find_packages(),
    package_data={"matmath": ["py.typed"]},
    include_package_data=True,
)
