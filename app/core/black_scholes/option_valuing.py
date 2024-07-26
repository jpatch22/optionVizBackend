import numpy as np
import scipy.stats as stats
from typing import List
from pydantic import BaseModel
from app.models.bs_op_val import RowDataExtended


class BSOptionValues:
    @staticmethod
    def getOptionVal(options: List[RowDataExtended], r, vol, stockValue):
        """
        Calculate option values for the given parameters across a mesh of stock values and time.
        """
        T = max([float(op.timeToExpiry) for op in options])
        N = 200
        time_grid = np.linspace(0, T, N)
        price_grid = np.linspace(0.5 * stockValue, 1.5 * stockValue, N)
        time_mesh, price_mesh = np.meshgrid(time_grid, price_grid)
        portfolioVal = np.zeros((N, N))

        for option in options:
            expValue = float(option.contractPrice)
            print(type(r), type(T), type(vol))
            sign = 1 if option.longShort.lower() == "long" else -1
            if option.optionType.lower() == "call":
                call_values = BSOptionValues.getCallValue(time_mesh, \
                        price_mesh, expValue, vol, r, T)
                portfolioVal += sign * call_values
            elif option.optionType.lower() == "put":
                put_values = BSOptionValues.getPutValue(time_mesh, price_mesh, expValue, vol, r, T)
                portfolioVal += sign * put_values

        portfolioVal = np.nan_to_num(portfolioVal, nan=0)
        return np.round(portfolioVal, 3), time_grid, price_grid

    @staticmethod
    def getCallValue(t, S, E, vol, r, T):
        d1 = BSOptionValues.get_d1(S, E, vol, r, T, t)
        d2 = BSOptionValues.get_d2(S, E, vol, r, T, t)
        return S * stats.norm.cdf(d1) - E * np.exp(-r * (T - t)) * stats.norm.cdf(d2)

    @staticmethod
    def getPutValue(t, S, E, vol, r, T):
        d1 = BSOptionValues.get_d1(S, E, vol, r, T, t)
        d2 = BSOptionValues.get_d2(S, E, vol, r, T, t)
        return - S * stats.norm.cdf(-d1) + E * np.exp(-r * (T - t)) * stats.norm.cdf(-d2)

    @staticmethod
    def get_d1(S, E, vol, r, T, t):
        return (np.log(S / E) + (r + 0.5 * vol ** 2) * (T - t)) / (vol * np.sqrt(T - t))

    @staticmethod
    def get_d2(S, E, vol, r, T, t):
        return (np.log(S / E) + (r - 0.5 * vol ** 2) * (T - t)) / (vol * np.sqrt(T - t))
