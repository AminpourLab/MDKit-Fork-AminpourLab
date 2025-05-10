import sys
import setuptools

# Enforce minimum Python 3 version (adjust as needed)
if sys.version_info < (3, 6):
    sys.exit("Python 3.6+ is required to install the MDKit package.")

setuptools.setup(
    name='mdkit',
    version="0.1.4",
    packages=['mdkit', 'mdkit.amber', 'mdkit.namd', 'mdkit.utility'],
    package_data={'mdkit.amber': ['PROTON_INFO', 'atomic_ions.cmd']},
    include_package_data=True,
    scripts=['bin/prepare_md.py', 'bin/pdb2mol2'],
    install_requires=[
    	'networkx',
    	'numpy',
    	'decorator'
    ],
    license='LICENSE.txt',
    description='Tools to prepare and analyze MD simulations conducted with popular MD packages',
    python_requires='>=3.6',
)

