from setuptools import setup


with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()


setup(
    name ="src",
    version = "0.0.1",
    author = "vikassalaria",
    description = " A small [package for ml dvc pipeline",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url ="https://github.com/vikassalaria2412/dvc_ml_ops",
    author_email = "engg.vikassalaria@gmail.com",
    packages = ['src'],
    python_requires =">=3.7",
    install_requires = [
        'dvc',
        'pandas',
        'scikit-learn'

    ]

)
