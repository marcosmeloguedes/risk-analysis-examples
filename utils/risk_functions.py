import numpy as np
import pandas as pd

def calculate_var(returns, confidence_level=0.95):
    """
    Calcula o VaR histórico para uma série de retornos.
    """
    return np.percentile(returns, (1 - confidence_level) * 100)
