from setuptools import setup, find_packages


setup(
    name="msca", 
    version="0.0.1",
    author="Rafael Vescovi",
    author_email="ravescovi@gmail.com",
    description="MSCA Class Package",
    long_description_content_type="text/markdown",
    url="https://github.com/ravescovi/python_for_analitycs",
    packages=find_packages(exclude=["*test*"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
