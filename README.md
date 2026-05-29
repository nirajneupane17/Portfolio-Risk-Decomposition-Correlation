# Portfolio Risk Decomposition & Correlation Modeling

**Project 10 of 10 — Series Finale**

End-to-end portfolio risk decomposition — correlation analysis across market
regimes, marginal and component risk contribution, portfolio optimisation
(minimum variance, maximum Sharpe, risk parity), covariance modeling, and
factor risk attribution across six systematic risk factors.

![Bloomberg Dashboard](results/portfolio_risk_bloomberg.gif)

---

## Key Results

| Metric | Equal Weight | Market Cap | Risk Parity |
|---|---|---|---|
| Annualised Vol | 6.6% | 8.2% | 5.8% |
| Sharpe Ratio | 0.18 | 0.14 | 0.22 |
| Max Drawdown | -24.1% | -28.3% | -18.6% |
| Mean Pairwise Corr | 0.312 | 0.312 | 0.312 |
| PC1 Concentration | 42% | 42% | 42% |

---

## What This Project Covers

**Correlation Analysis**
- Full-sample correlation matrix across 10 assets
- Regime-conditional correlations: Full · COVID crash · Calm 2023
- Rolling 63-day pairwise correlations
- PC1 variance concentration as systemic risk indicator
- Correlation breakdown during crisis vs diversification in calm

**Risk Decomposition**
- Marginal risk contribution (MRC) per asset per strategy
- Component risk contribution (CRC)
- Percent risk contribution (PRC)
- Three strategies compared: Equal Weight · Market Cap · Risk Parity

**Portfolio Optimisation**
- Efficient frontier via SLSQP constrained optimisation
- Minimum variance portfolio
- Maximum Sharpe ratio portfolio
- Risk parity portfolio (equal risk contribution)
- Strategy comparison: return, vol, Sharpe, max drawdown

**Covariance & Regime Analysis**
- Rolling 21-day realised volatility by asset
- Volatility regime classification: Low (<10%) · Medium (10-20%) · High (>20%)
- Rolling portfolio volatility by strategy
- PC1 concentration time series

**Factor Risk Attribution**
- Six-factor model: Market · Size · Value · Rates · Credit · Dollar
- Systematic vs idiosyncratic variance decomposition per asset
- Factor beta heatmap across all 10 assets
- Portfolio-level factor attribution and tracking error

---

## Project Structure

```
Portfolio-Risk-Decomposition-Correlation/
├── data/
│   ├── returns.csv              (10 assets, 2018-2024, 1,827 obs)
│   ├── prices.csv               (indexed prices)
│   ├── portfolio_weights.csv    (3 strategy weights)
│   └── factor_data.csv          (6 risk factors)
├── notebooks/
│   ├── 01_correlation_analysis.ipynb
│   ├── 02_rolling_correlation.ipynb
│   ├── 03_risk_decomposition.ipynb
│   ├── 04_portfolio_optimisation.ipynb
│   └── 05_factor_attribution.ipynb
├── src/
│   ├── correlation_engine.py
│   ├── risk_decomposition.py
│   └── factor_model.py
├── results/
│   ├── 01_correlation_heatmap.png
│   ├── 02_rolling_correlation.png
│   ├── 03_risk_decomposition.png
│   ├── 04_portfolio_optimisation.png
│   ├── 05_covariance_regime.png
│   ├── 06_factor_attribution.png
│   ├── 07_summary_dashboard.png
│   ├── portfolio_risk_bloomberg.gif
│   └── portfolio_risk_video.mp4
└── README.md
```

---

## 10-Project Quant Risk Series — Complete

| # | Project | Status |
|---|---|---|
| 1 | VaR-CVaR-Expected-Shortfall-Modeling | ✅ |
| 2 | GARCH-Volatility-Forecasting | ✅ |
| 3 | Monte-Carlo-Risk-Derivatives-Pricing | ✅ |
| 4 | Options-Analytics-Volatility-Surface | ✅ |
| 5 | Stress-Testing-Scenario-Analysis | ✅ |
| 6 | Model-Risk-Validation-SR11-7 | ✅ |
| 7 | Fixed-Income-Risk-Duration-Modeling | ✅ |
| 8 | ML-Risk-Estimation-Forecasting | ✅ |
| 9 | Market-Data-Analysis-PnL-Modeling | ✅ |
| **10** | **Portfolio-Risk-Decomposition-Correlation** | ✅ |

---

## Author

**Niraj Neupane** — Quantitative Risk Analyst · BlackRock
MS Financial Economics · University of Wisconsin–Madison
CA (ICAI) · FRM Candidate
GitHub: [github.com/nirajneupane17](https://github.com/nirajneupane17)
