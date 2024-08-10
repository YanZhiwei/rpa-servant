import os
import re
import setuptools

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

with open("src/RpaServant/__init__.py", "r") as fileObj:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fileObj.read(), re.MULTILINE
    ).group(1)


setuptools.setup(
    name="rpaServant",
    version=version,
    author="RpaServant",
    author_email="yan.zhiwei@hotmail.com",
    description="Rpa servant sdk",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    test_suite='tests',
    include_package_data = True,
    url="https://github.com/YanZhiwei",
    project_urls={
        "Documentation": "https://github.com/YanZhiwei"
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_data={
        '':['*.dll','*.config','*.xml']
    }
)