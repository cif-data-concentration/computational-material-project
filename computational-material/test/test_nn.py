import keras
from computational_material.models.Neural_Network import neural_network_model
from computational_material.quality_test.NN_metrics import nn_mse
from computational_material.optimization.hypersearch_nn import TPE

data = pd.read_csv('./doc/dataset/bg_struct.csv', index_col=0)
X = data[['cell_lentgh_b', 'cell_lentgh_c', 'cell_angle_alpha', 'cell_angle_beta', 'cell_angle_gamma']].values
Y = data[['cell_length_a']].values
X_train_pn, X_test_pn, y_train, y_test = train_test_split(X, Y,
                                                         test_size=0.20,
                                                         random_state=seed)
X_train_scaler = StandardScaler().fit(X_train_pn)
X_train = X_train_scaler.transform(X_train_pn)
X_test = X_train_scaler.transform(X_test_pn)

def test_neural_network_model():

    test_estimator = KerasRegressor(build_fn=neural_network_model,
                               n1=32, n2=64, n3=64,
                               act1="relu", act2="relu", act3="sigmoid",
                               epochs=1500, batch_size=1000, verbose=1, lr=0.01)
    test_history = estimator.fit(X_train, y_train, validation_split=0.30, epochs=150,
                            batch_size=1000, verbose=1)
    assert isinstance(test_estimator, tensorflow.python.keras.wrappers.scikit_learn.KerasRegressor)
    assert isinstance(test_history, tensorflow.python.keras.callbacks.History)

def test_NN_metrics():

    test_val_mse = nn_mse(n1=32, n2=64, n3=64,
                          act1='relu', act2='relu', act3='sigmoid', lr=0.01)
    assert isinstance(test_val_mse, float)
