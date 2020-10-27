import numpy as np

class Regression():

    def __init__(self):
        # your code
        self.params = {}

    def get_params(self):
        # your code
        return self.params

    def fit(self, X, y):
        # your code
        raise NotImplementedError

    def predict(self, X):
        return X.dot(self.params.get("coefficients")) + self.params.get("intercept")*np.ones((len(X), 1))

    def score(self, X, y):
        # your code
        ymean = np.sum(y) / len(y) 
        sst = 0
        for i in range(0,len(y)):
                sst = sst + ((i - ymean)**2)
        yHat = X.dot(self.params.get("coefficients")) + self.params.get("intercept")*np.ones((len(X), 1))
        sse = 0
        for i in range(0,len(y)):
            sse = sse + ((y[i] - yHat[i])**2)
        R2 = 1 - (sse/sst)
        return R2


    def set_params(self, **kwargs):
        for key, value in kwargs.items():
            if key == "alpha":
                self.params["alpha"] = kwargs[key]


class LinearRegression(Regression):
    def __init__(self):
        Regression.__init__(self)
    
    def fit(self, X, y):
        X = list(np.append(np.array(X), np.ones((len(X), 1)), axis=1))
        dagger = np.linalg.pinv(np.array(X))
        #dagger equals (Xtranspose*X)^-1 * Xtranspose
        weight = list(np.dot(dagger,y))
        params = {
            "coefficients": weight[:-1],
            "intercept": weight[-1]
        }
        self.params = params


class RidgeRegression(LinearRegression):
    def __init__(self):
        Regression.__init__(self)
    
    def fit(self, X, y):
        X = list(np.append(np.array(X), np.ones((len(X), 1)), axis=1))
        #define gamma
        gamma = np.identity(len(y))*self.params.get("alpha")
        #dagger equals (Xtranspose*X + GammaTranspose*Gamma)^-1 * Xtranspose
        dagger = np.matmul(((np.matmul((np.array(X).transpose()), (np.array(X))) + np.matmul(gamma.transpose(), gamma))**-1), np.array(X).transpose())
        weight = list(np.dot(dagger,y))
        params = {
            "coefficients": weight[:-1],
            "intercept": weight[-1]
        }
        self.params = params
