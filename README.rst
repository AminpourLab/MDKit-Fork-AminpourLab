## About This Repository

This is a **forked version** of the original [MDKit](https://github.com/jp43/MDKit) repository, developed by Dr. Jordane Preto.

Our goal is to **modernize and expand MDKit** as part of an integrated toolkit for molecular docking and molecular dynamics simulations. This version adds:

- Python 3 support
- Compatibility with modern HPC clusters (e.g., Narval)
- Support for Amber 22, AmberTools 23, NAMD 3, Gromacs 2024
- Protocols for post-translational modifications (PTMs)
- Unified CLI and TOML configuration support


*****
MDKit
*****

MDKit is a python package that allows to easily perform MD simulations with Amber. MDKit is especially helpful
thanks to its *prepare_md.py* routine which can set up all the steps required for MD: system preparation
with or without ligands, 2 steps of minimization, equilibration in NVT ensemble, equilibration in NPT ensemble.
*prepare_md.py* can be used to run MD on globular proteins or embedded membrane proteins (prepared with NAMD GUI)
and to run standard or accelerated MD.

**Versions of Amber supported by MDKit**

Currently, only Amber14 and Amber16 are supported. Notably, AmberTools should also be installed (versions 14-17).


Installation
************

The easiest way to install MDKit is to create a virtual environment. In this way, MDKit
and its dependencies can easily be installed in user-space without clashing with potentially
incompatible system-wise packages.

Once virtualenv has been properly installed, simply type (and press the return key)

::

 virtualenv env
  
on the command line followed by

::

 source env/bin/activate
 
to activate the virtual environment (do not forget to activate your environment every time you log into a new shell environment).

Finally, the MDKit package can be set up by going in MDKit installation directory and typing:

::

 python setup.py install
 
 
Installation is complete!

