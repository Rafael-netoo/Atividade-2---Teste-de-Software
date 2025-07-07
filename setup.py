from setuptools import setup, find_packages

setup(
    name="sistema_bancario_teste_de_software",
    version="0.1",
    packages=find_packages(include=["src", "src.*", "test", "test.*"]),
    author="Multimegaman",
)