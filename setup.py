from setuptools import setup, find_packages

with open("README.md", "r") as f:
  long_description = f.read()

setup(
    name="s3go",
    version="0.1",
    description="upload local folder to s3 bucket",
    longdescription=long_description,
    url="https://github.com/flyfj/s3deploy",
    author="Jie Feng",
    author_email="jiefengdev@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["boto3", "tqdm"])
