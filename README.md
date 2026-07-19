# KQOS: Middleware for NV⁻ Spin-Photon Interface Control

Glad to see you there.

This repository will introuce you about the **KQOS**  that is a specialized hardware control middleware designed to interface, orchestrate, and experiments on Nitrogen-Vacancy (NV⁻) center spin-photon interfaces.

---

##  Overview

Implementing a robust spin-photon interface demands nanosecond-scale precision and reliable hardware-software synchronization. KQOS bridges the gap between high-level experimental logic and low-level FPGA execution, housing the essential sequences needed to establish and evaluate quantum node performance.

## Features

This branch contains the sequence of the experiments and communication protocols.
if you want to seek other situations(like auto-align, laser tuning and etc), you may move to **nv-client** branch

<img width="1280" height="720" alt="논문_figure_JP_260310" src="https://github.com/user-attachments/assets/2c1cc96e-ab7c-4305-b1a0-03e94cf20846" />

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
