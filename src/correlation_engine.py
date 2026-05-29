"""
correlation_engine.py — Correlation & covariance analysis engine.
Author: Niraj Neupane | github.com/nirajneupane17
Project 10/10 — Portfolio Risk Decomposition & Correlation Modeling
"""
import numpy as np, pandas as pd
from typing import Dict, List, Optional

def rolling_correlation(returns: pd.DataFrame, window: int=63) -> pd.DataFrame:
    """Rolling pairwise correlation (mean across all pairs)."""
    result=[]
    for i in range(window,len(returns)):
        c=returns.iloc[i-window:i].corr().values
        upper=c[np.triu_indices_from(c,k=1)]
        result.append(upper.mean())
    return pd.Series(result,index=returns.index[window:],name='mean_corr')

def regime_correlation(returns: pd.DataFrame, periods: Dict[str,slice]) -> Dict:
    """Compute correlation matrices across defined regimes."""
    return {nm: returns.loc[sl].corr() for nm,sl in periods.items()}

def pca_concentration(returns: pd.DataFrame, window: int=63) -> pd.Series:
    """PC1 variance concentration — systemic risk indicator."""
    result=[]
    for i in range(window,len(returns)):
        c=returns.iloc[i-window:i].corr().values
        ev=np.linalg.eigvalsh(c)[::-1]
        result.append(ev[0]/ev.sum())
    return pd.Series(result,index=returns.index[window:],name='pc1_concentration')

def nearest_pd(A: np.ndarray) -> np.ndarray:
    """Project matrix to nearest positive definite."""
    eigvals,eigvecs=np.linalg.eigh(A)
    eigvals=np.maximum(eigvals,1e-8)
    B=eigvecs@np.diag(eigvals)@eigvecs.T
    d=np.sqrt(np.diag(B)); return B/d[:,None]/d[None,:]

def correlation_stability(returns: pd.DataFrame, window: int=63) -> pd.DataFrame:
    """Measure correlation stability — std of rolling pairwise correlations."""
    pairs=[(a,b) for i,a in enumerate(returns.columns) for b in returns.columns[i+1:]]
    result={f'{a}/{b}': returns[a].rolling(window).corr(returns[b]) for a,b in pairs[:10]}
    return pd.DataFrame(result)

if __name__=='__main__':
    np.random.seed(42)
    r=pd.DataFrame(np.random.randn(500,5)*0.01,columns=list('ABCDE'))
    print('Mean corr:', rolling_correlation(r).tail(3))
    print('PC1 conc:', pca_concentration(r).tail(3))
    print("correlation_engine.py OK")
