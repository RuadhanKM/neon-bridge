import pathlib
import setuptools

setuptools.setup(
    name="neon",
    version="0.0.1",
    description="A bridge layer for matrix emulation.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/RuadhanKM/neon-bridge",
    author="RuadhanKM",
    license="The MIT License",
    python_requires=">=3.10,<3.12",
    install_requires=["adafruit-circuitpython-matrixportal"],
    packages=setuptools.find_packages(),
    include_package_data=True
)