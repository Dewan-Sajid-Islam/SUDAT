# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-08-02

### Initial Public Release

This is the first frozen benchmark release of the SUDAT Effective Theory implementation.

### Added

- **Modular cosmology framework**:
  - Core modules for scalar field evolution (`cosmology/equations.py`)
  - Numerical integrator with adaptive step‑size control (`cosmology/integrator.py`)
  - Observable calculators (Hubble parameter, deceleration parameter, etc.) (`cosmology/observables.py`)
  - Background evolution pipeline (`cosmology/background.py`)

- **Numerical validation suite**:
  - Consistency checks against analytical expectations
  - Stability tests for the healthy parameter region
  - Convergence tests for the integration scheme

- **Analysis and visualisation**:
  - Scripts for generating diagnostic plots and reports (`analysis/`)
  - Parameter exploration tools

- **Observational comparison**:
  - Script to compare the SUDAT expansion history with ΛCDM (`observations/expansion_history.py`)

- **Theoretical documentation**:
  - Full derivation notes (`theory/`)
  - Research notes covering audit, state, design principles, open questions, and future directions (`research_notes/`)

- **Manuscript**:
  - LaTeX source and bibliography for the accompanying paper (`manuscript/`)

### Philosophy and Benchmarking

- The repository is declared a **frozen benchmark** (v1.0.0) to provide a stable reference for future research.
- All generated figures and experimental results are stored under `results/`.
- The project explicitly acknowledges that the current implementation **does not reproduce the observed ΛCDM expansion history** — this is a known limitation, not a claim of success.

### Known Limitations

- The expansion history predicted by the effective theory differs substantially from ΛCDM.
- The parameter space has not been optimised for observational concordance.
- Only background evolution is implemented; perturbations and structure formation are absent.
- Numerical stability near the critical density may require fine‑tuning of integration parameters.

### License

This release is distributed under the Apache License 2.0.

### Notes

This version (v1.0.0) is intentionally frozen.
Subsequent theoretical developments will be implemented in future versions while preserving this release as the historical benchmark.