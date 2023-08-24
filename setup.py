import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.1'

REPO_NAME = 'Test Summarizer'
AUTHOR_USERNAME = 'Abhi'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'test@test.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)