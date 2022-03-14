import keras
import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

def neural_network_model(n1, n2, n3, act1, act2, act3, lr):
    """
    activation: 'relu', 'sigmoid', 'linear', 'tanh', 'selu', 'elu'
    """
    model = Sequential()
    model.add(Dense(n1, input_dim=5, kernel_initializer='normal', activation=act1))
    model.add(Dense(n2, kernel_initializer='normal', activation=act2))
    model.add(Dense(n3, kernel_initializer='normal', activation=act3))
    model.add(Dense(1, kernel_initializer='normal'))

    opt = tensorflow.keras.optimizers.Adam(learning_rate=lr)

    model.compile(loss='mean_squared_error', optimizer=opt)
    return model
