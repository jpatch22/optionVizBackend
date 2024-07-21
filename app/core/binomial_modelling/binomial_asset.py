import numpy as np

class BinomialModelling:
    @staticmethod
    def calculateBaseVol(sigma, S0, T, N):
        dt = T / N
        u = 1 + sigma * np.sqrt(dt)
        v = 1 - sigma * np.sqrt(dt)
        return BinomialModelling.calculate_asset_prices(S0, u, v, N)

    @staticmethod
    def calculateAssetBase(S0, u, v, N):
        return BinomialModelling.calculate_asset_prices(S0, u, v, N)

    @staticmethod
    def calculateOptionBase(S0, u, v, sigma, N, K, r, T, payoff_func):
        assetValues = BinomialModelling.calculate_asset_prices(S0, u, v, N)
        dt = T / N
        p = 0.5 + r * np.sqrt(dt) / (2 * sigma)
        return BinomialModelling.calculate_option_prices(assetValues, K, r, dt, p, payoff_func)

    @staticmethod
    def calculateOptionVol(sigma, S0, T, N, K, r, payoff_func):
        dt = T / N
        p = 0.5 + r * np.sqrt(dt) / (2 * sigma)
        assetValues = BinomialModelling.calculateBaseVol(sigma, S0, T, N)
        return BinomialModelling.calculate_option_prices(assetValues, K, r, dt, p, payoff_func)

    @staticmethod
    def calculate_asset_prices(S0, u, v, N):
        asset_prices = np.zeros((N + 1, N + 1))
        asset_prices[0][0] = S0
        for i in range(1, N + 1):
            asset_prices[i][0] = v * asset_prices[i - 1][0]
            for j in range(1, i + 1):
                asset_prices[i][j] = asset_prices[i - 1][j-1] * u

        return asset_prices

    @staticmethod
    def calculate_option_prices(asset_prices, K, r, delta_t, p, payoff_func):
        N = asset_prices.shape[1] - 1
        option_values = np.zeros_like(asset_prices)
        
        # Initialize option values at maturity
        for j in range(N + 1):
            option_values[j, N] = payoff_func(asset_prices[j, N], K)
        
        # Back prop
        for i in range(N - 1, -1, -1):
            for j in range(i + 1):
                option_values[j, i] = np.exp(-r * delta_t) * (p * option_values[j, i + 1] + (1 - p) * option_values[j + 1, i + 1])
        
        return option_values

