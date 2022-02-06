#!/usr/bin/env python3
import setuptools

with open('README.md', "r") as f:
    readme = f.read()

setuptools.setup(
    name="PyMLX90614",
    description="MLX90614 temperature sensor library",
    version="0.0.4",
    author="Connor Kneebone",
    author_email="connor@sfxrescue.com",
    url="https://github.com/Conr86/PyMLX90614",
    license='MIT',
    packages=setuptools.find_packages(exclude=['tests', 'notebooks']),
	long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=['smbus2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='mlx90614 i2c smbus smbus2',
)
