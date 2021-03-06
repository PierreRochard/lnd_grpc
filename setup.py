import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lnd_grpc",
    version="0.1.1",
    author="Will Clark",
    author_email="will8clark@gmail.com",
    description="LND gRPC pre-packaged",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/willcl-ark/lnd_grpc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="lnd grpc",
    install_requires=[
        "grpcio",
        "grpcio-tools",
        "googleapis-common-protos"
    ],
    python_requires='>=3',
)
