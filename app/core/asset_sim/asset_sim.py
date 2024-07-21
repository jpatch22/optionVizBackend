import numpy as np

class AssetSim:
    @staticmethod
    def doLognormalAssetWalk(s, T, N, sigma, drift):
        if N == 0:
            return []
        N = 10
        dt = T / N
        t = np.linspace(0, T, num=N)
        res = np.zeros((2, N))
        res[0, :] = t

        dX = np.random.normal(0, np.sqrt(dt), N)
        X = np.cumsum(dX)

        S = s * np.exp((drift - 0.5 * (sigma**2)) * t[1:] + sigma * X[1:])
        print("S:", S)
        res[1, 0] = s
        res[1, 1:] = S
        print("finish calcs", res, type(res))

        return res

