# Portfolio Performance Dashboard

## Overview  
This project analyzes and visualizes the risk and return characteristics of multiple investment portfolios. It highlights how higher returns do not always imply better risk-adjusted performance, focusing on metrics like Sharpe ratio and maximum drawdown.

## Features  
- Calculates portfolio returns, volatility, Sharpe ratio, and drawdown  
- Interactive visualizations comparing multiple portfolios  
- Enables "what-if" analysis with leverage adjustments  
- Designed for fund governance and investment oversight use cases  

## Data  
- Uses historical price data from Yahoo Finance (`yfinance`) or provided CSV files  
- Cleaned and stored in `/data/processed`  

## Setup  
1. Create a Python environment  
```bash
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt


#Proposed folder & file structure

portfolio-performance-dashboard/
│
├── data/
│   ├── raw/                  # Raw downloaded or scraped data (e.g. CSVs)
│   └── processed/            # Cleaned/preprocessed data ready for analysis
│
├── notebooks/
│   └── portfolio_analysis.ipynb    # Main Jupyter notebook for exploration & dashboard prototyping
│
├── src/
│   ├── data_loader.py        # Functions to load & preprocess data
│   ├── analysis.py           # Functions for calculating returns, volatility, Sharpe, drawdown
│   └── visualization.py      # Functions for plotting charts & interactive dashboards
│
├── reports/
│   └── performance_summary.pdf   # Exported report or slides (optional)
│
├── requirements.txt          # Python dependencies for the project
├── README.md                 # Project overview, how to run, and insights
└── .gitignore                # Ignore env, pycache, etc.

jupyter notebook notebooks/portfolio_analysis.ipynb

pandas
numpy
matplotlib
seaborn
plotly
jupyter
yfinance


---

# **Starter notebook (`notebooks/portfolio_analysis.ipynb`) outline**

1. **Introduction**  
   Brief project goals and metrics to analyze.

2. **Data Import & Cleaning**  
   Load sample data for 3-4 example portfolios/funds.

3. **Calculate Metrics**  
   Functions for returns, volatility, Sharpe ratio, drawdown.

4. **Visualization**  
   Plot time series of returns, bar charts for Sharpe, drawdowns.

5. **What-if Scenarios**  
   Simple leverage impact on returns and Sharpe ratio.

6. **Summary & Next Steps**  
   Wrap up findings and mention how this could be extended.

---

# **requirements.txt example**

