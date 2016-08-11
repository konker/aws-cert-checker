import sys

from distutils.core import setup
from setuptools import find_packages

version = '0.1.3'

install_requires = [
    'boto3'
]

if sys.version_info < (2, 7):
    install_requires.append('mock<1.1.0')
else:
    install_requires.append('mock')

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='aws-cert-checker',
    version=version,
    description="A simple utility to check whether the an AWS Server Certificate has expired",
    url='https://github.com/konker/aws-cert-checker',
    author="Konrad Markus",
    author_email='konker@luxvelocitas.com',
    license='ISC',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    keywords = ['aws', 'certificate'],
    entry_points = {
        'console_scripts': [
            'aws-cert-checker = aws_cert_checker.main:main_exec'
        ]
    }
)
