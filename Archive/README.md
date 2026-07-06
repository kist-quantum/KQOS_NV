# Reconstructing the Modified QICK Vivado Project

This package provides the additional firmware and Vivado project files required to reconstruct the modified QICK FPGA project used in the manuscript.

The full QICK repository is not redistributed here. Instead, the user should clone the upstream QICK repository, check out the exact base commit used in this work, copy the provided `firmware/` contents into the QICK `firmware/` directory, and run the provided Vivado Tcl script.

## Base QICK Version

Upstream QICK repository:

```bash
https://github.com/openquantumhardware/qick.git
```

Base commit used in this work:

```text
7dac72966638e70a3f0cad23b3724f482ce95a4c
```

## Required Software

The Vivado project Tcl script was generated and tested using:

```text
Xilinx Vivado 2020.2
```

Using the same Vivado version is recommended. Other Vivado versions may require IP upgrade or block-design migration.

## Provided Files

This package contains:

```text
README.md
firmware/
  proj_111_photon_counter.tcl
  xdc/
  ip/
  bd/
```

The `firmware/` directory contains the custom IP, board-specific XDC constraints, exported block-design Tcl files, and the Vivado project reconstruction Tcl script.

## Reconstruction Steps

Run the following commands from the directory containing this `README.md` file.

### 1. Clone the upstream QICK repository

```bash
git clone https://github.com/openquantumhardware/qick.git
```

This will create a local directory:

```text
qick/
```

### 2. Check out the exact QICK commit used in this work

```bash
cd qick
git checkout 7dac72966638e70a3f0cad23b3724f482ce95a4c
```

Optional: confirm the checked-out commit:

```bash
git rev-parse HEAD
```

The output should be:

```text
7dac72966638e70a3f0cad23b3724f482ce95a4c
```

### 3. Copy the provided firmware files into the QICK firmware directory

Return to the directory containing this `README.md` file:

```bash
cd ..
```

Copy the provided firmware contents into the QICK `firmware/` directory:

```bash
cp -r firmware/* qick/firmware/
```

This overlays the provided files onto the original QICK `firmware/` directory.

Do not delete the original QICK `firmware/` directory before copying. The provided files are intended to be added to the original QICK firmware tree.

### 4. Run the Vivado project Tcl script

Move into the QICK `firmware/` directory:

```bash
cd qick/firmware
```

Run Vivado in batch mode:

```bash
vivado -mode batch -source proj_111_photon_counter.tcl
```

If Vivado is not available in the system `PATH`, use the full Vivado 2020.2 executable path. For example, in Git Bash on Windows:

```bash
/c/Xilinx/Vivado/2020.2/bin/vivado.bat -mode batch -source proj_111_photon_counter.tcl
```

## Generated Overlay Files

After the Vivado implementation and bitstream generation are completed successfully, the generated overlay files can be found under the reconstructed QICK firmware directory.

Relative to `qick/firmware/`, the expected output files are:

```text
top_111_photon_counter/top_111_photon_counter.runs/impl_1/d_1_wrapper.bit
top_111_photon_counter/top_111_photon_counter.gen/sources_1/bd/d_1/hw_handoff/d_1.hwh
```

These `.bit` and `.hwh` files are the overlay files required for loading the generated FPGA design in the QICK/PYNQ environment.

## Notes

The Vivado Tcl script should be executed from inside the QICK `firmware/` directory.

The project is reconstructed from upstream QICK commit:

```text
7dac72966638e70a3f0cad23b3724f482ce95a4c
```

The Vivado project was generated and tested using:

```text
Vivado 2020.2
```

If path-related errors occur, check that:

1. The QICK repository was checked out to the correct commit.
2. The contents of the provided `firmware/` directory were copied into `qick/firmware/`.
3. Vivado was launched from inside the `qick/firmware/` directory.
4. The Tcl script references the local `ip/`, `bd/`, and `xdc/` directories relative to the `firmware/` directory.
