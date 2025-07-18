# Author: Kenta Nakamura <c60evaporator@gmail.com>
# Copyright (c) 2020-2021 Kenta Nakamura
# License: BSD 3 clause

from setuptools import setup
import BOSlib_GPU

DESCRIPTION = "the library of Background Oriented Schlieren"
NAME = 'BOSlib-GPU'
AUTHOR = 'Yuuki Ogasawara'
AUTHOR_EMAIL = 'yukiogasawara.research@gmail.com'
URL = 'https://github.com/ogayuuki0202/BOSlib-GPU'
LICENSE = 'GNU GENERAL PUBLIC LICENSE,'
DOWNLOAD_URL = 'https://github.com/ogayuuki0202/BOSlib-GPU'
VERSION = BOSlib_GPU.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'numpy>=1.20.3, <2.0',
    'tqdm >=4.0',
    'pandas >=1.0',
    "cv2"
]

EXTRAS_REQUIRE = {
}

PACKAGES = [
    'BOSlib_GPU'
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Multimedia :: Graphics',
    'Framework :: Matplotlib',
]

with open('README.md', 'r') as fp:
    readme = fp.read()
with open('CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts

setup(name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
    )
