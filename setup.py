from setuptools import setup
readme = open("README.md").read()

setup(
    name='distri-remesa-parser',
    version='0.1.6',
    description='A python library to parser payment order files with related invoices sended by the spanish "Distribuidoras" to the "Comercializadoras',
    url='https://github.com/Som-Energia/distri-remesa-parser',
    author='oriolpiera',
    author_email='oriol.piera@somenergia.coop',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=['distriremesaparser'],
    zip_safe=False,
    test_suite='tests',
)
