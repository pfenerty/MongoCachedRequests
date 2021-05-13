import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mongo-cached-requests",
    version="0.0.1",
    author="Patrick Fenerty",
    author_email="patrick@fenerty.me",
    description="Cache http requests to a mongo database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pfenerty/mongo-cached-requests",
    project_urls={
        "Bug Tracker": "https://github.com/pfenerty/mongo-cached-requests",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
