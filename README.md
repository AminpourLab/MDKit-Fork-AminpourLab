# MDKit - Updated Fork

## About This Repository

This is a **forked version** of the original [MDKit](https://github.com/jp43/MDKit) repository, developed by Dr. Jordane Preto.

Our goal is to **modernize and expand MDKit** as part of an integrated toolkit for molecular docking and molecular dynamics simulations. This version adds:

- Python 3 support
- Compatibility with modern HPC clusters (e.g., Narval)
- Support for Amber 22, AmberTools 23, NAMD 3, Gromacs 2024
- Protocols for post-translational modifications (PTMs)
- Unified CLI and TOML configuration support

---

## Overview

MDKit is a Python package that simplifies MD simulation workflows using Amber. The toolkit provides:

- Full preparation of protein systems (with or without ligands)
- Automated two-step minimization
- Equilibration in NVT and NPT ensembles
- Support for both globular and membrane proteins (prepared via NAMD GUI)
- Standard and accelerated MD simulation protocols

---

## Supported Versions

**Original Support**:
- Amber14
- Amber16  
(AmberTools 14–17 also required)

**This Fork Adds**:
- Amber 22
- AmberTools 23
- NAMD 3.0.1
- Gromacs 2024
- Enhanced PTM workflows

---

## Installation

We recommend using a virtual environment to avoid system package conflicts.

### Step 1: Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

> 💡 Remember to activate your environment every time you start a new terminal session.

### Step 2: Install MDKit

Navigate to the MDKit root directory and run:

```bash
python setup.py install
```

Installation is complete! 🎉

---

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## Acknowledgments

- Original Author: Dr. Jordane Preto  
- Fork Maintained By: [Your Organization Name]