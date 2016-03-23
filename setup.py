from setuptools import setup, find_packages

install_requires = [
    'requests',
    'jsonpickle'
]
dependency_links = []
setup_requires = []
tests_require = ['unittest', 'io']

setup(
    name='falkonryclient',
    version='0.1.1',
    author='Falkonry Inc',
    author_email='info@falkonry.com',
    license='MIT',
    url='https://github.com/Falkonry/falkonry-python-client',
    download_url = 'https://github.com/Falkonry/falkonry-python-client/tarball/0.1.1',
    description='Falkonry Python Client to access Condition Prediction APIs',
    packages=['falkonryclient'],
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    extras_require={
        'test': ['unittest', 'io'],
        'all': install_requires + tests_require
    },
    dependency_links=dependency_links,
    zip_safe=False,
    include_package_data=True,
    keywords='falkonry falkonryclient conditionprediction'
)
