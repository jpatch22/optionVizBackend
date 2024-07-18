from app.core.binomial_modelling.binomial_asset import BinomialAsset

class BinomialOptions:
    @staticmethod
    def binomialOptionBase(u, v, s, numSteps, p, r):
        assetPrices = BinomialAsset.binomial_asset_value_base(u, v, s, numSteps)


    @staticmethod
    def binomialOptionDrift(vol, numSteps, s, timeStep, r):
        assetPrices = BinomialAsset.binomial_asset_value_drift(s, vol, timeStep, numSteps)

    @staticmethod
    def calculateOptionValsFromAssetPrices(assetPrices, r, dt, pIncrease, payoffFunction):
        n = len(assetPrices)
        optionPrices = [[0 for _ in range(n)] for _ in range(n)]
        # Calculate @Expiry values
        for j in range(n):
            optionPrices[n - 1][j] = payoffFunction(assetPrices[n - 1][j])

        for i in reversed(range(n)):
            if 

    @staticmethod
    def payoff(assetPrice, strike):
        pass

