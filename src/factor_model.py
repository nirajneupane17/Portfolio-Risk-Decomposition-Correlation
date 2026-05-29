"""
factor_model.py — Factor risk attribution model.
Author: Niraj Neupane | github.com/nirajneupane17
Project 10/10 — Portfolio Risk Decomposition & Correlation Modeling
"""
import numpy as np, pandas as pd
from sklearn.linear_model import LinearRegression
from typing import Dict, List

def fit_factor_model(returns: pd.Series, factors: pd.DataFrame) -> Dict:
    common=returns.index.intersection(factors.index)
    X=factors.loc[common]; y=returns.loc[common]
    lr=LinearRegression(); lr.fit(X,y)
    r2=lr.score(X,y); resid=y-lr.predict(X)
    return {'betas':dict(zip(factors.columns,lr.coef_)),
            'alpha':lr.intercept_*252,'r2':round(r2,4),
            'systematic_pct':round(r2*100,2),
            'idiosyncratic_pct':round((1-r2)*100,2),
            'tracking_error':round(resid.std()*np.sqrt(252)*100,4)}

def portfolio_factor_attribution(port_returns: pd.Series, factors: pd.DataFrame) -> Dict:
    res=fit_factor_model(port_returns,factors)
    common=port_returns.index.intersection(factors.index)
    X=factors.loc[common]; y=port_returns.loc[common]
    lr=LinearRegression(); lr.fit(X,y)
    contrib={f: round(lr.coef_[i]*factors[f].std()*np.sqrt(252)*100,4)
             for i,f in enumerate(factors.columns)}
    res['factor_vol_contrib']=contrib
    return res

def rolling_factor_betas(returns: pd.Series, factors: pd.DataFrame,
                          window: int=126) -> pd.DataFrame:
    common=returns.index.intersection(factors.index)
    r=returns.loc[common]; f=factors.loc[common]
    betas=[]
    for i in range(window,len(r)):
        X=f.iloc[i-window:i]; y=r.iloc[i-window:i]
        lr=LinearRegression(); lr.fit(X,y)
        betas.append(list(lr.coef_))
    return pd.DataFrame(betas,columns=factors.columns,index=r.index[window:])

if __name__=='__main__':
    np.random.seed(42)
    r=pd.Series(np.random.randn(500)*0.01)
    f=pd.DataFrame(np.random.randn(500,3)*0.01,columns=['mkt','size','val'])
    print(fit_factor_model(r,f))
    print("factor_model.py OK")
