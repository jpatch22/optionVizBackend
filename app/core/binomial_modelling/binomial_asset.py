import numpy as np

class BinomialAsset:
    @staticmethod
    def binomial_asset_value_base(u, v, s, nSteps):
        assetValues = [[0 for _ in range(nSteps)] for _ in range(nSteps)]
        assetValues[0][0] = s
        for i in range(1, nSteps):
            assetValues[i][0] = v * assetValues[i - 1][0]
            for j in range(1, i + 1):
                assetValues[i][j] = assetValues[i - 1][j-1] * u

        return assetValues

    @staticmethod
    def binomial_asset_value_drift(s, vol, timeStep, nSteps):
        u = 1 + vol * np.sqrt(timeStep)
        v = 1 - vol * np.sqrt(timeStep)
        return binomial_asset_value_base(u, v, s, nSteps)


