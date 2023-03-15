import setuptools
from importlib.machinery import SourceFileLoader

version = SourceFileLoader(
    "caiber_test.version", "config/version.py").load_module()

with open("requirements.txt", "r") as fp:
    required = fp.read().splitlines()

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="caiber_test",
    version=version.__version__,
    author="Anubhav Tiwari",
    author_email="abt.exp@gmail.com",
    description="A Simple Test Library For Projectaile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caibernate/caiber_test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    project_urls={
        "Source": "https://github.com/caibernate/caiber_test",
        "Tracker": "https://github.com/caibernate/caiber_test/issues",
    },
    python_requires=">=3.6",
    install_requires=required,
    extras_require={
        "testing": [
            "rich"
        ]
    },
    entry_points={
        "console_scripts": []
    }
)
