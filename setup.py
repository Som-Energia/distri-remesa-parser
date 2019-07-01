from setuptools import setup

setup(
    name='distri-remesa-parser',
    version='0.1.1',
    description='A python library to parser payment order files with related invoices sended by the spanish "Distribuidoras" to the "Comercializadoras',
    url='https://github.com/Som-Energia/distri-remesa-parser',
    author='oriolpiera',
    author_email='oriol.piera@somenergia.coop',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=['distriremesaparser'],
    zip_safe=False,
    test_suite='tests',
)
