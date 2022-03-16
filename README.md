[![Anaconda-Server Badge](https://anaconda.org/anaconda/anaconda/badges/installer/conda.svg)](https://conda.anaconda.org/anaconda)
[![Anaconda-Server Badge](https://anaconda.org/anaconda/anaconda/badges/platforms.svg)](https://anaconda.org/anaconda/anaconda)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# computational-material-project
The project contains two separate parts. One is to extract the information of molecules from the cif file and compile to pandas dataframe, the other is to use machine learning to analyze the relationship between crystal structure and the band gap. And create an user interface to output the predict bandgap value.

## Cif Adaptor
This adaptor is a pre-process algorithm that massively extracts structural information from either user uploaded raw files in the same path or the open-source library using API for data access and then append the information with the properties of substances from the known libraries(Material Project).

## Machine Learning
Explore a specific structure-property relationship between lattice constants and the bandgap of a chosen range of materials.
![image](https://github.com/cif-data-concentration/computational-material-project/blob/main/doc/Image/pairplot.png)

### Neural Network
__Current Functionality__:
- [x] Instantialize, train a neural network model
- [x] Predict feature with the NN model
- [x] Model optimization using hyperparameters tuning

<p float="left">
  <img src=https://github.com/cif-data-concentration/computational-material-project/blob/main/doc/Image/optimal%20nn%20model%20loss.png width="45%" aligh = left />
  <img src=https://github.com/cif-data-concentration/computational-material-project/blob/main/doc/Image/actual%20vs%20predictde.png width="46.5%" align = right />
</p>

### Decision Tree & Random Forest
__Current Functionality__:
- [x] Model optimization using hyperparameters tuning
- [x] Train a decision tree and random forest model
- [x] Predict bandgap with the decision tree regressor and random forest regressor model
- [x] Create an user interface to output the predicted bandgap

### User Interface to predict the band gap
In the right hand side, users can enter the crystal lattice constant and choose the machine learning method and then the left hand side will output the predict band gap value.
<img src='https://github.com/cif-data-concentration/computational-material-project/blob/main/doc/Image/User%20Interface%20to%20predict%20band%20gap.png'>

## Installation
Install and activate the environment with `finalProject.yml` by:
> `conda env create -f finalProject.yml`
> `conda activate comma_env`
In console, execute the following command where <code>package_path</code> is the path to the folder containing this Readme (computational-material-project):
> <code>pip install package_path</code>
It can then be imported on the installed environment as <code>comma</code>.

## Repo structure
```
computational-material-project
-----
setup.py
finalProject.yml
computational-materials/
|-tests/
|-models/
| |-cifadaptor.py
| |-Neural_Network.py
| |-Devision_Tree.py
| |-Random_Forest.py
|-quality_test/
| |-NN_metrics.py
|-optimization/
| |-hypersearch_nn.py
| |-hypersearch_dt.py
| |-hypersearch_rf.py
examples/
|-NN_demo.ipynb
|-DTandRF_demo.ipynb
doc/
|-dataset/
| |-bg_struct.csv
|-Image/
| |-pairplot.png
| |-actual vs predicted.png
| |-optimal nn model loss.png
| |-User Interface to predict band gap.png

```
## Examples
See examples folder for more demonstrations on predicting feature with the available tools.

## Next step and lessons learned

