from Neural_Network import neural_network_model
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

def nn_mse(n1, n2, n3, act1, act2, act3, lr):
    estimator = KerasRegressor(build_fn=neural_network_model, 
                               n1=n1, n2=n2, n3=n3,
                               act1=act1, act2=act2, act3=act3, 
                               epochs=150, batch_size=100, verbose=0, lr=lr)
    history = estimator.fit(X_train, y_train, validation_split=0.30, epochs=150, 
                            batch_size=100, verbose=0)

    return history.history['val_loss'][-1]
