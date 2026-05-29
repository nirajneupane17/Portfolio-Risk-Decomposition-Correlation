"""
risk_decomposition.py — Portfolio risk decomposition engine.
Author: Niraj Neupane | github.com/nirajneupane17
Project 10/10 — Portfolio Risk Decomposition & Correlation Modeling
"""
import numpy as np, pandas as pd
from scipy.optimize import minimize
from typing import Dict, Tuple

def marginal_risk_contribution(weights: np.ndarray, cov: np.ndarray) -> np.ndarray:
    port_vol=np.sqrt(weights@cov@weights)
    return cov@weights/port_vol

def component_risk_contribution(weights: np.ndarray, cov: np.ndarray) -> np.ndarray:
    return weights*marginal_risk_contribution(weights,cov)

def percent_risk_contribution(weights: np.ndarray, cov: np.ndarray) -> np.ndarray:
    port_vol=np.sqrt(weights@cov@weights)
    return component_risk_contribution(weights,cov)/port_vol*100

def portfolio_stats(weights: np.ndarray, returns: pd.DataFrame) -> Dict:
    cov=returns.cov()*252; mu=returns.mean()*252
    pv=np.sqrt(weights@cov.values@weights); pm=weights@mu.values
    dd=((1+returns@weights).cumprod()/(1+returns@weights).cumprod().cummax()-1).min()
    return {'ann_return':round(pm*100,3),'ann_vol':round(pv*100,3),
            'sharpe':round(pm/pv,4),'max_dd':round(dd*100,2),
            'prc':percent_risk_contribution(weights,cov.values)}

def min_variance_weights(returns: pd.DataFrame, max_w: float=0.40) -> np.ndarray:
    n=len(returns.columns); cov=returns.cov().values*252
    def obj(w): return w@cov@w
    cons=[{'type':'eq','fun':lambda w:np.sum(w)-1}]
    res=minimize(obj,np.ones(n)/n,method='SLSQP',
        bounds=[(0,max_w)]*n,constraints=cons)
    return res.x if res.success else np.ones(n)/n

def max_sharpe_weights(returns: pd.DataFrame, max_w: float=0.40) -> np.ndarray:
    n=len(returns.columns); cov=returns.cov().values*252; mu=returns.mean().values*252
    def neg_sharpe(w): pv=np.sqrt(w@cov@w); return -w@mu/pv if pv>0 else 0
    cons=[{'type':'eq','fun':lambda w:np.sum(w)-1}]
    res=minimize(neg_sharpe,np.ones(n)/n,method='SLSQP',
        bounds=[(0,max_w)]*n,constraints=cons)
    return res.x if res.success else np.ones(n)/n

def risk_parity_weights(returns: pd.DataFrame) -> np.ndarray:
    n=len(returns.columns); cov=returns.cov().values*252
    def obj(w):
        prc=component_risk_contribution(w,cov)
        return sum((prc[i]-prc[j])**2 for i in range(n) for j in range(i+1,n))
    cons=[{'type':'eq','fun':lambda w:np.sum(w)-1}]
    res=minimize(obj,np.ones(n)/n,method='SLSQP',
        bounds=[(0.01,0.50)]*n,constraints=cons,options={'maxiter':1000})
    return res.x if res.success else np.ones(n)/n

if __name__=='__main__':
    np.random.seed(42)
    r=pd.DataFrame(np.random.randn(500,5)*0.01,columns=list('ABCDE'))
    w=np.array([0.2]*5)
    print('PRC:',percent_risk_contribution(w,r.cov().values*252))
    print('Min-var:',min_variance_weights(r))
    print("risk_decomposition.py OK")
