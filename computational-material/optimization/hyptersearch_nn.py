from NN_metrics import nn_mse
import optuna
import sklearn.model_selection
import sklearn.preprocessing
import seaborn as sns

def TPE(n_trials):

    def objective(trial):
        # define hyperparameter space
        n1 = trial.suggest_categorical('n1', [2, 8, 16, 64, 128, 256, 512])
        n2 = trial.suggest_categorical('n2', [2, 8, 16, 64, 128, 256, 512])
        n3 = trial.suggest_categorical('n3', [2, 8, 16, 64, 128, 256, 512])
        act1 = trial.suggest_categorical('act1', ['relu', 'sigmoid', 'linear', 'tanh', 'selu', 'elu'])
        act2 = trial.suggest_categorical('act2', ['relu', 'sigmoid', 'linear', 'tanh', 'selu', 'elu'])
        act3 = trial.suggest_categorical('act3', ['relu', 'sigmoid', 'linear', 'tanh', 'selu', 'elu'])
        lr = trial.suggest_categorical('lr', [0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0])

        # get the score for the hyperparameters chosen
        val_mse = nn_mse(n1, n2, n3, act1, act2, act3, lr)

        return val_mse

    # Create a study with the tep sampler
    study = optuna.create_study(sampler=optuna.samplers.TPESampler(), direction='minimize')
    # run the study.
    # this uses TPE to try different hyperparameters (in this case x and y)
    # and searches for the best ones
    study.optimize(objective, n_trials=n_trials)
    # get the results as dataframe
    results = study.trials_dataframe()

    return results
