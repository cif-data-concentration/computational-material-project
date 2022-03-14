import unittest
import numpy as np
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import bandgap_dt_rf

class UnitTests(unittest.TestCase):
    def test_bandgap_dt(self):
        '''
        This is a test function for bandgap_dt.
        '''
        assert type(bandgap_dt_rf.bandgap_dt(1.3, 1.4, 1.6, 70, 80, 90)) == 'numpy.float64'


    def test_bandgap_rf(self):
        '''
        This is a test function for bandgap_rf.
        '''
        assert type(bandgap_dt_rf.bandgap_rf(1.3, 1.4, 1.6, 70, 80, 90)) == 'numpy.float64'
