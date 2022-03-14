from Neural_Network import neural_network_model

import keras
import tensorflow
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('./doc/dataset/bg_struct.csv', index_col=0)
X = data[['cell_lentgh_b', 'cell_lentgh_c', 'cell_angle_alpha', 'cell_angle_beta', 'cell_angle_gamma']].values
Y = data[['cell_length_a']].values
X_train_pn, X_test_pn, y_train, y_test = train_test_split(X, Y,
                                                         test_size=0.20,
                                                         random_state=seed)
X_train_scaler = StandardScaler().fit(X_train_pn)
X_train = X_train_scaler.transform(X_train_pn)
X_test = X_train_scaler.transform(X_test_pn)

def nn_mse(n1, n2, n3, act1, act2, act3, lr):
    estimator = KerasRegressor(build_fn=neural_network_model,
                               n1=n1, n2=n2, n3=n3,
                               act1=act1, act2=act2, act3=act3,
                               epochs=150, batch_size=100, verbose=0, lr=lr)
    history = estimator.fit(X_train, y_train, validation_split=0.30, epochs=150,
                            batch_size=100, verbose=0)

    return history.history['val_loss'][-1]
