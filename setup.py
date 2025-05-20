from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='shortestpath12345678',  # Öğrenci numaranı yaz
    version='0.1.0',
    author='Ad Soyad',
    author_email='eposta@eposta.com',
    description='Kısa açıklama',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/kullaniciadi/repoadi',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pytest>=6.2.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
