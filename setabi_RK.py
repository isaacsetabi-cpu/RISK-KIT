import pandas as pd
import numpy as np

def Drawdown(return_series: pd.Series):
    """
    Computes Drawdown which is a defference
    between wealth and previous peaks as a percentage of previous peaks
    """
    wealth_index = 1*(1 + return_series).cumprod()
    previous_peak = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peak)/previous_peak
    return pd.DataFrame({
        "Wealth": wealth_index,
        "Peak": previous_peak,
        "Drawdown": drawdowns})

def get_ind_returns():
    """
    Loads industry returns
    """
    ind = pd.read_csv("G:/testenv/data/ind30_m_vw_rets.csv", 
                      header = 0, index_col = 0, parse_dates=True)/100
    ind.index = pd.to_datetime(ind.index, format="%Y%m").to_period('M')
    ind.columns = ind.columns.str.strip()
    return ind

def get_return_file():
    """
    Loads return file for farmer french
    """
    returns = pd.read_csv("G:/testenv/Portfolios_Formed_on_ME_monthly_EW.csv",
                          header = 0, index_col=0, parse_dates=True, na_values=-99.99
                         )
    columns = ["Lo 10", "Hi 10"]
    returns = returns[columns]
    returns = returns/100
    returns.columns = ["SmallCap","LargeCap"]
    returns.index = pd.to_datetime(returns.index, format="%Y%m").to_period('M')
    return returns

def annualized_return(return_series):
    """
    it computes annual return given a series of monthly data
    """
    no_of_months = return_series.shape[0]
    annual_return = (return_series + 1).prod()**(12/no_of_months) - 1
    return annual_return

def annualized_vol(return_series):
    """
    Computes voltility given a series of returns
    """
    return (return_series.std()*np.sqrt(12))

def skewness(returns: pd.Series):
    """
    this calculates skewness which is the a measure of variations 
    to normality
    """
    demeaned_returns = returns - returns.mean()
    voltility = returns.std(ddof=0)
    Expectation = demeaned_returns**3
    return Expectation / voltility**3

def kurtosis(returns: pd.Series):
    """
    this calculates kurtosis which is the a measure of variations 
    to normality
    """
    demeaned_returns = returns - returns.mean()
    voltility = returns.std(ddof=0)
    Expectation = demeaned_returns**4
    return Expectation / voltility**4

def Design_Price(ArtWork_Size, No_of_Colors):
    """
    Calculates the price of an artwork design given
    the area of the artwork in cm.
    """
    Multiplier = (15*(ArtWork_Size * No_of_Colors))/100
    return Multiplier * 100

def portfolio_return(weights, returns):
    """
    weight -> returns
    """    
    return weights.T @ returns

def portfolio_vol(weights, covmet):
    """
    weights -> vol
    """
    return (weights.T @ covmet @ weights)**0.5

def plot_ef2(no_points, er, cov, style=".-"):
    """
    plots the two asset efficient frontier
    """
    if er.shape[0] != 2 or er.shape[0] != 2:
        raise ValueError("plot_ef2 Can only plot 2-Asset frontier")
    weights = [np.array([w, 1-w]) for w in np.linspace(0, 1, no_points)]
    rets = [portfolio_return(w, er) for w in weights]
    vols = [portfolio_vol(w, cov) for w in weights]
    ef = pd.DataFrame({"Returns": rets, "Volatility": vols})
    return ef.plot.scatter(x="Volatility", y="Returns", style=style)

def optimal_weights(no_points, er, cov): # for use in plot_ef function
    """
    generates weights to run on the optimizer to minimize vol 
    """
    target_rs = np.linspace(er.min(), er.max(), no_points)
    weights = [minimize_vol(target_return, er, cov) for target_return in target_rs]
    return weights

from scipy.optimize import minimize

def muximum_sharpe_ratio(riskfree_rate, er, cov):
    """
    we want to find the muximum sharpe ration which is excess return (return less risk_free) per volotility
    """
    n = er.shape[0]
    init_gues = np.repeat(1/n, n)
    bounds = ((0.0, 1.0),)*n
    
    weights_sum_to_1 = {
        'type': 'eq',
        'fun': lambda weights: np.sum(weights) - 1
    }
    
    def neg_sharpe_ratio(weights, riskfree_rate, er, cov):
        """
        computes the negative of the sharpe ratio given weights
        """        
        r = portfolio_return(weights, er)
        vol = portfolio_vol(weights, cov)
        return -(r - riskfree_rate)/vol
    
    results = minimize(neg_sharpe_ratio, init_gues,
                      args=(riskfree_rate, er, cov), method='SLSQP',
                      options={'disp': False},
                      constraints=(weights_sum_to_1),
                      bounds=bounds 
                      )
    return results.x

def plot_ef(no_points, er, cov, style=".-", show_CML=False, riskfree_rate=0):
    """
    plots the two asset efficient frontier
    """
    weights = optimal_weights(no_points, er, cov)
    rets = [portfolio_return(w, er) for w in weights]
    vols = [portfolio_vol(w, cov) for w in weights]
    ef = pd.DataFrame({"Returns": rets, "Volatility": vols})
    ax = ef.plot.line(x="Volatility", y="Returns", style=style)
    if show_CML:
        ax.set_xlim(left = 0)
        w_msr = muximum_sharpe_ratio(riskfree_rate, er, cov)
        r_msr = portfolio_return(w_msr, er)
        vol_msr = portfolio_vol(w_msr, cov)
        #add CML
        cml_x = [0, vol_msr]
        cml_y = [riskfree_rate, r_msr]
        ax.plot(cml_x, cml_y, color = 'green', marker='o', linestyle='dashed')
    return ax    

from scipy.optimize import minimize

""" 
we can use the optimizer to generate some weights

the optizers work, you need to give it an objective function, give it some constraints
give it an initial  guess

for this,
the expected return vector (er) has as many assets as the number of corumns n
so our initial guess will be an equally weighted vector of 1/n, n times
we need the weights to have bounds
"""

def minimize_vol(target_return, er, cov):
    """
    given target -> weights
    """
    n = er.shape[0]                #n is number of assets, we have the same assets as columns(Expected Return vector has as many raws as assets)
    init_gues = np.repeat(1/n, n)  #our initial weights are 1/n for each asset
    bounds = ((0.0, 1.0),)*n       #our bounds should be a tupple of tupples between 0 and 1 inclusive
    
    """the first constraint is that if weights of our target return are used as inputs in our portfolio return function, 
    the return we get should be equal to the target return"""
    
    return_is_target = {
        'type': 'eq',
        'args': (er,),
        'fun': lambda weights, er: target_return - portfolio_return(weights, er)
    }
    
    """ the sum of the weights should equal to 1"""
    
    weights_sum_to_1 = {
        'type': 'eq',
        'fun': lambda weights: np.sum(weights) - 1
    }
    
    results = minimize(portfolio_vol, init_gues,
                      args=(cov), method='SLSQP',
                      options={'disp': False},
                      constraints=(return_is_target, weights_sum_to_1),
                      bounds=bounds 
                      )
    return results.x

