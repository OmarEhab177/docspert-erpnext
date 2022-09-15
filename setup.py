from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in docspert_crm/__init__.py
from docspert_crm import __version__ as version

setup(
	name="docspert_crm",
	version=version,
	description="customize models for docspert needs",
	author="omar",
	author_email="omarehap17@email.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
