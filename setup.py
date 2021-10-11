from setuptools import setup, find_packages

setup(
    name = "matmath",
    version = "v2.1.0",
    author = "Siddhesh Agarwal",
    author_email = "siddhesh.agarwal@gmail.com",
    description = "A simple and efficient module for matrix manipulation.",
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    license = "MIT",
    url = "https://github.com/Siddhesh-Agarwal/matmath",
    project_urls = {
        'Bug Tacker': 'https://github.com/Siddhesh-Agarwal/matmath/issues'
    },
    keywords = ["matmath", "math", "matrix", "matrices", "vector"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.6",
)
