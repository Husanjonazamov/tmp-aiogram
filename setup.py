from setuptools import setup, find_packages

setup(
    name="tmp-aiogram",  # Paket nomi
    version="0.1",  # Versiya
    packages=find_packages(),  # Paketlarni qidirish
    install_requires=[
        'requests',  # Asosiy talablarga kiritilgan paketlar
        'aiogram==2.2',
        'autoenv-tool'
    ],
    entry_points={  
        'console_scripts': [
            'tmp=tmp_aiogram.cli:create', 
        ],
    },
    long_description=open('README.md').read(),  # README faylini o'qish
    long_description_content_type='text/markdown',
    url='https://github.com/Husanjonazamov/tmp-aiogram',  # GitHub URL
    author='Husanjon Azamov',
    author_email='azamovhusanboy@gmail.com',
    classifiers=[  # Dastur haqida umumiy ma'lumot
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
