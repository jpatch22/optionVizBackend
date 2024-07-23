import numpy as np

class AssetSim:
    @staticmethod
    def doLognormalAssetWalk(s, T, N, sigma, drift):
        if N == 0:
            return []
        dt = T / N
        t = np.linspace(0, T, num=N + 1)
        res = np.zeros((2, N + 1))
        res[0, :] = t
        S = np.zeros(N+1)
        S[0] = s

        dX = np.random.normal(0, np.sqrt(dt), N) * np.sqrt(dt)
        print(dX)
        for i in range(1, N+1):
            S[i] = S[i - 1] * np.exp((drift - 0.5 * (sigma**2))*dt + sigma * dX[i - 1])
            
        res[1, :] = S

        return res

