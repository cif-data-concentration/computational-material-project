from pymatgen.ext.matproj import MPRester
import numpy as np
import pandas as pd
import os

def CIFdownload(api, filepath, lower_bound, higher_bound):
    
    """
    This is a function that allows the user to download band gap values and the crystal structure
    of the interested materialsfrom the library of Materials Project. The cif data will be extracted 
    from the downloaded raw data and save as individual files in the provided path with a naming 
    format "index.cif".
    
    References of query syntax and downlodable properties:
    https://docs.mongodb.com/manual/tutorial/query-documents/
    https://pymatgen.org/introduction.html
    """
    
    mpr = MPRester(api)
    data = mpr.query(criteria = {'$and':[{'band_gap': {'$gt': lower_bound}},{'band_gap': {'$lt': higher_bound}}]}, 
                     properties = ['pretty_formula','cif', 'band_gap'])
    
    for i in range(len(data)):
        with open(filepath+'%i.cif'%i, 'w') as w:
            w.write(data[i]['cif'])
    return data

    


def CIFconvert(filepath):
    
    """
    This is a function that reads cif files in the same path and 
    combine the cell parameters into a dataframe. The user will have 
    to first name their cif files with the sequential index.
        
    E.g. "1.cif", "2.cif",...
    """
    col = ['cell_length_a', 'cell_length_b', 'cell_length_c',
               'cell_angle_alpha', 'cell_angle_beta','cell_angle_gamma']
    df = pd.DataFrame(columns = col)
    for j in range(len(os.listdir(filepath))-1):# ignore the checkpoint
        with open(filepath+'%i.cif'%j, 'r') as r:
            line = r.readlines()
            val = []
            for l in line: # i don't know why AND won't work here
                if 'length' in l:
                    x = l.split(' ')
                    val.append(x[-1][:-1])
                if 'angle' in l:
                    x = l.split(' ')
                    val.append(x[-1][:-1])
        df_j = pd.DataFrame(data = [val], columns = col)
        df = pd.concat([df, df_j], ignore_index = True)
    return df

# Ask the user if they would upload the cif file themselves or download from materials project
response = input('Do you want to upload the cif file by yourself? (y/n):')

# Sequential input promp to define the range of band gaps the user is interested.
# Here for a fast demo, we strict the range to a narrow gap to reduce the datasize.
if response == 'n':
    api = input('Please provide with you API here:')
    lower_bound = float(input('Please provide the lower bound of the bandgap:'))
    higher_bound = float(input('Please provide the higher bound of the bandgap:'))
    path = input('Please provide a saving path for the cif files here:')
    data = CIFdownload(api, path, lower_bound, higher_bound)
if response == 'y':
    path = input('Please provide the path of your cif files here:')


# read cell parameters from the cif files and compile into a dataframe
cell = CIFconvert(path) 

# append the structure with the pretty formula and bandgap values
bandgap = []
pretty_formula = []
for i in range(len(data)):
    bandgap.append(data[i]['band_gap'])
    pretty_formula.append(data[i]['pretty_formula'])
dict = {'pretty_formula': pretty_formula, 'bandgap': bandgap}
df1 = pd.DataFrame(data = dict)  # The subdataframe that contains the pretty formula and the band gap

df = pd.concat([df1, cell], axis = 1)


# save the final dataframe into the path of the cif files.
df.to_csv(path+'CIF_data.csv')
