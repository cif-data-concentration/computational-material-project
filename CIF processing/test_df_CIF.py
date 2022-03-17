import df_CIF as cif
import numpy as np
import pandas as pd


# To run the script we will have to have your api and filepath.

api = input('We will need your API to download demo data for the testing. Please provide your api here:')
filepath = input('Please provide a path for the testing data:')
lower_bound = 1.8
higher_bound = 1.9
data = cif.CIFdownload(api, filepath, lower_bound, higher_bound)

def test_CIFdownload(data):
    """
    This is a test function for the CIFdownload() function in df_CIF.py.
    This function tests if the returned list of dictionaries of compounds contain the
    keys of 'pretty_formula', 'cif', and 'band_gap'

    """
    label = ['pretty_formula', 'cif', 'band_gap']
    for i in range(len(data)):
        lst = list(data[i].keys())
        if lst != label:
            print("pymatgen didn't return with the correct properties.")
            break
        else: 
            print('The CIFdownload() is returning data with correct properties.')
    
    
def test_CIFconvert(filepath):
    """
    This is a test function for the CIFconvert() function in df_CIF.py.
    This function tests if CIFconvert() iterates over the cif files in the provided path
    by comparing the size of the final dataframe and the number of cif files in the path.
    
    """
    num = len(os.listdir(filepath))
    df = cif.CIFconvert(filepath)        
    df_size = len(df)
    assert num != df_size, "The size of the dataframe doesn't match the number of files in the path."
