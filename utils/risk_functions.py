import numpy as np
import pandas as pd

def calculate_var_historical(returns, confidence_level=0.95):
    """
    Calcula o Value at Risk (VaR) Histórico.
    """
    return np.percentile(returns, (1 - confidence_level) * 100)

def calculate_drawdown(prices):
    """
    Calcula a série de Drawdown a partir de uma série de preços/cotas.
    Retorna o drawdown atual e o máximo drawdown do período.
    """
    # Calcula o pico acumulado
    rolling_max = prices.cummax()
    # Calcula o drawdown atual
    drawdowns = (prices - rolling_max) / rolling_max
    # O valor mais baixo da série de drawdowns é o Max Drawdown
    max_drawdown = drawdowns.min()
    
    return drawdowns, max_drawdown

def annualize_volatility(returns, periods=252):
    """
    Calcula a volatilidade anualizada baseada em retornos diários.
    """
    return returns.std() * np.sqrt(periods)
