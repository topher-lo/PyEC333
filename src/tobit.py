"""This module contains a simple implementation of Tobit.
"""
import numpy as np
import pandas as pd
import scipy

from scipy import stats

# Tobit from scratch


class Tobit:
    """Tobit class has two methods:
    1. __init__ method defines
    the Tobit's classes's attributes and is used to create an
    instance of Tobit.

    2. fit method solves the log-likelihood and returns the estimated
    coefficients.

    Note: model includes an intercept.
    """

    def __init__(self, endog, exog):
        """
        Args:
            endog (pd.Series):
                A Pandas Series of y.

            exog (pd.DataFrame):
                A Pandas DataFrame of X values.

        Note: endog and exog must have an index called "cutoff" with value 0
        for lower truncated data and 1 for untruncated data.

        Note: we are minimizing negative log-likelihoods
        to find the optimal point.
        """
        self.endog = endog
        self.exog = exog
        self.N_regressors = exog.shape[1]

    def _tobit(self, params, exog, endog):
        betas = params[:-1]  # First K parameters
        sd = params[-1]  # Last parameter

        # Negative likelihood
        negLL = 0

        # Lower truncated data
        # Select truncated and convert to an ndarray
        X_truncated = exog.query('cutoff == 0').to_numpy()
        y_truncated = endog[endog.index == 0].to_numpy()

        yhat = np.dot(X_truncated, betas)
        negLL = negLL + -np.sum(
            stats.norm.logsf(y_truncated, loc=yhat, scale=sd)
        )  # logsf = log survival function = log(1 - cdf)

        # Untruncated data
        X_untruncated = exog.query('cutoff == 1').to_numpy()
        y_untruncated = endog[endog.index == 1].to_numpy()

        yhat = np.dot(X_untruncated, betas)
        negLL = negLL + -np.sum(
            stats.norm.logpdf(y_untruncated, loc=yhat, scale=sd)
        )  # log normal ppdf

        return negLL

    def fit(self, method='Nelder-Mead', maxiter=100, verbose=True, seed=42):
        """Solves Tobit model via MLE using
        scipy.optimize.minimize

        Args:
            method (str):
                Type of solver.
                See scipy docs for list of solvers available.

            maxiter (int):
                Maximum number of iterations to perform.

            verbose (str):
                If True, prints convergence messages.
        """
        endog = self.endog
        exog = self.exog

        # Initial guess
        np.random.seed(seed)
        betas = np.random.randint(-100, 100, size=self.N_regressors)
        sd = 1
        params = np.append(betas, sd)

        kwargs = {}
        if verbose:
            kwargs['disp'] = verbose
        if maxiter:
            kwargs['maxiter'] = maxiter

        # Scipy minimize returns a dictionary of results and parameters
        # The optimal point (betas, sd) (K + 1) x 1 array
        # is stored in the 'x' key
        scipy_results = scipy.optimize.minimize(self._tobit,
                                                params,
                                                args=(exog, endog),
                                                method=method,
                                                options=kwargs)
        # Get regressor names
        exog_cols = self.exog.columns.to_list()
        # Create DataFrame of beta and cd estimates
        result = pd.DataFrame({'estimate': exog_cols + ['sd'],
                               'coeff': scipy_results['x']})

        return result


if __name__ == "__main__":
    pass
