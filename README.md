# Scalar Unified Dark Adaptive Theory (SUDAT)

### Effective Theory v1.0.0

Apache-2.0

Python 3.10+

Research

Cosmology

Version 1.0.0

Welcome.

**Short Name:** SUDAT  
**Author:** Dewan Sajid Islam  
**Current Version:** SUDAT Theory v1.0.0  
**Repository Status:** Frozen Benchmark Release  
**Language:** Python

---

## Scientific Motivation

The nature of dark energy and dark matter remains one of the most profound open questions in modern cosmology. While the ΛCDM model provides an excellent phenomenological description of a wide range of observations, its theoretical foundations—particularly the cosmological constant and its extreme fine-tuning—suggest that a deeper understanding of the dark sector is required.

SUDAT explores a novel approach: the hypothesis that the vacuum state of the dark sector is not a universal constant but is instead dynamically determined by the local matter density. This repository presents the first complete, effective cosmological implementation of this idea, modeling the density-dependent vacuum through a scalar field potential with environmental couplings.

The current implementation demonstrates:

- Density-induced symmetry breaking in the scalar potential.
- A critical density that separates qualitatively different vacuum phases.
- The emergence of both matter-like and dark-energy-like branches from a unified scalar framework.
- A stable vacuum structure over a well-defined, healthy parameter region.
- A modular, extensible Python framework for cosmological simulations.
- A rigorous validation pipeline for numerical accuracy and theoretical consistency.

This repository is **not** a claim that SUDAT replaces ΛCDM or that it is observationally successful. It is a foundational research tool: a complete, reproducible, and documented implementation of the effective theory, designed to enable systematic investigation, validation, and future theoretical refinement.

---

## Key Features

- **Modular Cosmology Framework:** A clean, object-oriented implementation of the cosmological evolution equations, including a flexible integrator and observable calculators.
- **Density-Dependent Scalar Potential:** Implementation of the core SUDAT potential with environment-driven symmetry breaking.
- **Critical Density Threshold:** Numerical identification and handling of the density threshold that separates the two vacuum branches.
- **Background Evolution:** Computation of the expansion history, including the Hubble parameter and deceleration parameter.
- **Validation Pipeline:** Automated comparison of numerical results against analytical expectations and theoretical consistency checks.
- **Visualization and Analysis:** Comprehensive plotting and diagnostic tools for exploring the parameter space and interpreting results.
- **Reproducible Research:** All experimental stages, results, and figures are versioned and stored within the repository.

---

## Repository Structure

```
ScalarUnifiedDarkAdaptiveTheory/
│
├── analysis/                  # Analysis scripts and diagnostic reports
│
├── cosmology/                 # Modular cosmological framework
│   ├── equations.py           # Evolution equations for the scalar field
│   ├── integrator.py          # Numerical integrator (e.g., Runge-Kutta)
│   ├── observables.py         # Computation of cosmological observables
│   └── background_v2.py          # Background evolution routines
│
├── observations/              # Observational comparison scripts
│   └── expansion_history.py   # Comparison of expansion history with ΛCDM
│
├── results/                   # Output data, figures, and experimental logs
│
├── research_notes/            # Documentation of the research process
│   ├── theory_audit.md        # Audit of the theoretical underpinnings
│   ├── project_state.md       # Current state of the project
│   ├── design_principles.md   # Guiding design decisions
│   ├── open_questions.md      # Open theoretical questions
│   └── future_directions.md   # Future research directions
│
├── theory/                    # Theoretical development and derivations
│
├── manuscript/                # LaTeX manuscript and bibliography
│
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── LICENSE                    # Apache License 2.0
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Dewan-Sajid-Islam/SUDAT.git
cd ScalarUnifiedDarkAdaptiveTheory
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv sudat_env
source sudat_env/bin/activate   # On Linux/macOS
# or
sudat_env\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

The code is written in Python 3.8+ and requires the following packages:

| Package          | Version (tested) | Purpose                     |
|------------------|------------------|-----------------------------|
| `numpy`          | ≥1.21.0          | Numerical arrays & math     |
| `scipy`          | ≥1.7.0           | Integration and ODE solvers |
| `matplotlib`     | ≥3.4.0           | Plotting and visualization  |
| `astropy`        | ≥4.2.0           | Cosmological constants      |
| `pandas`         | ≥1.3.0           | Data handling               |
| `pyyaml`         | ≥5.4.0           | Configuration files         |

---

## Quick Start

To run a baseline evolution of the SUDAT effective theory:

```python
python -m analysis.background_report
import matplotlib.pyplot as plt

# Initialize the cosmology with default parameters
cosmo = SUDATCosmology()

# Evolve from redshift z=100 to present day
cosmo.evolve(z_start=100.0, z_end=0.0)

