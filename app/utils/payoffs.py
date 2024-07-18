class OptionPayoffFunctions:    
    """ 
    S: Current Price
    K: Strike Price
    """
    @staticmethod
    def euCallPayoff(S, K):
        return max(0, S - K)

    @staticmethod
    def euPutPayoff(S, K):
        return max(0, K - S)

    payoff_map = {
        "europeanCall": euCallPayoff,
        "europeanPut": euPutPayoff,
    }

    @staticmethod
    def calculatePayoff(option_type, S, K):
        if option_type in OptionPayoffFunctions.payoff_map:
            return OptionPayoffFunctions.payoff_map[option_type](S, K)
        else:
            return f"No payoff function found for {option_type}"
