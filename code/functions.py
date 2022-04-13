
import numpy as np

def getRipple25():
    def f(x):
        if (in_domain(x)):
            result = -np.exp(-2 * np.log10(2) * np.power((x - .1) / 0.8 , 2)) * np.power((np.sin(5 * np.pi * x)), 6)
            return np.sum(result)
        return float("inf")
    def in_domain(x):
        for val in x:
            if (0 < val < 1) == False:
                return False
        return True
    def get_domain():
        return (0, 1)
    return (f, in_domain, get_domain)

def getMishra1():
    def f(x):
        if (in_domain(x)):
            gn = (np.size(x) - np.sum(x[:-1]))
            return (np.power(1 + gn, gn))
        return float("inf")
    def in_domain(x):
        for val in x:
            if (0 <= val <= 1) == False:
                return False
        return True
    def get_domain():
        return(0,1)
    return (f, in_domain, get_domain)
