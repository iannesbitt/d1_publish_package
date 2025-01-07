import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    author='Ian Nesbitt',
    author_email='nesbitt@nceas.ucsb.edu',
    name='d1_publish_package',
    version="1.0.0",
    description='DataONE package publishing tool — a command line tool for adding public access to DataONE package objects.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DataONEorg/d1-publish-package',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'dataone.common',
        'dataone.libclient'
    ],
    extras_require={
        'dev': [
            'sphinx',
        ]
    },
    entry_points = {
        'console_scripts': [
            'd1_publish_package=d1_publish_package.cli:cli',
            'd1_publish_package-test=d1_publish_package.test:test'
        ],
    },
    python_requires='>=3.9, <4.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    license='Apache Software License 2.0',
)