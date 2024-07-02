The KNIME node for MolCompass project
=======
## Introduction

<img align="left" src="https://user-images.githubusercontent.com/4963384/218703831-1460bc07-7e9f-417e-9b0c-c9675db5de9f.png"> 
<p align="justify">
`MolCompassKnime` is a part of the `MolCompass` project. It is a KNIME extension that provides a pretrained parametric t-SNE model for molecular visualization. This extension generates X and Y coordinates for compounds, ensuring that similar compounds group together, forming well-recognizable clusters. 
</p>

<br>
<br>

## Installation


### Installation from pre-build package (recommended)
To install `MolCompassKnime` from Zenodo, follow the instructions below:
1. Download the pre-compiled zip archive  for your KNIME version from Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12624633.svg)](https://doi.org/10.5281/zenodo.12624633)
2. Open KNIME Analytics Platform.
3. Click on the `Help` menu and select `Install New Software`.
4. Click on `Add` and select `Local` to add the downloaded extension.
5. Select the path to the folder containing the extension and click on `OK`.
6. Select the extension and click on `Next`.
7. Follow the instructions to install the extension.
8. Restart KNIME Analytics Platform.


### Building from scratch (optional, recommended only for developers)

To build `MolCompassKnime` from scratch, follow the instructions below:

1. **Prepare the Building Environment for KNIME**: 
    ```bash
    conda create -n knime-ext-bundling -c knime -c conda-forge knime-extension-bundling
    conda activate knime-ext-bundling
    ```

2. **Run the Build Command**: 
    ```bash
    python build_python_extension.py --knime-version [version] molcompass molcompass_build_[version]
    ```

   Replace `[version]` with the desired KNIME version (e.g., 5.2).

<br>

Also, you can clone the repo and run GitHub action for building. 

## Usage
You will see the `MolCompass` node in the `Community Nodes`/`Pharmacoinformatics` category.
Using `MolCompassKnime` is straightforward. After building and installing the extension, you can incorporate it into your KNIME workflows.

### Minimal Workflow
Drag and drop the `MolCompassKnime` node into your workflow. Connect it with, for example, a CSV reader and read a dataset.
You can find the example in `workflows` folder. 

<img src="https://github.com/sergsb/MolCompassKnimeNode/assets/4963384/80796c17-c1ac-4114-bf7a-c3cb417455fb" alt="drawing" width="200"/>

<br>


### Advanced Workflow
<img src="https://github.com/sergsb/MolCompassKnimeNode/assets/4963384/e2a60ba6-600f-4378-8f10-e2968fa0373d" alt="drawing" width="500"/>
<br>

<img src="https://github.com/sergsb/MolCompassKnimeNode/assets/4963384/ddec71d5-f7bd-4881-9257-77049d244e14" alt="drawing" width="300"/>

## Support

For any questions, issues, or feedback, please refer to
sergey.sosnin@univie.ac.at 

<br>


