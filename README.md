# KQOS: Middleware for NV⁻ Spin-Photon Interface Control

**KQOS** is a specialized hardware control middleware designed to interface, orchestrate, and automate experiments on Nitrogen-Vacancy (NV⁻) center spin-photon interfaces. This repository provides the core pulse sequencing routines required to initialize, manipulate, and characterize NV⁻ electron spins for quantum networking and quantum engineering applications.

---

##  Overview

Implementing a robust spin-photon interface demands nanosecond-scale precision and reliable hardware-software synchronization. KQOS bridges the gap between high-level experimental logic and low-level FPGA execution, housing the essential sequences needed to establish and evaluate quantum node performance.

---

## Included Experimental Sequences

The repository contains automated execution scripts and configuration files for standard NV⁻ characterization protocols:

### 1. Spin Coherence & Relaxation Measurements
* **$T_1$ (Spin Relaxation Time):** Measures the longitudinal relaxation time of the electron spin to evaluate ambient thermal/magnetic environment coupling.
* **$T_2$ (Spin Echo):** Cancels static inhomogeneous broadening using a refocusing pulse to determine the true spin coherence time.
* **$T_2^*$ (Ramsey):** Evaluates the dephasing time and characterises the local magnetic field environment/detuning.

### 2. Optical & Resonant Control
* **Resonant Optical Excitation Sequence:** Implements state-selective optical readout and spin-photon entanglement protocols via precise laser pulse routing and photon-counting synchronization.

---

## Requirements

KQOS is built on top of the QICK (https://github.com/openquantumhardware/qick.git) framework to enable seamless, low-latency control over the RF/digital channels of the hardware.

Ensure your FPGA environment meets the following specific dependency versions:

* **Python** == 3.8.2
* **QICK** == 0.2
* **PYNQ** == 3.0.1

---
