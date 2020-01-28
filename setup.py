import setuptools

with open('README.rst') as f:
    README = f.read()

setuptools.setup(
    author="Grégoire Fruleux",
    author_email="gregoire.fruleux.pro@gmail.com",
    name='aoe2de_rms_genobj_parser',
    license="MIT",
    description='aoe2de_rms_genobj_parser is a python package to parser Age of Empires2: Definitive Edition RMS',
    version='v1.0.0',
    long_description=README,
    url='https://github.com/gfruleux/aoe2de_rms_genobj_parser',
    packages=setuptools.find_packages(),
    python_requires=">=3.8.1",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
