import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graphene-django-cud",
    version="0.13.1",
    author="Tormod Haugland",
    author_email="tormod.haugland@gmail.com",
    description="Create, update and delete mutations for graphene-django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tOgg1/graphene-django-cud",
    packages=setuptools.find_packages(),
    install_requires=[
        "graphene-django>=3.2.3",
        "graphene-file-upload>=1.2",
        "graphene-luna>=1.0.0",
        "gunicorn>=23.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
