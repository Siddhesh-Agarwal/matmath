from setuptools import setup, Extension
import sys

# Define the C extensions
extensions = [
    Extension(
        'matmath._vector',
        sources=['matmath/_vector.c'],
        extra_compile_args=[
            '/O2' if sys.platform == 'win32' else '-O3',
            '/fp:fast' if sys.platform == 'win32' else '-ffast-math',
        ],
    ),
    Extension(
        'matmath._matrix',
        sources=['matmath/_matrix.c'],
        extra_compile_args=[
            '/O2' if sys.platform == 'win32' else '-O3',
            '/fp:fast' if sys.platform == 'win32' else '-ffast-math',
        ],
    ),
]

setup(
    name='matmath',
    version='4.0.0',
    description='A simple and efficient module for matrix and vector manipulation with C extensions.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Siddhesh Agarwal',
    author_email='siddhesh.agarwal@gmail.com',
    url='https://github.com/Siddhesh-Agarwal/matmath',
    packages=['matmath'],
    ext_modules=extensions,
    python_requires='>=3.9,<4.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: C',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    keywords=['matrix', 'vector', 'math', 'linear algebra', 'algebra', 'matmath', 'cpython', 'performance'],
)
