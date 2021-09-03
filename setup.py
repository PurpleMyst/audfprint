import pkg_resources
import setuptools

with open("requirements.txt") as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name="audfprint",
    version="1.0.1",
    packages=["audfprint"],
    install_requires=install_requires,
)
