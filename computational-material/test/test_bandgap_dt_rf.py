import unittest
import numpy as np
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv('../../../doc/dataset/bg_struct.csv', index_col=0)
X = df[['cell_length_a','cell_lentgh_b', 'cell_lentgh_c',
        'cell_angle_alpha', 'cell_angle_beta', 'cell_angle_gamma']]
y = df['bandgap']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,
                                                    random_state=42)


# Define the decision tree regressor object
regr = DecisionTreeRegressor(max_depth=9, min_samples_split=37, min_samples_leaf=4,
                  splitter='best', min_weight_fraction_leaf=0.00952179564895864)

#Fit to the training data
regr = regr.fit(X_train, y_train)

# Define a random forest regressor object
rand = RandomForestRegressor(n_estimators=99, max_depth=23, min_samples_split=14,
            min_samples_leaf=3, min_weight_fraction_leaf=2.9893745932052474e-05)

# Fit to your training data
rand = rand.fit(X_train, y_train)

def bandgap_dt(a, b, c, alpha, beta, gamma):
    '''
    This function is to use the training decision tree regressor model to
    predict the bandgap value.
    '''
    test = [a, b, c, alpha, beta, gamma]
    # convert the list to the dataframe
    test_point = pd.DataFrame([test], columns=['cell_length_a','cell_lentgh_b', 'cell_lentgh_c',
                                             'cell_angle_alpha', 'cell_angle_beta', 'cell_angle_gamma'])
    return regr.predict(test_point)[0]


def bandgap_rf(a, b, c, alpha, beta, gamma):
    '''
    This function is to use the training decision tree regressor model to
    predict the bandgap value.
    '''
    test = [a, b, c, alpha, beta, gamma]
    # convert the list to the dataframe
    test_point = pd.DataFrame([test], columns=['cell_length_a','cell_lentgh_b', 'cell_lentgh_c',
                                             'cell_angle_alpha', 'cell_angle_beta', 'cell_angle_gamma'])
    return rand.predict(test_point)[0]



class UnitTests(unittest.TestCase):
    def test_bandgap_dt(self):
        '''
        This is a test function for bandgap_dt.
        '''
        assert type(bandgap_dt(1.3, 1.4, 1.6, 70, 80, 90)) == 'numpy.float64'


    def test_bandgap_rf(self):
        '''
        This is a test function for bandgap_rf.
        '''
        assert type(bandgap_rf(1.3, 1.4, 1.6, 70, 80, 90)) == 'numpy.float64'
