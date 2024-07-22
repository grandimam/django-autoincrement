from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-autoincrement",
    version="0.1.0",
    author="Fauzan Baig",
    author_email="baig.fauzan@gmail.com",
    description="A Django app providing an auto-incrementing field.",
    url="https://github.com/grandimam/django-autoincrement",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "Django>=2.2",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'create_sequences=autoincfield.management.commands.create_sequences:Command',
        ],
    },
)
