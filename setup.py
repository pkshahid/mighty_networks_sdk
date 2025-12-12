"""
Setup configuration for Mighty Networks SDK
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mighty-networks-sdk",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A production-ready Python SDK for the Mighty Networks API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mighty-networks-sdk",
    packages=find_packages(exclude=["tests", "examples", "docs"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
            "types-requests>=2.28.0",
        ],
    },
    keywords="mighty networks api sdk community management social network",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/mighty-networks-sdk/issues",
        "Source": "https://github.com/yourusername/mighty-networks-sdk",
        "Documentation": "https://github.com/yourusername/mighty-networks-sdk/wiki",
    },
)
