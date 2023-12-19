#!/usr/bin/env python

from os import path, walk

import sys
from setuptools import setup, find_packages

NAME = "Orange3-Radya"

VERSION = "0.1.0+dev"

AUTHOR = "Radya Labs"
AUTHOR_EMAIL = "dev@radyalabs.com"

URL = "https://orangedatamining.com/download"
DESCRIPTION = "Orange3 add-on from Radya for displaying data from api"

LICENSE = "GPL3+"

PACKAGES = find_packages()

PACKAGE_DATA = {
    "orangecontrib.apifetcher.widgets": ["icons/*"],
}

DATA_FILES = [
    # Data files that will be installed outside site-packages folder
]

INSTALL_REQUIRES = [
    "AnyQt",
    # shap's requirement, force users for numba to get updated because compatibility
    # issues with numpy - completely remove this pin after october 2024
    "numba >=0.58",
    "numpy",
    "Orange3 >=3.34.0",
    "orange-canvas-core >=0.1.28",
    "orange-widget-base >=4.19.0",
]

ENTRY_POINTS = {
    "orange.widgets": ("Radya = orangecontrib.radya.widgets",),
}

CLASSIFIERS = [
    "Development Status :: 1 - Beta",
    "Programming Language :: Python :: 3 :: Only",
]


def include_documentation(local_dir, install_dir):
    global DATA_FILES
    # if "bdist_wheel" in sys.argv and not path.exists(local_dir):
    #     print(
    #         "Directory '{}' does not exist. "
    #         "Please build documentation before running bdist_wheel.".format(
    #             path.abspath(local_dir)
    #         )
    #     )
    #     sys.exit(0)

    doc_files = []
    for dirpath, dirs, files in walk(local_dir):
        doc_files.append(
            (
                dirpath.replace(local_dir, install_dir),
                [path.join(dirpath, f) for f in files],
            )
        )
    DATA_FILES.extend(doc_files)


if __name__ == "__main__":
    setup(
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        classifiers=CLASSIFIERS,
        data_files=DATA_FILES,
        description=DESCRIPTION,
        entry_points=ENTRY_POINTS,
        install_requires=INSTALL_REQUIRES,
        long_description_content_type="text/markdown",
        license=LICENSE,
        name=NAME,
        namespace_packages=["orangecontrib"],
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        url=URL,
        version=VERSION,
        zip_safe=False,
    )
