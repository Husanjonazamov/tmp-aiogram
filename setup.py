from setuptools import setup, find_packages

setup(
    name="tmp-aiogram",
    version="0.1.0",
    description="Aiogram bot shablonini yaratishga yordam beruvchi paket",
    author="Ismingiz",
    author_email="email@domain.com",
    packages=find_packages(),
    install_requires=[
        "aiogram==2.20",
        "autoenv-tool==0.6",
        "requests",
        "git+https://github.com/username/repository.git@branch#egg=package_name"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
