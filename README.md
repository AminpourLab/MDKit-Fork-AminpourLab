# MDKit

MDKit is a Python package that allows you to easily perform MD simulations with Amber.  
MDKit is especially helpful thanks to its `prepare_md.py` routine which can set up all the steps required for MD:  
- System preparation with or without ligands  
- 2 steps of minimization  
- Equilibration in NVT ensemble  
- Equilibration in NPT ensemble  

`prepare_md.py` can be used to run MD on globular proteins or embedded membrane proteins (prepared with NAMD GUI),  
and to run standard or accelerated MD.

## Versions of Amber supported by MDKit

Currently, only **Amber14** and **Amber16** are supported.  
Notably, **AmberTools** should also be installed (versions 14–17).

---

## Installation

The easiest way to install MDKit is to create a virtual environment.  
This allows MDKit and its dependencies to be installed in user-space without clashing with system-wide packages.

Once `virtualenv` has been properly installed, run the following in the terminal:

```bash
virtualenv env
```

Then activate the virtual environment:

```bash
source env/bin/activate
```

> ⚠️ Don't forget to activate your environment every time you open a new shell.

Finally, navigate to the MDKit installation directory and run:

```bash
python setup.py install
```

✅ **Installation is complete!**


# MDKit - Updated Fork

## About This Repository

This is a **forked version** of the original [MDKit](https://github.com/jp43/MDKit) repository, developed by Dr. Jordane Preto.