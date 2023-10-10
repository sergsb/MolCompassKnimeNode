The KNIME node for MolCompass project
=======
### Introduction

<img align="left" src="https://user-images.githubusercontent.com/4963384/218703831-1460bc07-7e9f-417e-9b0c-c9675db5de9f.png"> 
<p align="justify">
`MolCompassKnime` is a part of the `MolCompass` project. It is a KNIME extension that provides a pretrained parametric t-SNE model for molecular visualization. This extension generates X and Y coordinates for compounds, ensuring that similar compounds group together, forming well-recognizable clusters. 
</p>

<br>
<br>

## Access 
This KNIME workflow is built automatically using GitHub Actions. You can
download builds from ...
## Building from scratch 

To build `MolCompassKnime` from scratch, follow the instructions below:

1. **Prepare the Building Environment for KNIME**: 
    ```bash
    conda create -n knime-ext-bundling -c "knime/label/nightly" -c conda-forge knime-extension-bundling
    conda activate knime-ext-bundling
    ```

2. **Run the Build Command**: 
    ```bash
    python build_python_extension.py --knime-version [version] molcompass molcompass_build_[version]
    ```

   Replace `[version]` with the desired KNIME version (e.g., 4.6 or 4.7).

<br>


## Usage

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