# Plot the expansion history
cosmo.plot_hubble()
plt.show()
```

For a complete run with parameter exploration and validation:

```bash
python analysis/run_validation.py --params params.yaml --output results/
```

---

## Typical Workflow

A researcher using this repository would typically follow these steps:

1. **Explore the theory:** Read the theoretical derivations in `theory/` and the research notes in `research_notes/` to understand the assumptions and framework of the effective theory.

2. **Run the baseline model:** Execute the quick start commands to reproduce the benchmark evolution and verify the installation.

3. **Modify parameters:** Adjust the parameters of the scalar potential (e.g., coupling constants, mass scales) in the configuration files (`params.yaml`) to explore different regions of the parameter space.

4. **Analyze results:** Use the analysis scripts in `analysis/` to examine the resulting expansion history, scalar field dynamics, and stability properties.

5. **Compare with observations:** Run the `observations/expansion_history.py` script to compare the SUDAT expansion history with the ΛCDM model or other observational data sets.

6. **Extend the framework:** Add new observables, modify the potential, or experiment with different numerical integration schemes.

---

## Repository Philosophy

This release (v1.0.0) is a **frozen benchmark** of the effective theory. Its purpose is to:

- Provide a stable, well-documented, and reproducible implementation of the SUDAT effective theory as described in the accompanying manuscript.
- Establish a baseline for future theoretical and numerical developments.
- Enable researchers to verify our results and build upon them with confidence.

Future work will be compared against this version. The frozen status ensures that all subsequent theoretical modifications or numerical improvements are grounded in a fully reproducible reference framework. This repository is not a project in continuous, incremental development; it is a snapshot of a specific scientific milestone.

---

## Current Scientific Status

### Validated

- **Numerical integrator:** Accuracy and stability verified against analytical solutions for simple potentials.
- **Consistency checks:** The evolution equations satisfy energy conservation and other key constraints within numerical precision.
- **Stability regions:** The boundary of the healthy parameter region has been mapped and verified.
- **Density-induced symmetry breaking**
- **Stable vacuum**
- **Healthy parameter region**
- **Matter-like branch**
- **Dark-energy-like branch**
- **Modular implementation**
- **Background diagnostics**
- **Energy-budget diagnostics**
- **Field-dynamics diagnostics**

### Partially Validated

- **Symmetry breaking mechanism:** The density-induced transition is reproduced, but the numerical precision near the critical density is sensitive to the step size.
- **Branch identification:** The distinction between matter-like and dark-energy-like branches is robust, but the transition dynamics require further investigation.

### Future Work

- Derive the scalar potential from a more fundamental theoretical framework (e.g., from quantum field theory or modified gravity).
- Extend the implementation to include linear perturbations and structure formation.
- Improve numerical handling of the critical density transition.
- Compare with additional observational datasets (e.g., Supernovae, Baryon Acoustic Oscillations, Cosmic Microwave Background).

---

## Known Limitations

This repository is a **scientific research tool**, not a validated cosmological model. Researchers must be aware of the following limitations:

- **Expansion history:** The current implementation does **not** reproduce the observed expansion history of the ΛCDM model. The SUDAT effective theory predicts a significantly different evolution of the Hubble parameter at late times.
- **Parameter tuning:** The parameter space has not been optimized to match observations. The current parameters were chosen to demonstrate the qualitative features of the theory, not to achieve observational concordance.
- **Numerical precision:** The integrator can be unstable for extreme parameter values or near the critical density. Users should verify convergence and stability for their chosen parameters.
- **No perturbations:** This implementation only handles the background (homogeneous and isotropic) cosmology. Perturbations, structure formation, and gravitational lensing are not included.

These limitations are openly acknowledged as part of the research process. The repository is explicitly designed to enable systematic investigation of these issues.

---

## Research Program

This repository represents **Version 1** of the effective theory of SUDAT. The immediate goal is not to tune parameters to fit observations but to:

1. **Establish a rigorous theoretical foundation.** Future research will focus on deriving the density-dependent scalar potential from a more fundamental principle, rather than treating it as an effective parameterization.

2. **Understand the physics.** The current implementation serves as a testbed for exploring the novel features of the theory (e.g., the critical density, the branch transition) and understanding their physical implications.

3. **Build a reproducible benchmark.** This frozen version provides a reference point for all future comparisons and developments.

Future generations of SUDAT will be developed only when supported by new theoretical derivations and validated against the Version 1 benchmark.

---

## Contributing

Contributions are welcomed from the scientific community, particularly in the form of:

- **Theoretical insights:** New derivations, alternative formulations, or connections to other theoretical frameworks.
- **Numerical improvements:** Enhancements to the integrator, adaptive step-size control, or handling of stiff equations.
- **New observables:** Extensions to include perturbations, growth of structure, or additional probes.
- **Bug reports and fixes:** Reproducible bug reports and well-documented fixes.

---

## Publications

This repository accompanies the ongoing development of the Scalar Unified Dark Adaptive Theory (SUDAT).

Current manuscript:

- Scalar Unified Dark Adaptive Theory (working manuscript)

Future peer-reviewed publications and preprints will be listed here.

---

### Guidelines

- All contributions must be **scientifically motivated** and clearly documented.
- **Arbitrary parameter tuning** without a theoretical basis is discouraged and will not be merged.
- Contributions should include clear explanations of their purpose, implementation, and validation.
- Please open an issue first to discuss major changes or new features.

---

## Citation

A `CITATION.cff` file is included in this repository to facilitate proper citation of this software. Please cite this work if you use it for your research.

---

## License

This project is released under the Apache License 2.0.