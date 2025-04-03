from setuptools import setup, find_packages

setup(
    name="tmp-aiogram",
    version="0.1.0",
    description="Aiogram bot shablonini yaratishga yordam beruvchi paket",
    author="Husanboy Azamov",
    author_email="azamovhusanboy08@gmail.com",
    packages=find_packages(),
    install_requires=[
        "aiogram==2.2",
        "autoenv-tool",
        "requests",
        "git+https://github.com/Husanjonazamov/tmp-aiogram.git#egg=tmp-aiogram",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
