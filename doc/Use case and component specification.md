 
### Project Outline
 
The project mainly contains two separate parts. One is to extract the information of molecules from the cif file and compile to pandas dataframe, the other is to use machine learning method to analyze the relationship between the crystal structure and the band gap of the materials.
 
 
 
### User stories
 
Jennie is a researcher who has a bunch of cif files containing the molecular structures from her experiments. She would like to have an automotive program that extracts the structural parameters of her molecules and compiles them into a dataframe that is easy for data visualization, and statistical analysis in the future. Jennie’s job only needs to know how to use the function and does not need to know the details of file converting process.
 
Vicky is a researcher who wants to anticipate the band gap of a polymer material currently under exploration, or a theoretical polymer from the computation. She has the basic structural information from experiments or computation stored in the form of .cif  and is seeking an accurate software to get the predicted band gap of the polymer before she applies tons of computational resources on that. Jennie’s job is to know how to call the function using python and pass the known information as parameters.
 
 
### User Case
 
1. Convert cif format files to dataframe

*User*: Provide the cif format files

*Software*: Process cif format files and convert the data to dataframe
 
2. Predict some properties depending on the molecular structure

*User*: Input the lattice parameters of molecules

*Software*: Predict certain properties of the molecules based on the machine-learning model
 
3. Predict the property depending on the known properties, we will try to find the relationship between some properties, with such a basic background, the engineer should have the potential to anticipate the properties of material not yet studied, or the materials not even developed.

*User*: Input the value of properties that are known

*Software*: Predict certain properties of the molecules based on the machine-learning model
 
 
### Component design
 
**Component design 1**:

*Name*:

- CifConverter

*What it does*:

- Extract the structural parameters and the chemical formula of materials from user uploaded cif files and compile the data to a dataframe. Users are allowed to upload additional property files that could be further appended to the dataframe, or summarize the property in the comment of the cif files.

*Inputs*:

- The path of the cif files of users own database, a string

*Outputs*:

- The dataframe format information
  

**Component design 2**:

*Name*:

- CifDownload

*What it does*:

- Take inputs from the sequential prompt in CIF_Process.py to download the band gap data from Materials Project.

- Create .cif files for each compound.

*Inputs*:

- api keys, file path, interested boundary of band gaps

*Outputs*:

- A list of dictionaries of inidividual compounds and relevant information
- Local cif files written from the structural information downloaded from the library.



**Component design 3**:

*Name*:

- BandgapPredictor

*What it does*:

- Train a model between the lattice parameters, dielectric constants and band gap based on the polymer database generated from Component 1.

- Predict the band gap of a new polymer based on the trained model

*Inputs*:

- Lattice parameters and dielectric constants of a material, a list

*Outputs*:

- a dictionary with a key “band_gap” and the value of the predicted bandgap. 
 

