from setuptools import setup, find_packages

setup(
    name = "matmath",
    version = "v0.0.1",
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
    keywords = ["matmaths", "math", "matrix", "matrices"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
    ],
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.6",
)
